# Examples — one feature, two ways

Both examples use the article's scenario: *"A user wants to buy a red shoe for under $90."*

| Folder | What |
|---|---|
| [`spec-kit/`](./spec-kit/) | Complete GitHub Spec Kit document set for the feature |
| [`idsd/`](./idsd/) | The same feature as intent, expectations and context pointers |

## Side by side

| | Spec Kit | IDSD |
|---|---|---|
| Documents written before code | 8 (constitution, spec, plan, research, data model, contract, quickstart, tasks) | 2 (intent, expectations) + a context pointer list |
| Who writes them | Engineer with the agent, in one flow | Product owner writes intent and expectations; harness pulls context |
| Open questions ("is burgundy red?", "is shipping inside $90?") | Marked `[NEEDS CLARIFICATION]` in `spec.md`, then answered in `research.md` as technical decisions | Answered by the owner in the intent's constraints |
| Definition of done | Success criteria and acceptance scenarios inside the spec | Separate expectations file with a reference shelf, owned by the intent owner |
| What the agent checks against | Tasks and tests derived from the spec | "Done when" / "failed if" table, repeated until met |

## Where each Spec Kit document goes in IDSD

| Spec Kit | IDSD |
|---|---|
| `spec.md` user stories, edge cases | Intent: what is wanted, failure and success scenarios |
| `spec.md` requirements, `research.md` decisions on meaning | Intent: constraints |
| `spec.md` success criteria, `quickstart.md` | Expectations: reference shelf, done when, failed if, limits |
| `constitution.md` | Context (platform rules, reused as-is) |
| `plan.md`, `research.md` technical choices, `data-model.md`, `contracts/` | Context: read from the existing code and API catalogue by the harness |
| `tasks.md` | Internal to the agent loop |
