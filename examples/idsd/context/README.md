# Context — owned by the harness

In IDSD, context is **not written by the intent owner** and not bundled into one up-front document. The harness (the agent tooling) pulls it progressively, as the loop needs it, from sources that already exist.

This folder therefore holds no hand-written spec. It holds only a pointer list: [`context-sources.yaml`](./context-sources.yaml) tells the harness where to look.

## How the loop uses it

1. Read the intent and expectations (human-owned).
2. Look up the connected intents (INT-010 … INT-020) for shared definitions.
3. Pull only the context the current step needs: for colour matching, the catalogue module and the colour vocabulary; for checkout, the checkout module and pricing rules.
4. Build, then validate against the expectations. Not met → repeat from step 3.
5. Met → merge request, with the expectations run attached as evidence.

## Where the Spec Kit documents went

| Spec Kit document | In IDSD |
|---|---|
| constitution.md | Stays: platform rules are context (`sources.rules`) |
| plan.md, research.md | Produced by the harness while working, not up front |
| data-model.md | Read from the existing schema (`sources.code`) |
| contracts/ | Read from the existing API catalogue; changes proposed by the harness |
| quickstart.md | Replaced by the reference shelf in the expectations |
| tasks.md | Internal to the loop; not a human-maintained document |
