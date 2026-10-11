# Online marketing 2026 ősz · nappali · hol tartunk

Ez a doksi az induló állapot minden új chathez ebben a Projectben. Utolsó frissítés: 2026. október 5.

## Összefoglaló

A kurzus (VEGTKMB5, nappali, hét hétfői alkalom, alkalmanként négy 45 perces blokk) teljes digitális infrastruktúrája él. Az 1. alkalom (2026. szeptember 14.) és a 2. alkalom (2026. szeptember 28.) lement. A hallgatók ügynökségként dolgoznak egy valós magyar márkán, minden alkalom végén egy beadandóval, amire a többi csapat csillaggal és kötelező indoklással szavaz. Hét beadandó a jegy 70%-a. A soron következő munka a 3. alkalom, 2026. október 12., „A saját terep”, beadandó a landing page-audit és e-mail-folyamat.

## Hol dolgozunk

A projektmappa az oktató gépén: `/Users/birincsik/Claude/Projects/Egyetem`. Ez a helyi git-klón. **Minden új chat ezt a mappát adja hozzá az elején**, és a kész fájlokat egyenesen ide írja, nem a letöltésekbe.

A lánc: a chat ír a mappába, Claude Code commitol és pushol, a szerver cronnal húz. Kézi fájlmozgatás sehol nincs. Ha a chat nincs a géphez kötve (például mobilról), akkor marad a letöltéses tartaléklánc, ennek menete a `CLAUDE.md`-ben van.

A mappa rendje (2026. október 5.): a webre kerülő fájlok a gyökérben maradnak, a félév egészére vonatkozó munkadoksik (ez a doksi, `ALKALOM-SZABALYOK.md`, `ALKALOM-INDITO-PROMPT.md`, `gondolati-iv-7-epizod.md`, `forrasfeldolgozas-online-marketing-2026.md`, `findq.py`) a `munkadoksik/` alatt, az alkalmankénti munkadoksik az `alkalom-N/` alatt vannak, mindegyikben egy `README.md`-vel. A forrásjegyzetek és a v9 deck szövege a `konyvek/` alatt. Részletek a gyökérben lévő `UJ-FIOK-INDULAS.md`-ben.

Remote: `git@github.com:birincsik-byte/egyetem.git`, publikus.
Weboldal: https://egyetem.bemind.dev/om2026nappali/
A szerveroldali klón egy másik gépen: `/home2/egyetembemind/repos/egyetem`, innen másolja a deploy a `.cpanel.yml` szerinti fájlokat a `public_html/om2026nappali/` mappába.
Deploy: cPanel Git-klón és cron. A cron negyedóránként fut (a perc mezője `14-59/15`), tehát push után legfeljebb negyed óra az élesedés.

## Új alkalom indítása

Minden új alkalom új chatben indul, az `ALKALOM-INDITO-PROMPT.md` első üzenetként való bemásolásával (a szögletes zárójeles részeket kitöltve). A prompt írja le a menetet, a fájlok helyét és a deployt; a tartalom és a nyelv szabályai az `ALKALOM-SZABALYOK.md`-ben vannak. Mindkettő 2026. szeptember 24-én készült újra, és felülírja a korábbi, szeptember 13-i szabályokat.

A sorrend (oktatói döntés, 2026. szeptember 24.): először a téma feldolgozása (könyvek, `forrasfeldolgozas-[N]-alkalom.md`; jegyzet-kutatás, `jegyzet-kutatas-[N]-alkalom.md`), utána egy részletes, kidolgozott jegyzet (`jegyzet-[N]-alkalom.md`), és csak utána a deck és a gyakorlat. Minden lépés után az oktató jóváhagyása kell.

Az alkalom szerkezete fix (oktatói döntés, 2026. szeptember 24.): az első fele elmélet, a második fele gyakorlat, a deck logikusan építkezik. A beadandó feladatfüggő, mindig az adott alkalom előtt találjuk ki; a mezők alkalmanként mások, csak az `f3` (egymondatos lényeg) kötött. Fix végig: a csapatok és a márkáik.

