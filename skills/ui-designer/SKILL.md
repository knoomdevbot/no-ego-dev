---
name: ui-designer
description: "Use when creating project UI guidelines, reviewing implemented UI against those guidelines, identifying visual/UX/accessibility inconsistencies, and filing UI bugs in the issue system."
version: 0.1.0
author: NoEgoDev
license: MIT
metadata:
  hermes:
    tags: [no-ego-dev, ui-design, product-design, qa]
    related_skills: [product-manager, qa, project-manager]
---

# UI Designer

## Overview

Own the product's visual and interaction quality bar. Create a durable UI guideline for the project, review real implemented screens against that guideline, and turn UI defects into actionable issue-managed bugs.

UI design work is not only aesthetics. Good UI guidance makes the product easier to use, consistent across screens, accessible enough for real users, and feasible for the codebase/design system that exists.

## Durable UI Artifact Locations

Prefer project-local artifacts so future product, coding, and QA agents can reuse them:

- UI guideline: `.projects/<project>/design/ui-guidelines.md`
- UI review reports: `.projects/<project>/design/ui-reviews/<YYYYMMDD-HHMMSS>-<scope>.md`
- UI assets/screenshots, if not attached to issues: `.projects/<project>/design/.artifacts/<review-id>/`

If the project already has a design-system or docs convention, follow it and mention the path used in the report.

## Creating a UI Guideline

Create or update the UI guideline when a project is new, when no guideline exists, before major UI implementation, or when repeated UI bugs show the existing guideline is too vague.

A useful guideline should be specific enough that a coder or QA agent can apply it without guessing. Include:

- Product context: target user, core user journey, product tone, and primary jobs-to-be-done.
- Layout principles: page structure, spacing rhythm, content density, responsive breakpoints, navigation, and hierarchy.
- Visual language: typography, color roles, contrast expectations, elevation/borders, icons, imagery, and motion restraint.
- Components and states: buttons, forms, inputs, tables/lists, cards, modals, empty/loading/error/success states, toasts, and destructive actions.
- Accessibility basics: keyboard reachability, focus states, visible labels, contrast, target sizes, reduced-motion concerns, and semantic headings where applicable.
- Copy and microcopy: tone, button labels, empty-state copy, error messages, confirmation text, and formatting conventions.
- Do / don't examples when helpful.
- Open questions and intentionally deferred design decisions.

Do not invent a massive design system when the project needs a small MVP. Start with the smallest durable guideline that prevents inconsistent implementation.

## Reviewing UI Against the Guideline

Review the real UI, not only code. Use screenshots, browser inspection, local/staging/production URLs, storybook, previews, or existing QA artifacts as available.

1. **Orient**
   - Identify project, target environment, review scope, relevant PRD/issue/PR, and current UI guideline path.
   - If no guideline exists, create a minimal one first or explicitly mark the review as `baseline UI review without guideline` and create a follow-up guideline task.

2. **Collect evidence**
   - Capture screenshots for every screen/state reviewed, especially failures.
   - Include viewport/device, browser, URL, timestamp, commit/build if known, and console/network notes when relevant.
   - Check key responsive widths when the UI is user-facing or mobile-relevant.

3. **Compare against the guideline**
   - Look for mismatches in layout, spacing, hierarchy, typography, color roles, component variants, copy tone, states, accessibility basics, and responsive behavior.
   - Separate objective guideline violations from subjective preferences. If the guideline is ambiguous, file or create a guideline-improvement task rather than pretending the UI is wrong.

4. **Prioritize findings**
   - **Critical**: UI causes data loss, security/privacy confusion, impossible checkout/auth/core workflow, or blocks a launch-critical path.
   - **High**: confusing or broken core journey, inaccessible primary action, severe responsive failure, or misleading state/error.
   - **Medium**: inconsistent component/state/copy that degrades trust or comprehension but has a workaround.
   - **Low**: cosmetic polish, minor spacing/alignment, or guideline cleanup that does not affect comprehension.

5. **File actionable UI bugs**
   - Search the issue system before filing to avoid duplicates.
   - File or update an issue for each real fixable defect. Group small related polish issues only when they share one screen/component and one owner.
   - Link to the guideline section that defines expected behavior when possible.

## UI Bug Template

```text
Title: [UI] <screen/component> <specific problem>

Environment:
- URL/environment:
- Browser/device/viewport:
- Build/commit/version if known:

Severity: <critical/high/medium/low>

Guideline reference:
- <path + section, or "baseline review / guideline missing">

Steps to observe:
1.
2.
3.

Expected UI:

Actual UI:

Evidence:
- Screenshot(s): <links or attachments>
- Review report: <link/path>
- Console/network notes if relevant:

Duplicate search performed:
- Query 1:
- Query 2:
- Existing related issues:
```

## UI Guideline Template

```markdown
# UI Guidelines: <project>

Last updated:
Owner: NED UI Designer
Related PRD/spec/issues:

## Product and User Context
- Target user:
- Primary journey:
- Product tone:

## Design Principles
1.
2.
3.

## Layout and Responsive Rules
- Page shell/navigation:
- Spacing/content density:
- Breakpoints:

## Visual Language
- Typography:
- Color roles and contrast:
- Borders/elevation:
- Icons/imagery/motion:

## Components and States
- Buttons/links:
- Forms/inputs:
- Lists/tables/cards:
- Modals/toasts:
- Empty/loading/error/success states:

## Accessibility Baseline
- Keyboard/focus:
- Labels/headings:
- Target sizes:
- Reduced motion/contrast:

## Copy and Microcopy
- Voice/tone:
- CTA labels:
- Error/empty-state conventions:

## Open Questions / Deferred Decisions
-
```

## UI Review Report Template

```markdown
# UI Review: <scope>

Status: PASS | FAIL | BLOCKED
Date/time:
Reviewer: NED UI Designer
Environment:
Guideline: <path/link>
Related issue/PR/milestone:

## Summary
- Screens/states reviewed:
- Overall assessment:
- Bugs filed/updated:
- Guideline updates needed:

## Findings
### <finding title>
Severity: critical | high | medium | low
Status: filed | duplicate updated | no issue filed
Guideline reference:
Expected:
Actual:
Evidence:
Issue:

## Screenshots / Evidence Index
-

## Follow-ups
-
```

## Common Pitfalls

1. **Reviewing from taste instead of guidelines.** Personal preference is not a bug. Tie findings to the guideline, user journey, accessibility, or clear product comprehension impact.
2. **Skipping the guideline.** If no guideline exists, create a minimal one before serious review or file the missing guideline as a blocker/follow-up.
3. **Filing vague UI bugs.** "Make it look better" is not actionable. Include screen, expected behavior, actual behavior, screenshot, severity, and guideline reference.
4. **Ignoring states.** Loading, empty, error, disabled, success, hover/focus, and responsive states often carry the most user-facing UI bugs.
5. **Duplicating QA without design judgment.** QA proves flows work; UI design reviews judge consistency, hierarchy, clarity, accessibility basics, and polish against the product's intended experience.

## Verification Checklist

- [ ] UI guideline exists or was updated at a durable project path.
- [ ] Guideline covers layout, visual language, components/states, accessibility basics, and copy tone.
- [ ] Review used the real implemented UI or documented why it was blocked.
- [ ] Screenshots/evidence were captured for reviewed failures.
- [ ] Findings are tied to guideline sections, user journey impact, or accessibility/product clarity.
- [ ] Duplicate search was performed before filing UI bugs.
- [ ] UI bugs include severity, repro/observation steps, expected vs actual, screenshot evidence, and guideline reference.
- [ ] Review report names durable artifact paths and follow-up issues.
