# IDSD example — the same feature in intent form

The same feature as [`../spec-kit/`](../spec-kit/), written as intent-driven software development (IDSD), following the ICE frame (Intent, Context, Expectations) from Kapil Viren Ahuja's article (May 2026).

| File | Craft | Owner |
|---|---|---|
| [`intents/INT-001-buy-red-shoe-under-90.md`](./intents/INT-001-buy-red-shoe-under-90.md) | Intent: what is wanted, constraints, failure and success scenarios, connections | Human (product owner) |
| [`expectations/INT-001-buy-red-shoe-under-90.expectations.md`](./expectations/INT-001-buy-red-shoe-under-90.expectations.md) | Expectations: done when, failed if, limits | Human (same owner) |
| [`context/`](./context/) | Context: where the harness finds the how | Harness |

The connected intents (INT-010 to INT-020) are referenced to show traceability; they are not part of this example.

**Note**: The article defines the five parts of an intent and the role of expectations and context, but no file format. The layout here is one possible interpretation.
