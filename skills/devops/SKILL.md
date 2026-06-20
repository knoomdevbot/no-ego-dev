---
name: devops
description: "Use when setting up CI/CD, deployments, environment management, or operational health checks."
version: 0.4.0
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

Before designing CI/CD or deployment, check whether the agent already has working access to the essential external tools. Devops work should begin with an **upfront access request** that covers the whole deployment/operations lifecycle, not one small permission request at a time.

Essential access usually means:

- **GitHub** or the repository host: permission to read/write the repo, create branches/PRs, configure Actions, manage environments, and add repository secrets.
- **Cloud/deployment provider**: permission to create/manage the app, services, databases, storage, environment variables, deploy hooks, logs, domains, rollback settings, and billing-safe resource settings.
- **Optional but common**: package registry, database provider, DNS provider, error monitoring, uptime monitoring, analytics/observability tools, and third-party APIs used by the app.

Ask once, upfront, for the complete set of access needed to deploy and manage the service end-to-end. The goal is to let the agent perform all normal devops operations—CI/CD, staging/prod deploys, secrets setup, logs, monitoring, rollback, domain wiring, and incident checks—without repeatedly stopping to ask the user for each permission. Prefer CLI/API access to hosting, DNS, and cloud providers so the full setup can be driven from chat after the user completes a one-time login or key-creation step. Use owner/admin/collaborator access to the specific project/team/repo/provider when that is the simplest safe option; otherwise request scoped API keys/tokens or CLI/browser auth with the minimum scopes that cover the full lifecycle.

Do not ask the user to paste broad secrets into chat. Prefer:

- user authenticates the local CLI/browser session for providers with official CLIs;
- user creates provider API keys through the provider dashboard and stores them in the local profile `.env`, CI secret store, or provider secret manager after being guided step by step;
- user adds the agent/user account as a repo/cloud collaborator with the required role;
- user creates scoped tokens and stores them directly in the appropriate secret manager;
- user confirms non-secret identifiers such as project/team/service names after access is granted.

## Upfront Access Request

When access is missing, choose the simplest option for the user and give step-by-step instructions. Do not dump a menu of every cloud provider unless the product constraints require it.

Default recommendations:

- GitHub access: ask the user to authenticate the local `gh` CLI or add the agent/user account as a collaborator.
- Frontend/static/Next.js app: prefer Vercel unless the user already has another provider.
- Full-stack app/API with simple managed deploy: prefer Render, Railway, or Fly.io based on the stack and existing account; choose one and explain why.
- Existing cloud account/project: use the user's current provider rather than migrating.
- Hosting, DNS, domain registrar, and infrastructure providers such as GoDaddy, Cloudflare, Render, Railway, Fly.io, Vercel, AWS, GCP, Azure, Supabase, Neon, or similar: prefer official CLI/API access over manual dashboard work when available.

## CLI/API Provider Access Setup

For hosting providers, DNS providers, registrars, and managed infrastructure, make the setup doable via chat by guiding the user through one short provider-specific credential flow, then doing the remaining work with CLI/API commands.

Default process:

1. Identify the exact provider, account, project/domain/service, and required operations: create app, deploy, set env vars, manage DNS/domain, inspect logs, rollback, create database/storage, or manage monitoring.
2. Check for an official CLI first. If available, ask the user to run or approve the login command and complete browser/device-code authentication. Examples: `vercel login`, `fly auth login`, `railway login`, `render login`, `supabase login`, `wrangler login`, `gh auth login`.
3. If there is no suitable CLI, use the provider API. Guide the user step by step through creating a scoped API key/token from the provider dashboard. Ask for the minimum scopes needed for the full devops lifecycle, not a read-only token that will fail mid-task.
4. Tell the user exactly where to put the token so the setup remains chat-driven and repeatable: local profile `.env`, GitHub Actions secret, provider secret manager, or a password-manager-backed CLI prompt. Avoid raw token values in chat when possible; if chat is the only path, ask for a short-lived or revocable scoped token and rotate/remove it after use.
5. Verify access immediately with a harmless CLI/API call such as `whoami`, account/domain list, project list, or read-only GET before making changes.
6. Continue using CLI/API for the actual setup and report the exact resources created/changed.

Provider API-key instruction template:

```text
I can complete the <provider> setup from chat if you create one scoped API key for me.

Please do this:
1. Open <provider dashboard URL>.
2. Go to <exact menu path, e.g. Account Settings → API Keys>.
3. Click <Create API Key/Token>.
4. Name it: <project>-ned-devops.
5. Grant these scopes only: <scopes needed for deploy/DNS/env/logs/etc.>.
6. Save it into <exact destination, e.g. this machine's NED profile .env as PROVIDER_API_KEY, GitHub secret PROVIDER_API_KEY, or provider secret manager>. Do not commit it.
7. Tell me the non-secret identifiers I need: <account id/team id/domain/project/service names>.

After that I will verify access with <CLI/API command> and finish the setup via CLI/API.
```

