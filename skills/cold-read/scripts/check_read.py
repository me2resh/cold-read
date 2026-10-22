#!/usr/bin/env python3
"""Check a Cold Read note against the output specification (references/outputs.md).

Usage: python3 check_read.py <note.md> [--lens deal|join|invest|position|people]
The lens is inferred from the file name when not given. Exit 1 on any failure.
"""
import re, sys, pathlib

SKELETONS = {
    "deal": ["1. The answer in one paragraph", "2. The deals, side by side", "3. What it says and what it does",
             "3a. What it says", "3b. What it does", "3c. The brand and platform plan, as far as it can be read",
             "4. The integration so far", "5. The platform picture", "6. The openings as a plan", "6a. The counts",
             "6b. The five ads that matter most", "6c. Predictions by horizon",
             "6d. Ten roles that would tell the most if they appeared next", "7. The outside view and the base rate",
             "7a. Analyst split", "7b. Regulatory climate", "7c. Comparables", "7d. The general pattern",
             "8. What it means for the acquired company", "9. What it means for the reader", "10. Legal pointer",
             "11. Signals to watch, dated", "12. Sources by lane"],
    "join": ["1. The platform in one paragraph", "2. Chapters", "3. Platform, infrastructure, delivery and quality",
             "4. Regulatory, quality and security", "5. Org and ways of working", "6. Leadership", "7. Market", "8. Money",
             "9. What it means for the mandate", "10. Vocabulary to have ready", "11. Questions by round",
             "12. Job ads and the stack each one names", "13. Sources by lane"],
    "invest": ["1. The answer in one paragraph", "2. Price against what was bought", "3. What it says and what it does",
               "4. The business today", "5. The outside view", "6. What would settle it", "7. Signals to watch, dated",
               "8. Sources by lane"],
    "position": ["1. The answer in one paragraph", "2. Market map", "3. The moat, as the record shows it",
                 "4. Regulatory climate", "5. What it says and what it does",
                 "6. Three dated events that would change the ranking", "7. Sources by lane"],
    "people": None,  # numbered per person; checked structurally below
}
MARKS = "✅🟡❔"

def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if not args:
        print(__doc__); sys.exit(2)
    path = pathlib.Path(args[0]); text = path.read_text(encoding="utf-8")
    lens = None
    if "--lens" in sys.argv: lens = sys.argv[sys.argv.index("--lens") + 1]
    else:
        m = re.search(r"-(deal|join|invest|position|people)\.md$", path.name)
        lens = m.group(1) if m else None
    fails, warns = [], []
    lines = text.splitlines()

    # header
    if not lines or not lines[0].startswith("# "): fails.append("line 1 must be the title '# ...'")
    head = "\n".join(lines[:8])
    if not re.search(r"^Read on \d{1,2} [A-Z][a-z]+ \d{4}\. Public record only\. No LinkedIn profile was opened\.", head, re.M):
        fails.append("header line missing: 'Read on D Month YYYY. Public record only. No LinkedIn profile was opened.'")
    if "Legend: ✅" not in head: fails.append("header legend line missing")
    msrc = re.search(r"^Sources: (\d+) footnotes across (\d+) lanes\.", head, re.M)
    if not msrc: fails.append("header line missing: 'Sources: N footnotes across L lanes.'")

    # sections
    heads = [re.sub(r"^#+\s*", "", l).strip() for l in lines if re.match(r"^##+ ", l)]
    if lens in SKELETONS and SKELETONS[lens]:
        want = SKELETONS[lens]; pos = -1
        for w in want:
            try:
                i = next(i for i, h in enumerate(heads) if h.startswith(w) or h == w)
            except StopIteration:
                fails.append(f"section missing: '{w}'"); continue
            if i < pos: fails.append(f"section out of order: '{w}'")
            pos = max(pos, i)
    elif lens == "people":
        if not any(h.startswith("Structural reading") or re.match(r"\d+\. Structural reading", h) for h in heads):
            fails.append("people note needs a 'Structural reading' section")
        if not any("Sources by lane" in h for h in heads): fails.append("people note needs 'Sources by lane'")
    else:
        warns.append("lens not given and not in file name; skeleton not checked")

    # footnotes
    defined = set(re.findall(r"^\[\^(s\d+-\d+)\]:", text, re.M))
    used = set(re.findall(r"\[\^(s\d+-\d+)\](?!:)", text))
    bad_ids = [f for f in defined | used if not re.match(r"s[1-7]-\d+$", f)]
    for f in sorted(used - defined): fails.append(f"footnote used but not defined: [^{f}]")
    for f in sorted(defined - used): warns.append(f"footnote defined but never used: [^{f}]")
    for f in bad_ids: fails.append(f"footnote id not of the form s<lane>-<n>: {f}")
    lanes = {f.split("-")[0] for f in defined}
    if msrc:
        n, l = int(msrc.group(1)), int(msrc.group(2))
        if n != len(defined): fails.append(f"header says {n} footnotes, note defines {len(defined)}")
        if l != len(lanes): fails.append(f"header says {l} lanes, footnotes span {len(lanes)}")

    # marks: a ✅ must be followed on the same line by a link or a footnote
    in_sources = False
    for i, l in enumerate(lines, 1):
        if re.match(r"^## .*Sources by lane", l): in_sources = True
        if in_sources or l.startswith("#") or l.startswith("Legend:") or not l.strip(): continue
        for m in re.finditer("✅", l):
            tail = l[m.end():m.end() + 160]
            if not re.search(r"\]\(https?://|\[\^s\d+-\d+\]", tail):
                fails.append(f"line {i}: ✅ without a link or footnote after it")
        # bare numbers in prose/table rows without any mark on the line
        if re.search(r"(£|\$|€|GBP|USD|EUR|AUD)\s?\d|\d+(\.\d+)?x\b|\d+%", l) and not any(c in l for c in MARKS) \
           and not l.startswith("|--") and "not public" not in l.lower():
            warns.append(f"line {i}: a figure with no mark on the line")

    # quotes need a who and when nearby (same line)
    for i, l in enumerate(lines, 1):
        if in_sources: break
        if re.search(r"\"[^\"]{12,}\"", l) and not re.search(r"\d{4}", l):
            warns.append(f"line {i}: a quote without a year on the line")

    for w in warns: print("warn:", w)
    for f in fails: print("FAIL:", f)
    print(f"{path.name}: {len(defined)} footnotes, {len(lanes)} lanes, {len(fails)} failures, {len(warns)} warnings")
    sys.exit(1 if fails else 0)

if __name__ == "__main__":
    main()
