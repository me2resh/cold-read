# Platterloop and the Head of Engineering role: the stack, the mandate and the people, from the outside

Read on 9 May 2026. Public record only. No LinkedIn profile was opened.
Legend: ✅ cited to a source read that day and linked; 🟡 inferred from the record, or from a snippet that could not be opened; ❔ not found after looking.
Sources: 69 footnotes across 7 lanes.
Sample read: the company is a sample and the figures are illustrative; links point at example.org; the method, the sources and the marks are as shipped.

## 1. The platform in one paragraph

Platterloop sells ordering, kitchen display and payments to about 2,400 UK restaurants, the count the homepage carried on the day of the read ✅ [^s2-8]. The pricing page sells the three products as separate tiers, and the FY2024 accounts put 70% of revenue on the ordering product alone ✅ [^s2-1] [^s1-2]. The estate is one Rails monolith on AWS London with a React front end and a React Native staff app, as the ads and the response headers agree ✅ [^s6-3] [^s5-3]. A newer Go payments service sits between the monolith and the card acquirer, described in an engineering post of 9 September 2025 ✅ [^s3-7]. Ads posted since January 2026 describe a split of the monolith into "ordering" and "kitchen" services and a move of reporting from Postgres read replicas to a cloud data warehouse ✅ [^s6-3] [^s6-4] [^s6-7]. Whether any slice of the split has shipped is 🟡, because the ads say the work "has started" (Senior Backend Engineer (Ordering) ad, 27 January 2026) and no changelog entry names a service. The founder CTO is moving to product and the Head of Engineering role will report to the CEO, both stated in the ad ✅ [^s6-2]. Fourteen roles were open on the applicant-tracking board on the day of the read, nine of them in engineering ✅ [^s6-1].

## 2. Chapters

The chapters follow the order the company uses on its own product navigation: ordering, kitchen display, payments, then reporting ✅ [^s2-8].

### 2.1 Ordering

Ordering is the oldest product and the one most customers buy; the pricing page sells it on its own and the accounts put 70% of FY2024 revenue on it ✅ [^s2-1] [^s1-2]. The ordering product page describes QR ordering at the table, a staff app for order taking and a till integration ✅ [^s2-2]. Four open ads sit in this area: two backend, one React Native, one engineering manager ✅ [^s6-1].

| Component | What it does | Runs on today | Mark | Where it is heading |
|---|---|---|---|---|
| Menu and order API | Order capture from QR, staff app and till | Rails, Postgres, Sidekiq and Redis, named in three ads ✅ [^s6-3] [^s6-10] [^s6-9] | ✅ [^s6-3] | Extraction to an "ordering" service; two ads name "Go or Kotlin" for it (ads of 27 January and 15 April 2026) ✅ [^s6-3] [^s6-10]; whether it has shipped is 🟡, because the changelog has no entry for it |
| QR web ordering | Guest-facing menu, basket and pay on the phone | React and Next.js served by a static hosting vendor, per the response headers and the page source ✅ [^s5-3] [^s5-8] | ✅ [^s5-3] | Unchanged 🟡, because no ad asks for a change to it |
| Staff app | Order taking at the table, rated 4.3 on the iOS store, last update 2026-04-02 ✅ [^s2-5] | React Native, named in the ad and in the store metadata ✅ [^s6-9] [^s5-7] | ✅ [^s2-5] | Monthly releases, eleven versions in the twelve months to the read on the store history ✅ [^s2-5] |
| Till integration | Pushes orders into third-party tills | Rails jobs and partner webhooks, per the integrations directory of 23 partners ✅ [^s2-12] | 🟡, because the directory lists the partners but not the mechanism | A "till partner API" is promised for "summer 2026" in the changelog entry of 2026-03-18 ✅ [^s2-7] |
| Menu sync | Keeps menus the same across QR, app and till | ❔ not described in the four ordering ads, the help centre or the changelog | ❔ | ❔ |

### 2.2 Kitchen display

The kitchen display product runs on tablets in the kitchen and takes orders from the ordering product; the product page describes it as "works when the wifi drops" ✅ [^s2-3]. The Android store listing for the kitchen app shows its last update on 2026-03-26 ✅ [^s2-6]. One ad, Senior Backend Engineer (Kitchen), is open in this area ✅ [^s6-4].

| Component | What it does | Runs on today | Mark | Where it is heading |
|---|---|---|---|---|
| Kitchen screen app | Ticket display, bump and recall on a tablet | React in a native shell, "offline-first" per the kitchen ad of 3 February 2026 ✅ [^s6-4] [^s2-6] | ✅ [^s6-4] | A "kitchen" service extracted from the monolith, named in the same ad ✅ [^s6-4]; 🟡 on timing, because the ad gives none |
| Order routing | Sends each ticket to the right station | Rails with Action Cable websockets, per the kitchen ad ✅ [^s6-4] | ✅ [^s6-4] | The CTO's 2023 talk called websockets "the part that keeps me up" (Ruby conference, 21 September 2023) ✅ [^s7-3]; a managed pub-sub is 🟡, because a hostname `events.` appears in the certificate log and nowhere in words |
| Printer bridge | Prints tickets where there is no screen | A locally installed bridge; language not named ❔ not in the ad, the help centre or the product page | ❔ | ❔ |
| Ticket times | Measures prep time per dish and per station | A changelog entry of 2025-11-04 added "ticket times" to the owner dashboard ✅ [^s2-7] | ✅ [^s2-7] | Feeds the reporting chapter 🟡, because the Analytics Engineer ad names "kitchen timing models" |

