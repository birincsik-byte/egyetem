# 3. alkalom · folytatás · innen veszed fel a szálat

Online marketing 2026 ősz · nappali · Pannon Egyetem · 3. alkalom, „A saját terep”, 2026. október 12.
Készült: 2026. október 11. Ez a doksi felülírja az `UJ-FIOK-INDULAS.md` 3. alkalomra vonatkozó részét és a `munkadoksik/HOL-TARTUNK.md` „A következő alkalom” szakaszának régi mondatait. Ha bármi ellentmond, ez az érvényes, és kérdezd meg az oktatót.

## Összefoglaló

2026. október 11. délután: a deck (v0.14, 37 dia), az anatómia-aloldal (v0.4) és a beadandó-eszköz (`oldal-vizsgalat.html` v2.1) kész, az `app.html` `ep3`, az `index.html` 3. sora és a `.cpanel.yml` `cp` sorai is. Minden alkalom webes fájlja a saját `alkalom-N/` mappájában van, a `.cpanel.yml` onnan másol. Következik: a deploy (Claude Code), utána a jegyzetek a deckbe (7. fázis). Előtte: Az 1. és a 2. fázis (forrásfeldolgozás, jegyzet-kutatás) kész, a tematika jóvá van hagyva, a deck kattintható vázlata (v0.12, 30 dia) és az anatómia-aloldal (v0.3) kész, az oktató átnézi. A kidolgozott jegyzet (3. fázis) az oktató kérésére a deck után készül. Következik: a deck további javítása az oktató visszajelzései szerint, utána az 5. fázis, a feladat kitalálása.

## Ami érvényes

- **Tematika:** `alkalom-3/tematika-3-alkalom.md` v6. Hangsúly: a hallgatók értsék meg, mennyire fontos a weboldal és a landing, és mitől lesz jó (layout, szöveg, grafika, ergonómia, tipikus felépítések, miért így építjük, mitől tiszta és egyértelmű), mert ha a látogatónak energiát spórolunk, szívesebben vásárol, és nő a bizalma.
- **A hármas (B változat, az oktató választotta 2026. október 6-án):**
  - Miről szól: weboldal és landing, tipikus felépítések, layout, szöveg, grafika, ergonómia, bizalom, regisztráció és e-mail.
  - Kulcsgondolat: a jó weboldal energiát spórol a látogatónak, és ezért cserébe bizalmat kap.
  - Tanulság: ha a látogatónak gondolkodnia kell, hol van és mit tegyen, az oldal már veszített.
- **A nap:** másfél óra elmélet, másfél óra csoportmunka. Az idők relatívak, az oktató szabályozza.
- **A beadandó (eldöntve 2026. október 11.):** a saját márka oldala és egy külső oldal ugyanazzal a nyolc szemüveggel, három körben: Ránézés (1. Miről szól az oldal? 2. Mit akar az oldal? 3. Mit mond a márka, milyen a hangvétel?), Olvasás (4. Tartalom, 5. Layout), Cselekvés (6. Folyamat: vezetett az oldal a szövegeivel? 7. Konverziós pontok, 8. Bizalom). Szemüvegenként egy jelölés (működik, részben, nem működik) és bizonyíték, a végén egy mondat és „mit vinnétek át”. Szavazás nincs. Ha a márkának nincs weboldala: amit a keresés hoz, és két külső oldal. Eszköz: `alkalom-3/oldal-vizsgalat.html`, benne a Tunki-Tunki minta; a deckben a Tunki-bemutató szemüvegenként (27–34. dia). Külső lista (ellenőrizve 2026. október 11.): Hunguest Hotels, Bamba Marha, Babilon Nyelvstúdió, Paloznaki Jazzpiknik (szezonon kívül, a jegyoldal nem él), Tisza Cipő, Szamos, Más.
- **Deck:** `alkalom-3/online-marketing-2026-evad-3-epizod.html` v0.14 (37 dia), diánkénti vázlat: `alkalom-3/deck-vazlat-3-alkalom.md` v1.2 (a számozás a v1.0-é, a kikerült diák jelölve).
- **Aloldal:** `alkalom-3/oldal-anatomia.html` v0.4: a landing anatómiája kész oldalként és drótvázként, landingtípusok (mikor, mi a siker), layout-sablonok (mikor, nem jó), bizalom, oldaltípusok, szín. A deckből gomb nyitja új lapon (16. dia).

## Ami el van engedve (ne hozd vissza)

