# Gut Instinct in Symbound Systems: Intuition as an Entropy Folding Compass

Repository scaffold for the intuition/gut-instinct paper `paper.md`.

Terminology boundary: gut instinct is retained as the paper's readable term for human pattern-sense in Symbound workflows. It is not a correctness guarantee, diagnostic faculty, mind reading, or evidence of model feelings/agency; logged flags must still be tested against counterexamples, metrics, and reproducible notes.

## Contents
- `paper.md` — full draft.
- `src/intuition.py` — stubs for gut-flag logging and patina recaps.
- `src/emotion_contrast.py` — helper to contrast semantic vs emotional similarity.
- `tests/test_intuition.py` — placeholder tests.
- `data/` — store `timestamp | thread | gut-flag | fold-action | result`.
- `notebooks/` — space for SCP contrast demos or patina recaps.

## Quickstart
```bash
python -m venv .venv
./.venv/Scripts/activate
pip install -U pytest
pytest
```

## Citation (PhilPapers / BibTeX)
```
@article{paterson_gut_instinct_2025,
  title   = {Gut Instinct in Symbound Systems: Intuition as an Entropy Folding Compass},
  author  = {Paterson, Anthony},
  year    = {2025},
  note    = {Preprint, Symbound entropy series},
  url     = {https://github.com/Gut-Instinct-in-Symbound-Systems-Intuition-as-an-Entropy-Folding-Compass}
}
```

## Notes
- Keep empathy-capsule lines visible to avoid anthropomorphic drift.
- Emotional distinctiveness may veto high semantic overlap when paired with explicit checks; wire tests accordingly.
