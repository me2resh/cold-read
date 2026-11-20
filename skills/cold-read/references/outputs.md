# Output specification

The layout is fixed. A reader who has seen one Cold Read note can find anything in the next one without reading it through, and a script can check that nothing was dropped. Do not reorder, rename, merge or omit sections. Where a section has nothing, write the heading and one line: "Not found after looking at <what was looked at>."

Run `python3 scripts/check_read.py <note.md>` before finishing. It fails on a missing or misordered section, an unmarked fact line, a ✅ without evidence, a dangling or unused footnote, or a missing header line.

## 1. File and header

File name: `YYYY-MM-DD-<company-or-companies>-<lens>.md`, lens one of `deal`, `join`, `invest`, `position`, `compete`, `partner`, `people`. Lane files sit beside it as `lane-1-corporate-record.md` through `lane-7-people.md`, with raw material in `raw/`.

Every note starts with exactly these lines (a YAML front matter block before them is allowed for notes kept in a vault; the checker skips it):

```
# <Title in sentence case>

Read on <D Month YYYY>. Public record only. No LinkedIn profile was opened.
Legend: ✅ cited to a source read that day and linked; 🟡 inferred from the record, or from a snippet that could not be opened; ❔ not found after looking.
Sources: <N> footnotes across <L> lanes.
```

The title names the companies and the question, never the lens word: "Hollowmere and Kerbline: the integration, from the outside", not "Deal read".

## 2. Marks and citations

- Every bullet or sentence that states a fact about the company ends with a mark. Write facts as bullets, one fact per bullet, so each carries its own mark.
- ✅ is always followed by its evidence: an inline link `([short label](url))`, a footnote `[^s<lane>-<n>]`, or both. Both for a number that matters. A ✅ with neither is an error.
- 🟡 carries its reasoning in the same sentence ("🟡, because the same vendor appears on both estates") or names the ✅ facts it rests on.
- ❔ says what was looked at ("❔ not in the annual report, the registry or the three ads read").
- Footnote ids are `s<lane>-<n>`: `[^s1-4]` is the fourth source in lane 1. Footnotes are defined in "Sources by lane", grouped under a heading per lane, in id order, each as `[^s1-4]: <what it is, date> <url>`.
- A number is never bare. Price, count, date, multiple, percentage: each carries a mark and a source.
- Quotes are verbatim, in double quotes, with speaker, occasion and date.
- Dates are `D Month YYYY` in prose and `YYYY-MM-DD` in tables.

## 2a. Section 1 of every skeleton

The first section keeps its heading ("The answer in one paragraph", or "The platform in one paragraph" for join) so older notes and the checker still match, but its body is four to eight bullets in three bold groups:

- **The short answer:** the answer to the one question, in one or two bullets.
- **The evidence:** the three to five facts it rests on, each with its mark and source.
- **The position** (deal, invest, position, compete), **The mandate** (join) or **The terms** (partner): what follows, marked 🟡 with the facts it rests on.

## 3. Skeleton A: deal (acquisition or integration)

```
## 1. The answer in one paragraph
## 2. The deals, side by side
## 3. What it says and what it does
### 3a. What it says
### 3b. What it does
### 3c. The brand and platform plan, as far as it can be read
## 4. The integration so far
## 5. The platform picture
## 6. The openings as a plan
### 6a. The counts
### 6b. The five ads that matter most
### 6c. Predictions by horizon
### 6d. Ten roles that would tell the most if they appeared next
## 7. The outside view and the base rate
### 7a. Analyst split
### 7b. Regulatory climate
### 7c. Comparables
### 7d. The general pattern
## 8. What it means for the acquired company
## 9. What it means for the reader
## 10. Legal pointer
## 11. Signals to watch, dated
## 12. Sources by lane
```

Fixed tables, exact columns:

- §2: rows `Announced and closed`, `Price and structure`, `What was bought`, `Purchase price allocation`, `What the allocation says`, `Earn-out status`, `Goodwill impairment`; one column per deal.
- §3a: `Date | Who, where | Quote | Mark`. §3b: `Date | What happened | Where it shows | Mark`.
- §4: `Date | Event | Source | Mark`, ascending, at least ten rows or a "Not found" line.
- §6a: `Company | Open roles | Engineering | Product | Operations | Other | Locations | Board read on`.
- §6b: `# | Title, company | Posted | Why it matters | Mark`.
- §6c: `Horizon | Prediction | Rests on`; horizons `6 months`, `12 months`, `24 months`; every row 🟡.
- §6d: numbered list of ten, each "Role: what it would tell."
- §7a: `Firm or person | Date | View | One-line reason | Mark`.
- §7c: `Deal | Year, price | Brand kept? | Platform outcome | Leadership outcome | Engineering outcome | Months to absorption | Mark`; five to eight rows.
- §11: `Date | Event | What to look for | Source`.

