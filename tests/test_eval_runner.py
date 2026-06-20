from pathlib import Path
import json

from eval_runner.core import discover_eval_files, load_eval, render_reports, run_eval


def test_discovers_eval_yaml_files(tmp_path):
    (tmp_path / "a").mkdir()
    (tmp_path / "a" / "EVAL.yaml").write_text("prompt: hi\nexpectations: [done]\n")
    (tmp_path / "b").mkdir()
    (tmp_path / "b" / "EVAL.yml").write_text("prompt: bye\nexpectations: [done]\n")

    found = discover_eval_files([tmp_path])

    assert found == [tmp_path / "a" / "EVAL.yaml"]


def test_load_eval_validates_required_fields(tmp_path):
    path = tmp_path / "EVAL.yaml"
    path.write_text("prompt: Build it\nexpectations:\n  - result exists\nparameters:\n  repo: local\n")

    spec = load_eval(path)

    assert spec.prompt == "Build it"
    assert spec.expectations == ["result exists"]
    assert spec.parameters["repo"] == "local"


def test_run_eval_writes_result_json_without_hermes(tmp_path):
    eval_dir = tmp_path / "skill"
    eval_dir.mkdir()
    eval_path = eval_dir / "EVAL.yaml"
    eval_path.write_text("prompt: Say done\nexpectations:\n  - done appears\nparameters:\n  mode: offline\n")

    result = run_eval(eval_path, output_root=tmp_path / "runs", hermes_command=None)

    assert result.eval_path == str(eval_path)
    assert result.passed is True
    assert result.elapsed_seconds >= 0
    result_json = Path(result.result_path)
    assert result_json.exists()
    data = json.loads(result_json.read_text())
    assert data["failure_reasons"] == []


def test_render_reports_outputs_html_and_markdown(tmp_path):
    eval_dir = tmp_path / "skill"
    eval_dir.mkdir()
    eval_path = eval_dir / "EVAL.yaml"
    eval_path.write_text("prompt: Echo done\nexpectations:\n  - done\n")
    result = run_eval(eval_path, output_root=tmp_path / "runs", hermes_command=None)

    html, md = render_reports([result], tmp_path / "report", markdown=True)

    assert html.exists()
    assert md is not None and md.exists()
    assert "Echo done" in html.read_text()
    assert "Echo done" in md.read_text()
