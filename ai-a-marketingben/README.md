# AI a marketingben · 2026 ősz · gyakorlat

Élesben: https://egyetem.bemind.dev/ai-in-marketing/ (külön mappa a szerveren).

Hat csütörtöki gyakorlat 2026. november 5. és 2026. december 10. között, 8:00-12:00. Oktató: Birincsik Albert. 11 hallgató, egyéni munka.

## Ami ebben a mappában van

- `index.html`: a kezdőlap Neptun-kódos belépéssel és a hat alkalommal. Deploykor a szerveren `index.html` néven az `ai-in-marketing` mappába kerül.
- `ai-marketing-2026-alkalom-1.html` … `ai-marketing-2026-alkalom-6.html`: alkalmanként egy diasor, magyarul és angolul (HU/EN gomb vagy L billentyű). Az 1. alkalom diasora a tárgy bevezetőjével kezdődik. Jegyzet funkció nincs, a J billentyű a javító mód.
- A közös `api.php` a gyökérből megy ki ide is, a belépés ezen keresztül működik.
- `forras/`: a diasorok generátora (`build.py`, `content.py`) és a promptok (`codeblocks_hu.json`, `codeblocks_en.json`). Nem megy ki a webre, nincs `cp` sora. A diasorokat nem kézzel írjuk át: a chatben módosul a `content.py`, és `python3 forras/build.py` újragenerálja az összes HTML-t ebbe a mappába.

## A szerveren, kézzel (nincs a gitben)

- `neptun.php`: a 11 hallgató Neptun-kódja, helye `public_html/ai-in-marketing/neptun.php`. Amíg nincs fent, csak az oktatói kulccsal lehet belépni a kezdőlapon; a diasorok közvetlen linkkel belépés nélkül is megnyílnak.
- `key.php`: az oktatói kulcs, ugyanaz, mint a nappalin, helye `public_html/ai-in-marketing/key.php`.
- A feltöltendő két fájl itt van: `ai-a-marketingben/szerverre-kezzel/`. A `.gitignore` meglévő `neptun.php` és `key.php` sora miatt nem kerülnek a repóba.

## Forrás

A tartalom az „AI a marketingben hallgatói feladatleírás” Claude-dokumentumból készült (magyar és angol fül), a 2026. november 4-i állapot szerint.
