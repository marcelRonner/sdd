# Spec Kit example — "A user wants to buy a red shoe for under $90"

A complete, filled-in set of GitHub Spec Kit documents for one feature, following the structure of the Spec Kit templates (github.com/github/spec-kit, main branch, October 2026). The repository layout mirrors what `specify init` and the slash commands create.

| File | Created by | Content |
|---|---|---|
| [`.specify/memory/constitution.md`](./.specify/memory/constitution.md) | `/speckit.constitution` | Project-wide principles |
| [`specs/001-red-shoe-under-90/spec.md`](./specs/001-red-shoe-under-90/spec.md) | `/speckit.specify` | User stories, requirements, success criteria |
| [`plan.md`](./specs/001-red-shoe-under-90/plan.md) | `/speckit.plan` | Technical context, constitution check, structure |
| [`research.md`](./specs/001-red-shoe-under-90/research.md) | `/speckit.plan` | Decisions on open points |
| [`data-model.md`](./specs/001-red-shoe-under-90/data-model.md) | `/speckit.plan` | Entities and rules |
| [`contracts/shop-api.yaml`](./specs/001-red-shoe-under-90/contracts/shop-api.yaml) | `/speckit.plan` | API contract |
| [`quickstart.md`](./specs/001-red-shoe-under-90/quickstart.md) | `/speckit.plan` | How to run and validate |
| [`tasks.md`](./specs/001-red-shoe-under-90/tasks.md) | `/speckit.tasks` | 30 ordered tasks |

The `[NEEDS CLARIFICATION]` markers in `spec.md` are intentional: they show where the spec leaves holes. In this example, `research.md` answers them as technical decisions. Compare with [`../idsd/`](../idsd/), where the product owner closes the same holes in the intent.

The example product, platform and stack are fictional.
