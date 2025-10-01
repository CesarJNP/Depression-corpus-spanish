#!/usr/bin/env python3
import argparse, csv, random, os
from collections import defaultdict

ap = argparse.ArgumentParser()
ap.add_argument("csv_path")
ap.add_argument("--seed", type=int, default=42)
ap.add_argument("--train", type=float, default=0.8)
ap.add_argument("--val", type=float, default=0.1)
ap.add_argument("--test", type=float, default=0.1)
ap.add_argument("--outdir", default="data/splits")
args = ap.parse_args()

random.seed(args.seed)

rows = []
with open(args.csv_path, encoding="utf-8") as f:
    r = csv.DictReader(f)
    for row in r:
        rows.append(row)

by_label = defaultdict(list)
for row in rows:
    by_label[row["label"].strip()].append(row)

splits = {"train": [], "val": [], "test": []}
for label, items in by_label.items():
    random.shuffle(items)
    n = len(items)
    n_train = int(n*args.train)
    n_val = int(n*args.val)
    train = items[:n_train]
    val = items[n_train:n_train+n_val]
    test = items[n_train+n_val:]
    splits["train"].extend(train)
    splits["val"].extend(val)
    splits["test"].extend(test)

os.makedirs(args.outdir, exist_ok=True)
for name, part in splits.items():
    outp = os.path.join(args.outdir, f"{name}.csv")
    with open(outp, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id","text","label"])
        w.writeheader()
        for row in part:
            w.writerow(row)
    print(f"Escribí {len(part)} filas en {outp}")
