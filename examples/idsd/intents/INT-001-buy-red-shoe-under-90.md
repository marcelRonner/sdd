---
id: INT-001
title: Buy a red shoe for under $90
owner: Product Owner
status: agreed
created: 2026-10-11
expectations: ../expectations/INT-001-buy-red-shoe-under-90.expectations.md
---

# INT-001 — Buy a red shoe for under $90

> No technology, no stack, no services. This file says what the buyer wants and where the edges are. How it gets built is the harness's job (see `../context/`).

## 1. What is wanted

A shopper who wants a red shoe can find one in their size, for under $90, that can actually be delivered to them, and buy it at the price they saw.

## 2. Constraints

- **"Red"** means anything a shopper would call red: red, burgundy, wine and cherry count; coral, pink and orange do not. A multi-coloured shoe counts only if red is its main colour.
- **"Under $90"** means the price the shopper pays for the shoe, including tax, strictly below $90.00. Shipping is not part of the limit, but it is shown before payment.
- A sale price counts if the sale is active at the moment the shopper sees it.
- Only the shopper's size counts, and only if at least one pair is available to buy now.
- Only shoes that can be delivered to the shopper's address count. If no address is known yet, the shopper is asked for a postcode before checkout, not before searching.
- The price the shopper confirms is the price they pay. It never changes silently.

## 3. It has failed if …

- The shopper is shown or sold a shoe that costs $90 or more ($90.00 exactly is a failure).
- The shopper is shown or sold a shoe that is not red by the definition above.
- The shopper buys a shoe that is out of stock in their size or cannot be delivered to them.
- The shopper pays a different amount from the one they confirmed.
- The shopper has to understand colour codes, warehouse names or tax rules to get a result.

## 4. It has succeeded if …

- A shopper looking for a red shoe in size 42 under $90 sees only shoes that meet all constraints, and the cheapest is easy to find.
- The shopper adds one to the cart and completes checkout, paying exactly the confirmed price.
- If the price or stock changes before payment, the shopper is told in plain words and can decide again.
- If nothing matches, the shopper is told so and offered a sensible way to widen the search.

## 5. Connections

Changes to any of these may change this intent, and the other way round:

| Intent | Why it is connected |
|---|---|
| INT-010 Show the price the buyer will pay | Defines "price incl. tax" used by constraint 2 |
| INT-011 Never sell what we cannot ship | Defines availability and stock reservation |
| INT-012 Deliver only where we can deliver | Defines delivery zones and the postcode question |
| INT-013 Pay what you confirmed | Defines price confirmation at checkout |
| INT-020 Describe colours the way shoppers do | Owns the colour vocabulary behind "red" |

## Decisions taken by the owner (instead of left to the agent)

| Question an agent would otherwise guess | Owner decision |
|---|---|
| Does burgundy count as red? | Yes (constraint 1) |
| List price or sale price? | Price at the moment the shopper sees it (constraint 3) |
| Is shipping inside the $90? | No, shown separately before payment (constraint 2) |
| Multi-coloured shoes? | Only if red is the main colour (constraint 1) |
