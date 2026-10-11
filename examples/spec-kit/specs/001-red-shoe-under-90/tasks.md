# Tasks: Find and Buy an Affordable Shoe by Colour

**Input**: Design documents from `/specs/001-red-shoe-under-90/`
**Prerequisites**: plan.md (required), spec.md (required for user stories), research.md, data-model.md, contracts/
**Tests**: Included (constitution principle I, test-first)
**Organization**: Tasks are grouped by user story so each story can be implemented and tested independently.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel (different files, no dependencies)
- **[Story]**: The user story the task belongs to (US1, US2, US3)

## Phase 1: Setup (Shared Infrastructure)

- [ ] T001 Create feature branch `001-red-shoe-under-90` and link spec in PR template
- [ ] T002 [P] Add seed fixture `shoes-red-under-90` in backend/prisma/seeds/shoes-red-under-90.ts
- [ ] T003 [P] Add contract test harness for shop-api.yaml in backend/tests/contract/setup.ts

## Phase 2: Foundational (Blocking Prerequisites)

- [ ] T004 Migration: create `colour_family` and `colour_mapping` tables in backend/prisma/migrations/
- [ ] T005 Migration: add `colour_family_id` to `variant` and `price_confirmed` to `cart_line`
- [ ] T006 [P] Seed initial colour families and mappings (red, blue, black, white, ...) in backend/prisma/seeds/colours.ts
- [ ] T007 [P] Add `sellingAmountInclTax(variant, region)` to backend/src/pricing/selling-price.ts

**Checkpoint**: Schema and pricing helper ready; user stories can start.

## Phase 3: User Story 1 - Filter shoes by colour, price and size (Priority: P1) MVP

**Goal**: Shoppers see only in-stock red shoes under $90 in their size.
**Independent Test**: quickstart.md scenario 1.

### Tests for User Story 1

- [ ] T008 [P] [US1] Contract test GET /shoes/search in backend/tests/contract/search.test.ts
- [ ] T009 [P] [US1] Integration test: burgundy maps to red, $140 excluded, size without stock excluded in backend/tests/integration/search-filter.test.ts

### Implementation for User Story 1

- [ ] T010 [US1] Implement colour family resolution in backend/src/catalogue/colour-family.ts
- [ ] T011 [US1] Extend search query with colourFamily, maxPrice and size filters in backend/src/catalogue/search.ts
- [ ] T012 [US1] Join available stock and exclude zero-stock variants in backend/src/catalogue/search.ts
- [ ] T013 [P] [US1] Filter panel component with text labels and swatches in frontend/src/components/filters/ShoeFilters.tsx
- [ ] T014 [US1] Wire filters to shopApi.searchShoes in frontend/src/pages/shoes/index.tsx
- [ ] T015 [P] [US1] Empty state with "widen price or colour" suggestion in frontend/src/components/filters/EmptyResults.tsx
- [ ] T016 [US1] Log request ID and filter parameters in backend/src/catalogue/search.ts

**Checkpoint**: User Story 1 works on its own.

## Phase 4: User Story 2 - Buy the selected shoe at the price shown (Priority: P2)

**Goal**: The shopper pays the price they confirmed; out-of-stock items cannot be bought.
**Independent Test**: quickstart.md scenarios 2 and 3.

### Tests for User Story 2

- [ ] T017 [P] [US2] Contract test POST /cart/{id}/checkout/validate in backend/tests/contract/checkout-validate.test.ts
- [ ] T018 [P] [US2] E2E test: price change shown before payment in frontend/tests/e2e/checkout-price-change.spec.ts

### Implementation for User Story 2

- [ ] T019 [US2] Implement line validation (priceChanged, outOfStock) in backend/src/checkout/validate.ts
- [ ] T020 [US2] Store `price_confirmed` on shopper confirmation in backend/src/checkout/confirm.ts
- [ ] T021 [US2] Reject order when current price differs from `price_confirmed` in backend/src/checkout/place-order.ts
- [ ] T022 [US2] Price-change and out-of-stock notices in frontend/src/pages/checkout/index.tsx

**Checkpoint**: User Stories 1 and 2 work independently.

## Phase 5: User Story 3 - See delivery availability before checkout (Priority: P3)

**Goal**: Results show whether they can be delivered to the shopper's postcode.
**Independent Test**: quickstart.md scenario 4.

- [ ] T023 [P] [US3] Integration test for postcode → deliverable flag in backend/tests/integration/delivery.test.ts
- [ ] T024 [US3] Add `deliverable` to search results when postcode is given in backend/src/delivery/zone-lookup.ts
- [ ] T025 [US3] Postcode input and delivery label in frontend/src/components/filters/PostcodeInput.tsx
- [ ] T026 [US3] Disable add-to-cart for non-deliverable results in frontend/src/components/product/AddToCart.tsx

## Phase 6: Polish & Cross-Cutting Concerns

- [ ] T027 [P] Load test search at 200 rps, p95 < 1 s (SC-001)
- [ ] T028 [P] Accessibility audit of filter panel (WCAG 2.1 AA)
- [ ] T029 [P] Merchandising admin view for colour mappings
- [ ] T030 Run quickstart.md validation end to end

## Dependencies & Execution Order

- Phase 1 → Phase 2 → user stories. US1, US2 and US3 can then run in parallel; US2 uses search results from US1 only in the E2E test.
- Within each story: tests first (must fail), then backend, then frontend.

## Implementation Strategy

MVP first: Phases 1–3, validate US1, then add US2 and US3 incrementally.