## A fájlok

- `index.html` – gyűjtőoldal a hét alkalommal, Neptun-kódos beléptetéssel
- `alkalom-1/online-marketing-2026-evad-1-epizod.html` – az 1. alkalom deckje, 29 dia (2026. október 11. óta minden alkalom webes fájlja a saját `alkalom-N/` mappájában van, a `.cpanel.yml` onnan másol)
- `app.html` – ügynökségi app, öt nézet: csapat, leadás, szavazás, eredmény, oktatói panel (`?ep=ep1&v=csapat`)
- `api.php` – PHP háttér, JSON-tár a `data/` mappában, `flock` zárolással
- `neptun.php` és `key.php` – csak a mappában és a szerveren, a gitben nincsenek

Belépés: a hallgató a Neptun-kódjával lép be (18 kód a `neptun.php`-ben, nevek nélkül), az oktató az oktatói kulccsal. A jogosultságot HMAC-aláírt `omauth` süti tartja. Az oktatói fül csak akkor látszik, ha az `api.php?a=me` oktatót ad vissza.

## Verziószámok

2026. szeptember 28-án a projektmappából ellenőrizve, az `a54ca9e` commit állapotában (a mappa tiszta, minden fent van):

- `alkalom-1/online-marketing-2026-evad-1-epizod.html` · v1.7 · 2026. szeptember 13.
- `alkalom-2/online-marketing-2026-evad-2-epizod.html` · v1.32 · 2026. szeptember 27.
- `app.html` · v2.9 · 2026. szeptember 28. (commitolva: `d8bfa7e`)
- `index.html` · v1.6 · 2026. szeptember 24.
- `alkalom-2/journey-terkep.html` · v1.11 · 2026. szeptember 24.
- `alkalom-2/journey-tippek.html` · v1.1 · 2026. szeptember 24.

A hiteles forrás mindig a projektmappa és az élő oldal lábjegyzete, nem ez a doksi.

## A titkok állapota

A `.gitignore` jelenleg kizárja a `data/`, `key.php`, `neptun.php`, `.DS_Store`, `BCKP/`, `.claude/` és `konyvek/` elemeket (az utolsó kettő 2026. szeptember 24-én került be, commitra vár; a `konyvek/` tankönyvszöveg, ezért nem mehet a publikus repóba). A git történetében a `neptun.php`, a `key.php` és a `data/` soha nem szerepelt, tehát a Neptun-kódok nem szivárogtak ki a publikus repóba. Ezt a sort ne vedd ki a `.gitignore`-ból.

## A következő alkalom

