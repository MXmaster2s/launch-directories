# Contributing

Additions and corrections are welcome, from people and from agents.

Not comfortable with git? Open an issue with the
[Add a place](../../issues/new?template=add-a-place.yml) or
[Correct a place](../../issues/new?template=correct-a-place.yml) form and we will do the
rest.

## Add a place

1. Read the place's submit page and its free terms.
2. Add an entry to `data/directories.json`, in name order. Every field is required;
   `data/schema.json` says what each one means. Use `null` for anything the site does
   not say.

   ```json
   {
     "id": "example-directory",
     "name": "Example Directory",
     "url": "https://example.com",
     "submit_url": "https://example.com/submit",
     "kinds": ["launch-directory"],
     "accepts": ["web", "saas"],
     "free": true,
     "needs_account": true,
     "needs_badge_or_backlink": false,
     "queue": "About 2 weeks",
     "paid_upgrades": true,
     "status": "active",
     "checked": "2026-11-03",
     "notes": "What the free tier needs, in plain words."
   }
   ```

   If you only know the place exists, set `status` to `unchecked` and `checked` to
   `null`.
3. Run `python3 scripts/build_readme.py` and `python3 -m unittest discover tests`.
4. Commit the data and README together: `Add Example Directory`.

## Correct a place

Change the fields, set `checked` to today, rebuild, and commit:
`Update Example Directory: badge no longer required`.

## What does not belong here

Paid-only listings, link farms and backlink sellers. When a place turns out to be
one, keep the entry with `status: avoid` so nobody checks it again.