### 2.3 Payments

Payments is the newest product and the one the CEO calls the growth bet: "payments is where the next three years come from" (trade press interview, 11 February 2026) ✅ [^s3-4]. The payments page sells card terminals, tap to pay on the staff app and a fee "from 1.4%" per transaction ✅ [^s2-4]. One Go ad is open in this area ✅ [^s6-5].

| Component | What it does | Runs on today | Mark | Where it is heading |
|---|---|---|---|---|
| Payments service | Authorises, captures and ledgers each payment | Go on ECS, with an idempotent ledger in Postgres, per the engineering post of 9 September 2025 ✅ [^s3-7] | ✅ [^s3-7] | The Go ad asks for "a second engineer on the service" (10 March 2026) ✅ [^s6-5]; a team of one today is 🟡, because the post is by one author and the ad asks for a second |
| Card acquiring | Moves the money | A licensed e-money institution for which Platterloop is a registered agent ✅ [^s1-8] | ✅ [^s1-8] | Unchanged 🟡, because the register entry is dated 2025-11-20 and nothing newer appears |
| Card data | Keeps card numbers off Platterloop servers | Hosted fields from the acquirer, "card data never touches our servers" per the payments page (read 9 May 2026) ✅ [^s2-4] | ✅ [^s2-4] | Unchanged 🟡, because a change here would need a new regulator entry and none exists |
| Terminals and tap to pay | Card-present payment at the table | Acquirer-supplied terminals; tap to pay on the staff app added in the changelog entry of 2026-03-04 ✅ [^s2-7] | ✅ [^s2-7] | Tap to pay on the kitchen tablet is "coming" per the same entry ✅ [^s2-7] |
| Payouts and tronc | Daily payout files and tip allocation | A payout file documented in the help centre, updated 2026-02-03, and a tronc feature added after the 2024 tips rules ✅ [^s2-11] [^s2-7] [^s4-8] | ✅ [^s2-11] | ❔ not in the ads or the changelog |

### 2.4 Reporting and data

Reporting today is a set of owner dashboards on Postgres read replicas, as the Data Engineer ad says in plain words ✅ [^s6-7]. Two ads, Data Engineer and Analytics Engineer, are open in this area and both describe a move to a cloud data warehouse ✅ [^s6-7] [^s6-8].

| Component | What it does | Runs on today | Mark | Where it is heading |
|---|---|---|---|---|
| Owner dashboard | Sales, items, ticket times per site | Rails views on Postgres read replicas, per the Data Engineer ad of 18 February 2026 ✅ [^s6-7] | ✅ [^s6-7] | Rebuilt on the warehouse 🟡, because both data ads say "move reporting off the replicas" |
| Exports | CSV exports and the payout file | Nightly jobs documented in the help centre ✅ [^s2-11] | ✅ [^s2-11] | ❔ not in the ads or the changelog |
| Warehouse | A copy of the data for analysis | A cloud data warehouse and a managed ELT tool, named in the Data Engineer ad ✅ [^s6-7] | 🟡, because the ad names the tools as the target, not the present | The first hire for it is the open Data Engineer ad ✅ [^s6-7] |
| Analytics models | Shared metrics across sites | A SQL modelling tool, named in the Analytics Engineer ad of 1 April 2026 ✅ [^s6-8] | 🟡, because nothing on the site shows these models exist yet | "Benchmarks across sites" is a waitlist page on the site ✅ [^s2-8] |
| Data in the apps | Ticket times, menu performance in the staff app | ❔ not in the store listings or the changelog | ❔ | ❔ |

## 3. Platform, infrastructure, delivery and quality

The Platform Engineer ad names AWS eu-west-2, ECS on Fargate, Terraform, the git host's hosted CI and a hosted observability vendor ✅ [^s6-6]. The status page monitors the same observability vendor's endpoint and lists the API, the ordering page, the kitchen app and payments as four components ✅ [^s5-4] [^s2-10]. DNS resolves the API hostname to an application load balancer in eu-west-2 (`dig +short api.platterloop.example.org`, run 9 May 2026) ✅ [^s5-1]. The certificate log shows 23 hostnames issued since 2024-01-01, among them `kds.`, `pay.`, `events.` and `api-v2.` ✅ [^s5-2]. The `api-v2.` hostname is 🟡 as the home of the split services, because it appears in the certificate log and in no ad or page. The archived DNS record for the ordering page points at a different host on 2024-09-02 than it does today, so the move of QR ordering to the static hosting vendor is 🟡 dated to between September 2024 and the read [^s5-5].

