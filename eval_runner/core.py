from __future__ import annotations

import dataclasses
import html
import json
import os
import shutil
import subprocess
import time
from pathlib import Path
from typing import Any, Iterable

try:
    import yaml
except Exception:  # pragma: no cover
    yaml = None


@dataclasses.dataclass
class EvalSpec:
    path: Path
    prompt: str
    expectations: list[str]
    setup_commands: list[str]
    teardown_commands: list[str]
    parameters: dict[str, Any]


@dataclasses.dataclass
class EvalResult:
    eval_path: str
    prompt: str
    expectations: list[str]
    passed: bool
    failure_reasons: list[str]
    elapsed_seconds: float
    token_counts: dict[str, int]
    output: str
    result_path: str
    run_dir: str

    def to_dict(self) -> dict[str, Any]:
        return dataclasses.asdict(self)


def discover_eval_files(paths: Iterable[str | Path]) -> list[Path]:
    found: list[Path] = []
    for raw in paths:
        path = Path(raw).expanduser().resolve()
        if path.is_file() and path.name == "EVAL.yaml":
            found.append(path)
        elif path.is_dir():
            found.extend(sorted(path.rglob("EVAL.yaml")))
    return sorted(dict.fromkeys(found))


def _ensure_yaml() -> None:
    if yaml is None:
        raise RuntimeError("PyYAML is required to load EVAL.yaml files")


def load_eval(path: str | Path) -> EvalSpec:
    _ensure_yaml()
    eval_path = Path(path).expanduser().resolve()
    data = yaml.safe_load(eval_path.read_text()) or {}
    if not isinstance(data, dict):
        raise ValueError(f"{eval_path} must contain a YAML mapping")
    prompt = data.get("prompt")
    expectations = data.get("expectations")
    if not isinstance(prompt, str) or not prompt.strip():
        raise ValueError(f"{eval_path} requires non-empty string field: prompt")
    if not isinstance(expectations, list) or not all(isinstance(x, str) and x.strip() for x in expectations):
        raise ValueError(f"{eval_path} requires expectations: string[]")
    setup = data.get("setupCommands", data.get("setup_commands", [])) or []
    teardown = data.get("teardownCommands", data.get("teardown_commands", [])) or []
    parameters = data.get("parameters", {}) or {}
    if not isinstance(setup, list) or not all(isinstance(x, str) for x in setup):
        raise ValueError("setupCommands must be a string array")
    if not isinstance(teardown, list) or not all(isinstance(x, str) for x in teardown):
        raise ValueError("teardownCommands must be a string array")
    if not isinstance(parameters, dict):
        raise ValueError("parameters must be a map")
    return EvalSpec(eval_path, prompt.strip(), [x.strip() for x in expectations], setup, teardown, parameters)


def _run_shell_commands(commands: list[str], cwd: Path, env: dict[str, str]) -> list[str]:
    outputs: list[str] = []
    for command in commands:
        proc = subprocess.run(command, cwd=cwd, env=env, shell=True, text=True, capture_output=True, timeout=600)
        outputs.append(f"$ {command}\n{proc.stdout}{proc.stderr}")
        if proc.returncode != 0:
            raise RuntimeError(f"Command failed ({proc.returncode}): {command}\n{proc.stderr}")
    return outputs


def _copy_distribution(run_profile: Path) -> None:
    root = Path(__file__).resolve().parents[1]
    for name in ["SOUL.md", "AGENTS.md", "config.yaml", "skills", "evaldata"]:
        src = root / name
        if not src.exists():
            continue
        dst = run_profile / name
        if src.is_dir():
            shutil.copytree(src, dst, dirs_exist_ok=True)
        else:
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(src, dst)


def _judge_output(output: str, expectations: list[str]) -> tuple[bool, list[str]]:
    lower = output.lower()
    failures = [f"Expectation not observed in output: {exp}" for exp in expectations if exp.lower() not in lower]
    return not failures, failures


