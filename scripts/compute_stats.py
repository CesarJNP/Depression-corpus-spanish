#!/usr/bin/env python3
import sys, csv, statistics
from collections import Counter

if len(sys.argv) < 2:
    print("Uso: python scripts/compute_stats.py data/corpus.csv")
    sys.exit(1)

path = sys.argv[1]
labels = []
lengths = []
with open(path, encoding="utf-8") as f:
    r = csv.DictReader(f)
    for row in r:
        txt = row["text"]
        labels.append(int(row["label"]))
        lengths.append(len(txt))

c = Counter(labels)
n = len(labels)
p0 = 100*c.get(0,0)/n if n else 0
p1 = 100*c.get(1,0)/n if n else 0

print(f"N = {n}")
print(f"Clase 0: {c.get(0,0)} ({p0:.2f}%)")
print(f"Clase 1: {c.get(1,0)} ({p1:.2f}%)")
print(f"Longitud media (caracteres): {statistics.mean(lengths):.1f}")
