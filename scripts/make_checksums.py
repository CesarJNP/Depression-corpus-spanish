#!/usr/bin/env python3
import hashlib, sys, pathlib

def sha256_of(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()

paths = sys.argv[1:] or ["data/corpus.csv"]
for p in paths:
    pth = pathlib.Path(p)
    if pth.exists():
        print(sha256_of(pth), pth)
    else:
        print(f"[WARN] No existe {p}")
