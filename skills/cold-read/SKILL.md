---
name: cold-read
description: Reverse-engineer a company from the public record alone (filings, registries, press, job boards, app stores, DNS and certificate logs, analysts, comparables) and turn it into a sourced, dated reading of what the company says, what it does, and what happens next. Use it whenever someone wants to understand a company before investing in it, before interviewing with or joining it, when it is buying or being bought (deal terms, integration, who survives, whether the price was cheap), to work out its market position against competitors, to read one named competitor from where you stand (what they sell, where they are heading, where they are exposed, how they will respond to you), or to decide whether to tie yourself to a prospective partner, supplier, reseller or client (can they deliver, who decides, how they treat partners, what terms to ask for). Trigger on phrases like "research this company", "what is going on at X", "is X a good place to join", "was X bought cheap", "what will the acquirer do with X", "read the job ads", "what is their stack", "who are the people I'll meet", "outside view", "due diligence from public sources", "competitor analysis", "teardown of X", "how do we beat X", "battlecard", "should we partner with X", "vet this supplier", "partner due diligence", "can we rely on X", even when the user does not say "research". For a whole category where the competitors are not yet named, use market-read; Cold Read is for named companies.
tools: Read, Write, Edit, Grep, Glob, Bash, WebSearch, WebFetch
keywords: [company research, due diligence, outside view, acquisition, integration, job hunt, interview prep, stack, job boards, filings, comparables, base rate, competitor analysis, partner due diligence, supplier vetting]
---

# Cold Read

Read a company the way an analyst, a candidate, an acquirer, a competitor and a prospective partner would, using only what is public, and write it up so that every claim is either cited or marked as inference. The method was built by reading a listed acquirer and its acquisitions and several prospective employers across unrelated sectors; it generalises because every company leaves the same kinds of trace.

## The idea in one paragraph