§9 exists in the working copy only; the shareable copy keeps the heading with "Removed from the shareable copy." §10 is a pointer to the relevant employment or shareholder protections in the jurisdiction, three to six lines, ending "A pointer, not advice."

## 4. Skeleton B: join (a role at the company)

```
## 1. The platform in one paragraph
## 2. Chapters
### 2.<n> <Chapter name>        (one per engineering area, in the company's own order)
## 3. Platform, infrastructure, delivery and quality
## 4. Regulatory, quality and security
## 5. Org and ways of working
## 6. Leadership
## 7. Market
## 8. Money
## 9. What it means for the mandate
## 10. Vocabulary to have ready
## 11. Questions by round
## 12. Job ads and the stack each one names
## 13. Sources by lane
```

- Each chapter table: `Component | What it does | Runs on today | Mark | Where it is heading`.
- §6: `Person | Title, confirmed where and when | Background | Mark`; link to the people note.
- §8: `Item | Figure | Period | Source | Mark` (runway, going concern, last raise, revenue by segment).
- §9: four fixed paragraphs headed `Owns`, `Inherits`, `Is broken`, `First quarter must deliver`.
- §11: subsections per round as known; otherwise `Recruiter`, `Hiring manager`, `Peers`, `Executive`.
- §12: `Ad | Posted | Location | Stack named | Signal`.

## 5. Skeleton C: invest (price and prospects)

```
## 1. The answer in one paragraph
## 2. Price against what was bought
## 3. What it says and what it does
## 4. The business today
## 5. The outside view
## 6. What would settle it
## 7. Signals to watch, dated
## 8. Sources by lane
```

- §2: one column per deal; rows `Price and structure`, `Customers or units`, `Price per customer or unit`, `Trailing revenue and multiple`, `Profitability at sale`, `Goodwill share`, `What was done with it`. Write "not public" rather than estimate.
- §3: `Date | Who, where | Quote | Then what happened | Mark`.
- §4: `Segment | Revenue | Margin | Trend | Mark`.
- §5: analyst table as §7a of skeleton A, then one regulatory paragraph.
- §6: the one number or event that would settle the question, whether it is public, and when it next appears.
- §7: `Date | Event | What to look for | Source`.

## 6. Skeleton D: position (market)

```
## 1. The answer in one paragraph
## 2. Market map
## 3. The moat, as the record shows it
## 4. Regulatory climate
## 5. What it says and what it does
## 6. Three dated events that would change the ranking
## 7. Sources by lane
```

- §2: `Operator | Size (unit stated) | Markets | Price | Model | Mark`.
- §5: `Date | Who, where | Quote | Then what happened | Mark`.
- §6: `Date | Event | Why it changes the ranking | Source`.

## 7. Skeleton E: people

```
## 1. <Person>: <title as confirmed, date>
### Career from the public record
### What they have written or said about how they work
### Public roles
### Name collisions ruled out
### One-line read
## 2. <next person> ...
## N. Structural reading
## N+1. Questions this suggests
## N+2. Sources by lane
```

## 8. Skeleton F: compete (one named competitor)

```
## 1. The answer in one paragraph
## 2. What they sell, to whom, at what price
## 3. Traction, as far as the record shows it
## 4. What it says and what it does
## 5. Where they are heading
### 5a. What shipped in the last twelve months
### 5b. The openings as a roadmap
## 6. Where they are strong and where they are exposed
## 7. Head to head
## 8. How they are likely to respond
## 9. Signals to watch, dated
## 10. Sources by lane
```

- §2: `Product or tier | Buyer | Price (unit, date read) | What the tier gates | Mark`. Below it, every price change found in archived copies, dated.
- §3: `Measure | Figure | As of | Source | Mark` (revenue, funding, headcount, customers who name them, marketplace and review counts, downloads). Write "not public" rather than estimate. A logo on their own site is a claim, marked 🟡; a customer is ✅ only when the customer says so.
- §4: `Date | Who, where | Quote | Then what happened | Mark`.
- §5a: `Date | Release | What changed | Mark`, newest first. §5b: `# | Title | Posted | What it says they will build | Mark`, five rows or a "Not found" line.
- §6: two bold groups, `Strong` and `Exposed`. Every strength rests on ✅ facts. Every exposure is 🟡 and names the facts it rests on.
- §7: `Dimension | Them | You (stated by the reader) | Edge`. The "Them" cells carry marks and sources. The "You" cells are the reader's own statements from step 0 and carry no mark. This section exists in the working copy only; the shareable copy keeps the heading with "Removed from the shareable copy."
- §8: `If you | They are likely to | Rests on`; every row 🟡, and "Rests on" names a dated earlier response of theirs, or says "no precedent in the record".
- §9: `Date | Event | What to look for | Source`.

