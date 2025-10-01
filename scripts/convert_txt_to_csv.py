#!/usr/bin/env python3
"""
Convierte un .txt de líneas "mensaje ... etiqueta" a CSV UTF-8 (id,text,label).

Uso:
  python scripts/convert_txt_to_csv.py input.txt data/corpus.csv --anonymize
"""
import re, csv, sys, argparse
from pathlib import Path

LABEL_RE = re.compile(r'^(?P<text>.*?)[\s,;|]+(?P<label>[01])\s*$')
EMAIL_RE = re.compile(r'[\w\.-]+@[\w\.-]+', re.UNICODE)
PHONE_RE = re.compile(r'(\+?\d[\d\s\-\(\)]{7,}\d)')
URL_RE   = re.compile(r'(https?://\S+|www\.\S+)', re.UNICODE)
USER_RE  = re.compile(r'@\w+', re.UNICODE)

def anonymize(s: str) -> str:
    s = EMAIL_RE.sub('<email>', s)
    s = URL_RE.sub('<url>', s)
    s = PHONE_RE.sub('<phone>', s)
    s = USER_RE.sub('<user>', s)
    return s

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("input_txt")
    ap.add_argument("output_csv")
    ap.add_argument("--anonymize", action="store_true")
    args = ap.parse_args()

    in_path = Path(args.input_txt)
    out_path = Path(args.output_csv)
    out_path.parent.mkdir(parents=True, exist_ok=True)

    rows = []
    with in_path.open("r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            line = line.strip()
            if not line:
                continue
            m = LABEL_RE.match(line)
            if not m:
                print(f"[WARN] Línea {i} no coincide con el patrón esperado, se omite:\n  {line}\n", file=sys.stderr)
                continue
            text = m.group('text').strip()
            label = int(m.group('label'))
            if args.anonymize:
                text = anonymize(text)
            rows.append((i, text, label))

    with out_path.open("w", encoding="utf-8", newline="") as fout:
        w = csv.writer(fout)
        w.writerow(["id","text","label"])
        for rid, text, label in rows:
            w.writerow([rid, text, label])

    print(f"Escribí {len(rows)} filas en {out_path}")

if __name__ == "__main__":
    main()
