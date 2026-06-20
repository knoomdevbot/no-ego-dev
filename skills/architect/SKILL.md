---
name: architect
description: "Use when turning a PRD into a technical spec or reconstructing missing architecture docs from a codebase."
version: 0.1.0
author: NoEgoDev
license: MIT
metadata:
  hermes:
    tags: [no-ego-dev, software-development]
---

# Architect

## Overview

Translate product intent into a technical plan that a coder can implement safely. The architect reads the current codebase first, then writes specs grounded in reality.

## Tech Spec Contents

- Current architecture summary.
- Components to add/change/remove.
- Component interfaces: APIs, function signatures, events, contracts.
- Database schema or persistence changes.
- Data flow and error handling.
- Security, privacy, and operational concerns.
- Test and rollout plan.

## Workflow

1. Inspect the repository and existing project knowledge.
2. Create retrospective specs for key components if missing.
3. Choose the simplest sustainable architecture.
4. Name every affected component and interface.
5. Save the spec under `.projects/<project>/tech-specs/`.

## Verification Checklist

- [ ] Spec is grounded in current code.
- [ ] Affected components and interfaces are explicit.
- [ ] Schema/data migrations are described when relevant.
- [ ] Tests and rollout are included.
