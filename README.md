# Launch Directories

Every place we know of where an app, an MCP server, an AI tool or its maker can be
listed for free, with what the free listing actually asks for: an account, a badge on
your site, a wait in a queue. Checked by hand, dated, and kept in one data file.

**Site:** https://launchdirectories.fyi (the list with filters, plus
[`directories.json`](https://launchdirectories.fyi/directories.json) and
[`agents.md`](https://launchdirectories.fyi/agents.md) for agents).

Use it to plan where a new product goes, in what order, and what to prepare before you
start. Coding agents can do that planning for you: they read `AGENTS.md`.

## Start

- **To plan listings for a product**, copy `plans/TEMPLATE.md` to `plans/<product>.md`
  and fill in the brief, or ask your agent to (say "read AGENTS.md").
- **To find a place**, read the tables below, or filter `data/directories.json`:

  ```sh
  # Free MCP directories that need no badge
  jq '.directories[] | select(.accepts | index("mcp")) | select(.needs_badge_or_backlink == false) | .name' data/directories.json
  ```

- **To help build the list**, add a place or fix one: see `CONTRIBUTING.md`, or open an
  issue with the Add a place form. Every pull request is checked by CI.

## How to read the tables

- **Takes**: what the place lists (`ios`, `mac`, `mcp`, `ai-tool`, `maker` and so on).
- **Account**: whether the free listing needs an account on that site.
- **Badge or backlink**: whether the free listing needs their badge or a link on your site.
- **Free queue**: how long the free tier waits, in the site's words.
- **Checked**: the day someone last read the free terms. Terms change; re-read anything
  older than three months before relying on it.
- `?` means not known yet.

Paid upgrades exist almost everywhere. They are noted, never recommended.

## Directories

<!-- directories:start -->

25 checked free listings, 40 still to check, 5 to skip.

### AI app stores and MCP directories

| Directory | Takes | Account | Badge or backlink | Free queue | Checked | Notes |
|---|---|---|---|---|---|---|
| [API Tracker](https://apitracker.io/submit) | api, mcp | no | no |  | 2026-10-28 | No payment or backlink needed; every request is reviewed for accuracy. Also takes corrections to existing profiles. |
| [ChatGPT plugin directory](https://platform.openai.com/plugins) | mcp, chatgpt-plugin | yes | no |  | 2026-10-28 | Needs identity verification of the org, a domain challenge at /.well-known/openai-apps-challenge, readOnlyHint/destructiveHint/openWorldHint on every tool, reviewer credentials with no MFA or email codes, 5 positive and 3 negative test cases, and release notes. No plans or upgrades shown in the plugin; the name may not end in MCP or Plugin. |
| [Claude directory](https://claude.ai/directory/manage) | mcp, claude-plugin | yes | no | Weeks of review | 2026-10-28 | Connectors need a title and readOnlyHint/destructiveHint on every tool, plus reviewer test credentials for a populated account. Plugins come from a public GitHub repo (README of 40+ words, LICENSE) with GitHub connected on claude.ai. 10 submissions a day. |
| [mcprush](https://mcprush.com) | mcp, skill | yes | no |  | 2026-10-28 | Lists MCP servers and skills with a grade; badge optional. |
| [Official MCP Registry](https://registry.modelcontextprotocol.io) | mcp | yes | no |  | 2026-10-28 | Publish with the mcp-publisher CLI; the server name's namespace must be verified (GitHub or DNS). |
| [Prowl](https://prowl.world/app) | api, mcp, saas | yes | no |  | 2026-10-28 | Entering a domain runs a free check and creates a listing. Claim it with a DNS TXT record; the score is capped at 75 until verified. Renames go to agent@prowl.world. |
| [Wellknown](https://wellknown.network) | mcp, api | yes | ? |  | 2026-10-28 | Claim to become the verified owner; offers a badge. |

### Launch platforms and directories

| Directory | Takes | Account | Badge or backlink | Free queue | Checked | Notes |
|---|---|---|---|---|---|---|
| [CodeHype](https://www.codehype.ai/submit) | web, saas, ai-tool | yes | ? |  | 2026-10-28 |  |
| [DeepLaunch](https://deeplaunch.io/submit) | web, saas, app, ai-tool | ? | yes | 5 free launch slots a day; pick a date after badge check | 2026-10-28 | Badge is re-checked; removing it turns your link nofollow. |
| [Dodo Payments Index](https://index.dodopayments.com) | web, saas, app | yes | ? |  | 2026-10-28 | Claimable profile. No self-edit for free listings; changes go by email to support@dodopayments.com. |
| [DodoDirectory](https://dododirectory.com/submit) | web, saas, app | ? | yes | About 2 weeks | 2026-10-28 | Badge must stay on your site; removing it deletes the listing. |
| [Dofollow.Tools](https://dofollow.tools/submit) | web, saas, ai-tool | yes | ? | 7 days | 2026-10-28 |  |
| [Fazier](https://fazier.com/submit) | web, saas, app | yes | ? |  | 2026-10-28 |  |
| [FollowX](https://followx.today) | web, saas, app | ? | ? |  | 2026-10-28 | Offers a badge. |
| [Huzzler](https://huzzler.so/submit-product) | web, saas, app | yes | yes | About 72 days | 2026-10-28 | Free plan needs a Huzzler badge on your homepage. |
| [Hype Star](https://hypestar.org/submit) | web, saas, app | no | yes |  | 2026-10-28 | No registration, no card. New free listings need a Hype Star badge on your site. |
| [Launch Llama](https://tools.launchllama.co/submit) | web, saas, ai-tool | ? | ? |  | 2026-11-03 | Free permanent listing with its own product page, upvotes and a dofollow link; featured tier is paid. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi). |
| [neeed.directory](https://neeed.directory/pricing) | web, saas, app, ios | ? | yes |  | 2026-10-28 | Free with their badge on your site, or paid once with no badge. |
| [PeerPush](https://peerpush.com) | web, saas, app, ai-tool | yes | ? | About 7 weeks in the free launch queue | 2026-10-28 |  |
| [Twelve Tools](https://twelve.tools/submit) | web, saas, app, ai-tool | ? | yes | Reviewed within 72 hours | 2026-10-28 | Free tier needs a backlink on your homepage or footer; paid tier skips it. |

### AI tool directories

| Directory | Takes | Account | Badge or backlink | Free queue | Checked | Notes |
|---|---|---|---|---|---|---|
| [AI Tool Trek](https://aitooltrek.com/submit) | ai-tool | ? | yes | Reviewed within 72 hours, listed within 15 days | 2026-10-28 | Listing is removed if the backlink is removed. |
| [AI Toolz Dir](https://www.aitoolzdir.com/submit) | ai-tool | ? | yes |  | 2026-10-28 |  |
| [ToolPilot](https://www.toolpilot.ai/pages/submit-your-ai-tool) | ai-tool | ? | yes |  | 2026-10-28 | AI tools only. A link back is mandatory for free listings. |

### Maker profiles and communities

| Directory | Takes | Account | Badge or backlink | Free queue | Checked | Notes |
|---|---|---|---|---|---|---|
| [IndieMakerList](https://indiemakerlist.com/submit/) | maker | no | no |  | 2026-10-28 | A maker profile, not a product page. Send the template from the submit page as a DM to @johnrush on X. |
| [MakerMap](https://www.makermap.lol/me) | maker | yes | no |  | 2026-10-28 | Products on your profile are free; map placement and rank are paid. |

### Not checked yet

Known places whose free terms nobody has read. Read them before planning a listing, then update the entry.

- [ActiveSearchResults](https://www.activesearchresults.com) (web): A search engine that takes site submissions. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [AI Agents Directory](https://aiagentsdirectory.com/submit-agent) (ai-agent)
- [AlternativeTo](https://alternativeto.net) (web, saas, app, ios, mac): Check whether unreleased or TestFlight apps are accepted.
- [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers/pulls) (mcp): Listing is a pull request to the README; read CONTRIBUTING first.
- [BetaList](https://betalist.com) (web, saas, app)
- [Brownbook](https://www.brownbook.net) (web): Refused automated requests (403). From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [Code.market](https://code.market) (web, saas): Refused automated requests (403). From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [CompareCamp](https://comparecamp.com) (saas): Refused automated requests (403). From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [Dang.ai](https://dang.ai/new) (ai-tool): Submitting needs a login. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [DevHunt](https://devhunt.org) (web, saas, api): Weekly launches of developer tools. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [FeedMyStartup](https://feedmystartup.com/submit-your-app/) (web, saas, app): Separate forms for apps and startups. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [Futurepedia](https://www.futurepedia.io) (ai-tool)
- [G2](https://www.g2.com) (saas, app): Useful once there are real user reviews. Refused automated requests (403). From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [Glama](https://glama.ai/mcp/servers) (mcp)
- [Indie Hackers](https://www.indiehackers.com/products) (web, saas, app)
- [KittyLaunch](https://kittylaunch.com/new/product) (web, saas)
- [LinkCentre](https://www.linkcentre.com) (web): General web directory. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [MacUpdate](https://www.macupdate.com) (mac)
- [MagicBox](https://magicbox.tools/submit) (ai-tool): From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [mcp.so](https://mcp.so) (mcp)
- [Microlaunch](https://microlaunch.net) (web, saas, app, ai-tool): From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [Product Hunt](https://www.producthunt.com/posts/new) (web, saas, app, ios, mac, ai-tool)
- [PulseMCP](https://www.pulsemcp.com) (mcp)
- [Ramen Tools](https://ramen.tools) (web, saas): Shows the tools indie makers use. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [Roozna](https://roozna.com/submit) (web, saas)
- [SaaSHub](https://www.saashub.com) (web, saas, app)
- [ScrollLaunch](https://www.scrolllaunch.com/pricing) (web, saas): Advertises a free launch; terms not read yet.
- [Sidebar](https://sidebar.io/submit) (web): Five design links a day; submitting needs an account. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [SideProjectors](https://www.sideprojectors.com) (web, saas, app): A marketplace for buying and selling side projects. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [Smithery](https://smithery.ai) (mcp)
- [StackShare](https://stackshare.io) (saas, api): Rate-limited automated requests (429). From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [Startup Fame](https://startupfa.me) (web, saas, app): Rate-limited automated requests (429). From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [Startup Stash](https://startupstash.com/add-listing/) (saas): Directory of tools and resources for startups. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [There's An AI For That](https://theresanaiforthat.com) (ai-tool)
- [Toolify](https://toolify.ai) (ai-tool): Refused automated requests (403). From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [Uneed](https://www.uneed.best) (web, saas, app)
- [Uno Directory](https://uno.directory/submit) (web, saas)
- [Viesearch](https://viesearch.com/submit) (web): Community search engine; offers reciprocal-link listings. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [What Launched Today](https://whatlaunched.today/dashboard/submit) (web, saas, app): Submitting needs an account; paid tiers exist. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [YourStory](https://yourstory.com/companies) (saas, app): Company profiles on a startup news site. Refused automated requests (403). From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).

### Skip

- [Boost Domain Rating](https://boostdomainrating.com/boost/submit) (avoid, 2026-10-28): Paid backlink packages, not a free listing.
- [DokeyAI](https://dokeyai.com/en/submit) (avoid, 2026-10-28): Free tier needs a link to a third-party partner's product in your footer.
- [Hashnode](https://hashnode.com) (avoid, 2026-11-03): A blogging platform, not a directory. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).
- [HotVsNot](http://www.hotvsnot.com) (down, 2026-10-28): Did not answer on 2026-10-28.
- [Neil Patel AI tools](https://aitools.neilpatel.com) (down, 2026-11-03): Redirects to ubersuggest.com/en/apps-integrations; the directory looks gone. From the post "30 websites to get free 'Do Follow' backlinks" (Miracle Nnamdi).

<!-- directories:end -->

## Repository layout

```
data/directories.json   the list, one entry per place (the only source)
data/schema.json        what each field means and which values it takes
data/listings.json      where a product is already listed (shown as badges on the page)
plans/TEMPLATE.md       a listing plan for one product
plans/<product>.md      plans in progress or done
scripts/build_readme.py writes the tables above from the data
scripts/build_site.py   builds the landing page into site/dist from the data
scripts/make_icons.swift draws the icon: an SF Symbol on a blue tile (macOS)
scripts/directories.py  loads and checks the data
site/src/               the page template, styles, script, icon and agent guide
site/og.svg             source of the social image (site/src/og.png)
tests/                  checks the data, the README, the page and AGENTS.md
```

## Checks

```sh
python3 scripts/build_readme.py      # rebuild the tables after editing the data
python3 -m unittest discover tests   # what CI runs
```

Python 3.9 or later, standard library only.

## Landing page

Cloudflare Pages project `launch-directories`, direct upload of `site/dist`:

```sh
python3 scripts/build_site.py
npx wrangler@4 pages deploy site/dist --project-name launch-directories --branch main
```

Wrangler reads `CLOUDFLARE_API_TOKEN` and `CLOUDFLARE_ACCOUNT_ID` from the
environment. Rebuild and deploy after every change to the data. The social image
(`site/og.svg`, drawn to `site/src/og.png` with
`sips -s format png site/og.svg --out site/src/og.png`) has no counts, so it only needs
redrawing when its words change.

### The icon

The site's icon is the SF Symbol `paperplane.fill` in white on a blue tile. To change
it, edit `symbolName` in `scripts/make_icons.swift` and run:

```sh
swiftc -o /tmp/make_icons scripts/make_icons.swift && /tmp/make_icons site/src
```

Then redraw the social image (it embeds `icon-208.png`) and rebuild the site. Apple's
terms limit SF Symbols in logos and icons, so treat the symbol as a placeholder if the
project ever becomes more than a small free list.

### Where a product is listed

`data/listings.json` records where the product that owns this copy is listed, one entry
per place and kind (`app`, `mcp`, `plugin`), with a state (`live`, `in-review`,
`in-queue`), the listing's URL and the day it was last seen. The page shows each as a
badge with the product's icon on that place's card.

## Credits

Research and lead generation by
[Lighteningly](https://lighteningly.com/?utm_source=launch-directories&utm_medium=referral&utm_campaign=credit&utm_content=github-readme).

## Licence

The list is dedicated to the public domain under [CC0 1.0](LICENSE).
