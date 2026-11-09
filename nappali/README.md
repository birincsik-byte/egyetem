# Online marketing · Pannon Egyetem · 2026 ősz · nappali

A félév weboldala és az ügynökségi app. Élesben: https://egyetem.bemind.dev/om2026nappali/

## Mi van itt

- `index.html` – gyűjtőoldal, a hét alkalom
- `app.html` – ügynökségi app: csapat, leadás, szavazás, eredmény, oktató (`?ep=ep1&v=csapat`)
- `api.php` – az app háttere, JSON-tár a `data/` mappában
- `munkadoksik/` – a félév munkadoksijai (állapot, szabályok, gondolati ív, forrástérkép); nem mennek ki a webre
- `alkalom-N/` – alkalmanként minden, ami az alkalomhoz tartozik: a deck (`online-marketing-2026-evad-N-epizod.html`), a beadandó-eszköz és a segédlet (ezek mennek ki a webre, `cp` sorral), valamint a forrásfeldolgozás és a jegyzetek (ezek nem)
- `UJ-FIOK-INDULAS.md` – belépési pont egy új munkamenethez
- `.cpanel.yml` – ez mondja meg a cPanelnek, mit másoljon a mappába deploykor
- `key.php.example` – az oktatói kulcs mintája; a szerveren `key.php` néven, a gitben nincs

Nincs a gitben, szándékosan: `data/` (a beküldések és szavazatok), `key.php` (a kulcs) és `neptun.php` (a hallgatók Neptun-kódjai, a nyitólap belépéséhez). Deploykor ezekhez nem nyúl.

## Új alkalom hozzáadása

1. Új deck fájl az alkalom mappájába (`alkalom-N/online-marketing-2026-evad-N-epizod.html`).
2. `app.html` elején az `EPISODES` listában az `ep2` mezőit átírni a beadandóhoz.
3. `index.html`-ben a 2. alkalom sorát élesíteni (az `off` osztály törlése, linkek).
4. `.cpanel.yml`-be egy új `cp` sor az új deck fájlra, a mappával együtt (`/bin/cp alkalom-N/... $DEPLOYPATH`). A szerveren a fájl a gyökérbe kerül, a webcím nem változik.
5. Commit, push; a cron legfeljebb negyed órán belül deployol (a pontos ütemezés a `CLAUDE.md`-ben).
