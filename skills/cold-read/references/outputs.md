# Output specification

The layout is fixed. A reader who has seen one Cold Read note can find anything in the next one without reading it through, and a script can check that nothing was dropped. Do not reorder, rename, merge or omit sections. Where a section has nothing, write the heading and one line: "Not found after looking at <what was looked at>."

Run `python3 scripts/check_read.py <note.md>` before finishing. It fails on a missing or misordered section, an unmarked fact line, a ✅ without evidence, a dangling or unused footnote, or a missing header line.

## 1. File and header

File name: `YYYY-MM-DD-<company-or-companies>-<lens>.md`, lens one of `deal`, `join`, `invest`, `position`, `people`. Lane files sit beside it as `lane-1-corporate-record.md` through `lane-7-people.md`, with raw material in `raw/`.

Every note starts with exactly these lines (a YAML front matter block before them is allowed for notes kept in a vault; the checker skips it):

```
# <Title in sentence case>

Read on <D Month YYYY>. Public record only. No LinkedIn profile was opened.
Legend: ✅ cited to a source read that day and linked; 🟡 inferred from the record, or from a snippet that could not be opened; ❔ not found after looking.
Sources: <N> footnotes across <L> lanes.
```

The title names the companies and the question, never the lens word: "Hollowmere and Kerbline: the integration, from the outside", not "Deal read".

## 2. Marks and citations

- Every sentence that states a fact about the company ends with a mark. A paragraph of facts carries a mark per sentence, not one at the end.
- ✅ is always followed by its evidence: an inline link `([short label](url))`, a footnote `[^s<lane>-<n>]`, or both. Both for a number that matters. A ✅ with neither is an error.
- 🟡 carries its reasoning in the same sentence ("🟡, because the same vendor appears on both estates") or names the ✅ facts it rests on.
- ❔ says what was looked at ("❔ not in the annual report, the registry or the three ads read").
- Footnote ids are `s<lane>-<n>`: `[^s1-4]` is the fourth source in lane 1. Footnotes are defined in "Sources by lane", grouped under a heading per lane, in id order, each as `[^s1-4]: <what it is, date> <url>`.
- A number is never bare. Price, count, date, multiple, percentage: each carries a mark and a source.
- Quotes are verbatim, in double quotes, with speaker, occasion and date.
- Dates are `D Month YYYY` in prose and `YYYY-MM-DD` in tables.

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

## 8. Quality bar

A note is not finished until:

- every section of the skeleton is present, in order, with its number;
- every fact sentence carries a mark, every ✅ has a link or footnote, every footnote is defined and used;
- the header's footnote count is true (the checker recomputes it);
- §4 of a deal note has ten dated rows or a "Not found" line, §7c has five comparables or says why fewer exist;
- every quote has speaker, occasion and date;
- "not public" appears wherever a figure was wanted and not found, with the source that would carry it;
- the shareable copy, if one is made, has §9 removed and no sentence that only an insider could have written.

For scale: a full deal read runs 400 to 700 lines with 100 to 200 footnotes; a join read 300 to 600 lines; invest and position 150 to 300. Shorter is fine when the record is thin, and the ❔ lines say so.

## 9. Writing rules

- Plain sentences. A table where items are parallel. No marketing adjectives.
- Real names for companies, brands and executives named in public filings or press. Initials or no names for staff below executive level, and for anyone known only from inside.
- Say "not public" rather than estimating; name the source that would settle it.
- The reader's own notes are never referenced in the shareable copy.