2026. október 5.: a 3. alkalom munkája új Claude-fiókban folytatódik, a belépési pont a gyökérben az `UJ-FIOK-INDULAS.md`. A munkadoksik helye az `alkalom-3/`. Eldöntve 2026. október 5.: előbb az 1–3. fázis, utána a deck és a feladat; a deck alapmérete kb. 20%-kal nagyobb (1440 px-en kb. 23 px, semmi 18 px alatt); az e-mail-feliratkozás előre kiadása nem kell. Ugyanaznap eldöntve: a korábbi sessionből beemelt kulcsgondolat, tanulság és fázis-sor nem az oktatóé, elengedve; az új hármas a `forrasfeldolgozas-3-alkalom.md` v2 „3. alkalom” szakaszában; a beadandó a saját és egy külső márka oldalának elemzése javító javaslat nélkül, a külső oldalt a csapatok listából választják; a nap másfél óra elmélet és másfél óra csoportmunka; a mérésből a weboldal kulcseseményei és eszközei (cookie, hőtérkép) kerülnek elő, a mérési terv a 6. alkalomé. Webes kutatás: `alkalom-3/webkutatas-3-alkalom.md` v2. A 3. alkalom tematikája: `alkalom-3/tematika-3-alkalom.md` v6, benne a hármas B változata és a deck interaktív, wireframe-szerű layout-bemutatásának döntése, 2026. október 6.; példaoldalak: `alkalom-3/ux-peldaoldalak-3-alkalom.md` (2026. október 6., az oktató jóváhagyta: hangsúly a weboldalon és a landingen, mitől lesz jó; 0–M blokk a szelektálással, az L blokk kikerült). A v1 (2026. október 5.) (kilenc elméleti blokk másfél órában, a design system, a mikrointerakciók, az akadálymentesség és a UX-szövegírás csak a jegyzetbe). Chaffey 9. és 10. fejezete 2026. október 5-én bekerült (a teljes könyvből, `konyvek/`), a `findq.py` a 10. fejezet páratlan oldalainak futófejét is felismeri. A deck kattintható vázlata (v0.12, 30 dia, 2026. október 6.: egységes kártya- és címelrendezés; „Mi a UX, és mi a UI?” és „Ugyanaz az oldal kétszer” (forrás: `alkalom-3/ux-ui-hatar-3-alkalom.md`); nincs soronkénti felfedés, csak az interaktív elemek kattinthatók; új „Mi micsoda?” definíciós dia; az „Amit a hirdetés ígért” is átkerült a 4. alkalomhoz; a hirdetés és a landing relevanciájáról szóló dia és öt gyakorlat 2026. október 6-án az oktató kérésére átkerült a 4. alkalomhoz: `alkalom-4/hirdetes-landing-jatek.html`, `alkalom-4/README.md`; a 3. deckben az „Amit a hirdetés ígért” gyakorlat maradt, interaktív drótvázas diák, nagyobb betűméret; új aloldal: `oldal-anatomia.html` v0.3, a landing anatómiája, landingtípusok, layout-sablonok mikor melyiket, bizalom, oldaltípusok, szín; a deckből gomb nyitja új lapon; ennek is kell majd `cp` sor) a gyökérben: `online-marketing-2026-evad-3-epizod.html`, 2026. október 6.; még nincs `cp` sora, nem élesíthető, a jegyzetek helyén helykitöltő. A deckvázlat: `alkalom-3/deck-vazlat-3-alkalom.md` v1.0. A 2. fázis kész, átnézésre vár: `alkalom-3/jegyzet-kutatas-3-alkalom.md` v1 (a tematika kilenc blokkja szerint). Az 1. fázis (v3): `alkalom-3/forrasfeldolgozas-3-alkalom.md` (Chaffey 7., 6., 3., 4., Kotler 5. és 6./171., valamint három új könyv: Krug 2014, Weinschenk 2011, Yablonski 2024; ezek szövege a `konyvek/3ik alkalom/` alatt, idézetellenőrző `munkadoksik/findq_pdf.py`). A deckvázlat: `alkalom-3/deck-vazlat-3-alkalom.md` v0.3.

2026. október 11.: a 3. alkalom anyaga kész, deployra vár: `alkalom-3/online-marketing-2026-evad-3-epizod.html` v0.14, `alkalom-3/oldal-anatomia.html` v0.4, `alkalom-3/oldal-vizsgalat.html` v2.1 (a beadandó, nyolc szemüveg, szavazás nélkül), `app.html` v2.10 (`ep3`), `index.html` v1.7 (3. sor élő), `.cpanel.yml` (`cp` sorok mappával). Ugyanaznap minden alkalom webes fájlja a saját `alkalom-N/` mappájába került. A részletek: `alkalom-3/FOLYTATAS.md`.