A company cannot hide its plan. The plan is in what it files (money, deals, directors), in what it hires for (the job boards are next year's org chart), in what it ships (app stores, release notes, privacy pages, DNS and certificates show which platform serves which brand), in what it says to investors (and the gap between that and what it does), and in what happened to companies like it (the base rate). Read all six lanes, then write the reading in the order a busy reader needs: the answer, the evidence, the comparables, what it means for the reader, and the dated signals that would prove the reading wrong.

## Rules that make the output trustworthy

- **Public record only.** Filings, registries, press, job ads, public web pages, public APIs, DNS, certificate transparency, archived pages. Nothing behind a login, nothing scraped against a site's terms, no credentials, no social-engineering, no contacting staff under a pretext.
- **Do not open people's LinkedIn profiles.** Profile views are visible to the person and tell them they are being researched. Use search snippets, company team pages, press, talks, podcasts, GitHub and conference bios instead, and say "no profile was opened" at the top of a people note.
- **Mark every claim.** ✅ cited to a source read today (link it). 🟡 inferred, or from an aggregator snippet that could not be opened. ❔ unknown after looking. A reader must be able to tell the three apart at a glance; this is what separates research from gossip.
- **Infrastructure findings: use them, cite them, confirm them before you say them.** DNS, certificate logs and page headers are public and go in the note with the command that produced each one. They show that something exists, not why: a new hostname can be a pilot, a vendor trial or a migration. So before quoting one to the company, confirm it from a job ad, a page or a filing and quote that instead. Quote the fingerprint itself only when the audience is technical, the finding is favourable to them and you can say exactly what you ran; to most listeners it otherwise sounds like you watched their network rather than read their company.
- **Keep inside knowledge separate.** If the reader works there or has heard things, record those facts in a clearly marked internal section and never let them leak into a shareable copy. The shareable copy must be reconstructible from the cited sources alone.
- **Dates on everything.** Say when each board was pulled and each page read; snippets go stale within weeks, careers pages reorganise, and a reading is only as good as its date.
- **Name collisions are the common error in people research.** Check the employer and city on every hit before attributing a talk, a repo or a job ad to a person.
- **Reviews are a gauge, not evidence.** Customer, staff and partner reviews show how people feel and where a company is exposed; each one is a single account, and unhappy people write most of them. Record the score, the count, the date read, the trend and the themes that recur; mark what a review claims 🟡, never ✅. Under about 20 reviews, say "too few to read". Read them from search snippets or from a page the reader opens and passes on; never log in, post, or contact a reviewer.
- **Vendor and agency claims are not evidence about the company.** An agency's portfolio page saying it built the company's platform is marketing; note it, do not cite it.
- **No pretexts with a competitor or a partner.** Do not sign up for a trial or a demo to read a competitor's product, do not ask its sales or support team questions under another identity, and do not ask its customers or staff under a pretext. A prospective partner can be asked openly, by the reader, in the reader's own name; what it answers is "stated by the partner" and stays 🟡 until a document confirms it.
- **What arrives under an NDA is inside knowledge.** Once the reader has signed a confidentiality agreement with the company, anything received under it stays out of the public-record sections and out of every shareable copy.
- **Read it as the subject before sharing.** Before a copy goes to anyone, read it as each person and company named in it would. Check what it says about them, whether any line is an inference stated as a fact, and whether it shows who wrote it. A competitor or partner read can reach its subject; write nothing in it you would not stand behind in front of them.

## Step 0: frame the job

Settle four things before searching, in one short exchange or by stating assumptions:

| Question | Why it matters |
|---|---|
| Which lens? invest, join, deal, position, compete, partner | Decides which lanes get depth and which output template to use (see `references/outputs.md`) |
| What is the one question? | "Was it bought cheap", "will my function survive", "what will I inherit", "who wins the UK market", "where can we beat them", "should we sign with them, and on what terms" |
| Where does the reader stand? (compete and partner only) | One or two lines the reader states: what they sell, to whom and at what price (compete), or what the partnership would be and what they would depend on (partner). These are the reader's own facts, recorded as "stated by the reader", never as findings |
| Who reads the result, and can it be shared? | Shareable means no inside facts, no private names, no references to the reader's own notes |
| Time box | A two-hour read is six lanes at snippet depth; a day is full lanes with raw outputs saved |

## Step 1: run the lanes

Each lane is a self-contained brief in `references/lanes.md` (read it before spawning). The lane file layout is fixed too: header, sources table, ten facts, findings, implications, sources. Run them in parallel as separate agents when you have them, otherwise in sequence. Each lane writes its own file with a header (date, sources read, fallbacks tried, legend) and returns a ten-fact summary at the top.

| Lane | Question it answers | Primary sources |
|---|---|---|
| 1 Corporate record | Who owns it, what it bought or sold, for how much, who runs it, how much cash and debt | Securities filings, company registries, deal releases, annual reports, director changes |
| 2 Counterparty or product | For a deal: the other company in the same depth. For a single company: products, pricing, customers, money | Same as lane 1 for the other party; pricing pages, app stores, customer counts |
| 3 Says versus does | What leadership tells investors and press, against what the releases, privacy pages, app stores and migrations show actually happened | Earnings calls, shareholder letters, press releases, privacy and terms pages, app store listings, archived pages |
| 4 Market, analysts, base rate | How outsiders rate it, the regulatory climate, and what happened in comparable situations | Analyst notes, trade press, regulator enforcement, five to eight named comparables, review sites as a gauge |
| 5 Infrastructure fingerprint | Which platform serves which brand, which vendors, which identity and mail tenants, how the estates are joined | DNS, certificate transparency, HTTP headers, public page source, archived copies, app store metadata. Passive and read-only; cited with the command |
| 6 Openings as the plan | What the company is building, where, at what seniority, and what it has stopped hiring | Applicant-tracking-system public APIs and boards, aggregator snippets for closed ads |
| 7 People | Who the reader will meet or report to, what they have said and written, one-line read of what each will test | Team pages, press, talks, podcasts, books, blogs, GitHub, conference bios, filings for directors |

Lane 7 runs for the join lens, for the partner lens (who signs and who the reader would work with), or when a specific person matters to the question. Lane 5 feeds every lens; its findings are quoted to the company only once confirmed in words elsewhere.

`references/sources.md` lists the sources by country and type, with the commands and public endpoints that worked (ATS APIs, certificate search, archive lookups, app store search), and the fallbacks when a site blocks fetches.

## Step 2: synthesise, to the fixed layout

Write one note from the lane files, to the skeleton for the lens in `references/outputs.md`. The layout is fixed on purpose: a reader who has seen one Cold Read can find anything in the next without reading it through, and the checker can prove nothing was dropped. Do not reorder, rename, merge or omit sections; a section with nothing says "Not found after looking at ..." under its heading.

The standard the note has to meet, in brief (the specification has the exact tables and columns):

- The header carries the read date, "Public record only. No LinkedIn profile was opened.", the legend, and a true count of footnotes and lanes.
- Every fact sentence ends with a mark. Every ✅ is followed by an inline link, a footnote of the form `[^s<lane>-<n>]`, or both. A number is never bare. Quotes carry speaker, occasion and date.
- Sources are footnotes grouped by lane at the end, so the note can be rebuilt from them.
- A full deal read is long because the record is long: hundreds of lines, one to two hundred footnotes, ten dated timeline rows, five to eight comparables, ten roles to watch for, a dated signals table. Short is right only when the record is thin, and the ❔ lines then say what was looked at.

Before finishing, run `python3 scripts/check_read.py <note.md>` and fix every failure it prints. Keep the shareable copy separate from the working copy if the working copy holds inside facts, personal implications or private references; the shareable copy keeps the reader's section heading ("What it means for the reader", or "Head to head" in a compete read) with the line "Removed from the shareable copy."

## Lens notes

**Invest.** The question is usually "what did they pay for, and is it worth it". Work the price per customer and per unit of revenue when revenue is public, and say plainly when it is not; compare the purchase price allocation (channels, technology, trade name, customer relationships, goodwill) with what the acquirer then did with each asset. An earn-out that is "resolved" or "fixed" early usually means a negotiated settlement, and that is a signal about the acquirer's view of the targets. Read the analyst split as a range, not a verdict.

**Join.** Produce a stack-by-chapter note (one section per engineering area: what it does, what it runs on today, confidence, where it is heading), a mandate section (what the role would own, what it inherits, what is broken), vocabulary to have ready, questions for each round, and a people note with a one-line read per person. The research belongs in the interview, not in the cover letter; the letter is about the candidate.

**Deal.** Two companies side by side, then the integration timeline, then the base rate from comparables: brand retirement order, platform absorption window (usually 12 to 24 months after the second close), leadership exits at the first retention cliff, which functions move first (usually duplicated leadership and back office, then platform and infrastructure, then product engineering). End with the surviving roles and the cutover window, both marked 🟡, and a legal pointer where employees are affected.

**Position.** Market map with named competitors, pricing where public, the moat as the purchase price allocation reveals it (channels versus technology versus brand), the regulatory climate as the real constraint, and the two or three dated events that would change the ranking.

**Compete.** One named competitor, read from where the reader stands. The question is usually "where do they beat us, where can we beat them, and what will they do next". Lanes 2, 3 and 6 carry the weight: what each tier sells and gates, with prices dated from archived pricing pages; what shipped in the last twelve months from release notes, changelogs, repositories and app version histories; and the openings as their roadmap. Traction is read from what the record will bear (accounts, funding, customers who name them, marketplace and review counts), and "not public" is written wherever it will not. Strengths rest on ✅ facts; exposures are 🟡 and name the facts they rest on. The likely response to a move is read from how the competitor answered earlier entrants: dated price changes, copied features, comparison pages, acquisitions. The head-to-head table puts the competitor's cited facts beside the reader's own stated ones and is the part to remove before sharing. For a category where the competitors are not yet named, run market-read first and bring the names here.

**Partner.** A prospective partner the reader would depend on: a reseller or channel, a technology or integration partner, a supplier, a large client, a joint venture, a co-founder's company. The question is usually "should we tie ourselves to them, on what terms, and how would we know early that it is going wrong". Start with the legal entity that would sign, not the brand: its owners, directors, accounts, charges and late filings (lane 1). Then whether it can deliver (money, capacity, customers who confirm it themselves, certifications checked on the issuer's register), how it has treated earlier partners (the partner programme as written against what happened to named partners, and whether it has ever launched against one), what it wants from this, where interests conflict, and what breaks if it stops or is sold. Lane 6 matters twice: hiring in the function the reader depends on is capacity, and an ad to build what the reader would supply is a plan to replace them. The read ends with terms to ask for, each tied to a fact in the note, and questions to put to the partner openly. A reference the partner supplies is the partner's choice; look for one it did not choose.

## Pitfalls learned the hard way

- Careers pages often return 403 to scripts; the applicant-tracking system behind them usually has a public JSON API (see sources). Count roles from the API, not from the marketing page.
- A corporate board and a regional board can list the same company's roles; de-duplicate before counting, and note evergreen requisitions (first-published dates a year old) so they do not read as fresh signals.
- Pages behind a bot challenge can usually be read from an archived copy; say which date's copy was read.
- Search snippets of aggregator pages (employee directories, salary sites) are 🟡 at best; the pages themselves are often blocked and sometimes wrong.
- A customer count or consultation count is not revenue; do not compute a multiple from it and call it a revenue multiple. Price per customer is a fair comparison between deals by the same buyer.
- The absence of a person in the public record is a finding, not a gap to fill with a guess.
- Keep raw outputs (DNS dumps, certificate lists, board JSON, archived HTML) next to the lane file so a later reader can re-check without re-fetching.