On-call is "shared across squads, one week in five" per the Platform Engineer ad (17 March 2026) ✅ [^s6-6]. The platform team is two people, 🟡, because the same ad says "join a platform team of two" and no other source gives a number. No SRE, DevOps or security role has ever been advertised ❔ not on the board, the archived careers page of 14 January 2025 or an aggregator search run on 9 May 2026 [^s6-15] [^s6-16]. The status page shows seven incidents in the 90 days to the read, two of them on payments, with a mean time to resolve of 41 minutes ✅ [^s2-10]. The payments incidents were 2026-02-27 and 2026-04-11, both "degraded card capture" ✅ [^s2-10].

Delivery cadence is monthly for the staff app on the store history ✅ [^s2-5], and the changelog carries 14 entries in 2026 to the read ✅ [^s2-7]. The CTO wrote in 2024 that the company runs "trunk-based development and deploys to production many times a day" (blog post, 12 June 2024) ✅ [^s3-2]. Whether that still holds under the split is 🟡, because the 2026 posts do not repeat the claim. Quality is one open ad, Test Automation Engineer, which asks for "our first dedicated QA hire" (22 April 2026) ✅ [^s6-11]; before it, testing was 🟡 left to squads, because no ad or post names anyone else doing it.

## 4. Regulatory, quality and security

Platterloop is a registered agent of a licensed e-money institution on the payments regulator's register, entry dated 2025-11-20 ✅ [^s1-8]. It is not itself licensed ❔ not on the register under its own name or either trading name. The payments page states that card data never touches Platterloop servers and that card capture uses the acquirer's hosted fields ✅ [^s2-4]; the PCI scope that implies is 🟡 the smallest self-assessment, because the page says so in effect and no attestation is published. The regulator's 2025 review of acquiring fees for small merchants is the document that sets what "from 1.4%" competes against ✅ [^s4-5].

The privacy policy lists 11 sub-processors and was updated on 1 March 2026 ✅ [^s3-6]. The mail records carry SPF and a DMARC policy of "p=none" on the day of the read ✅ [^s5-6]; that is an observation about mail configuration, not a finding to raise unless asked. No ISO 27001, SOC 2 or penetration test claim appears ❔ not on the security page, the pricing page or the help centre. No security role has been advertised ❔ not on the board or the aggregator search [^s6-16].

Two product rules shape the ordering and payments chapters. The ordering page carries allergen information per dish and says the product meets the 2021 pre-packed food labelling rules ✅ [^s2-2]. The tronc feature in payments followed the 2024 tips allocation rules, in force from 1 October 2024 ✅ [^s4-8] [^s2-7].

## 5. Org and ways of working

The FY2024 accounts give an average of 118 employees for the year ✅ [^s1-2]. The Head of Engineering ad says the engineering team is 38 people and that the hire will "double the team over 18 months" (ad of 8 April 2026) ✅ [^s6-2]. Against 14 open roles, the ad's "double" is 🟡 a plan rather than a budget, because 14 is less than half of 38. The board JSON names five squads in the ad metadata: Ordering, Kitchen, Payments, Data and Platform ✅ [^s6-1]. The Engineering Manager, Ordering ad is the only manager role open and asks for "our first engineering manager" (15 April 2026) ✅ [^s6-10]; the squads today are 🟡 led by senior engineers reporting to the CTO, because the ad says "first" and the team page lists no managers.

Ads for backend roles say "hybrid, two days in the London office" ✅ [^s6-3], and the Go payments ad says "remote within the UK" ✅ [^s6-5]. The archived careers page of 14 January 2025 showed six open roles, all engineering ✅ [^s6-15]. A closed Senior Rails Engineer ad was first seen on an aggregator in June 2025 and is 🟡, because the aggregator page could not be opened [^s6-14]. Levels, pay bands and the interview loop are ❔ not in any of the ten ads read or on the careers page.

The CTO's 2024 post set the engineering style: "we pick boring technology and we pay for it with discipline, not with tooling" (blog post, 12 June 2024) ✅ [^s3-2]. The engineering blog carried four posts in 2025 and two in 2026 to the read ✅ [^s3-7] [^s3-3]. The January 2026 post explains the split as a reaction to "deploys that take the whole kitchen product down with an ordering bug" (20 January 2026) ✅ [^s3-3].

## 6. Leadership

The people note for this read sits beside it as `2026-05-09-platterloop-people.md` and is not included in the samples. Titles below are confirmed from the team page read on 9 May 2026 or from a dated release, as the table says ✅ [^s7-1].

