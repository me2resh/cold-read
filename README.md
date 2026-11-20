# Cold Read

**Read any company from the outside before you invest in it, join it, buy it, compete with it or partner with it.**

Cold Read is an add-on for Claude Code, Codex and Cursor (and anything else that reads the Agent Skills format, with a rule file for GitHub Copilot). Point it at a company and it reads the public record in six places at once, marks every line as sourced, inferred or not found, and writes one dated note: the answer first, then the evidence, then what it means for you, then the dates that would prove it wrong.

Site with example views: https://me2resh.github.io/cold-read/

## Six uses

| Lens | The question | Output |
|---|---|---|
| Invest | What did they pay for, and is it worth it? | Price against what was bought, says versus does, dated signals |
| Join | What would I inherit, and who will I meet? | Stack by chapter, mandate, questions by round, people with one-line reads |
| Deal | What happens to the acquired company, and was it cheap? | Two deals side by side, timeline, base rate, cutover window, surviving roles |
| Position | Who wins the market, and what would change it? | Market map, the moat as the filings show it, three dated events |
| Compete | Where can we beat this competitor, and what will it do next? | Tiers and dated prices, what shipped, the openings as a roadmap, strengths and exposures, head to head, likely responses |
| Partner | Should we tie ourselves to them, and on what terms? | Who signs and who owns them, money and capacity, how they treated earlier partners, business model and pricing, conflicts, dependency and exit, terms to ask for |

Compete and partner read one named company. For a whole category where the competitors are not yet named, use the sibling skill Market Read and bring the names here.

## The six lanes

1. **Corporate record**: filings, registries, deals, directors, cash.
2. **Counterparty or product**: the other company in a deal, or products, pricing and money.
3. **Says versus does**: investor statements against releases, privacy pages, app stores and migrations.
4. **Market, analysts, base rate**: the analyst split, the regulators, five to eight comparables, and customer and staff reviews as a gauge.
5. **Infrastructure fingerprint**: DNS, certificates, headers, archived pages. Passive, read-only, cited with the command.
6. **Openings as the plan**: the job boards as next year's org chart.

Plus a **people** lane for the join and partner lenses, with no LinkedIn profile ever opened.

## Install

Claude Code, one line:

```
/plugin install cold-read --marketplace me2resh/cold-read
```

Older Claude Code, two steps: `/plugin marketplace add me2resh/cold-read`, then `/plugin install cold-read@cold-read`. From the shell: `claude plugin install cold-read --marketplace me2resh/cold-read`. The skill then answers to `/cold-read` (or `/cold-read:cold-read`).

Codex and other agents that read the Agent Skills format: clone the repo and run `./install.sh codex` (copies `skills/cold-read/` into `~/.codex/skills/`), or `./install.sh /path/to/your/agent/skills`. Cursor: copy `.cursor/rules/cold-read.mdc` into your project. Copilot: copy `.github/copilot-instructions.md`. Anything else: add `AGENTS.md` to its instructions and keep `skills/cold-read/` readable.

Then ask: *"Cold read Acme Ltd before my interview on Thursday"*, *"Was Acme bought cheap, and what happens to its engineers?"*, *"Read Acme as a competitor: where can we beat them?"* or *"Acme wants a three-year exclusive. Should we sign?"*

## The output is deterministic

Every read follows a fixed skeleton for its lens (deal, join, invest, position, compete, partner, people): numbered sections in a fixed order, tables with fixed columns, a mark on every claim, footnotes as `[^s<lane>-<n>]` grouped by lane at the end, and a header with a true source count. `skills/cold-read/references/outputs.md` is the specification; `skills/cold-read/scripts/check_read.py` fails a note that drifts from it, and the skill runs it before finishing. The six sample reads in `skills/cold-read/examples/` pass it.

## Rules the skill enforces

- Public record only. Nothing behind a login, no scraping against terms, no pretexts. No trial sign-ups or demo requests to read a competitor; a prospective partner is asked openly or not at all.
- Every claim marked ✅ cited, 🟡 inferred, ❔ unknown.
- No LinkedIn profile views; snippets and public pages only.
- Infrastructure findings are cited with the command that produced them, and confirmed from an ad, a page or a filing before being quoted to the company.
- Inside knowledge stays in a separate, marked section; the shareable copy reconstructs from sources alone. Anything received under an NDA counts as inside knowledge.
- Before a copy is shared, it is read as each person and company named in it would read it.
- Dates on every board pull and page read.

## Repository

```
.claude-plugin/plugin.json          plugin manifest
.claude-plugin/marketplace.json     this repo is also its own marketplace
skills/cold-read/SKILL.md           the skill (Agent Skills format)
skills/cold-read/references/        lanes, sources and endpoints, output templates
skills/cold-read/examples/          six sample reads to the fixed layout, 40 to 70 footnotes each
skills/cold-read/scripts/check_read.py   layout and citation checker
docs/build/build_samples.py          renders the samples to docs/samples/*.pdf
AGENTS.md                           generic agent instructions (Codex and others)
.cursor/rules/                      Cursor rule
.github/copilot-instructions.md
docs/                               the website
install.sh                          copies the skill for agents without plugins
```

## Licence

MIT.

---

Part of [me2resh skills](https://github.com/me2resh/skills), free and open source: Cold Read, Field Read, Tayyib and Job Apply. Add them all with `/plugin marketplace add me2resh/skills`.
