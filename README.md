# sdd — Spec-driven vs. intent-driven development

Material for a management briefing on **spec-driven development (SDD)** with AI coding agents, drawing on two critiques: the **intent-driven alternative (IDSD)** proposed by Kapil Viren Ahuja (May 2026), and **"SDD as the new waterfall"** by Uberto Barbini (August 2026).

**The argument in one paragraph:** SDD asks one document to be the intent, the definition of done, the workflow and the technical context at once, and to be complete before any code exists. That never worked for classic upfront design specs, and with agents it fails faster: every gap in the spec becomes an agent decision, made instantly and at volume. IDSD splits the spec by owner. The person who wants the outcome writes the **intent** and the **expectations** (what counts as done or failed); the agent harness pulls the **context** (the how) as it needs it, and builds in a loop until the expectations are met.

**The second view:** Barbini places SDD in a line with CASE tools, RUP/CMMI and Model Driven Architecture, which made the same promise. A spec precise enough to generate a system is as complex as the system; regenerating from it is rewriting, not rebuilding; and agents churn out plausible documents never tested against reality. His alternative: keep the process agile and make **executable, non-mocked tests the real spec**.

**Combined (our synthesis):** owners write intent and expectations; the expectations become executable tests that stay the source of truth.

## Repository structure

```text
.
├── README.md                     # this file
├── presentation/                 # the briefing deck
│   ├── sdd-to-idsd.pdf           #   read or send
│   ├── sdd-to-idsd.html          #   open in a browser
│   ├── source/                   #   slide sources (deck.json + one HTML per slide)
│   └── build_deck.py             #   rebuilds HTML and PDF from source/
└── examples/                     # one feature, written both ways
    ├── README.md                 #   side-by-side comparison
    ├── spec-kit/                 #   complete GitHub Spec Kit document set
    │   ├── .specify/memory/constitution.md
    │   └── specs/001-red-shoe-under-90/
    │       ├── spec.md  plan.md  research.md  data-model.md
    │       ├── quickstart.md  tasks.md
    │       └── contracts/shop-api.yaml
    └── idsd/                     #   the same feature in intent form
        ├── intents/INT-001-buy-red-shoe-under-90.md
        ├── expectations/INT-001-buy-red-shoe-under-90.expectations.md
        └── context/              #   pointers only; owned by the harness
```

## Start here

1. **[The deck (PDF)](./presentation/sdd-to-idsd.pdf)**: 10 slides covering the problem with SDD, SDD as the new waterfall, the intent argument, how the two critiques combine, upfront spec vs. SDD vs. IDSD, the current SDD frameworks, Spec Kit in detail, and the example.
2. **[The example comparison](./examples/README.md)**: the article's scenario, *"a user wants to buy a red shoe for under $90"*, written as a Spec Kit spec and as an intent.
3. Then compare one open question in both: Spec Kit's [`spec.md`](./examples/spec-kit/specs/001-red-shoe-under-90/spec.md) flags *"does burgundy count as red?"* and [`research.md`](./examples/spec-kit/specs/001-red-shoe-under-90/research.md) answers it as a technical decision; the [intent](./examples/idsd/intents/INT-001-buy-red-shoe-under-90.md) has the product owner answer it as a constraint.

## At a glance

| | Classic upfront spec | SDD (e.g. Spec Kit) | IDSD |
|---|---|---|---|
| Written before code | Full design document | Spec, plan, research, data model, contracts, quickstart, tasks | Intent and expectations |
| Who closes the gaps | Developers, late | The agent, instantly | The intent owner, up front |
| Definition of done | Test phase at the end | Success criteria inside the spec | Separate expectations, owned by the intent owner |
| Human role during build | Builds | Reviews the diff at the end | Stays in the loop |

## Sources and caveats

- Kapil Viren Ahuja, "The Method That Replaces Spec-Driven Development — IDSD", Medium, 20 May 2026. The article defines the five parts of an intent and the roles of expectations and context, but no file format; the layout in `examples/idsd/` is one interpretation.
- Uberto Barbini, "Spec-Driven Development: The New Waterfall", Medium, August 2026: https://medium.com/@ramtop/spec-driven-development-the-new-waterfall-8426a908d4da
- Spec Kit structure follows the templates in [github/spec-kit](https://github.com/github/spec-kit) (main branch, October 2026).
- Framework overview in the deck: comparison articles and community repos from May to September 2026, listed on the slide.
- The example shop, platform and stack are fictional.
