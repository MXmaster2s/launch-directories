# Changelog

What changed in the list and the repository, newest first.

## 2026-11-03

- Credit for the research and lead generation to Lighteningly, in the site footer and the
  README, each link with its own UTM tags (`utm_content=site-footer` and `github-readme`).

- The site has its own domain, https://launchdirectories.fyi (Cloudflare Pages project
  `launch-directories`, with launch-directories.pages.dev as a fallback address). Canonical
  links, the sitemap, the agent prompt and the README use the new domain.

- The repository is public as `MXmaster2s/launch-directories`, started from a single clean
  commit. The entries below are the history it was built from.

- Contribution path for developers: a "Help build this list" section, a GitHub link in
  the navbar and footer, issue forms for adding or correcting a place, and a pull request
  template. The longbook plan is now a clean example with no internal notes.

- The site is now called Launch Directories, at https://launch-directories.pages.dev
  (Cloudflare Pages project `launch-directories`; the earlier `launchfast-directories`
  project is gone). Navbar, buttons and footer follow ShipCat's landing page: a 980 px
  bar with a pill call to action, rounded-rectangle buttons, and a two-line centred footer
  with a rule above.

- Removed the Checked and Unchecked pills and the Checked switch from the page; the
  checked date stays under Details.
- longbook's listing URLs verified in a browser: FollowX is /projects/longbook, MakerMap is
  the public profile /Rohthebuilder, the registry link is the exact latest version, and the
  Claude directory has no public page while in review (shown as plain text).
- Footer says which websites use the list for their listings.

- The page shows where longbook is already listed: a badge with its icon on each card
  ("longbook MCP listed", "longbook app in review"), from the new `data/listings.json`,
  plus a "longbook is listed" switch. Skipped places no longer appear on the page; they
  stay in the data and the README.
- New icon: the SF Symbol `paperplane.fill` on a blue tile, drawn by
  `scripts/make_icons.swift`, used for the favicon, home-screen icon, nav, hero and
  social image.

- Landing page simplified: the hero says to tell your AI agent to check the site, with one
  "Browse listing places" button; the list opens with "What have you made?" (MCP server,
  website, SaaS tool, Mac app, iPhone app, AI tool, pick any), and cards show only what a
  place asks, with the rest under Details. Fixed filtered-out cards staying visible.

- Landing page at https://launch-directories.pages.dev, built from the data by
  `scripts/build_site.py`: the list with filters by what you are listing, account,
  badge and checked, plus `directories.json`, `schema.json`, `agents.md` and `llms.txt`
  for agents. Light and dark, phone width.

- 24 places from the post "30 websites to get free 'Do Follow' backlinks", sent
  by the Analytics session: Launch Llama read and active, Hashnode marked avoid (not a
  directory), Neil Patel's AI tools marked down, the rest unchecked. New kinds:
  review-site, link-directory, marketplace, newsletter, tool-stack, news-site,
  blog-platform.

- First version: 46 places from longbook's listing work, 23 of them read and dated
  on 28 Oct 2026, with the data schema, the README generator, the agent guide, the plan
  template and longbook's plan.
