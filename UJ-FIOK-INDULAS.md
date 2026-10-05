# Új fiók, 3. alkalom · innen veszed fel a szálat

Online marketing 2026 ősz · nappali · Pannon Egyetem
Készült: 2026. október 5. · a régi fiók „Egyetem tanítás” Projectjéből és a korábbi chatekből

## Összefoglaló

Ez a doksi az átadás egy új Claude-fióknak. Az új fiók nem látja a régi Projectet, a memóriát és a korábbi chateket. Minden, ami kell, ebben a mappában van: `/Users/birincsik/Claude/Projects/Egyetem`. Ez a doksi megmondja, mit olvass el, hol tart a munka, és mi a dolgod. A 3. alkalom (2026. október 12., „A saját terep”) előkészítése a 2026. szeptember 28-i chatben elindult, de annak eredménye nem került a gépre, ezért az 1. fázist újra kell kezdeni.

## Ki vagyok, mi ez

Birincsik Albert (Berti) vagyok, a Pannon Egyetemen tanítom az Online marketing kurzust (VEGTKMB5, nappali, 2026 ősz). Hét hétfői alkalom, mindegyik négy 45 perces blokk. A hallgatók csapatokban, ügynökségként dolgoznak egy valós magyar márkán, amit az 1. alkalmon választottak, és a félév végéig fix. Minden alkalom végén leadnak egy beadandót, erre a többi csapat a saját telefonjáról szavaz egytől öt csillagig, kötelező indoklással; a saját csapatára senki nem szavaz. A hét beadandó a jegy 70%-a. Minden anyag egy weboldalon él: https://egyetem.bemind.dev/om2026nappali/

Az 1. alkalom 2026. szeptember 14-én, a 2. alkalom 2026. szeptember 28-án volt.

## A mappa rendje

2026. október 5-én rendeztem át. A webre kerülő fájlok a gyökérben maradtak, mert a nevük és a helyük a `.cpanel.yml`-hez és a szerverhez van kötve; ezeket soha ne mozgasd és ne nevezd át. A munkadoksik almappákba kerültek.

```
Egyetem/
├── UJ-FIOK-INDULAS.md          ez a doksi, az új fiók belépési pontja
├── CLAUDE.md                   a Claude Code szabályai (a gyökérben kell lennie)
├── README.md                   a repó leírása
│
├── index.html                  ┐
├── app.html                    │
├── api.php                     │ élesbe menő fájlok,
├── online-marketing-2026-evad-1-epizod.html   │ a .cpanel.yml másolja őket,
├── online-marketing-2026-evad-2-epizod.html   │ a gyökérben maradnak
├── journey-terkep.html         │
├── journey-tippek.html         ┘
├── .cpanel.yml  .gitignore  key.php.example
│
├── munkadoksik/                a félév egészére vonatkozó doksik
│   ├── HOL-TARTUNK.md
│   ├── ALKALOM-SZABALYOK.md
│   ├── ALKALOM-INDITO-PROMPT.md
│   ├── gondolati-iv-7-epizod.md
│   ├── forrasfeldolgozas-online-marketing-2026.md
│   └── findq.py                idézetellenőrző a könyvfájlokhoz
│
├── alkalom-1/README.md         mi tartozik az 1. alkalomhoz
├── alkalom-2/                  README, forrasfeldolgozas-2-alkalom.md, jegyzet-kutatas-2-alkalom.md
├── alkalom-3/                  README; ide kerülnek a 3. alkalom munkadoksijai
│
├── konyvek/                    könyvfejezetek és forrásjegyzetek (gitignorálva, nem mehet a publikus repóba)
│
└── nem gitbe: data/, key.php, neptun.php, BCKP/, .claude/, .DS_Store
```

