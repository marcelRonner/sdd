# Data Model: Find and Buy an Affordable Shoe by Colour

**Feature**: `001-red-shoe-under-90` | **Date**: 2026-10-11

## Entities

### Product (existing)
| Field | Type | Notes |
|---|---|---|
| id | UUID | PK |
| name | text | |
| brand | text | |
| category | enum | `shoes` for this feature |

### Variant (existing, extended)
| Field | Type | Notes |
|---|---|---|
| id | UUID | PK |
| product_id | UUID | FK → Product |
| sku | text | unique |
| supplier_colour | text | free text from supplier |
| colour_family_id | UUID | **new**, FK → ColourFamily, nullable until mapped |
| size_eu | numeric(3,1) | |

### ColourFamily (new)
| Field | Type | Notes |
|---|---|---|
| id | UUID | PK |
| key | text | unique, e.g. `red` |
| label | text | display label |

### ColourMapping (new)
| Field | Type | Notes |
|---|---|---|
| supplier_colour | text | PK, normalised lower case |
| colour_family_id | UUID | FK → ColourFamily |
| maintained_by | text | merchandising user |

### Price (existing)
| Field | Type | Notes |
|---|---|---|
| variant_id | UUID | FK → Variant |
| list_amount | integer | minor units |
| sale_amount | integer | nullable |
| currency | char(3) | `USD` |
| valid_from / valid_to | timestamptz | |

Derived: `selling_amount = coalesce(sale_amount, list_amount)`; filter compares `selling_amount + tax` to the maximum (research R2).

### StockLevel (existing)
| Field | Type | Notes |
|---|---|---|
| variant_id | UUID | FK → Variant |
| warehouse_id | UUID | |
| on_hand | integer | |
| reserved | integer | |

Derived: `available = sum(on_hand - reserved)` per variant.

### DeliveryZone (existing)
| Field | Type | Notes |
|---|---|---|
| id | UUID | PK |
| postcodes | text[] | |

### CartLine (existing, extended)
| Field | Type | Notes |
|---|---|---|
| cart_id | UUID | FK → Cart |
| variant_id | UUID | FK → Variant |
| quantity | integer | |
| price_at_add | integer | minor units |
| price_confirmed | integer | **new**, set when shopper confirms at checkout |

## Validation Rules

- A variant without `colour_family_id` is excluded from colour-filtered results.
- `quantity` must not exceed `available` at checkout.
- An order is rejected if any line's current price differs from `price_confirmed`.

## State Transitions (CartLine)

`added` → (`priceChanged` | `outOfStock` | `valid`) on checkout open → `confirmed` → `ordered`
