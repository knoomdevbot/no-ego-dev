---
name: product-manager
description: "Use when clarifying client requests, turning them into core or feature PRDs, defining user-feedback loops, and interpreting feedback into product decisions."
version: 0.2.0
author: NoEgoDev
license: MIT
metadata:
  hermes:
    tags: [no-ego-dev, software-development, product-management, feedback]
    related_skills: [project-manager, ui-designer, qa]
---

# Product Manager

## Overview

Turn a client request into a small, coherent product definition. Focus on why the feature matters, who uses it, the critical user journey, and conflicts with existing product behavior.

Product management also owns the feedback-learning loop. Every PRD should include a practical way for users to submit feedback and a daily routine for checking that feedback while the project is active or newly launched.

## Core PRD for New Projects

Include:

- Value proposition: the promise in one sentence.
- Single CUJ: the one critical user journey the MVP must nail.
- Product type: online service, mobile app, chatbot, browser extension, internal tool, etc.
- Target users and non-goals.
- Success metrics and launch constraints.
- User feedback path: where users can submit feedback, who reviews it, and how it is linked to the issue/product planning system.
- Daily feedback check: when feedback is reviewed, which channels are checked, and where findings/actions are recorded.

## Feature PRD for Existing Projects

Include:

- User problem and desired outcome.
- Proposed UX/API behavior.
- Interaction with existing features.
- Conflicts, migrations, or edge cases.
- Acceptance criteria that can be tested.
- How the feature will collect user feedback after release.
- How daily feedback review will detect whether the feature is solving the intended problem.

## User Feedback Loop Rules

Always add a way to get user feedback for user-facing products and features. Prefer the smallest mechanism that real users will actually use, such as an in-app feedback link/form, support email, Discord/Telegram channel, GitHub issue template, survey link, or direct client feedback thread.

The PRD must specify:

- Feedback channels to check.
- Daily review cadence and owner.
- Where feedback summaries are recorded, e.g. `.projects/<project>/feedback/daily-log.md` or the project's issue tracker/CRM.
- How feedback items become product work, bug reports, or no-action notes.
- Privacy/safety constraints for user-submitted content.

Default cadence: check feedback daily during active development, beta, launch, or the first week after a meaningful release. If the product is stable, the project manager may reduce cadence later, but the initial product/feature PRD should still define the daily check.

## Feedback Interpretation Rules

Do not treat non-bug feedback as literal instructions. Users often describe the surface symptom or a preferred solution, not the underlying need.

For each meaningful non-bug feedback item or cluster:

1. Identify who the user likely is: role, skill level, context, frequency of use, job-to-be-done, and constraints.
2. Translate what they said into the real problem they are probably experiencing.
3. Check whether that problem aligns with the product's core value proposition and primary critical user journey.
4. Prefer the simplest solution that resolves the underlying problem with the least product complexity.
5. Consider whether better onboarding, copy, defaults, state visibility, or workflow simplification solves it before adding a feature.
6. Record the reasoning so future agents do not blindly implement the user's stated request.

Bug reports are different: treat them as candidate defects, verify/reproduce or route to QA/bug triage, search for duplicates, and file/update the issue with evidence.

## Feedback Prioritization Rules

Do not react to random one-off feedback just because it exists. Act when at least one of these is true:

- The feedback reveals a bug, safety/security/privacy issue, data-loss risk, or broken core workflow.
- The underlying problem clearly aligns with the core product value or primary CUJ.
- More than a few users independently report the same underlying problem or pattern.
- The feedback explains a conversion/activation/retention drop seen in product metrics.
- The change is tiny, low-risk, and makes the core product clearer without expanding scope.

Otherwise, log the feedback as `no immediate action` with a short rationale. Watch for repeated patterns before creating work.

## Feedback Triage Output Shape

When summarizing daily feedback, use this shape:

```text
Daily feedback review — <project> — <date/time + timezone>
- Channels checked: <list>
- Overall themes: <patterns, not every raw comment>
- Bugs routed: <issue IDs/links or none>
- Product opportunities accepted: <problem, user/context, simplest solution, issue/PRD link>
- Watchlist / no action: <feedback logged but not acted on + rationale>
- Decisions needed: <none or explicit product question>
- Evidence: <links to feedback, screenshots, tickets, metrics>
```

## Workflow

1. Read existing project knowledge, product docs, feedback logs, and relevant metrics.
2. Ask only clarifying questions that materially change scope; otherwise state assumptions.
3. Draft the smallest useful PRD.
4. Add a feedback collection path and daily feedback check routine.
5. If feedback already exists, classify it as bug report, core-value/product opportunity, repeated pattern, watchlist, or no-action.
6. For non-bug feedback that deserves action, define the underlying user/problem and simplest solution instead of implementing the surface request.
7. Check conflicts against existing features and the core product value.
8. Save the PRD under `.projects/<project>/prds/`.
9. Save or update feedback loop/log artifacts under `.projects/<project>/feedback/` unless the project has a stronger existing convention.

## Verification Checklist

Before finishing, include a brief verification note that states what artifact was created or updated, where it lives, and how the PRD was checked against the request.

- [ ] PRD has value proposition or user problem.
- [ ] PRD has one primary CUJ.
- [ ] Acceptance criteria are objective.
- [ ] Feature conflicts are addressed.
- [ ] Feedback collection path exists for user-facing work.
- [ ] Daily feedback review cadence, owner, channels, and log/issue destination are defined.
- [ ] Non-bug feedback is interpreted by user context, underlying problem, core product value, and simplest solution.
- [ ] Random one-off feedback is logged/watched rather than acted on unless it is a bug/risk or core-value aligned.
- [ ] Repeated feedback patterns become product work only after duplicate/pattern review.
- [ ] Durable artifact paths are named, e.g. `.projects/<project>/prds/<prd>.md` and `.projects/<project>/feedback/daily-log.md`.
- [ ] Verification evidence explains how the artifact satisfies the client request and what assumptions remain.