Example for GoDaddy DNS/domain automation:

```text
I can manage the GoDaddy DNS setup from chat if you create a GoDaddy production API key and secret.

Please do this:
1. Open https://developer.godaddy.com/keys.
2. Sign in to the GoDaddy account that owns the domain.
3. Click Create New API Key.
4. Name it: <project>-ned-devops.
5. Choose Environment: Production.
6. Copy the API key and secret once.
7. Store them in the NED profile environment as GODADDY_API_KEY and GODADDY_API_SECRET, or approve me to add them to the local profile .env if you provide short-lived/revocable values.
8. Tell me the domain name and any required record targets, such as the provider's CNAME/A/AAAA values.

I will verify with a read-only GoDaddy API request for the domain records before changing DNS, then create/update only the required records and report the before/after state.
```

For every provider, include revocation/cleanup guidance in the runbook: where the token lives, what scope it has, how to rotate it, and when it can be deleted.

Access request template:

```text
I need upfront access to <repo/provider/tooling> so I can deploy and manage <service/project> end-to-end without interrupting you for every devops operation.

Please grant access for these operations:
- Repository/CI: read/write code, create branches/PRs, edit GitHub Actions/workflows, manage repo environments, and add/update repository or environment secrets.
- Deployment provider: create/manage apps/services, staging and production environments, env vars/secrets, deploy hooks, logs, domains, rollback/redeploys, and billing-safe resource settings.
- Supporting systems if used: database/storage, DNS, package registry, monitoring/error tracking/uptime alerts, and third-party API dashboards.

Easiest path:
1. <open URL or run command>
2. <click/select exact option>
3. <grant exact role/scope, preferably project/team/repo-scoped admin or owner if safe>
4. <confirm access by telling me non-secret project/team/service names, not passwords or raw secrets>

I will not ask for broad secrets in chat. If a token is unavoidable, create a scoped token with: <scopes>, and add it directly as <repo/cloud secret name> or authenticate the local CLI/browser session instead.
```

After the user grants access, verify it immediately with the relevant CLI/API (`gh auth status`, provider whoami/project list, DNS/domain read, repo secret/environment visibility where possible) and continue without asking again unless a new external system or stronger permission is genuinely required.

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

Concrete cloud-provider steps should be provider-specific, CLI/API-first, and minimal. Example for Vercel:

1. Open Vercel → project/team dashboard.
2. Import or select the GitHub repo.
3. Grant GitHub integration access only to that repo if possible.
4. Add required environment variables in Vercel Project Settings → Environment Variables.
5. Tell the agent the Vercel project URL and which environment(s) are configured.

When Vercel CLI access is available, prefer:

```bash
vercel login
vercel whoami
vercel projects ls
```

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
2. If end-to-end devops access is missing, make one upfront access request covering repository/CI, deployment provider, secrets/environments, logs, monitoring, rollback, domains, and supporting services needed for this project. Use the easiest-path step-by-step instructions above.
3. Prefer CLI/API access for hosting/DNS/cloud providers; guide the user step by step through login or scoped API-key creation so the rest of the setup can be completed via chat.
4. Verify granted access immediately with CLI/API checks, then proceed without repeated permission prompts unless a new external system or stronger permission is genuinely required.
5. Add the smallest CI workflow that blocks broken code.
6. Configure separate staging and production environments, including separate secrets/env var namespaces.
7. Add deployment automation that auto-deploys staging after CI passes on the integration branch.
8. Add a safe production deployment path with an explicit approval/tag/manual trigger unless the user asks for fully automatic production deploys.
9. Document required secrets as names only; never commit secret values.
10. Create or update the per-project deployment and system monitoring runbook at `.projects/<project>/runbooks/deployment-and-monitoring.md`.
11. Add health checks and operational runbook details.
12. Verify by running CI locally where possible, checking staging deployment status, and confirming the production deploy path and monitoring setup are documented.

## Verification Checklist

- [ ] CI runs tests/build on pull requests.
- [ ] End-to-end devops access was checked upfront across repository/CI, deployment provider, secrets/environments, logs, monitoring, rollback, domains, and supporting services.
- [ ] If access was missing, the user received one easiest-path upfront access request broad enough to avoid repeated permission prompts during normal devops operations.
- [ ] Hosting/DNS/cloud provider setup uses CLI/API access when available, with step-by-step user guidance for login or scoped API-key creation.
- [ ] Granted access was verified with CLI/API checks before proceeding.
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
