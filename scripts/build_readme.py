"""Write the directory tables into README.md from data/directories.json.

    python3 scripts/build_readme.py          # rewrite README.md
    python3 scripts/build_readme.py --check  # fail if README.md is out of date
"""

import sys

from directories import ROOT, load, problems

README = ROOT / "README.md"
START = "<!-- directories:start -->"
END = "<!-- directories:end -->"

GROUPS = [
    ("AI app stores and MCP directories", {"ai-app-store", "mcp-directory", "agent-directory", "api-directory", "awesome-list"}),
    ("Launch platforms and directories", {"launch-platform", "launch-directory", "alternatives-directory", "app-directory"}),
    ("AI tool directories", {"ai-directory"}),
    ("Maker profiles and communities", {"maker-profile", "maker-community"}),
]


def yes_no(value):
    return {True: "yes", False: "no", None: "?"}[value]


def link(d):
    target = d["submit_url"] or d["url"]
    return f"[{d['name']}]({target})"


def group_of(d):
    for title, kinds in GROUPS:
        if kinds & set(d["kinds"]):
            return title
    return "Other"


def table(rows):
    out = [
        "| Directory | Takes | Account | Badge or backlink | Free queue | Checked | Notes |",
        "|---|---|---|---|---|---|---|",
    ]
    for d in rows:
        notes = d["notes"].replace("|", "\\|")
        out.append(
            f"| {link(d)} | {', '.join(d['accepts'])} | {yes_no(d['needs_account'])} "
            f"| {yes_no(d['needs_badge_or_backlink'])} | {d['queue'] or ''} "
            f"| {d['checked'] or ''} | {notes} |"
        )
    return out


def render(directories):
    active = [d for d in directories if d["status"] == "active"]
    unchecked = [d for d in directories if d["status"] == "unchecked"]
    skipped = [d for d in directories if d["status"] in ("avoid", "down")]

    lines = [START, "", f"{len(active)} checked free listings, {len(unchecked)} still to check, {len(skipped)} to skip.", ""]
    for title in [g[0] for g in GROUPS] + ["Other"]:
        rows = [d for d in active if group_of(d) == title]
        if rows:
            lines += [f"### {title}", ""] + table(rows) + [""]

    if unchecked:
        lines += ["### Not checked yet", "", "Known places whose free terms nobody has read. Read them before planning a listing, then update the entry.", ""]
        lines += [f"- {link(d)} ({', '.join(d['accepts'])})" + (f": {d['notes']}" if d["notes"] else "") for d in unchecked]
        lines.append("")

    if skipped:
        lines += ["### Skip", ""]
        lines += [f"- {link(d)} ({d['status']}, {d['checked']}): {d['notes']}" for d in skipped]
        lines.append("")

    lines.append(END)
    return "\n".join(lines)


def main():
    directories = load()
    found = problems(directories)
    if found:
        print("\n".join(found), file=sys.stderr)
        return 1

    text = README.read_text()
    head, rest = text.split(START, 1)
    _, tail = rest.split(END, 1)
    updated = head + render(directories) + tail

    if "--check" in sys.argv:
        if updated != text:
            print("README.md is out of date: run python3 scripts/build_readme.py", file=sys.stderr)
            return 1
        return 0
    README.write_text(updated)
    return 0


if __name__ == "__main__":
    sys.exit(main())