| Person | Title, confirmed where and when | Background | Mark |
|---|---|---|---|
| The CEO | Chief Executive and co-founder, team page, 2026-05-09 ✅ [^s7-1] | Ran a six-site restaurant group before founding the company, per a press profile of 8 March 2024 ✅ [^s7-6]; two podcast appearances on operator pain, 2025-11-20 and 2026-03-12 ✅ [^s3-1] [^s3-9]; conference talk "Operators do not buy software", 2025-06-18 ✅ [^s7-2] | ✅ [^s7-1] |
| The CTO | Chief Technology Officer and co-founder, team page, 2026-05-09 ✅ [^s7-1]; "moving to a product role" per the Head of Engineering ad, 2026-04-08 ✅ [^s6-2] | Wrote the monolith's first version 🟡, because the 2023 talk is in the first person about "the code I wrote in 2018" (21 September 2023) [^s7-3]; author of the 2024 "boring technology" post ✅ [^s3-2] | ✅ [^s7-1] |
| The VP Product | VP Product, appointment release, 2025-10-07 ✅ [^s3-8] | Joined from a food-delivery marketplace, per the release ✅ [^s3-8]; described her approach as "release trains and a public roadmap" on a product podcast (29 January 2026) ✅ [^s7-4] | ✅ [^s3-8] |
| The Head of Engineering | The role; reports to the CEO, per the ad, 2026-04-08 ✅ [^s6-2] | Not yet filled ✅ [^s6-1]; the ad asks for "someone who has run a split like this before" ✅ [^s6-2] | ✅ [^s6-2] |
| The investor director | Non-executive director, registry appointment, 2025-03-10 ✅ [^s1-4] | Partner at the Series B fund, per the fund's team page ✅ [^s7-5] | ✅ [^s1-4] |

The registry lists four current directors: the two founders, the investor director and one earlier investor ✅ [^s1-10]. No COO, CFO or VP Engineering appears on the team page ❔ not on the team page, the officers list or any release.

One-line reads, each 🟡 because they are readings of what each person has said in public, not statements of fact:

- The CEO will test whether the candidate can talk to restaurant owners, not only to engineers 🟡, resting on the two podcast episodes about operator pain [^s3-1] [^s3-9].
- The CTO will test whether the candidate respects what was built; the 2024 post on boring technology is the tell 🟡, resting on that post and the 2023 talk [^s3-2] [^s7-3].
- The VP Product will test whether engineering can give dates 🟡, resting on her podcast description of release trains [^s7-4].
- The investor director will test the hiring plan against the raise 🟡, resting on the fund's stated focus on "capital-efficient growth" (fund team page, read 9 May 2026) [^s7-5].

## 7. Market

The trade body counted about 99,000 licensed hospitality sites in the UK in 2025 and put restaurant software spend at £1.1bn ✅ [^s4-1]. The industry survey recorded net closures of 3.2% of restaurant sites in 2025 ✅ [^s4-2]. Against that, Platterloop's homepage count went from 1,100 restaurants on the archived copy of 15 May 2024 to 2,400 on the day of the read ✅ [^s3-5] [^s2-8]; the growth is 🟡 partly from a 40-site group signed in November 2025, because that is the only customer the company names [^s2-9].

The analyst market map of March 2026 places 14 vendors in UK restaurant software and lists Platterloop among the "ordering-first" group, not the "till-first" group ✅ [^s4-4]. One competitor raised a Series C of £45m in September 2025 and says it will add payments ✅ [^s4-3]. The CEO's trade press interview of 11 February 2026 names the till-first vendors as the ones to beat and says "we will never build a till" ✅ [^s3-4].

The base rate that matters for this role is what happens after a founder CTO moves to product. Comparable A, a restaurant ordering company of similar size, moved its founder CTO to product in 2023 and hired a Head of Engineering the same year; the trade press reported the hire's departure within 14 months ✅ [^s4-6]. Comparable B split a monolith under a new engineering leader in 2024 and reported the leader's exit before the split finished ✅ [^s4-7]. Two cases are not a base rate 🟡, and the reading they support is only that the role has a short clock unless the founder's remit is settled on day one.

## 8. Money

| Item | Figure | Period | Source | Mark |
|---|---|---|---|---|
| Last raise | £18m Series B | 2025-03-04 | Press release ✅ [^s1-5]; shareholder list on the confirmation statement ✅ [^s1-3] | ✅ [^s1-5] |
| Earlier raise | £6m Series A | 2022-06-14 | Press release ✅ [^s1-6] | ✅ [^s1-6] |
| Revenue | £9.6m | FY2024 | Annual accounts, filed 2025-09-26 ✅ [^s1-2] | ✅ [^s1-2] |
| Revenue by segment | Ordering 70%, payments 18%, kitchen display 12% | FY2024 | Segment note in the annual accounts ✅ [^s1-2] | ✅ [^s1-2] |
| Operating loss | £4.1m | FY2024 | Annual accounts ✅ [^s1-2] | ✅ [^s1-2] |
| Cash at year end | £7.2m, before the Series B | 2024-12-31 | Annual accounts ✅ [^s1-2] | ✅ [^s1-2] |
| Going concern | "at least twelve months from the date of approval", with the Series B cited | Accounts approved 2025-09-19 | Annual accounts ✅ [^s1-2] | ✅ [^s1-2] |
| Runway | About four years at the FY2024 burn, before the hiring plan | From 2025-03-04 | Computed from cash, the raise and the loss above | 🟡, because the hiring plan in the ads would raise the burn and FY2025 accounts are not yet filed |
| Debt | A charge in favour of a venture lender; amount not public | 2025-10-15 | Charge register ✅ [^s1-9] | ✅ [^s1-9] |
| Pricing | £59 to £199 per site per month; payments "from 1.4%" | Read 2026-05-09 | Pricing and payments pages ✅ [^s2-1] [^s2-4] | ✅ [^s2-1] |
| FY2025 revenue | not public | FY2025 | Would be in the FY2025 accounts, due by 2026-09-30 at the registry [^s1-1] | ❔ not filed at the read |

