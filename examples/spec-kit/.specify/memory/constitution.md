# Shop Platform Constitution

## Core Principles

### I. Test-First (NON-NEGOTIABLE)
Every user story ships with acceptance tests written before the implementation. Tests MUST fail before code is written and pass before the story is marked done.

### II. Server-Side Truth for Money and Stock
Prices, taxes and stock levels are computed and validated on the server only. The client MAY display them but MUST NOT be the source of any value used at checkout.

### III. Accessible by Default
All customer-facing UI MUST meet WCAG 2.1 AA. Colour MUST never be the only way information is conveyed.

### IV. Observable Behaviour
Every API endpoint emits structured logs and request metrics. Search and checkout failures MUST be traceable to a single request ID.

### V. Simplicity
Prefer the existing platform modules (catalogue, pricing, inventory, cart, checkout) over new services. Any new service or dependency MUST be justified in the plan's Complexity Tracking section.

## Additional Constraints

- Stack: TypeScript, Node.js 20, Next.js 14, PostgreSQL 15.
- All money values are stored as integer minor units (cents) with an ISO 4217 currency code.
- Personal data (addresses) is processed according to the platform privacy policy and never logged in clear text.

## Development Workflow

- Feature work follows Spec Kit: `/speckit.specify` → `/speckit.clarify` → `/speckit.plan` → `/speckit.tasks` → `/speckit.implement`.
- Every pull request references its feature spec and passes the constitution check in `plan.md`.
- Reviews verify that tests map to acceptance scenarios in `spec.md`.

## Governance

This constitution supersedes other practices. Amendments require a pull request, approval by the product owner and the tech lead, and a version bump.

**Version**: 1.0.0 | **Ratified**: 2026-10-11 | **Last Amended**: 2026-10-11