Minden új alkalomnak saját `alkalom-N/` mappája van, benne egy `README.md` arról, mi tartozik hozzá, és a munkadoksik (`forrasfeldolgozas-N-alkalom.md`, `jegyzet-kutatas-N-alkalom.md`, `jegyzet-N-alkalom.md`). A deck, a beadandó-eszköz és a segédlet a gyökérbe kerül, `cp` sorral. A régi doksik (`ALKALOM-INDITO-PROMPT.md`, `CLAUDE.md`, `HOL-TARTUNK.md`) a munkadoksikat még fájlnévvel, mappa nélkül említik: a helyük a fenti rend szerint értendő.

## Mit olvass el, ebben a sorrendben

Mind a mappában van. Ha valamelyik hiányzik, állj meg, és kérd el.

1. **Ez a doksi** (`UJ-FIOK-INDULAS.md`).
2. **`munkadoksik/HOL-TARTUNK.md`**: az állapot és minden eddigi döntés dátummal. Ez a legfontosabb.
3. **`munkadoksik/ALKALOM-SZABALYOK.md`**: a tartalom, a nyelv és a dizájn szabályai.
4. **`munkadoksik/ALKALOM-INDITO-PROMPT.md`**: a régi fiók indító promptja, benne a kilencfázisú munkarend. A munkarend ugyanaz. Ahol „Projectet” említ, ott ezt a mappát értsd.
5. **`CLAUDE.md`**: a Claude Code és a deploy szabályai.
6. **`munkadoksik/gondolati-iv-7-epizod.md`**: csak a 3. epizód része és a fázis-táblázat.
7. **`munkadoksik/forrasfeldolgozas-online-marketing-2026.md`**: csak a 3. epizód szakasza.
8. **`alkalom-2/forrasfeldolgozas-2-alkalom.md`** és **`alkalom-2/jegyzet-kutatas-2-alkalom.md`**: csak a szerkezetük miatt, ez a minta a 3. alkalom doksijaihoz.
9. **`alkalom-3/README.md`**: mi hova kerül a 3. alkalomnál.

Utána nézd meg a gyökérben: `online-marketing-2026-evad-2-epizod.html` (a legfrissebb dizájnváz), `app.html`, `index.html`, `api.php`, `.cpanel.yml`, `.gitignore`, `journey-terkep.html`, `journey-tippek.html`; a `konyvek/` mappa öt 3. alkalmas fájlját, és a `munkadoksik/findq.py` idézetellenőrzőt.

Ha bármelyik doksi ellentmond ennek, jelezd, ne dönts helyettem.

## A 3. alkalom adatai

- Cím: „A saját terep”
- Dátum: 2026. október 12.
- A lánc kérdése: „Hol fogadjuk, amikor megérkezik hozzánk”
- Beadandó: landing page-audit és e-mail-folyamat
- Hivatalos tematikai pontok, szó szerint:
  - Weboldal és UX/UI mint forgalomterelő felület, loyalty/regisztrációs logika
  - (és a „Platformok és eszközök” pontból: automatizált email marketing)
  - (és a „Webanalitika és GDPR” pontból: a GDPR / jogi vonatkozások)

Az én mondataim, szó szerint mennek a deckbe:

- **Miről szól:** weboldal, UX/UI, regisztrációs és loyalty logika, automatizált e-mail, adatkezelés.
- **Kulcsgondolat:** a forgalom nem eredmény, és a weboldal az egyetlen felület, ami tényleg a tiéd.
- **Tanulság:** a konverzió ritkán meggyőzés kérdése, sokkal inkább súrlódásé. Egy akadály elvétele többet hoz, mint egy újabb érv.

A fázis-táblázat sora: mit hoz magával „Bizalom és meggyőzés.”, mire vált „Akadályok megszűntetése, percepció kialakítás a márkáról.”, mit tesz hozzá a végcélhoz „A felelősség átkerül a másik emberről a saját felületünkre.”

