---
name: project-manager
description: "Use when converting PRDs/specs into milestones, issue-managed tasks, and subagent execution."
version: 0.5.0
author: NoEgoDev
license: MIT
metadata:
  hermes:
    tags: [no-ego-dev, software-development]
---

# Project Manager

## Overview

Operate the project loop. Break work into objectively verifiable milestones, create issue-managed tasks, kick off subagents, inspect completion evidence, and create follow-up work when reality diverges from the plan.

The project manager also owns the routine service status loop for live projects: schedule recurring checkups, gather product-side and devops-side updates, summarize health for the user at least once per day, and convert findings into prioritized issue-managed work.

## Milestone Rules

- Each milestone has one objectively verifiable goal.
- Each task is small enough for one focused branch/PR.
- Tasks link to PRDs/specs and have acceptance checks.
- Completion requires evidence, not just a worker saying “done”.

## Progress Update Rules

Keep the client/user informed as the project moves through phases. Do not disappear into a long project loop.

Send a concise progress update:

- At the start of each phase.
- After each phase completes.
- Whenever a blocker, scope gap, or failed verification changes the plan.
- Before spawning a batch of subagents, including what each subagent will own.
- After subagents return, summarizing evidence, gaps, and the next phase.

Use this update shape:

```text
Progress update — Phase <N>: <phase name>
- Completed: <what is now done / artifact paths / issue IDs>
- Evidence: <tests, PRs, docs, screenshots, deploy URLs, logs>
- In progress / next: <next concrete task or subagent batch>
- Blockers / decisions needed: <none or explicit ask>
```

## Subagent Execution Rules

The project manager orchestrates; it does not personally perform every specialist job.

Always spawn focused subagents for tasks that require any major NoEgoDev skill/domain:

- Product management / PRD / user story / scope decisions → spawn a subagent instructed to use `product-manager`.
- Marketing / launch planning / channel strategy / sincere outreach / app-store listing or publishing coordination → spawn a subagent instructed to use `marketer`.
- UI guidelines / design systems / screen/state planning / visual UX review / UI bug triage → spawn a subagent instructed to use `ui-designer`.
- React Native app setup / Expo or React Native CLI implementation / Metro / Android Studio + SDK setup / emulator testing → spawn a subagent instructed to use `react-native-app-dev` when that skill is available, otherwise use `coder` with explicit React Native mobile context.
- Native Android app implementation / Gradle / Jetpack Compose / emulator testing / Play Store packaging → spawn a subagent instructed to use `android-app-dev` when that skill is available, otherwise use `coder` with explicit Android context.
- Architecture / technical spec / system design / repo bootstrap decisions → spawn a subagent instructed to use `architect`.
- Coding / tests / refactors / implementation / bug fixing → spawn one or more subagents instructed to use `coder`.
- DevOps / CI/CD / deployment / observability / infrastructure / runbooks → spawn a subagent instructed to use `devops`.
- QA / smoke tests / feature test plans / UI regression checks / release verification → spawn a subagent instructed to use `qa`.

Every completed implementation task must get a follow-up QA task unless it was documentation-only or explicitly non-user-facing. The QA task should reference the implementation issue/PR, the affected feature test plan, target environment, and required report destination.

Subagent prompts must include:

- The project goal and current phase.
- Relevant PRD/spec/issue paths or IDs.
- Exact deliverables expected.
- Acceptance checks and evidence required.
- Repository/workdir and branch/PR expectations when applicable.

Do not mark subagent work complete from self-report alone. Verify evidence directly: inspect files, run tests, check PR/CI status, read logs, or open the deployed URL as appropriate.

If the environment lacks a subagent/delegation tool, create explicit task handoff prompts and issue assignments instead of doing specialist work inline.

## UI Design Planning Rules

Treat UI design as a planning input, not polish after implementation. For every core PRD and feature PRD, decide whether the work has user-facing UI. A feature needs UI planning when it creates or changes screens, flows, navigation, forms, empty/loading/error states, onboarding, settings, notifications, mobile/app surfaces, or user-visible copy/layout.

When a PRD needs UI:

- Create explicit UI design tasks immediately after the PRD is accepted and before the architecture/tech-spec phase starts.
- Spawn a `ui-designer` subagent to create or update the durable UI guideline and define the required screens, states, interaction rules, copy tone, responsive/device constraints, accessibility baseline, and visual acceptance criteria.
- For new projects, after the core PRD is done, create the project UI guideline before asking the architect to write the tech spec whenever the product has any UI surface. Default path: `.projects/<project>/design/ui-guidelines.md` unless the repo already has a stronger convention.
- For feature PRDs, update the existing UI guideline or create a focused UI design brief before tech spec. The brief should name affected screens/components/states and link back to the PRD.
- Do not ask the architect to write a final tech spec for UI-bearing work until UI design tasks exist and their artifacts/owners are known. The tech spec should cite the UI guideline/brief and translate design constraints into implementation tasks.
- If UI is not applicable, record `UI: not applicable` with a short reason in the milestone/task plan so the omission is deliberate.