Payments revenue of 18% of £9.6m on FY2024 is about £1.7m, and the CEO's "next three years" claim rests on growing that share ✅ [^s1-2] [^s3-4]; whether the take rate holds against the regulator's fee review is 🟡, because the review recommends transparency, not caps [^s4-5]. The registered office moved on 2 July 2025 to a larger London address ✅ [^s1-7].

## 9. What it means for the mandate

**Owns.** The ad gives the role the five squads, the platform team and the hiring plan, reporting to the CEO ✅ [^s6-2]. It does not give the role product, which moves with the CTO ✅ [^s6-2]. What the role owns in architecture is 🟡, because the ad says "own the technical roadmap" and the CTO's new remit is not written down anywhere public.

**Inherits.** A monolith split that two ads say has started and none says has finished ✅ [^s6-3] [^s6-4]; a Go payments service that is the company's revenue bet and that two incidents in 90 days touched ✅ [^s3-7] [^s2-10]; a platform team of two with no SRE practice 🟡, resting on the Platform Engineer ad; a founder CTO moving sideways, which makes the first ninety days about trust with the people who built it 🟡, resting on the ad and the 2024 post; and 14 open roles against a "double the team" line, which makes the role a hiring role first ✅ [^s6-1] [^s6-2].

**Is broken.** Reporting runs on read replicas that both data ads want to leave ✅ [^s6-7] [^s6-8]. Deploys couple the kitchen product to ordering bugs, by the company's own January 2026 account ✅ [^s3-3]. Testing has had no owner, by the April 2026 ad's own words ✅ [^s6-11]. Card capture degraded twice in the 90 days to the read ✅ [^s2-10]. The management layer is one open engineering manager role and nothing else ✅ [^s6-10].

**First quarter must deliver.** A written remit between the role and the CTO, since the public record has none ❔ not in the ad, the release or the team page. One slice of the split in production with a changelog entry, so that the "has started" line becomes a date 🟡. A payments incident review that the CEO can read, since payments is the stated bet ✅ [^s3-4]. The first engineering manager and the first QA hire in seat, since both ads call them "first" ✅ [^s6-10] [^s6-11]. A hiring plan that reconciles 14 roles with "double the team" 🟡, resting on the board count and the ad.

## 10. Vocabulary to have ready

- "The split": the company's own name for extracting "ordering" and "kitchen" services from the Rails monolith, from the January 2026 post ✅ [^s3-3].
- "Ticket times": prep time per dish and per station, added to the owner dashboard in November 2025 ✅ [^s2-7].
- "Bump": clearing a ticket from the kitchen screen; the product page uses it ✅ [^s2-3].
- "Tronc": the pooled tips arrangement the payouts feature supports, under the 2024 rules ✅ [^s4-8].
- "Hosted fields": the acquirer's card entry components that keep card data off the company's servers ✅ [^s2-4].
- "Read replicas": where reporting runs today and what the data ads want to leave ✅ [^s6-7].
- "Boring technology": the CTO's 2024 phrase for the engineering style ✅ [^s3-2].
- "Ordering-first": the analyst map's label for the company's group of vendors ✅ [^s4-4].
- "Release trains": the VP Product's phrase for her cadence ✅ [^s7-4].
- "One week in five": the on-call rotation per the Platform Engineer ad ✅ [^s6-6].

## 11. Questions by round

The rounds are not published ❔ not in the ad or on the careers page, so the subsections below follow the usual order.

### Recruiter

1. Which of the 14 open roles are backfills and which are new seats? The board count is ✅ [^s6-1]; the split is not public.
2. Is the Head of Engineering a new role or a replacement, and when was it signed off? The ad is the first appearance of the title on the board ✅ [^s6-1].
3. What does the CTO's product role cover, and from what date? The ad says "moving" without a date ✅ [^s6-2].
4. What are the bands for this role and for the engineering manager role? Bands are ❔ not in any ad read.

### Hiring manager

