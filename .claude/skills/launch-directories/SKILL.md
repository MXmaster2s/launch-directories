---
name: launch-directories
description: Use for any work in the Launch Directories repository - adding or correcting a free listing place, planning listings for a product, submitting a listing, rebuilding the README or the landing page. Routes to the right part of AGENTS.md and CONTRIBUTING.md.
---

# Working on Launch Directories

Read `AGENTS.md` and `MEMORY.md` first. Then:

| Work | Read |
|---|---|
| Planning listings for a product | `AGENTS.md`: When the owner asks you to plan listings; `plans/TEMPLATE.md` |
| Submitting a listing | `AGENTS.md`: When you submit a listing |
| Adding or correcting a place | `CONTRIBUTING.md`, `data/schema.json`, `AGENTS.md`: Rules for the data |
| Rebuilding the README or the site | `AGENTS.md`: When you learn something about a place; `README.md`: Landing page |

## Done when

- `python3 scripts/build_readme.py` and `python3 -m unittest discover tests` pass, the data and README are
  committed together, and every submission's result is recorded in its plan (and in `data/listings.json`
  when a listing goes live).

## Go-ahead

- The owner, each time: every submission's exact text, any payment, account, terms or credential, any
  badge or backlink, and deploying the landing page.
