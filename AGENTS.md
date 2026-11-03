# AGENTS.md

This repository is a list of places where a product can be listed for free, and a way
to plan those listings. The list lives in `data/directories.json`; the field meanings
are in `data/schema.json`. `README.md`'s tables are generated from the data by
`scripts/build_readme.py`, so never edit them by hand.

## When the owner asks you to plan listings for a product

1. Look for `plans/<product>.md`. If it exists, continue it. If not, copy
   `plans/TEMPLATE.md` to it and fill in the brief from what the owner tells you and
   from the product's own site. Ask only for what the site does not say.
2. Pick candidates from `data/directories.json`:
   - `status` is `active`, and `accepts` overlaps what the product is.
   - Order them: no account and no badge first, then badge only, then account, then
     long queues. Platforms that review for weeks (`ai-app-store`) start early.
   - Skip `avoid` and `down`. For `unchecked` places, read their free terms first and
     update the entry before you put them in a plan.
3. Write the plan's table: one row per place, with what has to be ready (text, images,
   badge, account, test login) and who does each step.
4. Show the owner the plan before acting on any of it.

## When you submit a listing

- Show the owner the exact text for each submission and wait for a yes. One yes covers
  one submission.
- Never pay, never create an account, never accept terms and never type a password or
  any other credential. Those are the owner's; ask them.
- A badge or backlink is a change to the owner's site. Ask before planning one, and
  hand it to whoever edits the site.
- Record every result in the plan: status, the listing's URL, the account it lives
  under, the date. When a listing goes live, or its state changes, update
  `data/listings.json` too; the landing page shows it as a badge.

## When you learn something about a place

The data is only useful if it is true, so keep it current while you work:

- **New place:** add an entry (see `CONTRIBUTING.md`) with `status: unchecked`, or
  `active` with today's `checked` date once you have read its free terms yourself.
- **Changed terms:** update the entry and its `checked` date.
- **Gone or not worth it:** set `status` to `down` or `avoid` and say why in `notes`.

Then run `python3 scripts/build_readme.py` and `python3 -m unittest discover tests`,
and commit the data and README together. The landing page is rebuilt with
`scripts/build_site.py` and deployed as README.md's "Landing page" says; deploying
reaches outside this folder, so ask the owner first.

## Rules for the data

1. Only write what you saw on the site. When you do not know a value, use `null`.
2. `notes` say what the free tier needs, in plain words. No marketing, no prices.
3. Keep entries sorted by name; the tests fail otherwise.
4. Never reuse or rename an `id`; plans refer to them.