- A korábbi sessionből beemelt kulcsgondolat („a forgalom nem eredmény…”), tanulság („a konverzió ritkán meggyőzés kérdése…”) és fázis-sor („Bizalom és meggyőzés.” …). **Ezek nem az oktató mondatai** (2026. október 5.), akkor sem, ha a `HOL-TARTUNK.md`, az `UJ-FIOK-INDULAS.md` vagy a `gondolati-iv-7-epizod.md` annak írja.
- A mérés (események, mikro- és makrokonverzió, GA4, cookie, hőtérkép): a 6. alkalomra került, a feljegyzés a `HOL-TARTUNK.md` „Ami el van halasztva” szakaszában.
- A hirdetés és a landing relevanciája és a hat kattintható gyakorlat: a 4. alkalomhoz került, `alkalom-4/hirdetes-landing-jatek.html`.
- Kikerült diák: weboldal kontra landing kapcsoló, az alapképlet sávjai, a Tesler-csúszka, a kezdőlap drótváza, az oldaltípusok és a bizalmi elemek dia (ezek az aloldalra).
- A klasztermodell és az információs architektúra részletei: csak a jegyzetbe. Szintén csak a jegyzetbe: design system, mikrointerakciók, akadálymentesség, UX-szövegírás, OOUX.

## Az oktató kérései a deckhez

- Nincs soronkénti felfedés: minden dia egyben jelenik meg, csak az interaktív elemek kattinthatók.
- Egységes megjelenés: a 2. deck váza és palettája (sötétkék, kobalt, sárga), egy kártyatípus, a cím mindig ugyanott.
- Nagyobb betű: alap kb. 23 px 1440 px-en, a diákon semmi 18 px alatt; az alsó segédsor lehet kisebb.
- Interakció csak ott, ahol tényleg tanít. A „kütyü” interakciók (sávok, csúszkák) nem kellenek.
- A layout vizuális műfaj: az elv mellé mindig vizualitás, drótvázszerű bemutatás.
- Belső aloldal gombbal, új lapon nyílik, nem beágyazva.
- A diákra nem kerül forrás, az a jegyzet „Forrás:” sorába megy.

## Nyitott kérdések (az oktató dönt)

1. A GDPR (hivatalos tematikai pont) átmegy a 6. alkalomra, vagy kap egy mondatot a „Hogyan marad” dián?
2. A Baymard-szám a 23. dián: 18% (pénztári elhagyási okok) vagy 24% (2022-es felmérés)?
3. A goodwill-tartály (21. dia) interaktív marad-e.
4. A címlapon a kérdés végére kerüljön-e kérdőjel.
5. A `Claude outputs/` mappa a gyökérben (a deck egy régi példánya, a desktop app hozta létre): törölni vagy gitből kihagyni.

## A következő lépések

1. Az oktató visszajelzései a deckre (diaszámmal, vagy a J javító mód listájával).
2. 5. fázis: kész (2026. október 11.), lásd fent „A beadandó”.
3. 6. fázis: kész (2026. október 11.): `alkalom-3/oldal-vizsgalat.html`, `app.html` `ep3` (szavazás nélkül, „Beadandók” nézet), `index.html` 3. sor, `.cpanel.yml` `cp` sorok mappával. Hátra van a commit és a push (Claude Code).
4. 7. fázis: jegyzetek a deckbe (jelenleg helykitöltő), a forrásokból.

## Források és eszközök

- `alkalom-3/forrasfeldolgozas-3-alkalom.md` v3, `alkalom-3/jegyzet-kutatas-3-alkalom.md` v1 (a régi kilenc blokk szerint, a tartalma használható), `alkalom-3/webkutatas-3-alkalom.md` v2, `alkalom-3/ux-ui-hatar-3-alkalom.md`, `alkalom-3/ux-peldaoldalak-3-alkalom.md`.
- Könyvszövegek: `konyvek/` (gitignorált), az új UX-könyvek a `konyvek/3ik alkalom/` alatt. Idézetellenőrzés: `munkadoksik/findq.py` (Chaffey, Kotler; a 10. fejezet páratlan oldalait is felismeri), `munkadoksik/findq_pdf.py` (Krug fejezettel, Weinschenk, Yablonski oldallal).
- A deck építése: a 2. deck vázából, Playwright-renderteszt 1440×900-on, túlcsordulás és szkripthiba nincs.
- Mentés: a mappába, md5-tel ellenőrizve. Tapasztalat: a `device_commit_files` ugyanarra a staged fájlnévre néha a régi tartalmat írja; mindig új staged fájlnevet használj, és mentés után ellenőrizd az md5-öt a gépen.

## Szabályok (változatlanok)

A munkarend, a nyelvi és a forrásszabályok az `ALKALOM-INDITO-PROMPT.md`-ben, az `ALKALOM-SZABALYOK.md`-ben és az `UJ-FIOK-INDULAS.md` „Hogyan dolgozz velem” szakaszában. Commit és push nincs, azt a Claude Code session csinálja.
