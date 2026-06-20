---
name: devops
description: "Use when setting up CI/CD, deployments, environment management, or operational health checks."
version: 0.1.0
author: NoEgoDev
license: MIT
metadata:
  hermes:
    tags: [no-ego-dev, software-development]
---

# Devops

## Overview

Make the product shippable and observable. NED devops chooses boring, reliable automation before clever infrastructure.

## Responsibilities

- CI pipeline for tests, lint, type checks, build, and security basics.
- CD pipeline or documented deploy command.
- Environment variable and secret handling.
- Preview/staging/production environment strategy.
- Monitoring, logs, health checks, and rollback plan.

## Workflow

1. Inspect stack, hosting constraints, and existing pipelines.
2. Add the smallest CI workflow that blocks broken code.
3. Add deployment automation appropriate for the product stage.
4. Document required secrets as names only; never commit secret values.
5. Add health checks and operational runbook.
6. Verify by running CI locally where possible and checking remote status.

## Verification Checklist

- [ ] CI runs tests/build on pull requests.
- [ ] Secrets are documented but not committed.
- [ ] Deploy path is reproducible.
- [ ] Health/rollback docs exist.
