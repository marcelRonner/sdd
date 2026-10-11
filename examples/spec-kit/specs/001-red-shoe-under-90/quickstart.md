# Quickstart: Find and Buy an Affordable Shoe by Colour

**Feature**: `001-red-shoe-under-90`

## Setup

```bash
npm install
npm run db:migrate
npm run db:seed -- --fixture shoes-red-under-90
npm run dev
```

The fixture creates:

| SKU | Colour (supplier) | Family | Price | Size 42 stock |
|---|---|---|---|---|
| RS-079 | red | red | $79 | 3 |
| RS-140 | red | red | $140 | 5 |
| BG-069 | burgundy | red | $69 | 2 |
| BL-059 | navy | blue | $59 | 4 |
| RS-085 | cherry | red | $85 | 0 |

## Validation scenarios

1. **Filter (US1)**: `GET /shoes/search?colourFamily=red&maxPrice=9000&size=42` returns RS-079 and BG-069 only.
2. **Price change (US2)**: Add RS-079 to a cart, set its price to $95, call `POST /cart/{id}/checkout/validate`; line status is `priceChanged`, `canPay` is false until confirmed.
3. **Out of stock (US2)**: Add BG-069, set stock to 0, validate; status is `outOfStock`.
4. **Delivery (US3)**: Search with a postcode outside all zones; every result has `deliverable: false` and the add-to-cart button is disabled.

## Run the tests

```bash
npm run test:contract
npm run test:integration
npm run test:e2e -- --grep "red shoe"
```
