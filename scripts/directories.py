"""Load and check data/directories.json. Standard library only."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "directories.json"
LISTINGS = ROOT / "data" / "listings.json"
SCHEMA = ROOT / "data" / "schema.json"


def load():
    return json.loads(DATA.read_text())["directories"]


def load_listings():
    return json.loads(LISTINGS.read_text())


WHAT = ("app", "mcp", "plugin")
STATES = ("live", "in-review", "in-queue")


def listing_problems(listings, directories):
    """Where a product is listed: every entry must name a real directory."""
    ids = {d["id"] for d in directories}
    found, seen = [], set()
    for entry in listings["listings"]:
        where = f"{entry.get('directory')}/{entry.get('what')}"
        if entry.get("directory") not in ids:
            found.append(f"listings: {where}: no such directory")
        if entry.get("what") not in WHAT:
            found.append(f"listings: {where}: what must be one of {', '.join(WHAT)}")
        if entry.get("state") not in STATES:
            found.append(f"listings: {where}: state must be one of {', '.join(STATES)}")
        url = entry.get("url")
        if url is None:
            if entry.get("state") == "live":
                found.append(f"listings: {where}: a live listing needs its public url")
        elif not re.match(r"^https?://", url):
            found.append(f"listings: {where}: url must start with http(s)://")
        if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", entry.get("checked") or ""):
            found.append(f"listings: {where}: checked must be YYYY-MM-DD")
        if where in seen:
            found.append(f"listings: {where}: listed twice")
        seen.add(where)
    return found


def problems(directories):
    """Every way the data breaks the schema or the house rules, as sentences."""
    schema = json.loads(SCHEMA.read_text())["$defs"]["directory"]
    props = schema["properties"]
    found = []
    seen_ids, seen_urls = set(), set()

    for i, d in enumerate(directories):
        where = d.get("id") or f"entry {i}"
        missing = [k for k in schema["required"] if k not in d]
        extra = [k for k in d if k not in props]
        if missing:
            found.append(f"{where}: missing {', '.join(missing)}")
            continue
        if extra:
            found.append(f"{where}: unknown fields {', '.join(extra)}")

        if not re.fullmatch(props["id"]["pattern"], d["id"]):
            found.append(f"{where}: id must be a lowercase slug")
        for field in ("url", "submit_url"):
            value = d[field]
            if value is not None and not re.match(r"^https?://", value):
                found.append(f"{where}: {field} must start with http(s)://")
        for field in ("kinds", "accepts"):
            allowed = props[field]["items"]["enum"]
            if not d[field]:
                found.append(f"{where}: {field} is empty")
            for v in d[field]:
                if v not in allowed:
                    found.append(f"{where}: {field} has unknown value {v!r}")
        if d["status"] not in props["status"]["enum"]:
            found.append(f"{where}: unknown status {d['status']!r}")
        if d["checked"] is not None and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", d["checked"]):
            found.append(f"{where}: checked must be YYYY-MM-DD")
        if d["status"] in ("active", "avoid") and d["checked"] is None:
            found.append(f"{where}: status {d['status']} needs a checked date")
        if d["status"] == "active" and d["free"] is not True:
            found.append(f"{where}: active entries must have a free listing")

        key = d["url"].rstrip("/").lower()
        if d["id"] in seen_ids:
            found.append(f"{where}: duplicate id")
        if key in seen_urls:
            found.append(f"{where}: duplicate url {d['url']}")
        seen_ids.add(d["id"])
        seen_urls.add(key)

    names = [d.get("name", "").lower() for d in directories]
    if names != sorted(names):
        found.append("directories must be sorted by name")
    return found
