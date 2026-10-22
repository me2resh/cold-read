# Sources, endpoints and fallbacks

What worked, by type. Mark anything that comes from a snippet rather than an opened page as 🟡.

## Filings and registries

| Country or market | Source | Notes |
|---|---|---|
| US listed | SEC EDGAR full-text search and company filings (10-K, 10-Q, 8-K, proxy) | Business-combination notes carry price, allocation, earn-out status; proxy carries pay and directors |
| UK | Companies House (officers, filing history, accounts, charges); RNS via the LSE site, Investing.com or MarketScreener when the issuer's site blocks | Accounts give turnover for larger companies; small companies file abridged accounts without turnover |
| Germany | Handelsregister and Bundesanzeiger for accounts and officers | GmbH accounts are often abridged |
| Ireland | CRO | Officers and accounts |
| Australia | ASIC registers; ASX announcements for listed | Private company accounts are rarely public |
| Canada | SEDAR+ for listed; provincial registries | |
| Deals and funding | Deal press releases on the acquirer's investor site; startup press for private rounds; the acquirer's next quarterly filing for the real numbers | The release says "undisclosed"; the filing two months later does not |
| Regulators | Sector regulators' public registers and enforcement pages (health, financial, data protection, advertising, energy, telecoms, transport, as relevant) | Registers show responsible persons, licensed sites, addresses and dates; enforcement pages show the climate |
| Patents and research | Google Patents, Google Scholar, clinical trial registries | Shows what the company is building before it ships |

## Job boards (lane 6)

| System | Public endpoint | Notes |
|---|---|---|
| Ashby | `https://api.ashbyhq.com/posting-api/job-board/<org>` | Full text, dates, pay bands; find `<org>` from the board URL `jobs.ashbyhq.com/<org>` |
| Greenhouse | `https://boards-api.greenhouse.io/v1/boards/<org>/jobs?content=true` | First-published and updated dates; evergreen roles show old dates |
| Lever | `https://api.lever.co/v0/postings/<org>?mode=json` | |
| Teamtailor | `https://<org>.teamtailor.com/jobs.rss` or the custom careers domain plus `/jobs.rss`; each job page has JSON-LD with dates and locations | Department and location taxonomies in the filter UI |
| Workable | `https://apply.workable.com/api/v3/accounts/<org>/jobs` (POST) | |
| Personio | `https://<org>.jobs.personio.de/xml` | |
| SmartRecruiters | `https://api.smartrecruiters.com/v1/companies/<org>/postings` | |
| Closed ads | Search snippets from aggregators (Welcome to the Jungle, Built In, Otta, VC portfolio job pages, niche job boards); archived board pages | Mark 🟡 unless the page opens |

Careers pages on the marketing site commonly return 403 to scripts; go to the ATS endpoint instead.

## Infrastructure (lane 5), all passive

```
dig NS <domain> ; dig A <domain> ; dig MX <domain> ; dig TXT <domain> ; dig TXT _dmarc.<domain>
dig TXT <selector>._domainkey.<domain>      # selectors to try: google, default, selector1, selector2, mandrill, smtpapi, proofpoint, k1, s1, s2, cm, pm, mailgun
dig CNAME <host>.<domain>                   # www, app, api, auth, email, link, status, support, help, mail, shop, checkout
curl -sI https://<host> | sed -n '1,30p'    # server, via, x-cache, x-powered-by, set-cookie names, CSP
curl -s "https://crt.sh/?q=%25.<domain>&output=json"   # certificate transparency; dedupe on name_value; note not_before dates
curl -s "https://web.archive.org/cdx/search/cdx?url=<domain>/<path>&output=json&limit=50&filter=statuscode:200"   # archived copies; fetch one with https://web.archive.org/web/<timestamp>/<url>
curl -s "https://itunes.apple.com/search?term=<name>&country=<gb|de|au|us>&entity=software"   # iOS apps by country: sellerName, releaseDate, currentVersionReleaseDate
```

Page source tells you the front-end platform, analytics and tag managers, consent platform, error tracking, A/B testing, chat and support widgets. Privacy pages tell you the controller, the processors and, for regulated services, the suppliers. Status pages tell you the hosting provider of the status page and sometimes the components.

Google Play has no clean public search API; use the web listing for developer name and update date. Certificate transparency aggregators besides crt.sh: certspotter. If a site challenges fetches, read the archived copy and say so.

## Analysts, press, people (lanes 4 and 7)

- Analyst targets and quotes: Investing.com, MarketScreener, TipRanks summaries, Morningstar public pages, Seeking Alpha transcripts (often paywalled; the company's own investor site usually hosts the webcast and the prepared remarks).
- Trade press by sector; local business press for private companies (startup press, regional business journals).
- People: company team page, press releases announcing appointments, conference programmes and recorded talks, podcasts (search the name plus "podcast" or "episode"), personal sites and blogs (archived if parked), GitHub organisations and profiles, book author pages, university pages. Employee-directory and salary aggregators give titles as snippets; the pages themselves are usually blocked.
- Never open a LinkedIn profile for this work. Snippets from search are acceptable and marked 🟡.

## Comparables (lane 4)

Build the set from: the acquirer's own earlier deals; the sector's well-known integrations in the last ten years; deals by the same kind of buyer (platform acquirer buying regional operators, strategic buying a founder-led company, roll-up). For each, record from filings and press: price, brand outcome, platform outcome, leadership outcome, engineering outcome, timing. Five to eight is enough; the point is the pattern and its timing, not the list.
