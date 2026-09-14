# Online marketing · Pannon Egyetem · 2026 ősz · nappali

A félév weboldala és az ügynökségi app. Élesben: https://egyetem.bemind.dev/om2026nappali/

## Mi van itt

- `index.html` – gyűjtőoldal, a hét alkalom
- `online-marketing-2026-evad-1-epizod.html` – az 1. alkalom prezentációja (a többi alkalom ugyanígy, saját fájlban)
- `app.html` – ügynökségi app: csapat, leadás, szavazás, eredmény, oktató (`?ep=ep1&v=csapat`)
- `api.php` – az app háttere, JSON-tár a `data/` mappában
- `ALKALOM-SZABALYOK.md` – a további alkalmak készítési szabályai az 1. alkalom mintájára
- `forrasfeldolgozas-online-marketing-2026.md` – a könyvek fejezet-térképe epizódonként
- `.cpanel.yml` – ez mondja meg a cPanelnek, mit másoljon a mappába deploykor
- `key.php.example` – az oktatói kulcs mintája; a szerveren `key.php` néven, a gitben nincs

Nincs a gitben, szándékosan: `data/` (a beküldések és szavazatok), `key.php` (a kulcs) és `neptun.php` (a hallgatók Neptun-kódjai, a nyitólap belépéséhez). Deploykor ezekhez nem nyúl.

## Új alkalom hozzáadása

1. Új deck fájl a mappába (`...-2-epizod.html`).
2. `app.html` elején az `EPISODES` listában az `ep2` mezőit átírni a beadandóhoz.
3. `index.html`-ben a 2. alkalom sorát élesíteni (az `off` osztály törlése, linkek).
4. `.cpanel.yml`-be egy új `cp` sor az új deck fájlra.
5. Commit, push; a cron öt percen belül deployol.
