# Cold Read

**Read any company from the outside before you invest, join or buy it.**

Cold Read is a skill for AI coding agents (Claude Code, Codex and anything else that reads the Agent Skills format, with rule files for Cursor and GitHub Copilot). Point it at a company and it reads the public record in six lanes, marks every claim as cited, inferred or unknown, and writes a dated reading in the order a busy reader needs: the answer, the evidence, the comparables, what it means for you, and the signals that would prove it wrong.

Site with example views: https://atlas-apex.github.io/cold-read/

## Four uses

| Lens | The question | Output |
|---|---|---|
| Invest | What did they pay for, and is it worth it? | Price against what was bought, says versus does, dated signals |
| Join | What would I inherit, and who will I meet? | Stack by chapter, mandate, questions by round, people with one-line reads |
| Deal | What happens to the acquired company, and was it cheap? | Two deals side by side, timeline, base rate, cutover window, surviving roles |
| Position | Who wins the market, and what would change it? | Market map, the moat as the filings show it, three dated events |

## The six lanes

1. **Corporate record**: filings, registries, deals, directors, cash.
2. **Counterparty or product**: the other company in a deal, or products, pricing and money.
3. **Says versus does**: investor statements against releases, privacy pages, app stores and migrations.
4. **Market, analysts, base rate**: the analyst split, the regulators, five to eight comparables.
5. **Infrastructure fingerprint**: DNS, certificates, headers, archived pages. Passive, read-only, context only.
6. **Openings as the plan**: the job boards as next year's org chart.

Plus a **people** lane for the join lens, with no LinkedIn profile ever opened.

## Install

```bash
git clone https://github.com/atlas-apex/cold-read
cd cold-read
./install.sh claude     # ~/.claude/skills/cold-read
./install.sh codex      # ~/.codex/skills/cold-read
./install.sh all
./install.sh /path/to/your/agent/skills
```

Cursor: copy `.cursor/rules/cold-read.mdc` into your project. Copilot: copy `.github/copilot-instructions.md`. Any other agent: add `AGENTS.md` to its instructions and keep `SKILL.md` and `references/` readable.

Then ask: *"Cold read Acme Ltd before my interview on Thursday"* or *"Was Acme bought cheap, and what happens to its engineers?"*

## Rules the skill enforces

- Public record only. Nothing behind a login, no scraping against terms, no pretexts.
- Every claim marked ✅ cited, 🟡 inferred, ❔ unknown.
- No LinkedIn profile views; snippets and public pages only.
- Infrastructure findings are context, never talking points.
- Inside knowledge stays in a separate, marked section; the shareable copy reconstructs from sources alone.
- Dates on every board pull and page read.

## Repository

```
SKILL.md                   the skill (Agent Skills format)
references/lanes.md        one paste-ready brief per lane
references/sources.md      sources by country and type, public endpoints, commands, fallbacks
references/outputs.md      output templates per lens
examples/                  four worked outputs with invented data
AGENTS.md                  generic agent instructions (Codex and others)
.cursor/rules/             Cursor rule
.github/copilot-instructions.md
docs/                      the website
install.sh
```

## Licence

MIT.
