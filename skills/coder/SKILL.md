---
name: coder
description: "Use when implementing a tech-spec task or fixing a bug in a software repository."
version: 0.1.0
author: NoEgoDev
license: MIT
metadata:
  hermes:
    tags: [no-ego-dev, software-development]
---

# Coder

## Overview

Implement one focused task per branch. Write tests for the key path, keep the diff small, request review, iterate, merge, and clean up.

## Rules

1. Create a dedicated branch/PR for each task.
2. Read the tech spec and relevant code before editing.
3. Write unit tests for key paths; aim for useful coverage around 80%, not vanity 100%.
4. Verify with integration tests or manual UI evidence when the feature crosses boundaries.
5. Use a separate subagent to review the PR and iterate until approved.
6. A task is complete only after changes are merged to main.
7. After completion, clean up the branch and local checkout.

## Workflow

1. Confirm task scope and acceptance criteria.
2. Create branch.
3. Write or update tests first where possible.
4. Implement the minimal clean change.
5. Run targeted tests and full relevant suite.
6. Open PR with verification evidence.
7. Review, fix, merge, cleanup.

## Verification Checklist

- [ ] Branch/PR is dedicated to one task.
- [ ] Key path tests exist and pass.
- [ ] Integration/UI verification exists when needed.
- [ ] Review approved.
- [ ] Merged to main and branch cleaned.
