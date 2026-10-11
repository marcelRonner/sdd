# Implementation Plan: Find and Buy an Affordable Shoe by Colour

**Branch**: `001-red-shoe-under-90` | **Date**: 2026-10-11 | **Spec**: [spec.md](./spec.md)
**Input**: Feature specification from `/specs/001-red-shoe-under-90/spec.md`

## Summary

Add colour-family, maximum-price and size filters to shoe search, restrict results to in-stock and deliverable variants, and re-validate price and stock at checkout. Implementation extends the existing catalogue search endpoint and checkout service; colour families are introduced as a new lookup table maintained by merchandising.

## Technical Context

**Language/Version**: TypeScript 5.5, Node.js 20
**Primary Dependencies**: Next.js 14 (storefront), Fastify 4 (shop API), Prisma 5
**Storage**: PostgreSQL 15
**Testing**: Vitest (unit, contract), Playwright (end-to-end)
**Target Platform**: Web storefront (desktop and mobile browsers), Linux containers
**Project Type**: web (frontend + backend)
**Performance Goals**: p95 search latency < 1 s at 200 requests per second
**Constraints**: Prices in integer minor units; no client-side price calculation (constitution II)
**Scale/Scope**: ~40,000 shoe variants, ~2,000 delivery postcodes

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

| Principle | Check | Status |
|---|---|---|
| I. Test-First | Acceptance tests defined per user story in tasks.md before implementation | Pass |
| II. Server-Side Truth | Price filter and checkout re-validation run on the server | Pass |
| III. Accessible by Default | Colour filter uses text labels and swatches, not swatches alone | Pass |
| IV. Observable Behaviour | Search and checkout endpoints log request ID and filter parameters | Pass |
| V. Simplicity | Extends existing modules; one new table (colour_family) | Pass |

## Project Structure

### Documentation (this feature)

```text
specs/001-red-shoe-under-90/
├── plan.md              # This file (/speckit.plan output)
├── research.md          # Phase 0 output
├── data-model.md        # Phase 1 output
├── quickstart.md        # Phase 1 output
├── contracts/           # Phase 1 output
│   └── shop-api.yaml
└── tasks.md             # Phase 2 output (/speckit.tasks)
```

### Source Code (repository root)

```text
backend/
├── src/
│   ├── catalogue/       # search endpoint, colour family mapping
│   ├── pricing/         # price basis for filtering
│   ├── inventory/       # stock lookup per variant
│   ├── delivery/        # postcode → delivery zone
│   └── checkout/        # price and stock re-validation
└── tests/
    ├── contract/
    ├── integration/
    └── unit/

frontend/
├── src/
│   ├── components/filters/
│   ├── pages/shoes/
│   └── services/shopApi.ts
└── tests/e2e/
```

**Structure Decision**: Web application layout (frontend + backend) matching the existing repository.

## Complexity Tracking

| Violation | Why Needed | Simpler Alternative Rejected Because |
|---|---|---|
| New `colour_family` table | Product colours are free text from suppliers ("wine", "cherry") | Filtering on free-text colour misses most red shoes |