## 9. Skeleton G: partner (a company the reader would depend on)

```
## 1. The answer in one paragraph
## 2. Who they are and who decides
## 3. Can they deliver
### 3a. Money and staying power
### 3b. Capacity and track record
## 4. How they treat partners
## 5. What they want from this
## 6. Where interests conflict
## 7. Dependency and exit
## 8. What it says and what it does
## 9. Terms to ask for and questions to put openly
## 10. What it means for the reader
## 11. Signals to watch, dated
## 12. Sources by lane
```

- §2: `Entity or person | Role in the decision | Confirmed where and when | Mark`. First row is the legal entity that would sign, then its parent and owners, then directors, then whoever signs and whoever the reader would work with.
- §3a: `Item | Figure | Period | Source | Mark` (last accounts, cash, secured lenders and charges, going-concern wording, late filings, funding, court or insolvency notices, payment record where a register carries one).
- §3b: `Evidence | What it shows | Date | Mark` (customers who confirm it themselves, sites and capacity, certifications from the issuer's register with scope and expiry, incident history, hiring in the function the reader depends on).
- §4: `Partner or programme | Since | What happened | Source | Mark`; at least three named relationships or a "Not found" line. Say plainly whether the company has ever launched a product against a partner, dropped one or bought one.
- §5: 🟡 bullets, one per motive, each naming the facts it rests on.
- §6: `Area | What the record shows | Why it conflicts | Mark` (a competing product of their own, service to the reader's competitors, exclusivity given to others, owners or directors with interests elsewhere).
- §7: `Dependency | What breaks if they stop | How it could be replaced | Rests on`, then one line on change of control: who owns them, whether they are for sale or have been sold before, marked.
- §8: `Date | Who, where | Quote | Then what happened | Mark`.
- §9: two numbered lists. `Terms`: each "Term: the fact in this note that makes it worth asking". `Questions`: what the reader should ask the partner openly, in the reader's own name, each with the gap in the record it would fill. Ends "A pointer for the negotiation, not legal advice."
- §10 exists in the working copy only; the shareable copy keeps the heading with "Removed from the shareable copy."
- §11: `Date | Event | What to look for | Source`.

Anything the partner has told the reader directly is recorded as "stated by the partner, <date>" and marked 🟡 until a document confirms it. Anything received under a confidentiality agreement stays out of the note's public-record sections and out of every shareable copy.

## 10. Quality bar

A note is not finished until:

- every section of the skeleton is present, in order, with its number;
- every fact sentence carries a mark, every ✅ has a link or footnote, every footnote is defined and used;
- the header's footnote count is true (the checker recomputes it);
- §4 of a deal note has ten dated rows or a "Not found" line, §7c has five comparables or says why fewer exist;
- every quote has speaker, occasion and date;
- "not public" appears wherever a figure was wanted and not found, with the source that would carry it;
- the shareable copy, if one is made, has the reader's section removed (§9 of a deal read, §7 of a compete read, §10 of a partner read) and no sentence that only an insider could have written;
- before any copy is shared, it has been read as each person and company named in it would read it: no inference stated as a fact about them, and nothing that shows who wrote it unless the reader wants that.

For scale: a full deal read runs 400 to 700 lines with 100 to 200 footnotes; a join read 300 to 600 lines; invest, position, compete and partner 150 to 300. Shorter is fine when the record is thin, and the ❔ lines say so.

## 11. Writing rules

- Bullets, not paragraphs. Group related facts under a short bold label (for example **The short answer**, **The evidence**, **The position**), one fact per bullet, each bullet a plain sentence with its mark. A table where items are parallel.
- No paragraph longer than two sentences or about 60 words; the checker warns on longer ones. Prose is for a single framing line, not for the findings.
- No marketing adjectives.
- Real names for companies, brands and executives named in public filings or press. Initials or no names for staff below executive level, and for anyone known only from inside.
- Say "not public" rather than estimating; name the source that would settle it.
- The reader's own notes are never referenced in the shareable copy.