1. What has shipped from the split so far, and what is the next slice? The January 2026 post gives the reason and no date ✅ [^s3-3].
2. Who is on call tonight, and what happened the last time card capture degraded? The status page shows 2026-04-11 as the last time ✅ [^s2-10].
3. How many of the 38 engineers have been here since before the Series A? The team size is ✅ [^s6-2]; tenure is ❔ not public.
4. What does "double the team over 18 months" assume about revenue, and who signed it off? The line is ✅ [^s6-2].
5. Which decisions stay with the CTO after the move?

### Peers

1. For the VP Product: what does a release train look like today, and what slipped last quarter? Her description is ✅ [^s7-4].
2. For the senior engineers leading squads: what do they want from a first engineering manager? The ad calls it the first ✅ [^s6-10].
3. For the platform engineers: what runs on `api-v2.` today? The hostname is ✅ in the certificate log [^s5-2] and nowhere in words.
4. For the payments engineer: what does the second hire take off their plate? The ad asks for a second ✅ [^s6-5].

### Executive

1. For the CEO: what does "payments is where the next three years come from" mean in numbers, and what happens to the plan if the take rate falls? The quote is from 11 February 2026 ✅ [^s3-4].
2. For the CEO: what is the engineering budget for FY2026, and does it already include the 14 roles?
3. For the investor director: what does the board see as the test for this hire at six months? The fund's stated focus is ✅ [^s7-5].
4. For the CTO: what would make the move to product feel like a success a year from now?

## 12. Job ads and the stack each one names

Ten of the 14 ads on the board are listed; the other four are sales and support roles with no stack named ✅ [^s6-1]. Posted dates are the board's first-published dates ✅ [^s6-1].

| Ad | Posted | Location | Stack named | Signal |
|---|---|---|---|---|
| Head of Engineering ✅ [^s6-2] | 2026-04-08 | London, hybrid | Rails, Go, React Native, AWS | Reports to the CEO; "double the team over 18 months"; the CTO moving to product ✅ [^s6-2] |
| Senior Backend Engineer (Ordering) ✅ [^s6-3] | 2026-01-27 | London, hybrid | Rails, Postgres, Sidekiq, Redis, "Go or Kotlin" | The split "has started" ✅ [^s6-3] |
| Senior Backend Engineer (Kitchen) ✅ [^s6-4] | 2026-02-03 | London, hybrid | Rails, Action Cable, React, "offline-first" | A "kitchen" service to be extracted ✅ [^s6-4] |
| Software Engineer, Payments (Go) ✅ [^s6-5] | 2026-03-10 | Remote, UK | Go, Postgres, ECS | "A second engineer on the service" ✅ [^s6-5] |
| Platform Engineer ✅ [^s6-6] | 2026-03-17 | London, hybrid | AWS eu-west-2, ECS on Fargate, Terraform, hosted CI, hosted observability | "Platform team of two"; on-call "one week in five" ✅ [^s6-6] |
| Data Engineer ✅ [^s6-7] | 2026-02-18 | London, hybrid | Postgres read replicas, cloud data warehouse, managed ELT | Reporting to leave the replicas ✅ [^s6-7] |
| Analytics Engineer ✅ [^s6-8] | 2026-04-01 | London, hybrid | SQL modelling tool, cloud data warehouse | "Kitchen timing models"; benchmarks product 🟡, because the site only has a waitlist page |
| Senior React Native Engineer ✅ [^s6-9] | 2026-02-24 | London, hybrid | React Native, Rails API | Monthly app releases to continue ✅ [^s6-9] |
| Engineering Manager, Ordering ✅ [^s6-10] | 2026-04-15 | London, hybrid | Rails, "Go or Kotlin" | "Our first engineering manager" ✅ [^s6-10] |
| Test Automation Engineer ✅ [^s6-11] | 2026-04-22 | London, hybrid | Not named beyond "our web and mobile apps" | "Our first dedicated QA hire" ✅ [^s6-11] |
| Product Designer ✅ [^s6-12] | 2026-03-24 | London, hybrid | None | Reports to the VP Product ✅ [^s6-12] |
| Customer Success Manager ✅ [^s6-13] | 2026-04-29 | London, hybrid | None | Names the 40-site group as a reference account ✅ [^s6-13] |

No ad names Kafka, Kubernetes, a service mesh or a second cloud ❔ not in the twelve ads read. No ad was older than 2026-01-27 on the board, so there are no evergreen requisitions to discount ✅ [^s6-1].

## 13. Sources by lane

### Lane 1

