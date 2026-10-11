# Research: Find and Buy an Affordable Shoe by Colour

**Feature**: `001-red-shoe-under-90` | **Date**: 2026-10-11

Resolves the open points from `spec.md` and the technical unknowns in `plan.md`.

## R1 — Colour matching

- **Decision**: Introduce colour families. Each supplier colour name maps to exactly one family; burgundy, wine and cherry map to `red`; coral maps to `orange`.
- **Rationale**: Supplier colour names are inconsistent free text. A maintained mapping makes filtering predictable and testable.
- **Alternatives considered**: Free-text search on colour (misses synonyms); image-based colour detection (costly, non-deterministic).
- **Open**: Multi-coloured shoes are assigned their dominant colour only. Confirm with merchandising.

## R2 — Price basis for "under $90"

- **Decision**: Filter on the current selling price (sale price if active, otherwise list price), including sales tax for the shopper's region, excluding shipping.
- **Rationale**: Matches the price shown in results and charged for the item at checkout (FR-005).
- **Alternatives considered**: List price only (hides sale items the shopper can afford); total including shipping (requires the address before search).
- **Open**: Product owner to confirm that shipping is excluded.

## R3 — Stock source

- **Decision**: Use the inventory module's `available` quantity (on hand minus reserved) per variant, aggregated over all fulfilment warehouses.
- **Rationale**: Already used by product detail pages; consistent with checkout.
- **Alternatives considered**: Real-time warehouse API call per result (too slow for search).

## R4 — Delivery availability

- **Decision**: Resolve postcode to delivery zone with the existing `delivery_zone` table; results carry a `deliverable` flag when a postcode is given.
- **Rationale**: No new service required (constitution V).
- **Alternatives considered**: Carrier API lookup (latency, cost).

## R5 — Checkout re-validation

- **Decision**: On opening checkout, re-read price and stock for each cart line. Changes are returned as `priceChanged` or `outOfStock` flags and must be confirmed by the shopper.
- **Rationale**: Enforces SC-002 and SC-003 on the server.
- **Alternatives considered**: Price lock at add-to-cart (conflicts with pricing policy).
