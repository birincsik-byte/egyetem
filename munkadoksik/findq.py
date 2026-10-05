#!/usr/bin/env python3
"""Idézetellenőrző a könyvfejezetekhez.

Használat: python3 findq.py FÁJL "idézet"
Kimenet: az oldalszám(ok), ahol a szóközre normalizált idézet megtalálható, vagy NOT FOUND.
Az oldalszám a legközelebbi előtte álló futófejből jön:
  Chaffey: 'Chapter N ... 123' vagy '123  Part N ...'
  Kotler:  '... CHAPTER 5  125' vagy '124  PART ...'
Az idézőjeleket és a kötőjeleket normalizálja.
Eredetileg 2026. szeptember 28-án készült a 3. alkalom forrásfeldolgozásához.
"""
import re, sys, bisect

HDR = re.compile(r'^\s*(?:Chapter \d+ .*?\s(\d{2,3})\s*$|(\d{2,3})\s+Part \d|.*CHAPTER \d+\s+(\d{2,3})\s*$|(\d{2,3})\s+PART\b)')

def load(fn):
    lines = open(fn, encoding='utf-8', errors='replace').read().split('\n')
    page = None; toks = []
    for ln in lines:
        m = HDR.match(ln)
        if m:
            page = int([g for g in m.groups() if g][0]); continue
        for w in ln.split():
            toks.append((w, page))
    return toks

def norm(w):
    w = w.replace('–', '-').replace('—', '-')
    w = re.sub(r'[“”]', '"', w)
    return re.sub(r'[‘’´`]', "'", w)

def find(fn, q):
    toks = load(fn)
    ws = [norm(t[0]) for t in toks]
    text = ' '.join(ws); qt = ' '.join(norm(w) for w in q.split())
    offs = []; p = 0
    for w in ws:
        offs.append(p); p += len(w) + 1
    res = []; start = 0
    while True:
        i = text.find(qt, start)
        if i < 0: break
        ti = bisect.bisect_right(offs, i) - 1
        tj = bisect.bisect_right(offs, i + len(qt) - 1) - 1
        res.append((toks[ti][1], toks[tj][1])); start = i + 1
    return res

if __name__ == '__main__':
    r = find(sys.argv[1], sys.argv[2])
    print(r if r else 'NOT FOUND')
