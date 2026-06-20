---
name: project-knowledge-organization
description: "Use when starting or maintaining durable project knowledge for a client software project."
version: 0.1.0
author: NoEgoDev
license: MIT
metadata:
  hermes:
    tags: [no-ego-dev, software-development]
---

# Project Knowledge Organization

## Overview

Keep project knowledge in a predictable folder so future work starts with context. NED treats docs as part of the product, not a side quest.

## Standard Layout

```text
.projects/<project-slug>/
├── README.md                 # current project brief and links
├── decisions/                # ADR-style decisions
├── prds/                     # core and feature PRDs
├── tech-specs/               # architecture and implementation specs
├── milestones/               # milestone goals and task maps
├── runbooks/                 # deploy, ops, debug recipes
└── evidence/                 # screenshots, logs, test outputs, eval results
```

## Workflow

1. Create or locate the project slug.
2. Write `README.md` with client goal, product type, repo links, environments, and current status.
3. Record assumptions and open questions explicitly.
4. Save PRDs, specs, decisions, and verification evidence as separate files with dates.
5. Update the knowledge folder after each milestone; do not rely on chat history.

## Pitfalls

- Do not dump raw transcripts as “knowledge”. Extract decisions and constraints.
- Do not store secrets, access tokens, or private customer data unless the workspace is explicitly approved for it.
- Do not let docs drift: when implementation changes architecture, update the tech spec or add a retrospective spec.

## Verification Checklist

- [ ] Project folder exists.
- [ ] Current goal and links are in README.md.
- [ ] PRDs/specs/milestones have stable paths.
- [ ] Evidence exists for completed work.
