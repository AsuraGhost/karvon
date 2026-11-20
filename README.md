# Karvon

**Open-source Terminal Operating System for land freight terminals.**
Built for dry ports, border truck terminals, TIR parks and cross-dock warehouses.

*Karvon* means "caravan" in Uzbek. The project started at a border terminal on the
Uzbekistan–Afghanistan crossing, where trucks from Afghanistan and Pakistan are
parked, transloaded, weighed, cleared and released every day.

> **Status: alpha (v0.1).** The core visit flow works end to end. Feedback and
> contributors are very welcome. See the [roadmap](#roadmap).

<!-- TODO: add a screenshot or GIF of the dashboard here: docs/screenshot.png -->

## Why

Container seaports have plenty of terminal software. Land terminals mostly run on
spreadsheets, paper and expensive closed systems. Karvon gives them a free,
self-hosted system that models how a truck terminal really works:

- **Gate in / gate out.** Vehicle, driver, TIR carnet and CMR are registered at the gate.
- **Yard.** Zones and slots, automatic or manual slot assignment, a live yard board.
- **Operations.** Direct transfer (truck to truck), warehouse unloading and warehouse loading.
- **Warehouse.** Stock lots per cargo owner, created by unloads and consumed by loads.
- **Customs flag.** Customs can be cleared before *or* after the physical work.
- **Weighbridge.** Gross, tare and net weigh tickets.
- **Billing.** Configurable tariffs for parking per day, per tonne and per service.
  A truck can't leave until everything is done, cleared and paid.
- **Multilingual.** English, Russian and Uzbek are included. Add a language with one JSON file.
- **REST API** with OpenAPI docs at `/docs`, so you can connect cameras, scales or your ERP.

## Quick start

With Docker:

```bash
git clone https://github.com/OWNER/karvon.git
cd karvon
docker compose up
```

Open <http://localhost:8000>. A demo terminal with trucks in different stages is
created on first start.

Without Docker (uses SQLite):

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
uvicorn karvon.main:app --reload
```

## How a visit flows

```
gate in → park → plan operation → (customs) → start → complete → weigh
        → request exit → pay → gate out
```

The rules live in [`karvon/services.py`](karvon/services.py). The domain model and
lifecycle are in [`docs/architecture.md`](docs/architecture.md).

## Configuration

| Variable                  | Default                  | Description                      |
|---------------------------|--------------------------|----------------------------------|
| `KARVON_DATABASE_URL`     | `sqlite:///./karvon.db`  | Any SQLAlchemy URL (PostgreSQL recommended) |
| `KARVON_SEED_DEMO`        | `1`                      | Create demo trucks on an empty database |
| `KARVON_TERMINAL_NAME`    | `Demo Border Terminal`   | Shown in the UI                  |
| `KARVON_DEFAULT_LANGUAGE` | `en`                     | `en`, `ru`, `uz`, …              |
| `KARVON_CURRENCY`         | `USD`                    | Display currency                 |

## Roadmap

- [x] Gate, yard, operations, warehouse, weighbridge, billing
- [x] EN / RU / UZ interface
- [ ] Users, roles and audit log
- [ ] Database migrations (Alembic)
- [ ] Weighbridge hardware driver (RS-232 / TCP)
- [ ] ANPR camera at the gate
- [ ] CMR / TIR / invoice PDF generation
- [ ] Reports: dwell time, throughput, revenue
- [ ] More languages: Turkish, Dari, Pashto, Kazakh, Tajik

Have a terminal with a different process? [Open an issue](https://github.com/OWNER/karvon/issues).
Real-world processes shape the roadmap.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). Translating the UI is a great first contribution.

## License

[MIT](LICENSE)