Átvezetés a 2. alkalomból: a 2. deck zárása és az áramlási térkép dia („Hogyan érkeznek meg a weboldalra, és mi lesz belőle?”) már a 3. alkalom kérdésére mutat. A térkép Act / Do fázisában a látogató már a mi felületünkön jár. A v9 deck 25. diája (Kotler, Keller 170–171., hat kockázat) azt ígérte: „Minden kockázathoz tartozik egy weboldalelem, ami leveszi. Ez lesz a harmadik alkalom.”

Ha a gondolati ív doksiban ezek a mondatok másképp állnak, ne válassz, mutasd meg mindkettőt, és kérdezz.

## Hol tartunk (2026. október 5.)

**Ami biztos:** a 2. alkalom lement. A `munkadoksik/HOL-TARTUNK.md` 2026. szeptember 28-i állapotot ír le; 2026. október 5-én a mappa rendjével és ezzel az átadással frissítettem. Mindig a gépen lévő példányt tekintsd hitelesnek. A verziószámokat a fájlokból vedd, ne doksiból. Egy eltérésről tudok: a `HOL-TARTUNK.md` szerint az app v2.9 commitra várt, a git log szerint viszont már commitolva van (`d8bfa7e app v2.9`, előtte `7c6f435 app v2.8`). A mappa 2026. október 5-én tiszta volt. Hogy a push és a deploy is lement-e, az élő oldal lábjegyzetében nézd meg.

**A 3. alkalom eddig:** 2026. szeptember 28-án egy chat elindította. Feldolgozta Chaffey 3., 4., 6., 7. és Kotler 5. fejezetét, szó szerinti angol idézetekkel, mindegyiket a `findq.py`-val ellenőrizve. Ezek a fájlok (`out-ch7.md`, `out-ch6.md`, `out-ch3-ch4.md`, `out-kotler5.md`) a felhőben készültek, és nem kerültek a gépre: 2026. október 5-én a mappában nem volt sem `out-*.md`, sem `forrasfeldolgozas-3-alkalom.md`, sem 3. alkalmas deck. Az 1. fázist tehát újra el kell végezni. A `munkadoksik/findq.py` megvan, a gépen kipróbálva működik (a Kotler-idézetre a 125. oldalt adja), nem kell újraírni.

**A szeptember 28-i chat két megállapítása,** amit újra ellenőrizned kell, mielőtt tényként kezeled:

1. A kulcsgondolatom és a tanulságom szó szerint egyik fejezetben sincs meg. A súrlódáshoz Kotler customer-perceived value költségoldala áll a legközelebb. Ezt most ellenőriztem a Kotler-fájlban: „Total customer cost is the perceived bundle of costs customers expect to incur in evaluating, obtaining, using, and disposing of the given market offering, including monetary, time, energy, and psychological costs.” (Kotler, Keller 14. kiadás, 5. fejezet, 125. oldal). Ugyanott a Caterpillar-példában: „Second, it can reduce the buyer’s nonmonetary costs by reducing the time, energy, and psychological investment.” Az oldalszámot a `munkadoksik/findq.py`-val erősítsd meg.
2. A Chaffey 3. fejezetben (6. kiadás, 2016) a GDPR szó nem szerepel, a Data Protection Act és az EU Data Protection Directive igen. A jelenlegi jogi állapotot ez a könyv nem írja le, ahhoz külső, megnevezett, hivatalos forrás kell.

**A szeptember 28-i chat javaslata,** amit én nem hagytam jóvá: egy 25 diás vázlat öt elméleti pillérrel (miért a saját terep, mit lát a látogató öt másodperc alatt, mi állítja meg, hogyan tartjuk meg, milyen szabályok vonatkoznak rá), és egy journey-térkép mintájú interaktív beadandó-eszköz. Kiindulásnak használhatod, de nem döntés.

## Nyitott kérdések, ezekről én döntök

