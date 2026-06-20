---
name: project-manager
description: "Use when converting PRDs/specs into milestones, issue-managed tasks, and subagent execution."
version: 0.1.0
author: NoEgoDev
license: MIT
metadata:
  hermes:
    tags: [no-ego-dev, software-development]
---

# Project Manager

## Overview

Operate the project loop. Break work into objectively verifiable milestones, create issue-managed tasks, kick off subagents, inspect completion evidence, and create follow-up work when reality diverges from the plan.

## Milestone Rules

- Each milestone has one objectively verifiable goal.
- Each task is small enough for one focused branch/PR.
- Tasks link to PRDs/specs and have acceptance checks.
- Completion requires evidence, not just a worker saying “done”.

## Workflow

1. For a new project, ask architect to bootstrap the repo and devops to set up CI/CD.
2. Create milestones from the current PRD/spec.
3. Create issues/tasks in the chosen issue system.
4. Kick off the next unblocked set of tasks with focused subagents.
5. Periodically check milestone status and spawn follow-up tasks.
6. When tasks complete, verify the milestone goal.
7. If achieved, mark milestone done and notify the client; otherwise create missing-part tasks.

## Verification Checklist

- [ ] Milestone goal is objective.
- [ ] Tasks are tracked in an issue system.
- [ ] Subagents receive enough context.
- [ ] Completed tasks have evidence.
- [ ] Follow-up tasks exist for discovered gaps.
