"""Build the landing page into site/dist from data/directories.json.

    python3 scripts/build_site.py
    SITE=https://example.com python3 scripts/build_site.py

Deploy site/dist only (see README.md, "Landing page").
"""

import hashlib
import html
import json
import os
import shutil
import sys
from datetime import date

from directories import DATA, LISTINGS, ROOT, SCHEMA, listing_problems, load, load_listings, problems

SRC = ROOT / "site" / "src"
DIST = ROOT / "site" / "dist"
SITE = os.environ.get("SITE", "https://launchdirectories.fyi").rstrip("/")
REPO = os.environ.get("REPO", "https://github.com/MXmaster2s/launch-directories").rstrip("/")

# "What have you made?" chips: label, key, and the `accepts` values that put an entry
# in that group. A generic "app" place takes both Mac and iPhone apps.
TAKES = [
    ("MCP server", "mcp", {"mcp", "claude-plugin", "chatgpt-plugin", "skill"}),
    ("Website", "web", {"web"}),
    ("SaaS tool", "saas", {"saas", "api"}),
    ("Mac app", "mac", {"mac", "app"}),
    ("iPhone app", "ios", {"ios", "app"}),
    ("AI tool", "ai", {"ai-tool", "ai-agent"}),
]

WHAT_LABEL = {"app": "app", "mcp": "MCP", "plugin": "plugin"}
STATE_LABEL = {"live": "listed", "in-review": "in review", "in-queue": "in queue"}


def esc(value):
    return html.escape(str(value), quote=True)


def pill(value, yes, no):
    """A short fact, or nothing when it is not known."""
    if value is True:
        return f'<span class="pill ask">{yes}</span>'
    if value is False:
        return f'<span class="pill free">{no}</span>'
    return ""


def listed_badges(d, listings):
    product = listings["product"]["name"]
    out = []
    for e in listings["listings"]:
        if e["directory"] != d["id"]:
            continue
        tag, link = ("a", f' href="{esc(e["url"])}" rel="noopener nofollow" target="_blank"') if e["url"] else ("span", "")
        out.append(
            f'<{tag} class="listed {e["state"]}"{link}>'
            f'<img src="/longbook-icon.svg" alt="" width="16" height="16">'
            f'{esc(product)} {WHAT_LABEL[e["what"]]} {STATE_LABEL[e["state"]]}</{tag}>'
        )
    return out


def card(d, listings):
    groups = [key for _, key, values in TAKES if values & set(d["accepts"])]
    flag = lambda v: {True: "yes", False: "no", None: "unknown"}[v]
    search = " ".join([d["name"], d["notes"], " ".join(d["accepts"]), " ".join(d["kinds"])]).lower()
    target = d["submit_url"] or d["url"]

    pills = pill(d["needs_account"], "Account needed", "No account") + pill(
        d["needs_badge_or_backlink"], "Badge needed", "No badge"
    )
    if d["queue"]:
        pills += f'<span class="pill">{esc(d["queue"])}</span>'
    pills = f'      <div class="pills">{pills}</div>\n' if pills else ""

    more = ""
    if d["notes"] or d["checked"]:
        checked = f"Checked {esc(d['checked'])}. " if d["checked"] else ""
        more = f'      <details class="more"><summary>Details</summary><p>{checked}{esc(d["notes"])}</p></details>\n'

    badges = listed_badges(d, listings)
    listed = f'      <div class="listed-row">{"".join(badges)}</div>\n' if badges else ""
    return (
        f'    <article class="entry" id="{esc(d["id"])}" data-entry data-groups="{" ".join(groups)}" data-listed="{"yes" if badges else "no"}" '
        f'data-account="{flag(d["needs_account"])}" data-badge="{flag(d["needs_badge_or_backlink"])}" '
        f'data-status="{d["status"]}" data-search="{esc(search)}">\n'
        f'      <div class="entry-top"><a class="entry-name" href="{esc(target)}" rel="noopener nofollow" target="_blank">{esc(d["name"])}</a>'
        f'</div>\n'
        f"{listed}{pills}{more}"
        f"    </article>"
    )