1. **Az e-mail-feliratkozás előre kiadása.** Ha a beadandó része az e-mail-folyamat megfigyelése, a csapatoknak már most fel kell iratkozniuk a márkájuk hírlevelére, különben október 12-re nem lesz mit megfigyelni. Jelenleg egy hét van hátra. Ez időkritikus, ezzel kezdd: kérdezz rá, és ha igen, készíts rövid szöveget (indexre vagy a csapatoknak).
2. **A beadandó formája:** interaktív eszköz, ami maga a leadás (mint a 2. alkalom journey-térképe), vagy egyszerűbb űrlap az app Leadás nézetében.
3. **A betűméret.** 2026. szeptember 28-án kértem, hogy a 3. alkalomtól nagyobbak legyenek a betűk a deckben, mert órán sokat kell nagyítanom. A mértéke nincs eldöntve. A deck fázisában javasolj, és kérdezz, mielőtt alkalmazod.
4. **A 2. beadandóra hivatkozás.** Leadták-e a journey-térképeket. Ha nem tudod, kérdezd meg. A helyi `data/store.json` csak másolat, abból ne vonj le következtetést.

## A munkarend röviden

A teljes menet az `ALKALOM-INDITO-PROMPT.md`-ben van. A sorrend kötött, minden fázis végén megállsz, és várod a jóváhagyásomat:

1. könyvek feldolgozása → `alkalom-3/forrasfeldolgozas-3-alkalom.md`
2. jegyzet-kutatás → `alkalom-3/jegyzet-kutatas-3-alkalom.md`
3. kidolgozott jegyzet → `alkalom-3/jegyzet-3-alkalom.md`
4. deck → `online-marketing-2026-evad-3-epizod.html` (a gyökérbe) (először vázlat, utána a teljes deck, Playwright-renderteszt 1440×900-on)
5. a feladat kitalálása (javaslat kérdésekkel, amíg nem döntök, nem építed)
6. a feladat megvalósítása (eszköz, segédlet, `app.html` `ep3`, `index.html` 3. sor élesítése, `.cpanel.yml` új `cp` sorok)
7. jegyzetek a deckbe
8. ellenőrzés
9. átadás: `munkadoksik/HOL-TARTUNK.md` és `alkalom-3/README.md` frissítése, deploy-prompt

A forrásfeldolgozás könyvszövege a `konyvek/` mappában van (gitignorálva, nem mehet ki a publikus repóba):
- `chaffey-ch7-online-customer-experience.txt` (Chaffey 6. kiadás, 7. fejezet)
- `chaffey-ch6-relationship-marketing.txt` (6. fejezet, e-CRM és e-mail; a fájl a 301. oldallal kezdődik, a fejezet nyitóoldala hiányzik)
- `kotler-ch5-long-term-loyalty.txt` (Kotler, Keller 14. kiadás, 5. fejezet; a fájl a 125. oldallal kezdődik, a fejezet eleje hiányzik)
- `chaffey-ch3-online-macro-environment.txt` (3. fejezet, jogi környezet)
- `chaffey-ch4-digital-marketing-strategy.txt` (4. fejezet, benne az OVP)

Ha olyan fejezet kell, ami nincs meg, kérd el tőlem, pontosan megnevezve. Ellenőrizetlen forrásból ne dolgozz.

## Hol ér véget a munkád

Ez a chat a helyi mentésig dolgozik. Commitot, pusht és más git-írást nem csinálsz; a `git status` és a `git log` olvasásra használható. A deploy egy külön Claude Code sessionben fut: az commitol és pushol, a fájlok tartalmához nem nyúl. A szerveren a cPanel cron negyedóránként fut (a 14., 29., 44. és 59. percben), húz a repóból, és a `.cpanel.yml` szerint másol.