[^s1-1]: UK company registry, filing history for Platterloop Ltd, read 2026-05-09 https://example.org/registry/company/11223344/filing-history
[^s1-2]: Annual accounts for the year ended 31 December 2024, filed 2025-09-26 https://example.org/registry/company/11223344/accounts/2024.pdf
[^s1-3]: Confirmation statement with shareholder list, made up to 2026-01-31 https://example.org/registry/company/11223344/confirmation-statement/2026.pdf
[^s1-4]: Director appointment form for the investor director, 2025-03-10 https://example.org/registry/company/11223344/officers/appointment-2025-03-10
[^s1-5]: Series B press release, £18m, 2025-03-04 https://example.org/platterloop/press/series-b-2025
[^s1-6]: Series A press release, £6m, 2022-06-14 https://example.org/platterloop/press/series-a-2022
[^s1-7]: Registered office change, 2025-07-02 https://example.org/registry/company/11223344/address-change-2025
[^s1-8]: Payments regulator register, agent entry for Platterloop Ltd under a licensed e-money institution, entry dated 2025-11-20, read 2026-05-09 https://example.org/payments-register/agents/PL-900123
[^s1-9]: Charge registered against the company in favour of a venture lender, 2025-10-15 https://example.org/registry/company/11223344/charges/2025-10-15
[^s1-10]: Officers page, four current directors, read 2026-05-09 https://example.org/registry/company/11223344/officers

### Lane 2

[^s2-1]: Pricing page, three tiers, read 2026-05-09 https://example.org/platterloop/pricing
[^s2-2]: Ordering product page, read 2026-05-09 https://example.org/platterloop/product/ordering
[^s2-3]: Kitchen display product page, read 2026-05-09 https://example.org/platterloop/product/kitchen-display
[^s2-4]: Payments product page with the card-data and fee statements, read 2026-05-09 https://example.org/platterloop/product/payments
[^s2-5]: iOS store listing for the Platterloop staff app, version history, read 2026-05-09 https://example.org/ios-store/app/platterloop-staff/id1234567890
[^s2-6]: Android store listing for the Platterloop kitchen app, read 2026-05-09 https://example.org/android-store/details?id=org.example.platterloop.kds
[^s2-7]: Product changelog, entries from 2025-01 to 2026-05, read 2026-05-09 https://example.org/platterloop/changelog
[^s2-8]: Homepage with the "2,400 restaurants" line and the benchmarks waitlist, read 2026-05-09 https://example.org/platterloop/
[^s2-9]: Customer case study, a 40-site casual dining group, 2025-11-18 https://example.org/platterloop/customers/forty-site-group
[^s2-10]: Status page incident history, 90 days to 2026-05-09 https://example.org/status/platterloop/history
[^s2-11]: Help centre article on report exports and payout files, updated 2026-02-03 https://example.org/platterloop/help/reports-and-exports
[^s2-12]: Integrations directory, 23 listed partners, read 2026-05-09 https://example.org/platterloop/integrations

### Lane 3

[^s3-1]: The CEO on a hospitality operators podcast, episode 112, 2025-11-20 https://example.org/podcasts/operators/episode-112
[^s3-2]: The CTO's blog post "Boring technology at Platterloop", 2024-06-12 https://example.org/platterloop/engineering/boring-technology
[^s3-3]: Engineering blog post "Why we are splitting the monolith", 2026-01-20 https://example.org/platterloop/engineering/splitting-the-monolith
[^s3-4]: Trade press interview with the CEO on payments, 2026-02-11 https://example.org/hospitality-weekly/2026/02/platterloop-payments-interview
[^s3-5]: Archived homepage copy of 2024-05-15 with the "1,100 restaurants" line https://example.org/archive/20240515/platterloop.example.org/
[^s3-6]: Privacy policy with the sub-processor list, updated 2026-03-01 https://example.org/platterloop/legal/privacy
[^s3-7]: Engineering blog post on the Go payments service, 2025-09-09 https://example.org/platterloop/engineering/payments-service-in-go
[^s3-8]: VP Product appointment release, 2025-10-07 https://example.org/platterloop/press/vp-product-2025
[^s3-9]: The CEO on a founders podcast, episode 58, 2026-03-12 https://example.org/podcasts/founders/episode-58

### Lane 4

[^s4-1]: Trade body report on UK hospitality technology spend, 2025 edition, published 2025-10-01 https://example.org/hospitality-trade-body/reports/tech-spend-2025.pdf
[^s4-2]: Industry survey of UK restaurant site openings and closures in 2025, published 2026-01-22 https://example.org/market-research/uk-restaurant-sites-2025
[^s4-3]: Trade press on a competitor's £45m Series C, 2025-09-30 https://example.org/hospitality-weekly/2025/09/competitor-series-c
[^s4-4]: Analyst market map of UK restaurant software, 2026 edition, 2026-03-05 https://example.org/analyst-house/market-maps/uk-restaurant-software-2026
[^s4-5]: Regulator review of card acquiring fees for small merchants, 2025-07-17 https://example.org/payments-regulator/publications/card-acquiring-review-2025
[^s4-6]: Trade press on comparable A, the founder CTO's move to product and the Head of Engineering hire and exit, 2023-04-03 and 2024-06-10 https://example.org/hospitality-weekly/2024/06/comparable-a-head-of-engineering-exit
[^s4-7]: Trade press on comparable B, the monolith split and the engineering leader's departure, 2024-11-12 https://example.org/hospitality-weekly/2024/11/comparable-b-leadership-exit
[^s4-8]: Government guidance on the 2024 tips allocation rules, in force 2024-10-01 https://example.org/gov/guidance/tips-allocation-rules