def run_eval(eval_path: str | Path, output_root: str | Path = ".eval-runs", hermes_command: str | None = "hermes") -> EvalResult:
    spec = load_eval(eval_path)
    started = time.monotonic()
    stamp = time.strftime("%Y%m%d-%H%M%S")
    run_dir = Path(output_root).expanduser().resolve() / f"{spec.path.parent.name}-{stamp}-{abs(hash(str(spec.path))) % 100000}"
    run_profile = run_dir / "profile"
    run_dir.mkdir(parents=True, exist_ok=True)
    run_profile.mkdir(parents=True, exist_ok=True)
    _copy_distribution(run_profile)
    env = os.environ.copy()
    env["HERMES_HOME"] = str(run_profile)
    output_parts: list[str] = []
    failure_reasons: list[str] = []
    token_counts = {"prompt_tokens": 0, "completion_tokens": 0, "total_tokens": 0}
    try:
        output_parts.extend(_run_shell_commands(spec.setup_commands, spec.path.parent, env))
        if hermes_command:
            prompt_file = run_dir / "prompt.txt"
            prompt_file.write_text(spec.prompt)
            # Hermes one-shot mode uses the active HERMES_HOME as the isolated profile.
            # The historical shorthand is `hermes -z PROMPT`.
            command = f"{hermes_command} -z {json.dumps(spec.prompt)}"
            proc = subprocess.run(command, shell=True, text=True, capture_output=True, timeout=1800, env=env)
            output_parts.append(proc.stdout + proc.stderr)
            if proc.returncode != 0:
                failure_reasons.append(f"Hermes command failed with exit code {proc.returncode}")
        else:
            # Deterministic offline mode for CI/local smoke tests: judge the static
            # artifact text without making model calls or touching external systems.
            skill_file = spec.path.parent / "SKILL.md"
            static_text = spec.path.read_text()
            if skill_file.exists():
                static_text += "\n" + skill_file.read_text()
            output_parts.append(static_text)
        passed, expectation_failures = _judge_output("\n".join(output_parts), spec.expectations)
        failure_reasons.extend(expectation_failures)
    except Exception as exc:
        passed = False
        failure_reasons.append(str(exc))
    finally:
        try:
            output_parts.extend(_run_shell_commands(spec.teardown_commands, spec.path.parent, env))
        except Exception as exc:
            passed = False
            failure_reasons.append(f"teardown failed: {exc}")
    elapsed = time.monotonic() - started
    result = EvalResult(
        eval_path=str(spec.path),
        prompt=spec.prompt,
        expectations=spec.expectations,
        passed=passed,
        failure_reasons=failure_reasons,
        elapsed_seconds=elapsed,
        token_counts=token_counts,
        output="\n".join(output_parts),
        result_path=str(run_dir / "result.json"),
        run_dir=str(run_dir),
    )
    Path(result.result_path).write_text(json.dumps(result.to_dict(), indent=2))
    return result


def render_reports(results: list[EvalResult], output_prefix: str | Path, markdown: bool = False) -> tuple[Path, Path | None]:
    prefix = Path(output_prefix).expanduser().resolve()
    prefix.parent.mkdir(parents=True, exist_ok=True)
    html_path = prefix.with_suffix(".html")
    rows = []
    for r in results:
        rows.append(
            "<tr>"
            f"<td>{html.escape(Path(r.eval_path).parent.name)}</td>"
            f"<td>{'PASS' if r.passed else 'FAIL'}</td>"
            f"<td>{r.elapsed_seconds:.2f}s</td>"
            f"<td><pre>{html.escape(r.prompt)}</pre></td>"
            f"<td><pre>{html.escape(chr(10).join(r.failure_reasons))}</pre></td>"
            f"<td>{html.escape(r.result_path)}</td>"
            "</tr>"
        )
    html_path.write_text("""<!doctype html><meta charset='utf-8'><title>NED Eval Results</title>
<style>body{font-family:system-ui,sans-serif;margin:2rem}table{border-collapse:collapse;width:100%}td,th{border:1px solid #ddd;padding:.5rem;vertical-align:top}pre{white-space:pre-wrap}</style>
<h1>NoEgoDev Eval Results</h1><table><thead><tr><th>Eval</th><th>Status</th><th>Elapsed</th><th>Prompt</th><th>Failure reasons</th><th>Result JSON</th></tr></thead><tbody>""" + "\n".join(rows) + "</tbody></table>")
    md_path = None
    if markdown:
        md_path = prefix.with_suffix(".md")
        lines = ["# NoEgoDev Eval Results", ""]
        for r in results:
            lines.extend([
                f"## {Path(r.eval_path).parent.name}: {'PASS' if r.passed else 'FAIL'}",
                f"- Eval: `{r.eval_path}`",
                f"- Elapsed: {r.elapsed_seconds:.2f}s",
                f"- Result JSON: `{r.result_path}`",
                "- Prompt:", f"  {r.prompt}",
                "- Failure reasons:", *(f"  - {reason}" for reason in (r.failure_reasons or ["None"])), "",
            ])
        md_path.write_text("\n".join(lines))
    return html_path, md_path
