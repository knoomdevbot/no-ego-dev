---
name: product-manager
description: "Use when clarifying client requests and turning them into core or feature PRDs."
version: 0.1.0
author: NoEgoDev
license: MIT
metadata:
  hermes:
    tags: [no-ego-dev, software-development]
---

# Product Manager

## Overview

Turn a client request into a small, coherent product definition. Focus on why the feature matters, who uses it, the critical user journey, and conflicts with existing product behavior.

## Core PRD for New Projects

Include:

- Value proposition: the promise in one sentence.
- Single CUJ: the one critical user journey the MVP must nail.
- Product type: online service, mobile app, chatbot, browser extension, internal tool, etc.
- Target users and non-goals.
- Success metrics and launch constraints.

## Feature PRD for Existing Projects

Include:

- User problem and desired outcome.
- Proposed UX/API behavior.
- Interaction with existing features.
- Conflicts, migrations, or edge cases.
- Acceptance criteria that can be tested.

## Workflow

1. Read existing project knowledge and product docs.
2. Ask only clarifying questions that materially change scope; otherwise state assumptions.
3. Draft the smallest useful PRD.
4. Check conflicts against existing features.
5. Save the PRD under `.projects/<project>/prds/`.

## Verification Checklist

- [ ] PRD has value proposition or user problem.
- [ ] PRD has one primary CUJ.
- [ ] Acceptance criteria are objective.
- [ ] Feature conflicts are addressed.
