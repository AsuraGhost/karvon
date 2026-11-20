# Contributing to Karvon

Thanks for helping. Karvon is built for people who run real terminals, so
contributions from logistics people matter as much as code.

## Ways to help

- **Describe your terminal.** Open an issue that explains how trucks move through
  your site. Process descriptions shape the roadmap.
- **Translate.** Copy `karvon/i18n/en.json` to `<language-code>.json` and translate
  the values. A test checks that every language has the same keys.
- **Code.** Pick an issue labelled `good first issue`.

## Development

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
uvicorn karvon.main:app --reload   # http://localhost:8000
pytest
ruff check .
```

## Code layout

- `karvon/services.py` has the business rules. Put new rules here, not in the API or UI.
- `karvon/api.py` is the REST API and `karvon/web.py` is the HTML UI. Both stay thin.
- Every new rule needs a test in `tests/`.

## Pull requests

- Keep PRs small and focused.
- Describe the real-world situation the change supports.
- Make sure `pytest` and `ruff check .` pass.
