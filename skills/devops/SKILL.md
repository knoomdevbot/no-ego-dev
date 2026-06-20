---
name: devops
description: "Use when setting up CI/CD, deployments, environment management, or operational health checks."
version: 0.2.0
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
- At least two persistent environments for every deployable product: **staging** and **production**.
- Automatic deployment to staging from the integration branch after CI passes.
- Environment variable and secret handling.
- Preview/staging/production environment strategy.
- Monitoring, logs, health checks, and rollback plan.
- Per-project deployment and system monitoring documentation.

## Access and Tooling Prerequisites

Before designing CI/CD or deployment, check whether the agent already has working access to the essential external tools. If access is missing, pause and ask the user to grant it with the easiest safe path.

Essential access usually means:

- **GitHub** or the repository host: permission to read/write the repo, create branches/PRs, configure Actions, and add repository secrets.
- **Cloud/deployment provider**: permission to create/manage the app, environment variables, deploy hooks, logs, domains, and rollback settings.
- **Optional but common**: package registry, database provider, error monitoring, DNS provider, and analytics/observability tools.

Ask for the minimum permissions needed for the current phase. Prefer short-lived CLI/browser auth, scoped tokens, or adding the user as an owner/collaborator over asking them to paste broad secrets.

## Easiest-Path Access Request

When access is missing, choose the simplest option for the user and give step-by-step instructions. Do not dump a menu of every cloud provider unless the product constraints require it.

Default recommendations:

- GitHub access: ask the user to authenticate the local `gh` CLI or add the agent/user account as a collaborator.
- Frontend/static/Next.js app: prefer Vercel unless the user already has another provider.
- Full-stack app/API with simple managed deploy: prefer Render, Railway, or Fly.io based on the stack and existing account; choose one and explain why.
- Existing cloud account/project: use the user's current provider rather than migrating.

Access request template:

```text
I need access to <tool/provider> to set up <CI/deploy/secrets/logs>.
Easiest path:
1. <open URL or run command>
2. <click/select exact option>
3. <grant exact permission/scope>
4. <tell me when done or paste only the non-secret confirmation value>

I will not ask for broad secrets unless required. If a token is unavoidable, create a scoped token with: <scopes>, and add it as <repo/cloud secret name> rather than sending it in chat.
```

Concrete GitHub steps to offer:

```bash
# Option A: authenticate this machine's GitHub CLI
gh auth login
# Choose: GitHub.com → HTTPS or SSH → authenticate in browser

gh auth status
```

Or, for repo collaborator access:

1. Open the GitHub repo → **Settings** → **Collaborators and teams**.
2. Add the agent/user GitHub account with the minimum role needed.
3. For CI/CD setup, allow Actions workflow edits and repository secret management.
4. Tell the agent the repo URL and confirm access is granted.

Concrete cloud-provider steps should be provider-specific and minimal. Example for Vercel:

1. Open Vercel → project/team dashboard.
2. Import or select the GitHub repo.
3. Grant GitHub integration access only to that repo if possible.
4. Add required environment variables in Vercel Project Settings → Environment Variables.
5. Tell the agent the Vercel project URL and which environment(s) are configured.

## Environment Strategy

Every deployable product must have at least two persistent environments:

- **Staging**: production-like environment used for integration verification, demos, QA, migration rehearsals, and smoke tests.
- **Production**: customer-facing environment with stricter approvals, monitoring, backups, and rollback expectations.

Rules:

1. Configure staging and production as separate provider environments/projects/services when the provider supports it.
2. Keep secrets and environment variables separate; never reuse production secrets in staging unless the external service has no safe staging equivalent.
3. CI/CD must auto-deploy to staging after the main integration branch passes tests/build.
4. Production deployment should be deliberate: manual approval, release tag, protected branch, or explicit deploy command depending on project maturity.
5. Document environment URLs, deploy triggers, required secrets by name, rollback steps, and smoke tests in `.projects/<project>/runbooks/`.
6. If preview environments are available, use them for PRs, but previews do not replace persistent staging.

Recommended default triggers:

- Pull request → CI + optional preview deploy.
- Merge to `main`/integration branch → CI, build, then auto-deploy to staging.
- Release tag or manual approval → deploy to production.

## Deployment and Monitoring Documentation

For each project, maintain a durable deployment and system monitoring document under `.projects/<project>/runbooks/`, preferably `.projects/<project>/runbooks/deployment-and-monitoring.md`.

The document must be created or updated whenever CI/CD, hosting, environments, secrets, health checks, logging, monitoring, alerting, rollback, or production operations change.

Required contents:

- **Environment inventory**: staging and production URLs, provider/project/service names, regions, branches/tags that deploy, and owner/contact.
- **Deployment flow**: PR checks, staging auto-deploy trigger, production deploy trigger/approval, migration steps, smoke tests, and rollback steps.
- **Secrets and config**: required environment variables and secret names by environment, with no secret values committed.
- **System health**: health check endpoints, uptime checks, background job checks, database/storage checks, and expected healthy signals.
- **Monitoring and alerting**: log locations, dashboards, error tracking, alert destinations/escalation path, and key metrics/SLOs for the MVP.
- **Operational procedures**: how to inspect logs, restart/redeploy services, run migrations safely, verify staging, verify production, and handle incidents.

Prefer one concise, current runbook over scattered notes. If a provider generates its own docs or dashboard links, link them from the runbook and summarize the operational steps in-repo.

## Workflow

1. Inspect stack, hosting constraints, existing pipelines, and current authenticated access.
2. If GitHub/repo-host or cloud-provider access is missing, ask the user for access using the easiest-path step-by-step instructions above.
3. Add the smallest CI workflow that blocks broken code.
4. Configure separate staging and production environments, including separate secrets/env var namespaces.
5. Add deployment automation that auto-deploys staging after CI passes on the integration branch.
6. Add a safe production deployment path with an explicit approval/tag/manual trigger unless the user asks for fully automatic production deploys.
7. Document required secrets as names only; never commit secret values.
8. Create or update the per-project deployment and system monitoring runbook at `.projects/<project>/runbooks/deployment-and-monitoring.md`.
9. Add health checks and operational runbook details.
10. Verify by running CI locally where possible, checking staging deployment status, and confirming the production deploy path and monitoring setup are documented.

## Verification Checklist

- [ ] CI runs tests/build on pull requests.
- [ ] GitHub/repo-host access was checked, or the user received easiest-path access instructions.
- [ ] Cloud/deployment-provider access was checked, or the user received easiest-path access instructions.
- [ ] The chosen provider is the easiest viable path for the user and product stage.
- [ ] Staging and production environments are configured or explicitly documented as required setup.
- [ ] Staging auto-deploys from the integration branch after CI passes.
- [ ] Production deploy is protected by manual approval, release tag, protected branch, or documented explicit command.
- [ ] Environment variables/secrets are separated by environment and documented by name only.
- [ ] Per-project deployment and system monitoring doc exists at `.projects/<project>/runbooks/deployment-and-monitoring.md` or an equivalent documented path.
- [ ] The deployment/monitoring doc includes environment inventory, deployment triggers, rollback, health checks, logs, dashboards/alerts, and operational procedures.
- [ ] Secrets are documented but not committed.
- [ ] Deploy path is reproducible.
- [ ] Health/rollback docs exist.