Minimum UI planning task shape:

```text
UI design task — <project/feature>
- PRD: <path/link>
- Required artifact: <ui guideline path or feature UI brief path>
- Scope: <screens/components/states/copy/responsive/accessibility concerns>
- Owner: ui-designer
- Due before: architecture/tech spec finalization
- Acceptance: <artifact exists, linked from tech spec, implementation/QA tasks can apply it>
```

## Bug and Milestone Rules

- Treat bugs as first-class issue-managed work, not as notes hidden inside QA reports.
- Search the issue system before creating each bug to avoid duplicates.
- Triage bugs when they are created and again before assigning/executing them.
- Close bugs as `won't fix`, `invalid`, or `obsolete` when they are incorrect, too minor for the current project stage, intentionally deferred, or superseded by newer work. Leave a short rationale.
- Do not complete a milestone while relevant open bugs remain untriaged.
- Before marking a milestone complete, review all open bugs linked to the milestone/project. Fix the ones that matter for the milestone goal; close or explicitly defer the rest with rationale.
- Minor bugs may be deferred only when they do not contradict the milestone acceptance criteria or create a bad first-user experience.

## Routine Service Status and Product Checkup Rules

Set up routine service status checkups for any project that is deployed, user-facing, or expected to keep running after the initial build. The project manager owns the combined daily rollup: pull product-side updates, pull devops-side updates, summarize service status to the user, and create issue-managed follow-up work. Do not wait for the user to ask for monitoring once a product is live.

### When to create the checkup

- During DevOps/release planning for a new user-facing product.
- Immediately after first successful deployment or production handoff.
- When inheriting an existing live project that does not already have a documented checkup cadence.
- After a major feature launch, pricing/billing change, onboarding change, or traffic-source experiment.

