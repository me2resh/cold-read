---
name: cold-read
description: Reverse-engineer a company from the public record alone (filings, registries, press, job boards, app stores, DNS and certificate logs, analysts, comparables) and turn it into a sourced, dated reading of what the company says, what it does, and what happens next. Use it whenever someone wants to understand a company before investing in it, before interviewing with or joining it, when it is buying or being bought (deal terms, integration, who survives, whether the price was cheap), or to work out its market position against competitors. Trigger on phrases like "research this company", "what is going on at X", "is X a good place to join", "was X bought cheap", "what will the acquirer do with X", "read the job ads", "what is their stack", "who are the people I'll meet", "outside view", "due diligence from public sources", even when the user does not say "research".
tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
keywords: [company research, due diligence, outside view, acquisition, integration, job hunt, interview prep, stack, job boards, filings, comparables, base rate]
---

# Cold Read

Read a company the way an analyst, a candidate and an acquirer would, using only what is public, and write it up so that every claim is either cited or marked as inference. The method was built by reading a listed acquirer and its acquisitions and several prospective employers across unrelated sectors; it generalises because every company leaves the same kinds of trace.

## The idea in one paragraph

A company cannot hide its plan. The plan is in what it files (money, deals, directors), in what it hires for (the job boards are next year's org chart), in what it ships (app stores, release notes, privacy pages, DNS and certificates show which platform serves which brand), in what it says to investors (and the gap between that and what it does), and in what happened to companies like it (the base rate). Read all six lanes, then write the reading in the order a busy reader needs: the answer, the evidence, the comparables, what it means for the reader, and the dated signals that would prove the reading wrong.

## Rules that make the output trustworthy

- **Public record only.** Filings, registries, press, job ads, public web pages, public APIs, DNS, certificate transparency, archived pages. Nothing behind a login, nothing scraped against a site's terms, no credentials, no social-engineering, no contacting staff under a pretext.
- **Do not open people's LinkedIn profiles.** Profile views are visible to the person and tell them they are being researched. Use search snippets, company team pages, press, talks, podcasts, GitHub and conference bios instead, and say "no profile was opened" at the top of a people note.
- **Mark every claim.** ✅ cited to a source read today (link it). 🟡 inferred, or from an aggregator snippet that could not be opened. ❔ unknown after looking. A reader must be able to tell the three apart at a glance; this is what separates research from gossip.
- **Infrastructure findings are context, never talking points.** DNS and certificate logs tell you which platform serves which brand. Do not quote them to the company in an interview or a pitch; it reads as surveillance. Use them to form a view, then confirm the view from job ads, press or filings before citing it.
- **Keep inside knowledge separate.** If the reader works there or has heard things, record those facts in a clearly marked internal section and never let them leak into a shareable copy. The shareable copy must be reconstructible from the cited sources alone.
- **Dates on everything.** Say when each board was pulled and each page read; snippets go stale within weeks, careers pages reorganise, and a reading is only as good as its date.
- **Name collisions are the common error in people research.** Check the employer and city on every hit before attributing a talk, a repo or a job ad to a person.
- **Vendor and agency claims are not evidence about the company.** An agency's portfolio page saying it built the company's platform is marketing; note it, do not cite it.

## Step 0: frame the job

Settle four things before searching, in one short exchange or by stating assumptions:

| Question | Why it matters |
|---|---|
| Which lens? invest, join, deal, position | Decides which lanes get depth and which output template to use (see `references/outputs.md`) |
| What is the one question? | "Was it bought cheap", "will my function survive", "what will I inherit", "who wins the UK market" |
| Who reads the result, and can it be shared? | Shareable means no inside facts, no private names, no references to the reader's own notes |
| Time box | A two-hour read is six lanes at snippet depth; a day is full lanes with raw outputs saved |

## Step 1: run the lanes

Each lane is a self-contained brief in `references/lanes.md` (read it before spawning). Run them in parallel as separate agents when you have them, otherwise in sequence. Each lane writes its own file with a header (date, sources read, fallbacks tried, legend) and returns a ten-fact summary at the top.

| Lane | Question it answers | Primary sources |
|---|---|---|
| 1 Corporate record | Who owns it, what it bought or sold, for how much, who runs it, how much cash and debt | Securities filings, company registries, deal releases, annual reports, director changes |
| 2 Counterparty or product | For a deal: the other company in the same depth. For a single company: products, pricing, customers, money | Same as lane 1 for the other party; pricing pages, app stores, customer counts |
| 3 Says versus does | What leadership tells investors and press, against what the releases, privacy pages, app stores and migrations show actually happened | Earnings calls, shareholder letters, press releases, privacy and terms pages, app store listings, archived pages |
| 4 Market, analysts, base rate | How outsiders rate it, the regulatory climate, and what happened in comparable situations | Analyst notes, trade press, regulator enforcement, five to eight named comparables |
| 5 Infrastructure fingerprint | Which platform serves which brand, which vendors, which identity and mail tenants, how the estates are joined | DNS, certificate transparency, HTTP headers, public page source, archived copies, app store metadata. Passive and read-only |
| 6 Openings as the plan | What the company is building, where, at what seniority, and what it has stopped hiring | Applicant-tracking-system public APIs and boards, aggregator snippets for closed ads |
| 7 People | Who the reader will meet or report to, what they have said and written, one-line read of what each will test | Team pages, press, talks, podcasts, books, blogs, GitHub, conference bios, filings for directors |

Lane 7 runs only for the join lens or when a specific person matters to the question. Lane 5 is context for every lens and talking points for none.

`references/sources.md` lists the sources by country and type, with the commands and public endpoints that worked (ATS APIs, certificate search, archive lookups, app store search), and the fallbacks when a site blocks fetches.

## Step 2: synthesise

Write one note from the lane files. Order matters more than length; a reader with five minutes stops after the first two sections and must still leave with the answer.

1. **The answer in one paragraph.** State the reading and the confidence.
2. **The evidence table.** For a deal: the two sides side by side (price and structure, what was bought, purchase price allocation, earn-out status, impairment). For a single company: money, product, customers, leadership, in one table with marks.
3. **Says versus does.** Quotes with dates on the left, observed actions on the right.
4. **Timeline so far.** Dated, sourced, one line per event.
5. **The platform picture.** What runs where, which brands share rails, what a cutover or migration would look like.
6. **The openings as a plan.** Counts by function, location and seniority; the five ads that matter most; predictions by horizon; ten roles that would tell the most if they appeared next.
7. **Outside view and base rate.** Analyst split; regulatory climate in one paragraph; comparables table; the general pattern; what a unit inside such a company should expect.
8. **What it means for the reader.** This is the only section that changes with the lens; see `references/outputs.md`.
9. **Signals to watch, dated.** A table of date, event, what to look for, source. Earnings calls, registry filings, retention cliffs, regulator registers, board changes.
10. **Sources by lane.** Footnotes or a numbered list per lane; the note must be reconstructible from them.

Keep the shareable copy separate from the working copy if the working copy holds inside facts, personal implications or private references.

## Lens notes

**Invest.** The question is usually "what did they pay for, and is it worth it". Work the price per customer and per unit of revenue when revenue is public, and say plainly when it is not; compare the purchase price allocation (channels, technology, trade name, customer relationships, goodwill) with what the acquirer then did with each asset. An earn-out that is "resolved" or "fixed" early usually means a negotiated settlement, and that is a signal about the acquirer's view of the targets. Read the analyst split as a range, not a verdict.

**Join.** Produce a stack-by-chapter note (one section per engineering area: what it does, what it runs on today, confidence, where it is heading), a mandate section (what the role would own, what it inherits, what is broken), vocabulary to have ready, questions for each round, and a people note with a one-line read per person. The research belongs in the interview, not in the cover letter; the letter is about the candidate.

**Deal.** Two companies side by side, then the integration timeline, then the base rate from comparables: brand retirement order, platform absorption window (usually 12 to 24 months after the second close), leadership exits at the first retention cliff, which functions move first (usually duplicated leadership and back office, then platform and infrastructure, then product engineering). End with the surviving roles and the cutover window, both marked 🟡, and a legal pointer where employees are affected.

**Position.** Market map with named competitors, pricing where public, the moat as the purchase price allocation reveals it (channels versus technology versus brand), the regulatory climate as the real constraint, and the two or three dated events that would change the ranking.

## Pitfalls learned the hard way

- Careers pages often return 403 to scripts; the applicant-tracking system behind them usually has a public JSON API (see sources). Count roles from the API, not from the marketing page.
- A corporate board and a regional board can list the same company's roles; de-duplicate before counting, and note evergreen requisitions (first-published dates a year old) so they do not read as fresh signals.
- Pages behind a bot challenge can usually be read from an archived copy; say which date's copy was read.
- Search snippets of aggregator pages (employee directories, salary sites) are 🟡 at best; the pages themselves are often blocked and sometimes wrong.
- A customer count or consultation count is not revenue; do not compute a multiple from it and call it a revenue multiple. Price per customer is a fair comparison between deals by the same buyer.
- The absence of a person in the public record is a finding, not a gap to fill with a guess.
- Keep raw outputs (DNS dumps, certificate lists, board JSON, archived HTML) next to the lane file so a later reader can re-check without re-fetching.
