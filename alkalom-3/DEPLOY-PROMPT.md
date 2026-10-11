# Deploy-prompt a Claude Code-nak · 3. alkalom · 2026. október 11.

Ezt másold be a Claude Code-nak, a `/Users/birincsik/Claude/Projects/Egyetem` mappában:

---

Online marketing 2026, a 3. alkalom deployja. Olvasd el a `CLAUDE.md`-t, és aszerint dolgozz.

Mi változott 2026. október 11-én:
- Új: `alkalom-3/online-marketing-2026-evad-3-epizod.html` (deck v0.14), `alkalom-3/oldal-anatomia.html` (v0.4), `alkalom-3/oldal-vizsgalat.html` (beadandó-eszköz v2.1), `alkalom-3/` munkadoksik, `alkalom-4/`.
- Módosult: `app.html` (v2.10, `ep3`), `index.html` (v1.7, a 3. sor élő), `.cpanel.yml`, a README-k, `CLAUDE.md`, `UJ-FIOK-INDULAS.md`, `munkadoksik/HOL-TARTUNK.md`, `munkadoksik/ALKALOM-INDITO-PROMPT.md`, `munkadoksik/findq.py`, új `munkadoksik/findq_pdf.py`.
- Áthelyezve, a név nem változott: `online-marketing-2026-evad-1-epizod.html` → `alkalom-1/`, `online-marketing-2026-evad-2-epizod.html`, `journey-terkep.html`, `journey-tippek.html` → `alkalom-2/`. A `.cpanel.yml` `cp` sorai már a mappával együtt hivatkoznak rájuk, a szerveren a gyökérbe kerülnek, a webcím nem változik.

Lépések:
1. `git status`, egy mondatban mondd el, mi változott.
2. Ellenőrizd, hogy a `.cpanel.yml` minden `cp` sorának forrásfájlja létezik (10 sor). Ha bármelyik hiányzik, állj meg, és szólj.
3. `git add -A`, utána nézd meg a staged listát: nem lehet benne `data/`, `key.php`, `neptun.php`, `BCKP/`, `.claude/`, `konyvek/`, `.DS_Store`. Ha bármelyik benne van, állj meg. Az áthelyezett négy fájl átnevezésként (rename) jelenjen meg.
4. Commit: „3. alkalom: deck v0.14, oldal-anatómia, oldalvizsgálat, app ep3, index 3. sor; alkalmankénti mappák”. Push a `main` ágra, írd ki a hasht.
5. A következő cron-kör után (legfeljebb negyed óra) nézd meg élesben, hogy betölt-e: https://egyetem.bemind.dev/om2026nappali/ (3. sor), `online-marketing-2026-evad-3-epizod.html`, `oldal-anatomia.html`, `oldal-vizsgalat.html`, `app.html?ep=ep3&v=eredmeny`, és a régiek: `online-marketing-2026-evad-1-epizod.html`, `online-marketing-2026-evad-2-epizod.html`, `journey-terkep.html`.
