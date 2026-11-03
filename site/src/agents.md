# Launch Directories: guide for agents

You are planning free listings for a product: an app, an MCP server, an AI tool, or a
maker's profile. The list is at https://launch-directories.pages.dev/directories.json
and every field is defined in https://launch-directories.pages.dev/schema.json.

## Plan

1. Learn the product from its own site: what it is, what it runs on, whether it is
   released, and which words its maker avoids. Ask the owner only what the site does
   not say.
2. Pick entries whose `accepts` overlap the product, and whose `status` is `active`.
3. Order them: no account and no badge first (`needs_account` and
   `needs_badge_or_backlink` both `false`), then badge only, then account, then long
   queues. Places that review for weeks (`kinds` has `ai-app-store`) start early.
4. Skip `avoid` and `down`. Treat `unchecked` entries as leads: read their free terms
   before putting them in a plan. `null` means nobody knows yet, never "no".
5. Re-read the terms of anything whose `checked` date is older than three months.
6. Show the owner the plan as a table: place, what must be ready (text, images, badge,
   account, reviewer login), who does each step.

## Submitting

- Show the owner the exact text of each submission and wait for a yes. One yes covers
  one submission.
- Never pay, create an account, accept terms, or type a password or other credential
  for the owner. Those are theirs.
- A badge or backlink changes the owner's site: ask first.
- Record each result: status, listing URL, account, date.