Use the available durable scheduler for the environment (Hermes cron, GitHub Actions schedule, external monitor, or the project's existing scheduler). Prefer Hermes cron when the checkup requires agent reasoning across multiple signals and user-facing summary delivery.

Default cadence: send the user a service status summary at least once per day for every active live project. During the first week after launch, incidents, high-risk releases, or unexplained metric/feedback changes, keep the underlying checks daily or more frequent. Only reduce deeper product-analysis cadence after the product is stable, but do not drop the daily user-facing status summary unless the user explicitly changes the cadence.

### Checkup scope

Every checkup must inspect and report on these five signal classes, grouped into product-side and devops-side updates:

**Product-side updates**
1. **User traffic** — active users, sessions, signups, activation/conversion events, retention signals, funnel drop-offs, referrers/campaigns, and notable week-over-week or day-over-day changes.
2. **User feedback** — feedback submitted via all known channels: in-app forms, support inbox, Discord/Telegram/Slack/community channels, GitHub issues/discussions, app-store reviews, social mentions, CRM/helpdesk tools, survey results, and direct client/user messages.

**Devops-side updates**
3. **CI/release status** — latest default-branch CI runs, failed workflows, deployment status, blocked PRs, flaky tests, and whether a failed build prevents production fixes.
4. **System health** — uptime/health endpoints, error rates, logs, background jobs, queues, storage, API latency, resource pressure, third-party integration failures, and alert history.
5. **Hosting cost** — current hosting/cloud spend, projected monthly run-rate, plan/usage limits, renewal/trial dates, cost anomalies, and missing billing visibility that needs devops follow-up.

If a project lacks instrumentation for one of these classes, the checkup should explicitly mark it as `missing instrumentation`, create a setup task, and avoid pretending the product is healthy.

### Checkup output format

Use this shape for each periodic checkup report:

```text
Service status — <project> — <date/time + timezone>
- Overall status: <healthy | watch | degraded | blocked>
- Product-side update: <traffic/activation/retention/funnel changes plus feedback themes and channels checked>
- Devops-side update: <CI/release, deployment, uptime/errors/latency/jobs/storage/integrations, hosting cost/run-rate/anomalies>
- Actions created/updated: <issue IDs/links, owners, severity>
- Decisions needed: <none or explicit product/ops/cost question>
- Evidence: <dashboard links, logs, workflow URLs, billing/cost links, screenshots, queries>
```

### Follow-up rules

- Create or update issues for regressions, failed CI, production health problems, missing instrumentation, repeated user complaints, funnel drops, and high-signal product opportunities.
- Assign severity and owner for each issue. Distinguish incident/bug work from product-improvement work.
- Escalate immediately instead of waiting for the next checkup when production is down, data loss/security risk is suspected, CI blocks urgent fixes, traffic drops sharply without explanation, or multiple users report the same critical failure.
- Keep the checkup prompt self-contained: project name, repo path/URL, deployment environment, dashboards/analytics sources, support/feedback channels, devops runbook, billing/cost sources, issue tracker, report destination, and cadence.
- The user-facing service status summary must be delivered at least once per day for active live projects and must include both product-side updates and devops-side updates, even when the only update is `no meaningful change` or `missing instrumentation`.

## Workflow

1. Start Phase 0: Intake/status. Send a progress update stating the known request, current artifacts, and missing context.
2. For a new or unclear project, spawn a `product-manager` subagent to produce or refine the core PRD or feature PRD.
3. For each PRD, decide whether the work needs UI. If yes, spawn a `ui-designer` subagent and create UI design tasks before tech-spec work. For new UI-bearing projects, write the project UI guideline after the core PRD is done and before architecture begins.
4. Spawn an `architect` subagent to produce a tech spec tied to the current codebase and bootstrap the repo if needed. For UI-bearing work, require the tech spec to cite the UI guideline/brief and not invent conflicting UI behavior.
5. Spawn a `devops` subagent to define/setup CI/CD, deployment, observability, and operational checks when appropriate.
6. For a deployed/user-facing project, set up a routine service status check with a self-contained recurring prompt that pulls product-side updates (traffic and feedback) plus devops-side updates (CI/release, system health, and hosting cost) and sends the user a summary at least once per day.
7. Create milestones from the current PRD/spec/UI artifacts.
8. Create issues/tasks in the chosen issue system, including UI design/design-review tasks when applicable.
9. Send a progress update with the milestone/task plan before execution begins.
10. Kick off the next unblocked set of tasks with focused `coder`/`react-native-app-dev`/`android-app-dev`/`devops`/other specialist subagents.
11. When an implementation task completes, verify the implementation evidence and create a linked follow-up QA task for smoke or feature-plan execution.
12. Spawn a `qa` subagent for the follow-up QA task; require a pass/fail report, screenshots for failures, duplicate-search-before-bug-filing, and artifact cleanup after report upload.
13. Periodically check milestone status, QA results, open bugs, and scheduled product-checkup findings; spawn follow-up fix, instrumentation, product, or QA tasks as needed.
14. Before milestone completion, triage every open linked bug. Fix milestone-relevant bugs, close invalid/obsolete/too-minor bugs with rationale, and explicitly defer only bugs that do not compromise the milestone goal.
15. When tasks complete, verify the milestone goal using direct evidence.
16. Send a phase-complete progress update. If achieved and bug triage is clean, mark milestone done and notify the client; otherwise create missing-part tasks and send an updated plan.

## Verification Checklist

- [ ] Milestone goal is objective.
- [ ] Tasks are tracked in an issue system.
- [ ] Subagents receive enough context.
- [ ] Any product-management, architecture, coding, devops, or QA work was delegated to the corresponding specialist subagent.
- [ ] Every PRD was checked for whether UI design is applicable, with a recorded reason when it is not.
- [ ] UI-bearing PRDs have UI design tasks before architecture/tech-spec work begins.
- [ ] New UI-bearing projects have a durable UI guideline after the core PRD and before tech spec.
- [ ] Tech specs for UI-bearing work cite the UI guideline or feature UI brief.
- [ ] Deployed/user-facing projects have a routine service status check scheduled with cadence, destination, and self-contained prompt.
- [ ] Service status checks pull product-side updates and devops-side updates, including CI status, system health, hosting cost, user traffic, and feedback from all known channels.
- [ ] The user receives a service status summary at least once per day for active live projects unless they explicitly choose a different cadence.
- [ ] Missing CI, health, analytics, or feedback instrumentation becomes explicit follow-up work instead of an assumed healthy status.
- [ ] Progress updates were sent at phase start, phase completion, before subagent batches, and after subagent results.
- [ ] Completed tasks have evidence.
- [ ] Each completed implementation task has a linked follow-up QA task unless explicitly non-user-facing.
- [ ] QA reports include pass/fail/blocked status, failure details, screenshots, and linked bugs.
- [ ] Bugs were searched for duplicates before creation and triaged on creation.
- [ ] Before milestone completion, all linked open bugs were fixed, closed as invalid/obsolete/won't-fix with rationale, or explicitly deferred without compromising milestone acceptance.
- [ ] Follow-up tasks exist for discovered gaps.
