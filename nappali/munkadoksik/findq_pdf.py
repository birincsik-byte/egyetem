#!/usr/bin/env python3
"""Idézetellenőrző a pdftotext -layout kimenetéhez (a 3. alkalom új könyvei).
Használat: python3 findq_pdf.py FÁJL "idézet"
Kimenet: (nyomtatott oldalszám: Weinschenknél és Yablonskinál a PDF-lap mínusz a fix eltolás, vagy None, PDF-lapindex, fejezet) minden találatra, vagy NOT FOUND.
A nyomtatott oldalszámot a lap fej- vagy lábsorából olvassa ki
(Weinschenk: '8   HOW PEOPLE SEE', Yablonski: 'FITTS’S LAW | 21'). Krugnál a PDF-ben nincs
oldalszám, ezért ott a fejezetet adja ('Chapter N.').
Készült: 2026. október 5."""
import re, sys
def norm(s):
    s = s.replace('–','-').replace('—','-').replace('­','')
    s = re.sub(r'[“”]','"',s); s = re.sub(r'[‘’´`]',"'",s)
    s = re.sub(r'-\s*\n\s*','',s)  # sorvégi elválasztás
    return ' '.join(s.split())
def pageno(pg):
    ls=[l.strip() for l in pg.split('\n') if l.strip()]
    for l in ls[:2]+ls[-2:]:
        m=re.match(r'^(\d{1,3})\s{2,}[A-Z ]+$',l) or re.match(r'^[A-Z’\'\-– ]+\s*\|\s*(\d{1,3})$',l) or re.match(r'^(\d{1,3})\s*\|',l) or re.match(r'^\|\s*(\d{1,3})$',l)
        if m: return int(m.group(1))
    return None
OFFSET={'weinschenk':13,'yablonski':20}  # nyomtatott oldal = PDF-lap - eltolás (2026. október 5-én ellenőrizve)
def find(fn,q):
    pages=open(fn,encoding='utf-8').read().split('\f'); qn=norm(q); res=[]; chap=None
    for i,pg in enumerate(pages):
        m=re.findall(r'^\s*Chapter (\d+)\.',pg,re.M)
        if m: chap=int(m[-1]) if not m else int(m[0])
        nxt=pages[i+1][:600] if i+1<len(pages) else ''
        off=[v for k,v in OFFSET.items() if k in fn.lower()]
        pp=(i+1-off[0]) if off else pageno(pg)
        if qn in norm(pg): res.append((pp,i+1,chap))
        elif qn in norm(pg+' '+nxt) and qn not in norm(nxt): res.append((pp,i+1,chap,'lapon átnyúlik'))
    return res
if __name__=='__main__':
    r=find(sys.argv[1],sys.argv[2]); print(r if r else 'NOT FOUND')