2026. október 11. este: a 4–7. alkalom vázlata kész, jóváhagyásra: `munkadoksik/VAZLAT-4-7-ES-LEVELEZO.md` és `alkalom-N/vazlat-N-alkalom.md`. A GDPR a 6. alkalomba kerül (a tematikában a webanalitikával egy ponton van). Levelező: két alkalom (2026. október 16. és november 6., 14:30–19:00, A.2.A226), az 1–3. téma pénteken a nappali deckjeivel, a 4–7. november 6-án; témánként rövid órai gyakorlat, az alkalmak végén csapatmunka-szavazás, ugyanaz a márkalista. Saját oldal: om2026levelezo, a kezdőlap a `LEVELEZŐ/index.html`, az `app.html` (v2.12) a címből ismeri fel a levelezős oldalt és ott a rövid gyakorlatok mezőit mutatja; a `.cpanel.yml` mindkét mappába másol. A szerveren kézzel kell: `key.php` (egyelőre ugyanaz), `neptun.php` (a levelezős lista, Berti adja meg). A 3. alkalomnál „szemüveg” helyett „szempont” (2026. október 11., Berti kérése).

3. alkalom, „A saját terep”, 2026. október 12. A lánc kérdése: „Hol fogadjuk, amikor megérkezik hozzánk”. Beadandó a leadandók sorrendje szerint: landing page-audit és e-mail-folyamat. A feladat pontos formáját az alkalom előtt találjuk ki (lásd „Új alkalom indítása”).

A hivatalos tematikai pontok szó szerint, a gondolati ív doksiból:

> • Weboldal és UX/UI mint forgalomterelő felület, loyalty/regisztrációs logika
> • *(és a „Platformok és eszközök" pontból: automatizált email marketing)*
> • *(és a „Webanalitika és GDPR" pontból: a GDPR / jogi vonatkozások)*

Elengedve 2026. október 5-én, ezek nem az oktató mondatai, egy korábbi session emelte be őket; az érvényes hármas és tematika: `alkalom-3/FOLYTATAS.md`:

- Miről szól: weboldal, UX/UI, regisztrációs és loyalty logika, automatizált e-mail, adatkezelés.
- Kulcsgondolat: a forgalom nem eredmény, és a weboldal az egyetlen felület, ami tényleg a tiéd.
- Tanulság: a konverzió ritkán meggyőzés kérdése, sokkal inkább súrlódásé. Egy akadály elvétele többet hoz, mint egy újabb érv.

A fázis-táblázat sora (szintén elengedve): mit hoz magával „Bizalom és meggyőzés.”, mire vált „Akadályok megszűntetése, percepció kialakítás a márkáról.”, mit tesz hozzá a végcélhoz „A felelősség átkerül a másik emberről a saját felületünkre.”

Átvezetés a 2. alkalomból: a 2. deck zárása és az áramlási térkép dia („Hogyan érkeznek meg a weboldalra, és mi lesz belőle?”) már a 3. alkalom kérdésére mutat: hol fogadjuk, amikor megérkezik, mert a térkép Act / Do fázisában már a mi felületünkön jár. A források a lenti „Források a 3. alkalomhoz” szakaszban vannak.

A készítés sorrendje kötött, a jelenlegi menet a fenti „Új alkalom indítása” szakaszban van.

Egy alkalom ezeket érinti, egyszerre, egy commitban:

1. az új deck fájl (`alkalom-3/online-marketing-2026-evad-3-epizod.html`)
2. az `app.html`-ben az `EPISODES` objektum `ep3` bejegyzése a beadandó mezőivel (az `f3` mindig kötelező, ez a leadás egymondatos lényege, ezt mutatja a szavazólista és az eredmény oldal)
3. az `index.html`-ben a 3. alkalom sorának élesítése (az `off` osztály törlése, linkek)
4. a `.cpanel.yml`-ben új `cp` sor a deckre, és minden új fájlra (eszköz, segédlet), ha lesz

Az `app.html`, az `index.html` és az `api.php` mind a hét alkalmat kiszolgálja, tehát ezeket mindig a projektmappában lévő állapotukból kell módosítani.

## A 2. alkalom (lement, 2026. szeptember 28.)

2. alkalom, „Hogyan érjük el az embert és hogyan dönt?” (a gondolati ívben még „Hogyan dönt az ember”). A hivatalos tematikai pont szó szerint: „Elméleti keretrendszerek: user/decision journey, tölcsérmodell (See-Think-Do-Care, Kotler 5A)". Beadandó: a journey-térkép (`journey-terkep.html`), ami maga a leadás.

### Előkészítés és állapot, 2026. szeptember 23–28.

A 2. alkalom forrásdoksija elkészült: `forrasfeldolgozas-2-alkalom.md` (a Projectben és a projektmappában is). Az oktató átnézésére vár. A deckhez addig nem nyúlunk.

Eldöntve: a v9 26. diáján csak „A tölcsér nem a vásárló útja.” marad, utána a riportolvasat, végül az oktató tanulsága szó szerint (három lépcső a diák sorrendjéből, nem egy új mondatban). Az 5A forrása a Marketing 4.0, 5. fejezet („The New Customer Path”), a Marketing 5.0-ra nem hivatkozunk. Az STDC Kaushik két eredeti blogbejegyzéséből van feldolgozva. Nyitott még: a tölcsér két könyvbeli olvasatából mi kell, a v9-ből mely diák kerülnek át, a tölcsérszámolás helye, a 32. dia idézete, és hogy az AIDA, Rucker, 5A időrend legyen-e az elméleti gerinc.

A 2. alkalom fájljai a projektmappában vannak, commitra várnak: `online-marketing-2026-evad-2-epizod.html` v1.32 · 2026. szeptember 27. (30 dia, új áramlási térkép dia a csatornamix után: honnan jön, hová érkezik a weboldalon, mikro- és makrokonverzió, kilépés és visszahozás, szemléltető vastagsággal, a „Miről szól” szövege az oktató javításával, a címlap („Hogyan érjük el az embert és hogyan dönt?”) az első, utána a lánc-dia („Hogyan érjük el az embert.”, benne a korábbi nyitó dia), majd a „Múlt héten” dia; a fázis-táblázat dia („Mit tesz hozzá minden alkalom”) kikerült, a 2. és 3. dia szövege az oktató javításával, jobb alul lenyíló dianavigátor a számlálón, a megfigyelés négy lépése egymás mellett, a feladat szövege és a megfigyelés egy dián, a félreérthető 4 kártya és „A térkép kezelése” dia kikerült, utóbbi jegyzete a „Hogyan töltitek ki” diához került; a big shift négy dián mind a tizennégy gondolattal, See-Think-Do-Care csatornatérkép és Anna-demó, csatorna × fázis mátrix, Baptista STDC-sablonja), új fájl `journey-terkep.html` v1.11 (interaktív térkép: modellválasztás, fázisonként közönség, érzés, üzenet, KPI, csatorna-mátrix, lyuk; nyomtatható, és közvetlenül beküldi a nyolc blokkot az `ep2` Leadásba az api-n át; a böngészőben ment), `app.html` v2.9 · 2026. szeptember 28. (`ep2` nyolc mező, a Leadás nézet a térképre mutat; a beadandókban és az indoklásokban a linkek kattinthatók (az oktató `rich()` függvénye); a 2. alkalom beadandójában a fázisokat (f4) az eredmény ablakban és a szavazásnál táblázatként mutatja, fázisszínekkel és a jelölt lyukakkal, mert a szerver csak a nyolc szövegblokkot tárolja, a térkép nyers állapotát nem; a szavazásnál az indoklás alatt karakterszámláló (legalább 15), a hibaüzenet megnevezi a csapatot és kimondja, hogy írásjel nem kötelező; az Eredmény nézetben minden alkalomnál a csapat sorában „A teljes beadandó” gomb, ami az oldal fölött nyitja meg a leadást, „Új ablakban” gombbal is), `index.html` v1.6 (2. sor élesítve), `.cpanel.yml` (két új `cp` sor: 2. deck és journey-térkép). Eldöntve 2026. szeptember 24.: a 2. alkalomnál a journey-térkép maga a leadás. Az indexen egy link van („Leadás: journey-térkép”), az app Leadás nézete csak a beküldött szöveg javítására szolgál. A térképen az Ügynökség (csapat) és a Márka is legördülő lista, a márka a csapat bejegyzéséből töltődik, a márkalista a bejegyzett csapatok márkáiból áll. A feladat dekonstrukció: az 1. alkalmon választott márka útját írják le megfigyelés alapján, nem kitalálják. Eldöntve 2026. szeptember 24. délelőtt: az AIDA mindenhonnan kikerült. A See-Think-Do-Care az alap, az 5A és az öt lépcső választható, de indoklással (mit mutat meg jobban a márkánál). A deckben új diák: „Ugyanaz az út, más kérdés” (a három modell mint döntési/szándék folyamat modell, mire válaszol), fordítókulcs Annával három modellben, a három lyuk példával, a megfigyelés négy lépése, a térkép kezelése képernyőképpel (36 dia). Új fájl: `journey-tippek.html` v1.0, megfigyelési útmutató élő linkekkel, a térképről és a deckből elérhető, `.cpanel.yml` sora megvan. A „Mit mérnénk” sor marad, a hallgatók tippelnek (a mérés későbbi alkalom). A vevő és a használó szétválasztása kikerült a feladatból (csak az e10 elméleti diáján maradt). 2026. szeptember 24., az oktató szövegmódosításai után (deck v1.8, 36 dia): a deckben a kulcsgondolat „A figyelem több helyen van. A konverzió egy cél és folyamat is egyben.” (a gondolati ív doksija még a régit tartalmazza). A ROPO-dia kikerült. A tölcsérszámolás helyén tölcsér és STDC-körök ábra, a sorrend-dia kártyákra bontva, új dia: „Honnan tudjuk, melyik fázisban van?”. A bővebb jegyzetek a `jegyzet-kutatas-2-alkalom.md` alapján készülnek. A 2. alkalom címe az oktató döntése szerint (2026. szeptember 24.): „Hogyan érjük el az embert és hogyan dönt?”, a deckben, az indexen, az appban, a térképen és a tippek oldalon átírva; az 1. alkalom deckjében még a régi cím áll. A deck 34 diás: a STDC-sablon dia kikerült, a tölcsér és körök dia az Anna-példa után áll, a „Honnan tudjuk” dia összevonva a „Melyik körrel hol találkozol” diával. A térképen csak a See-Think-Do-Care (alap) és az 5A választható, az öt lépcső csak elméletként szerepel a deckben (oktatói döntés, 2026. szeptember 24.). Minden STDC-t érintő dián Kaushik színei (See kék, Think zöld, Do sárga, Care piros). A Sablon lap kikerült, a „mi keletkezik” dia a térkép szakaszait követi. Egy csapat egy böngészőben javasolt dolgozni (a térkép és a deck is kiírja); a beküldés figyelmeztet, ha már van leadás. A fejléc-csík diánként jelölve (`data-sec`): csak a lánc és a fázis-táblázat Évad, minden más 2.

## Források a 2. alkalomhoz

Minden forrás itt van a Projectben, egyik sem igényel mappa-hozzáférést.

- `konyvek/kotler-ch6-analyzing-consumer-markets.txt` – Kotler–Keller 14. kiadás, 6. fejezet, a vásárlási döntési folyamat
- `konyvek/chaffey-ch1-introducing-digital-marketing.txt` – Chaffey 6. kiadás, 1. fejezet, ebben a RACE
- `konyvek/chaffey-ch2-online-marketplace-customer-journeys.txt` – Chaffey 6. kiadás, 2. fejezet, customer journey és personák
- `gondolati-iv-7-epizod.md` – a gondolati ív teljes doksija, mind a hét alkalom
- `v9-deck-journey-blokk.md` – a „v9 deck" teljes szövege, diák és oktatói jegyzetek

A „v9 deck" a gondolati ív „Egy tény a már elkészült anyagról" szakaszában van meghatározva: a pivot előtti, 1. alkalomra készült deck („Élő műhely · 1. alkalom"), aminek a harmadik fázisa („Journey és tölcsér", a `ph:2` jelölésű diák) tartalmazza a vásárlói utat, a See-Think-Do-Care-t, a Kotler 5A-t, a ROPO-t és a tölcsérkritikát. Ez az anyag az epizódbeosztás szerint a 2. alkalomhoz tartozik. A szövege a `v9-deck-journey-blokk.md`-ben olvasható, az eredeti HTML az oktató gépén a `~/Downloads/10_Egyetem_oktatas/1-alkalom-hallgatoi-deck.html`. **Ez háttéranyag, nem a projekt fájlja**: nincs a gitben, nem kap `cp` sort, az `index.html` nem hivatkozik rá, és nem is kerül élesbe.

További ellenőrzött források: `konyvek/kotler-ch17-480-481-valaszhierarchia.md` (Kotler, Keller 480–481.) és `konyvek/kotler-5A-eredet.md` (Marketing 4.0, 5. fejezet). A Marketing 5.0 nincs meg, arra nem hivatkozunk. A 2026-os tematika ajánlott irodalma Chaffey 8. kiadás (2022), a feldolgozás a meglévő 6. kiadásból (2016) készült.

## Források a 3. alkalomhoz

A 3. alkalom (2026. október 12., „A saját terep”, beadandó: landing page-audit és e-mail-folyamat) fejezetei a `forrasfeldolgozas-online-marketing-2026.md` szerint, szövegként a Project `konyvek/` mappájában és a projektmappa `konyvek/` almappájában (2026. szeptember 24.):

- `konyvek/chaffey-ch7-online-customer-experience.txt` – Chaffey 6. kiadás, 7. fejezet
- `konyvek/chaffey-ch6-relationship-marketing.txt` – Chaffey 6. kiadás, 6. fejezet, e-CRM és e-mail. A fájl a 301. oldallal kezdődik, a fejezet nyitóoldala hiányzik.
- `konyvek/kotler-ch5-long-term-loyalty.txt` – Kotler–Keller 14. kiadás, 5. fejezet. A fájl a 125. oldallal kezdődik, a fejezet eleje hiányzik.
- `konyvek/chaffey-ch3-online-macro-environment.txt` – Chaffey 6. kiadás, 3. fejezet, jogi környezet és adatvédelem. A GDPR szó nincs benne (a kiadás 2016-os); a Data Protection Act és az EU Data Protection Directive szerepel.
- `konyvek/chaffey-ch4-digital-marketing-strategy.txt` – Chaffey 6. kiadás, 4. fejezet, ebben az OVP

## Ami el van halasztva

- A 6. alkalomhoz (mérés), az oktató döntése 2026. október 6.: a weboldal eseményei és mérőeszközei a 3. alkalomból ide kerülnek: esemény, oldalmegtekintés, elköteleződési idő, átkattintás, navigációs útvonal, mikro- és makrokonverzió, kulcsesemény (GA4), cookie, hőtérkép és munkamenet-felvétel (Microsoft Clarity-demó), mi látszik kívülről egy idegen oldalon. A források már megvannak: `alkalom-3/jegyzet-kutatas-3-alkalom.md` 8. blokk, `alkalom-3/webkutatas-3-alkalom.md` „Események, mérőeszközök, cookie és hozzájárulás” szakasz, Chaffey 10. fejezet (`konyvek/chaffey-ch10-evaluation-improvement.txt`, feldolgozva a `forrasfeldolgozas-3-alkalom.md`-ben).

- Csapatkódok a beadandók védelmére. Jelenleg bárki felülírhatja bármelyik csapat leadását, amíg az alkalom nincs lezárva; ezt ideiglenesen az oktatói zárolás kezeli. A csapatkódok a 2. alkalomnál jönnének.
- Saját vizsgakérdések kidolgozása. A jelenlegiek Nórától jött ötletek, nem véglegesek. A 2. alkalom után kerül elő.
- A deck közvetlen URL-lel Neptun-belépés nélkül is elérhető, a kapu csak az `index.html`-en van. Jelenleg csak a `noindex, nofollow` védi. Ha kell, szerveroldalon megoldható.
