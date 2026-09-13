# Online marketing · Pannon Egyetem · 2026 ősz · nappali

A félév weboldala és az ügynökségi app. Élesben: https://egyetem.bemind.dev/om2026nappali/

## Mi van itt

- `index.html` – gyűjtőoldal, a hét alkalom
- `online-marketing-2026-evad-1-epizod.html` – az 1. alkalom prezentációja (a többi alkalom ugyanígy, saját fájlban)
- `app.html` – ügynökségi app: csapat, leadás, szavazás, eredmény (`?ep=ep1&v=csapat`)
- `api.php` – az app háttere, JSON-tár a `data/` mappában
- `.cpanel.yml` – ez mondja meg a cPanelnek, mit másoljon a mappába deploykor
- `key.php.example` – az oktatói kulcs mintája; a szerveren `key.php` néven, a gitben nincs

Nincs a gitben, szándékosan: `data/` (a beküldések és szavazatok) és `key.php` (a kulcs). Deploykor ezekhez nem nyúl.

## Új alkalom hozzáadása

1. Új deck fájl a mappába (`...-2-epizod.html`).
2. `app.html` elején az `EPISODES` listában az `ep2` mezőit átírni a leadandóhoz.
3. `index.html`-ben a 2. alkalom sorát élesíteni (az `off` osztály törlése, linkek).
4. `.cpanel.yml`-be egy új `cp` sor az új deck fájlra.
5. Commit, push, cPanel: Update from Remote, Deploy HEAD Commit.