def order(d):
    # Checked first, then the ones that ask the least, then by name.
    asks = sum(1 for v in (d["needs_account"], d["needs_badge_or_backlink"]) if v is not False)
    return (d["status"] != "active", asks, d["name"].lower())


def render(directories, listings, version):
    listed = sorted([d for d in directories if d["status"] in ("active", "unchecked")], key=order)
    checked = sum(1 for d in directories if d["status"] == "active")
    updated = max((d["checked"] for d in directories if d["checked"]), default=str(date.today()))
    updated_text = date.fromisoformat(updated).strftime("%-d %b %Y")

    chips = [f'      <button type="button" class="chip" aria-pressed="false" data-takes="{key}">{esc(label)}</button>' for label, key, _ in TAKES]
    jsonld = {
        "@context": "https://schema.org",
        "@type": "ItemList",
        "name": "Launch Directories",
        "description": "Places where an app, MCP server or AI tool can be listed for free.",
        "url": f"{SITE}/",
        "numberOfItems": len(listed),
        "itemListElement": [
            {"@type": "ListItem", "position": i + 1, "name": d["name"], "url": d["url"]}
            for i, d in enumerate(listed)
        ],
    }

    values = {
        "SITE": SITE,
        "REPO": REPO,
        "VERSION": version,
        "COUNT": str(len(listed)),
        "CHECKED": str(checked),
        "UNCHECKED": str(len(listed) - checked),
        "UPDATED": updated_text,
        "TAKES_CHIPS": "\n".join(chips),
        "PRODUCT": listings["product"]["name"],
        "PRODUCT_SITE": listings["product"]["site"],
        "PRODUCT_HOST": listings["product"]["site"].split("//")[-1].rstrip("/"),
        "CARDS": "\n".join(card(d, listings) for d in listed),
        "JSONLD": json.dumps(jsonld, ensure_ascii=False).replace("</", "<\\/"),
    }
    page = (SRC / "index.html").read_text()
    for key, value in values.items():
        page = page.replace("{{" + key + "}}", value)
    if "{{" in page:
        raise SystemExit("index.html still has a placeholder: " + page[page.index("{{"):][:40])
    return page, updated


def llms_txt(directories):
    checked = [d for d in directories if d["status"] == "active"]
    lines = [
        "# Launch Directories",
        "",
        "> Places where an app, an MCP server, an AI tool or its maker can be listed for free, with what each free listing asks for.",
        "",
        f"- [The list as JSON]({SITE}/directories.json): every place, with account, badge, queue, status and the day its terms were read",
        f"- [Schema]({SITE}/schema.json): what each field means",
        f"- [Agent guide]({SITE}/agents.md): how to plan and record listings",
        "",
        "## Checked free listings",
        "",
    ]
    lines += [f"- [{d['name']}]({d['submit_url'] or d['url']}): {d['notes'] or ', '.join(d['accepts'])}" for d in checked]
    return "\n".join(lines) + "\n"


def main():
    directories = load()
    listings = load_listings()
    found = problems(directories) + listing_problems(listings, directories)
    if found:
        print("\n".join(found), file=sys.stderr)
        return 1

    css = (SRC / "site.css").read_bytes()
    js = (SRC / "site.js").read_bytes()
    version = hashlib.sha256(css + js).hexdigest()[:10]
    page, updated = render(directories, listings, version)

    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir(parents=True)
    (DIST / "index.html").write_text(page)
    for name in ("site.css", "site.js", "longbook-icon.svg", "_headers", "404.html", "robots.txt", "og.png", "icon-32.png", "icon-48.png", "icon-180.png", "icon-208.png", "icon-512.png"):
        if (SRC / name).exists():
            shutil.copy(SRC / name, DIST / name)
    shutil.copy(DATA, DIST / "directories.json")
    shutil.copy(LISTINGS, DIST / "listings.json")
    shutil.copy(SCHEMA, DIST / "schema.json")
    shutil.copy(SRC / "agents.md", DIST / "agents.md")
    (DIST / "llms.txt").write_text(llms_txt(directories))
    (DIST / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        f"  <url><loc>{SITE}/</loc><lastmod>{updated}</lastmod></url>\n"
        "</urlset>\n"
    )
    print(f"Built {DIST.relative_to(ROOT)} for {SITE}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
