# CLAUDE.md

Ez a repó a Pannon Egyetem Online marketing kurzus 2026 őszi nappali félévének weboldala és ügynökségi appja.
Élesben: https://egyetem.bemind.dev/om2026nappali/

## Hogyan kerül fel, amit készítünk

A tulajdonos teljes fájlt ad, mindig ugyanazzal a névvel, mint ami a repóban van. A fájl a régi helyére kerül, a gyökérbe, felülírva a korábbit. Utána commit és push a `main` ágra. A deployt a szerveren cPanel Git és cron végzi, tehát a push után nagyjából öt percen belül élesben van.

Ellenőrzés: a `main` legutóbbi commitjának tartalma öt perc múlva a fenti URL-en látszik.

## Mi van a repóban

- `index.html` gyűjtőoldal, a hét alkalom
- `online-marketing-2026-evad-N-epizod.html` az N. alkalom prezentációja, alkalmanként külön fájl
- `app.html` ügynökségi app: csapat, leadás, szavazás, eredmény (`?ep=ep1&v=csapat`)
- `api.php` az app háttere, JSON-tár a `data/` mappában
- `.cpanel.yml` ez mondja meg a cPanelnek, mit másoljon ki a deploy mappába
- `key.php.example` az oktatói kulcs mintája
- `README.md` a projekt leírása
- `CLAUDE.md` ez a fájl

## Új alkalom hozzáadása

Új deck fájl esetén három fájl megy együtt, egyetlen commitban:

1. az új deck, `online-marketing-2026-evad-N-epizod.html` néven
2. `index.html`, az adott alkalom sora élesítve
3. `.cpanel.yml`, benne egy új sor az új deck fájlra:
   `- /bin/cp online-marketing-2026-evad-N-epizod.html $DEPLOYPATH`

Ha az `app.html` leadandó mezői is változnak, az is mehet ugyanebbe a commitba.

Commit üzenet formája: `N. alkalom: mi változott`, például `2. alkalom: deck, index, cpanel`.

## Szabályok

Soha ne kerüljön a repóba a `data/` mappa és a `key.php` fájl. A `.gitignore` ezeket kizárja, ne módosítsd.

Ne hozz létre GitHub Actions workflow-t. A deploy cPanel Git és cron dolga.

Ne írd át a kapott fájlok tartalmát. Ami érkezik, az kész, azt kell a helyére tenni.

Ha új fájl kerül a repóba, aminek nincs `cp` sora a `.cpanel.yml`-ben, kérdezz rá, hogy kimásolandó-e a szerverre. Ne találgass. Kivétel a `README.md` és ez a `CLAUDE.md`, ezek szándékosan nem kerülnek ki a weboldalra.

Az `api.php` a `data/` mappába ír a szerveren. A deploy ehhez a mappához nem nyúl, tehát a beküldések és a szavazatok megmaradnak.
