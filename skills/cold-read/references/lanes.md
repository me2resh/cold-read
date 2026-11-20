# Lane briefs

Each brief is written so it can be handed to a separate agent as its whole prompt, after filling the placeholders in angle brackets. Every lane produces one Markdown file with this header:

```
# Lane N: <title>
<Companies>, read on <date>. Public sources only. No LinkedIn profiles opened.
Legend: ✅ cited to a source read today (linked); 🟡 inferred or from a snippet that could not be opened; ❔ unknown after looking.
## Sources and how each was read   (table: source | status | fallbacks tried)
## Ten facts that matter most       (numbered, each with a mark and a link)
## Findings                          (tables by topic)
## What it implies                   (🟡 bullets, one inference each, naming the facts it rests on)
## Sources                           (every URL used)
```

Write findings as tables or bullets, never as long paragraphs: one fact per bullet with its mark.

Save raw material (JSON from boards, DNS output, archived HTML) next to the lane file.

---

## Lane 1: corporate record

Goal: the money and the ownership. For `<company>` (and its parent if any): deals announced and closed with price, structure (cash, deferred, stock, earn-out with targets and dates), what was bought (entities, licences, registrations, channels), purchase price allocation (intangibles by class, goodwill), later impairment or earn-out changes; cash, debt and convertibles; directors and officers with appointment and resignation dates from the registry; registered addresses and group entities; auditor and going-concern language.

Sources in order: securities filings (annual report, quarterly reports, 8-K or RNS, notes on business combinations and contingent consideration), company registry filings in each country (directors, charges, accounts, confirmation statements), deal press releases, annual report pages on strategy and risk. Read the filing, not the press summary of it.

Output: a two-column table (item, finding with mark and link); a dated list of director and officer changes; the ten facts.

## Lane 2: counterparty, or product and money

For a deal: repeat lane 1 for `<other company>`, plus founding, funding history and valuations, revenue and losses from any public accounts, customer counts, brands, leadership and what each leader was promised at the deal (titles, earn-outs, retention).

For a single company: products and brands, pricing pages, customer and usage counts, revenue by segment where filed, gross margin and its drivers, the regulated status of each product (device class, licence, registration), release cadence from app stores and changelogs.

For the compete lens, go deeper on the product: every tier with its price, its unit (per seat, per site, per transaction) and what it gates; each price change dated from archived copies of the pricing page; the documentation and API reference as the true feature list; the changelog, release notes, public repositories and app version history for the last twelve months; integrations and marketplace listings in both directions (who lists them, whom they list); customers who name the company themselves (their own page, a case study with a named person, a procurement record), kept apart from logos on the company's site, which are claims. Do not sign up for a trial or a demo to read the product.

For the partner lens, read the offer the reader would rely on: the partner programme or supplier terms as published (tiers, margins, exclusivity, termination, who owns the customer), service levels and the status page's incident history, certifications checked on the issuer's register with scope and dates, sub-processors and where data sits, and every partner, reseller or supplier relationship the record names, with what became of each.

## Lane 3: what it says versus what it does

Collect dated quotes from earnings calls, shareholder letters, interviews and press releases about `<topic: integration, platform, brand, international, roadmap>`. Against each, record what then happened: product launches and their platform (which domain, which app, which privacy controller), brand retirements, account migration notices, privacy and terms page changes (controller, processors, suppliers named), app store listings by country (developer name, first release date, last update), archived page diffs over time.

Output: a two-column says/does table with dates and marks, then a dated timeline of what actually happened, then the brand and platform plan as far as it can be read.

For the compete lens the topics are the roadmap, pricing and the customers it claims; record too how it answered earlier entrants (price cuts, copied features, comparison pages, acquisitions), each dated. For the partner lens the topic is partners: what it says about partnership against what happened to named partners, including any it later competed with, dropped or bought.

## Lane 4: market, analysts, regulators, comparables

Analyst split with names, dates, ratings, targets and the one sentence each gave as a reason. Press framing (growth story, defensive move, distress). Regulatory climate for the business model in each main market: enforcement actions, guidance changes, advertising rulings, licence conditions, with dates. Then five to eight named comparable situations (same acquirer type, same sector, same integration shape) with: price, whether the brand survived, what happened to the platform, what happened to the leadership and the engineering organisation, and over what period. Close with the general pattern and the base rate it implies.

Output: analyst table; regulatory paragraph; comparables table; pattern paragraph marked 🟡.

For the compete lens, add review sites and community threads as snippets (🟡: each review is one person's account, and unhappy customers write most of them) and the two or three earlier entrants this competitor has faced, with what it did. For the partner lens the comparables are other companies that partnered with this kind of company (a platform and its integrators, a distributor and its suppliers, a large client and its small vendors): how long the relationship lasted, who ended it, and whether the larger side absorbed the smaller side's work.

## Lane 5: infrastructure fingerprint (passive, read-only, cited with the command)

Only passive public lookups: DNS records (NS, A, MX, TXT, CNAME for known hosts), certificate transparency search for each domain, HTTP response headers and public HTML of marketing, login, privacy and status pages, archived copies where live pages block fetches, app store metadata via public search APIs. No port scans, no login attempts, no authenticated endpoints, no rate-abusive crawling.

Record per company: DNS hosting and apex hosting; CDN and WAF; origin cloud and region; front-end and analytics tags; consent platform; error tracking; A/B testing; corporate mail provider and security vendors (MX, SPF, DKIM selectors, DMARC and where reports go); transactional and marketing mail providers; identity provider tenants; support tooling; privacy controller names and addresses per country; mobile apps by country with developer name and dates; vulnerability disclosure and phishing-simulation hosts; shared tenants or vendors across the group that show the estates are joined.

Output: one table per company with a mark and the command or URL for each row; a headline paragraph on what the fingerprint says about how the estates are joined; a short list of what a migration would look like in this data if it happened.

## Lane 6: the openings as the plan

Pull every open role for each company from the applicant-tracking system's public API where one exists (see sources), else the board page and its RSS feed, else aggregator snippets marked 🟡. For each role: title, function, location, seniority, brand or entity, posted date, and one line on what the ad says it will build or change. Then: counts by function, location and seniority; the five ads that matter most for the question and why; the roles that have disappeared compared with archived boards or earlier snippets; predictions by horizon (6, 12, 24 months) marked 🟡; ten roles that would tell the most if they appeared next.

For the compete lens, read each ad for what it says the company will build, enter or stop, and treat the five that matter most as roadmap items with a horizon. For the partner lens, read two things: hiring or cuts in the function the reader would depend on (capacity), and any ad to build or buy what the reader would supply (a plan to replace the partner), plus partnership, alliance and channel roles (how seriously partners are staffed).

Watch for: a corporate board and a regional board listing the same company; evergreen requisitions; a department and location taxonomy on a board with few roles in it (the taxonomy shows what the company was; the roles show what it is allowed to do now); an ad that merges two organisations or migrates two businesses, which is the clearest integration signal there is.

## Lane 7: people

For each named person: current title and the date it was confirmed (team page, press release, filing); career history from press, talks, books, podcasts, blogs, GitHub and conference bios; what they have written or said about how they work and what they value; whether they are on the board or the leadership page; what they are likely to test in a conversation, as a one-line read. Rule out name collisions explicitly (different employer, city, field). State at the top that no profile page was opened. Where a person does not appear in the public record, say so and stop; do not extrapolate from a title.

Output: one section per person with marks; a short structural reading of how the people fit together (who reports to whom, as far as public); three to five questions the reading suggests.
