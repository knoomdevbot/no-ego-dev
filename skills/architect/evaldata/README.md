# Eval data for architect

Static fixture for deterministic evals.

Scenario: LaunchPad Lite is a user-facing SaaS MVP that helps indie founders publish a simple product-launch page and collect signups. The PRD success metrics are launch-page publish rate, share-link clicks, signup conversion, signup-form error rate, and week-one return rate. The existing repo has a Next.js frontend, a small API backend, and no complete analytics setup yet.

A good architect response should create a durable tech-spec artifact, choose or recommend maintainable hosting, and add a product-metrics instrumentation plan. The metrics plan should define event names/properties and capture points for create page → publish → share link → signup, API success/failure events for signup errors, an analytics/dashboard destination, privacy constraints for user/session IDs, ownership/review cadence, and QA/tests proving events fire once and do not include sensitive payloads. Missing analytics infrastructure should become explicit implementation work rather than a vague future TODO.
