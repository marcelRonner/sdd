# Presentation — From spec-driven to intent-driven development

Management briefing, 10 slides.

| File | Use |
|---|---|
| [`sdd-to-idsd.pdf`](./sdd-to-idsd.pdf) | Read or send |
| [`sdd-to-idsd.html`](./sdd-to-idsd.html) | Open in a browser (fonts load from Google Fonts) |
| [`source/`](./source/) | Slide sources: `deck.json` plus one HTML section per slide, as in the Claude Slides deck |
| [`build_deck.py`](./build_deck.py) | Rebuilds the HTML and PDF from `source/` |

The editable original is the Claude Slides deck "From SDD to Intent-Driven Development", which also exports to PowerPoint. After editing it there, copy the changed slide files into `source/` and rebuild:

```bash
python3 build_deck.py --pdf            # needs: pip install playwright
```

Slides:

1. Cover
2. The problem with spec-driven development (Ahuja)
3. A second view: SDD as the new waterfall (Barbini)
4. The argument for intent: split the spec, assign owners (Ahuja)
5. Two critiques of SDD, one direction (Ahuja vs. Barbini, combined)
6. Three processes compared (upfront design spec, SDD, IDSD)
7. Current SDD frameworks
8. Spec Kit in detail
9. What a complete Spec Kit spec contains
10. One feature, two ways — links to [`../examples/`](../examples/)
