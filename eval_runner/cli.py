from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from .core import discover_eval_files, render_reports, run_eval


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run NoEgoDev EVAL.yaml files")
    parser.add_argument("paths", nargs="+", help="Files or folders to search for EVAL.yaml")
    parser.add_argument("--output-root", default=".eval-runs", help="Directory for per-eval result folders")
    parser.add_argument("--report", default=None, help="Report output prefix (default: .eval-runs/report-<timestamp>)")
    parser.add_argument("--markdown", action="store_true", help="Also generate a Markdown report")
    parser.add_argument("--no-hermes", action="store_true", help="Skip invoking Hermes and only validate/report")
    parser.add_argument("--hermes-command", default="hermes", help="Hermes executable/command to invoke")
    args = parser.parse_args(argv)

    evals = discover_eval_files(args.paths)
    if not evals:
        print("No EVAL.yaml files found", file=sys.stderr)
        return 1
    hermes_command = None if args.no_hermes else args.hermes_command
    results = [run_eval(path, output_root=args.output_root, hermes_command=hermes_command) for path in evals]
    prefix = Path(args.report) if args.report else Path(args.output_root) / f"report-{time.strftime('%Y%m%d-%H%M%S')}"
    html, md = render_reports(results, prefix, markdown=args.markdown)
    print(f"HTML report: {html}")
    if md:
        print(f"Markdown report: {md}")
    return 0 if all(r.passed for r in results) else 2


if __name__ == "__main__":
    raise SystemExit(main())