A mentés szabálya:
- A kész fájlt külön kérés nélkül a mappába írod, a régi helyére, ugyanazzal a névvel, emelt verziószámmal.
- Mentés után md5-tel ellenőrzöd, hogy a gépen lévő fájl azonos azzal, amit írtál, és ezt kiírod.
- Az `app.html`, `index.html` és `api.php` mind a hét alkalmat kiszolgálja: mindig a mappában lévő friss állapotukból módosítod.
- A `munkadoksik/HOL-TARTUNK.md`-t más chat is írhatja: mindig a gépen lévő friss példányt olvasod be, és csak a változó sort cseréled, soha nem írod felül az egészet.
- Soha nem nyúlsz ezekhez, és nem kerülhetnek gitbe: `neptun.php`, `key.php`, `data/`, `BCKP/`, `.DS_Store`, `.claude/`, `konyvek/`. Neptun-kód nem kerülhet a chatbe.

Átadáskor deploy-promptot írsz a Claude Code sessionnek: fájlnevek, verziók, új `cp` sorok, rövid magyar commit-üzenet. Az `alkalom-N/` és `munkadoksik/` alatti fájlok nem kapnak `cp` sort, ezt a deploy-promptban is írd meg, hogy a Claude Code ne álljon meg miattuk. Új fájlnál megírod, van-e rá `cp` sor, és hivatkozik-e rá az index.

## Hogyan dolgozz velem

- A mondataimat tilos átfogalmazni, rövidíteni, átkeretezni vagy „javítani”. Ha egy gondolatot adok, aszerint dolgozol. Javasolni szabad, de előbb kérdezel. Ha valami nyelvtanilag sántít, kérdezel, nem cserélsz.
- A szövegmódosításaimat diaszámmal és az eredeti szöveggel adom; pontosan azt cseréled.
- Egy kérdőjellel végződő mondatom információkérés: válaszolsz, de nem kezdesz bele a feladatba, amíg nem kérem.
- Tényt csak forrással írsz, és jelölöd, honnan van. A saját következtetésedet külön jelölöd. Amit nem tudsz vagy nem találsz, azt kimondod. Nem kombinálsz forrásokat egy állításba.
- Oldalszámra csak akkor hivatkozol, ha a szöveg megvan és ellenőrizhető. Másodkézből vett oldalszám nem kerül se a doksiba, se a deckbe.
- Ha nem értesz egyet, kimondod, és megírod, hol sántít a felvetésem. Ez nem jogosít fel arra, hogy magadtól átírd.
- Velem tömören, bevezető nélkül beszélsz, a kérdésemet nem ismétled vissza.
- Nyelv: magyarul, AI-mentes szöveggel. A mondatokban nincs gondolatjel. „Jelenleg”, nem „ma azonban”. Felsorolás csak akkor, ha tényleg lista. Dátum mindig így: 2026. október 12. Összefoglalónál a cím „Összefoglaló”. A hallgatóknak szóló szöveg tegező.
- Szóhasználat: mindenhol „alkalom”; az „évad” és „epizód” csak analógiaként a keretező diákon. A hallgatói munka neve „beadandó”, a gomb maradhat „Leadás”. „Csapatmunka-szavazás”. A diák kiscímén nincs „N. epizód” előtag. A fejléc-csík sárgája az aktuális szakaszt követi.
- A csapatkódos beküldésvédelem és a deck Neptun nélküli elérhetősége el van halasztva, nem nyúlsz hozzájuk, amíg nem kérem.

## Az első lépésed

1. Kérj hozzáférést a mappához. Ha a gépemhez kötő eszközök nincsenek meg, szólj, és a desktop appban a „+” menü „Add folder” pontjával adom hozzá. A shellben a mappa jellemzően `$HOME/mnt/Egyetem` alatt látszik; mondd meg, hol találtad.
2. Olvasd el a fenti listát, és nézd meg a mappa állapotát (`git log -5`, `git --no-optional-locks status`, hogy ne maradjon zárolófájl, verziók, `ep3` az appban, a 3. sor az indexen, `cp` sorok).
3. Egy bekezdésben írd le, hol tartunk, mi van meg, mi hiányzik, és mi az első lépés. Az e-mail-feliratkozás kérdését (Nyitott kérdések 1.) tedd fel rögtön. Utána állj meg.
