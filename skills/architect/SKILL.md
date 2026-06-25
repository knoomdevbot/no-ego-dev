---
name: architect
description: "Use when turning a PRD into a technical spec or reconstructing missing architecture docs from a codebase."
version: 0.2.0
author: NoEgoDev
license: MIT
metadata:
  hermes:
    tags: [no-ego-dev, software-development]
---

# Architect

## Overview

Translate product intent into a technical plan that a coder can implement safely. The architect reads the current codebase first, then writes specs grounded in reality. For user-facing products, the architecture must include a practical way to capture and review product metrics, not just ship features.

## Tech Spec Contents

- Current architecture summary.
- Components to add/change/remove.
- Component interfaces: APIs, function signatures, events, contracts.
- Database schema or persistence changes.
- Data flow and error handling.
- Security, privacy, and operational concerns.
- Product metrics instrumentation: analytics events, schemas/properties, capture points, dashboard/reporting path, retention/privacy constraints, and ownership.
- Hosting/deployment provider options that support the required stack, including tradeoffs and a recommended default.
- Test and rollout plan.

## Product Metrics Instrumentation

For any user-facing product or feature, include a minimal metrics architecture that lets the product manager and project manager tell whether the product is working after launch. Tie instrumentation to the PRD's value proposition, critical user journey, and success metrics.

The tech spec must define:

- Event/funnel capture points for activation, core CUJ completion, conversion/revenue when applicable, engagement/retention when repeated use matters, and feature-specific success metrics.
- Event names and required properties, with privacy-safe user/session identifiers and no sensitive raw payloads.
- Where events are emitted in the codebase: frontend interactions, backend API success/failure, background jobs, billing/webhook events, or integrations.
- Storage/analytics destination: existing analytics tool, warehouse/table, logs-to-metrics pipeline, or a lightweight MVP dashboard. Prefer existing tooling unless the PRD requires a new analytics provider.
- Dashboard/report path and review owner/cadence, coordinated with the product-manager metrics plan and project-manager status reporting.
- Backfill/baseline strategy when launching into an existing product, and how missing instrumentation will be detected.
- Tests or QA checks that prove metrics fire only once, fire on success/failure as intended, and do not leak private data.

If the repo has no analytics foundation, choose the smallest viable instrumentation path for the product stage and create explicit implementation tasks. Do not leave metrics as a vague future concern.

## Hosting Provider Selection

When the architecture depends on deployment constraints, choose or suggest the easiest-to-maintain viable hosting provider. Cost matters too: prefer providers with low operational overhead, predictable pricing, and generous free/low-cost tiers when they still satisfy the product requirements.

Process:

1. Identify the required stack from the PRD/codebase: frontend framework, backend/runtime, database, queues/workers, storage, realtime/websockets, cron, GPU/AI needs, regions/compliance, and expected scale.
2. Filter out providers that cannot support those requirements without awkward workarounds.
3. Select a recommended default that is easiest to maintain for the user and product stage, factoring in cost, existing accounts/infrastructure, deployment ergonomics, logs/rollback, and secret/environment management.
4. If more than one provider is plausible or the choice has meaningful tradeoffs, present 2-4 viable options and recommend one. Otherwise, choose the recommended provider and proceed.
5. Ask the user to choose only when provider choice materially affects cost, architecture, compliance, or account access.

Decision template:

```text
This stack needs <required capabilities>.
Recommended hosting provider: <Provider A> because it is the easiest viable option to maintain and should cost <cost expectation> at MVP scale.
Key tradeoff: <tradeoff>.
Alternatives considered: <Provider B> (<reason rejected/less ideal>), <Provider C> (<reason rejected/less ideal>).
```

If user choice is required:

```text
This stack needs <required capabilities>. The viable hosting options are:
1. <Provider A> — recommended; easiest to maintain because <reason>; cost: <cost expectation>; tradeoff: <tradeoff>.
2. <Provider B> — best for <reason>; cost: <cost expectation>; tradeoff: <tradeoff>.
3. <Provider C> — best for <reason>; cost: <cost expectation>; tradeoff: <tradeoff>.

Recommended default: <Provider A> because it minimizes maintenance while keeping MVP costs low.
Which hosting provider should we design for?
```

Default heuristics:

- Static/frontend/Next.js-first apps → prefer Vercel when low ops matters, unless backend/runtime needs make a full-stack host simpler.
- Full-stack apps with simple web services/databases/workers → prefer Render or Railway; choose the one that best matches the repo and expected always-on cost.
- Small containerized apps, websocket apps, or long-running services → consider Fly.io or Render, but avoid Kubernetes/cloud primitives unless needed.
- Strict enterprise/compliance or existing infra → prefer the user's current cloud/provider if it avoids new operational burden.
- AWS/GCP/Azure are usually not the MVP default unless the user already operates there or needs a managed service only they provide.

Do not finalize provider-specific architecture, secrets, CI/CD, or deployment layout until a provider has been chosen by the agent or by the user when tradeoffs require user input.

## Workflow

1. Inspect the repository and existing project knowledge.
2. Create retrospective specs for key components if missing.
3. Choose the simplest sustainable architecture.
4. Add product-metrics instrumentation tied to the PRD success metrics and CUJ, including event capture points, analytics destination, dashboards/reports, privacy constraints, and tests.
5. Identify hosting/runtime requirements and choose or suggest the easiest-to-maintain compatible hosting provider, factoring in MVP cost.
6. Ask the user to choose only when provider choice materially affects cost, architecture, compliance, or account access.
7. Name every affected component and interface.
8. Save the spec under `.projects/<project>/tech-specs/`.

## Verification Checklist

- [ ] Spec is grounded in current code.
- [ ] Required hosting/runtime capabilities are identified.
- [ ] User-facing products/features have a product-metrics instrumentation plan tied to the PRD success metrics and CUJ.
- [ ] Event names/properties, capture points, analytics destination, dashboard/report path, and owner/cadence are explicit.
- [ ] Metrics privacy constraints and tests/QA checks are included.
- [ ] The recommended hosting provider is the easiest viable option to maintain for this product stage.
- [ ] MVP cost expectations and provider tradeoffs are stated.
- [ ] User is asked to choose only when provider choice materially affects cost, architecture, compliance, or account access.
- [ ] Affected components and interfaces are explicit.
- [ ] Schema/data migrations are described when relevant.
- [ ] Tests and rollout are included.
