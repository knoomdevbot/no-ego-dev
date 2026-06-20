# NED Project Workspace Rules

This repository is a Hermes profile distribution. Do not commit runtime state, secrets, auth files, logs, sessions, memory databases, caches, or local workspaces.

When editing skills, keep each skill self-contained, include an EVAL.yaml, and keep eval fixtures under that skill's evaldata/ directory.

Run `python -m pytest` before committing changes to this distribution.
