---
intent: INT-001
owner: Product Owner
status: agreed
created: 2026-10-11
---

# Expectations for INT-001 — Buy a red shoe for under $90

> The boundary the agentic loop validates against. Written in the shopper's terms, owned by the same person as the intent. The loop repeats until every "Done when" passes and no "Failed if" occurs. Nothing here says how to build it.

## Reference shelf

The checks below use this example shelf. The harness turns it into test data; the owner only maintains the table.

| Shoe | Shopper would call it | Price incl. tax | Size 42 available | Delivers to 10001 |
|---|---|---|---|---|
| A | red | $79.00 | 3 | yes |
| B | red | $140.00 | 5 | yes |
| C | burgundy | $69.00 | 2 | yes |
| D | navy | $59.00 | 4 | yes |
| E | cherry | $85.00 | 0 | yes |
| F | red | $90.00 | 2 | yes |
| G | red and white, mainly white | $49.00 | 1 | yes |
| H | red | $72.00 | 2 | no |

## Done when

| # | The shopper … | Then … |
|---|---|---|
| D1 | enters postcode 10001 and looks for red, size 42, under $90 | sees A and C, and nothing else; H is shown as "not deliverable to you" or hidden |
| D2 | sorts the results by price | sees C before A |
| D3 | adds A to the cart and checks out | pays exactly $79.00 for the shoe; shipping was shown before payment |
| D4 | has A in the cart and its price rises to $95 before payment | is told the new price in plain words and can remove it or accept it |
| D5 | has C in the cart and the last pair sells before payment | is told it is no longer available and cannot pay for it |
| D6 | looks for red, size 47, under $90 (nothing matches) | is told nothing matches and is offered to widen price or colour |

## Failed if

| # | At any point … |
|---|---|
| F1 | B, D, E, F or G is offered as a match (too expensive, wrong colour, not available, exactly $90, mainly white) |
| F2 | H can be bought by a shopper in postcode 10001 |
| F3 | the shopper pays an amount different from the one they confirmed |
| F4 | a colour label is the only way the shopper can tell which shoe is red |

## Limits

- Results appear within about one second for a shopper on a normal connection.
- Nothing about other categories (boots, bags) changes behaviour.
- Existing orders, prices and stock figures are not changed by this work.
- Works for shoppers using a keyboard or a screen reader.
