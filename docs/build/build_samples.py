#!/usr/bin/env python3
"""Render the sample reads in skills/cold-read/examples/ to docs/samples/*.pdf.
Needs python-markdown (pip install markdown) and Google Chrome. Run from the repo root."""
import glob, os, re, subprocess, sys, pathlib
try:
    import markdown
except ImportError:
    sys.exit("pip install markdown")
ROOT = pathlib.Path(__file__).resolve().parents[2]
CHROME = os.environ.get("CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome")
CSS = '''@page{size:A4;margin:22mm 20mm 26mm}body{font-family:"Source Serif 4",Georgia,serif;font-size:10.5pt;line-height:1.5;color:#14202c}
h1{font-family:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif;font-size:19pt;letter-spacing:-.01em;margin:0 0 4pt;border-bottom:2px solid #14202c;padding-bottom:6pt}
h2{font-family:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif;font-size:13pt;margin:16pt 0 4pt;page-break-after:avoid}
h3{font-family:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif;font-size:11pt;margin:10pt 0 3pt;page-break-after:avoid}
p{margin:0 0 7pt}a{color:#0f4c75;text-decoration:none}
table{width:100%;border-collapse:collapse;font-size:9pt;margin:4pt 0 8pt;font-family:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif;page-break-inside:auto}
tr{page-break-inside:avoid}th,td{text-align:left;vertical-align:top;padding:4pt 6pt 4pt 0;border-bottom:1px solid #d7dde3}th{color:#5b6977;font-weight:500;border-bottom:1px solid #14202c}
li{margin:2pt 0}sup{font-size:7pt;color:#b4761a;font-family:\"Bricolage Grotesque\",Arial,sans-serif;margin-left:1px}
ul{padding-left:16pt}li b{color:#b4761a;font-weight:600}
.footnote{font-family:"Bricolage Grotesque","Helvetica Neue",Arial,sans-serif;font-size:8.5pt;color:#3b4652;border-top:1px solid #d7dde3;margin-top:14pt;padding-top:8pt}
.footnote ol{padding-left:18pt}.footnote li{margin:1.5pt 0}.footnote a.footnote-backref{display:none}
.end{font-family:"Bricolage Grotesque",Arial,sans-serif;font-size:8.5pt;color:#5b6977;border-top:1px solid #d7dde3;margin-top:18pt;padding-top:6pt}'''
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,400;12..96,600&family=Source+Serif+4:ital,opsz,wght@0,8..60,400;0,8..60,600;1,8..60,400&display=swap" rel="stylesheet">'
out = ROOT / "docs" / "samples"; out.mkdir(exist_ok=True)
tmp = pathlib.Path(os.environ.get("TMPDIR", "/tmp")) / "cold-read-samples"; tmp.mkdir(exist_ok=True)
for md in sorted(glob.glob(str(ROOT / "skills/cold-read/examples/*.md"))):
    if md.endswith("README.md"): continue
    text = pathlib.Path(md).read_text()
    # the "Sources by lane" section is rendered by the footnotes extension at the end; keep the lane headings as plain lines
    # keep the lane ids: references become superscripts, definitions become a list under their lane heading
    text = re.sub(r"^\[\^(s\d+-\d+)\]: (.*?)(https?://\S+)\s*$", r"- **\1** \2[\3](\3)", text, flags=re.M)
    text = re.sub(r"\[\^(s\d+-\d+)\]", r"<sup>\1</sup>", text)
    body = markdown.markdown(text, extensions=["tables"])
    name = pathlib.Path(md).stem
    html = f'<!doctype html><html><head><meta charset="utf-8">{FONTS}<style>{CSS}</style></head><body>{body}<p class="end">Cold Read, sample read. me2resh.github.io/cold-read</p></body></html>'
    hp = tmp / f"{name}.html"; hp.write_text(html)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", "--virtual-time-budget=8000",
                    f"--print-to-pdf={out / (name + '.pdf')}", f"file://{hp}"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, check=False)
    print("built", out / (name + ".pdf"))