### Lane 5

[^s5-1]: `dig +short api.platterloop.example.org` and the eu-west-2 load balancer hostname it returns, run 2026-05-09 https://example.org/raw/platterloop/dns-2026-05-09.txt
[^s5-2]: Certificate transparency search for platterloop.example.org, 23 hostnames issued since 2024-01-01, run 2026-05-09 https://example.org/ct-search/?q=platterloop.example.org
[^s5-3]: `curl -sI https://order.platterloop.example.org/` response headers naming the static hosting vendor and the framework, run 2026-05-09 https://example.org/raw/platterloop/headers-order-2026-05-09.txt
[^s5-4]: Status page component list with the hostnames it monitors, read 2026-05-09 https://example.org/status/platterloop/
[^s5-5]: Archived DNS record for order.platterloop.example.org, snapshot of 2024-09-02 https://example.org/dns-history/order.platterloop.example.org
[^s5-6]: MX, SPF and DMARC records for platterloop.example.org, run 2026-05-09 https://example.org/raw/platterloop/mail-records-2026-05-09.txt
[^s5-7]: Store metadata for the staff and kitchen apps, bundle ids and SDK list, read 2026-05-09 https://example.org/app-metadata/platterloop
[^s5-8]: Page source of the QR ordering page with the framework and build markers, read 2026-05-09 https://example.org/raw/platterloop/order-page-source-2026-05-09.html

### Lane 6

[^s6-1]: Applicant-tracking board JSON, 14 open roles with squad metadata, pulled 2026-05-09 https://example.org/ats/boards/platterloop/jobs.json
[^s6-2]: Head of Engineering ad, posted 2026-04-08 https://example.org/ats/boards/platterloop/jobs/head-of-engineering
[^s6-3]: Senior Backend Engineer (Ordering) ad, posted 2026-01-27 https://example.org/ats/boards/platterloop/jobs/senior-backend-ordering
[^s6-4]: Senior Backend Engineer (Kitchen) ad, posted 2026-02-03 https://example.org/ats/boards/platterloop/jobs/senior-backend-kitchen
[^s6-5]: Software Engineer, Payments (Go) ad, posted 2026-03-10 https://example.org/ats/boards/platterloop/jobs/software-engineer-payments-go
[^s6-6]: Platform Engineer ad, posted 2026-03-17 https://example.org/ats/boards/platterloop/jobs/platform-engineer
[^s6-7]: Data Engineer ad, posted 2026-02-18 https://example.org/ats/boards/platterloop/jobs/data-engineer
[^s6-8]: Analytics Engineer ad, posted 2026-04-01 https://example.org/ats/boards/platterloop/jobs/analytics-engineer
[^s6-9]: Senior React Native Engineer ad, posted 2026-02-24 https://example.org/ats/boards/platterloop/jobs/senior-react-native-engineer
[^s6-10]: Engineering Manager, Ordering ad, posted 2026-04-15 https://example.org/ats/boards/platterloop/jobs/engineering-manager-ordering
[^s6-11]: Test Automation Engineer ad, posted 2026-04-22 https://example.org/ats/boards/platterloop/jobs/test-automation-engineer
[^s6-12]: Product Designer ad, posted 2026-03-24 https://example.org/ats/boards/platterloop/jobs/product-designer
[^s6-13]: Customer Success Manager ad, posted 2026-04-29 https://example.org/ats/boards/platterloop/jobs/customer-success-manager
[^s6-14]: Aggregator snippet of a closed Senior Rails Engineer ad, first seen 2025-06, page could not be opened https://example.org/job-aggregator/platterloop/senior-rails-engineer-2025
[^s6-15]: Archived careers page of 2025-01-14, six open roles https://example.org/archive/20250114/platterloop.example.org/careers
[^s6-16]: Aggregator search for "Platterloop" with "SRE", "security" and "DevOps", zero results, run 2026-05-09 https://example.org/job-aggregator/search?q=platterloop+sre+security+devops

### Lane 7

[^s7-1]: Company team page with titles, read 2026-05-09 https://example.org/platterloop/about/team
[^s7-2]: The CEO's talk at a hospitality technology conference, "Operators do not buy software", 2025-06-18 https://example.org/conferences/hospitality-tech-2025/talks/operators-do-not-buy-software
[^s7-3]: The CTO's talk at a Ruby conference on running one monolith for 2,000 sites, 2023-09-21 https://example.org/conferences/ruby-uk-2023/talks/monolith-at-2000-sites
[^s7-4]: The VP Product on a product management podcast, episode 203, 2026-01-29 https://example.org/podcasts/product-people/episode-203
[^s7-5]: The investor director's biography on the fund's team page, read 2026-05-09 https://example.org/ventures/team/partner-platterloop-board
[^s7-6]: Press profile of the CEO's restaurant background, 2024-03-08 https://example.org/hospitality-weekly/2024/03/from-kitchen-to-software
