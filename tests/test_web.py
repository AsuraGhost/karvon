"""Smoke tests for the HTML UI, in every bundled language."""

import json
from pathlib import Path

import pytest

from karvon.i18n import languages

PAGES = ["/", "/gate", "/yard", "/stock", "/visits/1", "/visits/2", "/visits/3"]


@pytest.mark.parametrize("lang", sorted(languages()))
def test_pages_render(demo_client, lang):
    demo_client.cookies.set("lang", lang)
    for page in PAGES:
        r = demo_client.get(page)
        assert r.status_code == 200, (page, r.text[:500])
        assert "Karvon" in r.text


def test_translations_have_same_keys():
    d = Path(__file__).parents[1] / "karvon" / "i18n"
    en = set(json.loads((d / "en.json").read_text()))
    for path in d.glob("*.json"):
        assert set(json.loads(path.read_text())) == en, path.name


def test_gate_form_flow(client):
    r = client.post(
        "/gate",
        data={"plate_number": "01Z999ZZ", "driver_name": "Ali", "driver_passport": "AB1"},
        follow_redirects=False,
    )
    assert r.status_code == 303
    url = r.headers["location"]
    page = client.get(url)
    assert "01Z999ZZ" in page.text

    r = client.post(f"{url}/action/park", follow_redirects=False)
    assert r.headers["location"] == url
    assert "A-01" in client.get(url).text

    # errors come back as a message, not a 500
    r = client.post(f"{url}/action/weigh", data={"gross_kg": "abc", "tare_kg": "1"})
    assert r.status_code == 200 and "Not a number" in r.text


def test_language_from_query(demo_client):
    assert "Обзор терминала" in demo_client.get("/?lang=ru").text
    assert "Terminal overview" in demo_client.get("/?lang=xx").text
