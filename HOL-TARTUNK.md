# Online marketing 2026 ősz · nappali · hol tartunk

Ez a doksi az induló állapot minden új chathez ebben a Projectben. Utolsó frissítés: 2026. szeptember 23.

## Összefoglaló

A kurzus (VEGTKMB5, nappali, hét hétfői alkalom, alkalmanként négy 45 perces blokk) teljes digitális infrastruktúrája él. Az 1. alkalom kész és lement. A hallgatók ügynökségként dolgoznak egy valós magyar márkán, minden alkalom végén egy beadandóval, amire a többi csapat csillaggal és kötelező indoklással szavaz. Hét beadandó a jegy 70%-a. A soron következő munka a 2. alkalom, 2026. szeptember 28., „Hogyan dönt az ember", beadandó a journey-térkép.

## Hol dolgozunk

A projektmappa az oktató gépén: `/Users/birincsik/Claude/Projects/Egyetem`. Ez a helyi git-klón. **Minden új chat ezt a mappát adja hozzá az elején**, és a kész fájlokat egyenesen ide írja, nem a letöltésekbe.

A lánc: a chat ír a mappába, Claude Code commitol és pushol, a szerver cronnal húz. Kézi fájlmozgatás sehol nincs. Ha a chat nincs a géphez kötve (például mobilról), akkor marad a letöltéses tartaléklánc, ennek menete a `CLAUDE.md`-ben van.

Remote: `git@github.com:birincsik-byte/egyetem.git`, publikus.
Weboldal: https://egyetem.bemind.dev/om2026nappali/
A szerveroldali klón egy másik gépen: `/home2/egyetembemind/repos/egyetem`, innen másolja a deploy a `.cpanel.yml` szerinti fájlokat a `public_html/om2026nappali/` mappába.
Deploy: cPanel Git-klón és cron. A cron negyedóránként fut (a perc mezője `14-59/15`), tehát push után legfeljebb negyed óra az élesedés.

## A fájlok

- `index.html` – gyűjtőoldal a hét alkalommal, Neptun-kódos beléptetéssel
- `online-marketing-2026-evad-1-epizod.html` – az 1. alkalom deckje, 29 dia
- `app.html` – ügynökségi app, öt nézet: csapat, leadás, szavazás, eredmény, oktatói panel (`?ep=ep1&v=csapat`)
- `api.php` – PHP háttér, JSON-tár a `data/` mappában, `flock` zárolással
- `neptun.php` és `key.php` – csak a mappában és a szerveren, a gitben nincsenek

Belépés: a hallgató a Neptun-kódjával lép be (18 kód a `neptun.php`-ben, nevek nélkül), az oktató az oktatói kulccsal. A jogosultságot HMAC-aláírt `omauth` süti tartja. Az oktatói fül csak akkor látszik, ha az `api.php?a=me` oktatót ad vissza.

## Verziószámok

2026. szeptember 23-án közvetlenül a projektmappából és az élő oldalról ellenőrizve, a `09c286d` commit állapotában:

- `online-marketing-2026-evad-1-epizod.html` · v1.7 · 2026. szeptember 13.
- `app.html` · v1.8 · 2026. szeptember 14.
- `index.html` · v1.3 · 2026. szeptember 14.

A deck tehát v1.7, nem v1.8. A korábbi v1.8-as hivatkozás ebben a doksiban téves volt. A hiteles forrás mindig a projektmappa és az élő oldal lábjegyzete, nem ez a doksi.

## A titkok állapota

A `.gitignore` jelenleg kizárja a `data/`, `key.php`, `neptun.php`, `.DS_Store` és `BCKP/` elemeket. A git történetében a `neptun.php`, a `key.php` és a `data/` soha nem szerepelt, tehát a Neptun-kódok nem szivárogtak ki a publikus repóba. Ezt a sort ne vedd ki a `.gitignore`-ból.

## A következő alkalom

2. alkalom, „Hogyan dönt az ember", 2026. szeptember 28.

A hivatalos tematikai pont szó szerint: „Elméleti keretrendszerek: user/decision journey, tölcsérmodell (See-Think-Do-Care, Kotler 5A)".

Az oktató mondatai a gondolati ívből, ezek változatlanul mennek a deckbe:

- Miről szól: user journey, See-Think-Do-Care, Kotler 5A.
- Kulcsgondolat: az ember nem akkor vásárol, amikor te hirdetsz.
- Tanulság: a tölcsér nem riportsor, hanem tartalmi döntés arról, mit mondasz és mikor. A rossz üzenet legtöbbször jó üzenet rossz időben.

A készítés sorrendje kötött, az `ALKALOM-SZABALYOK.md`-ben van leírva: először a forrásfeldolgozás doksija az adott alkalomhoz, azt az oktató átnézi, és csak utána a deck. A kettőt nem szabad összevonni.

Egy alkalom négy dolgot érint, ezek egyszerre, egy commitban mennek:

1. az új deck fájl (`online-marketing-2026-evad-2-epizod.html`)
2. az `app.html`-ben az `EPISODES` objektum `ep2` bejegyzése a beadandó mezőivel (az `f3` mindig kötelező, ez a leadás egymondatos lényege, ezt mutatja a szavazólista)
3. az `index.html`-ben a 2. alkalom sorának élesítése (az `off` osztály törlése, linkek)
4. a `.cpanel.yml`-ben egy új `cp` sor

Az `app.html`, az `index.html` és az `api.php` mind a hét alkalmat kiszolgálja, tehát ezeket mindig a projektmappában lévő állapotukból kell módosítani.

### Állapot, 2026. szeptember 23.

A 2. alkalom forrásdoksija elkészült: `forrasfeldolgozas-2-alkalom.md` (a Projectben és a projektmappában is). Az oktató átnézésére vár. A deckhez addig nem nyúlunk.

Eldöntve: a v9 26. diáján csak „A tölcsér nem a vásárló útja.” marad, utána a riportolvasat, végül az oktató tanulsága szó szerint (három lépcső a diák sorrendjéből, nem egy új mondatban). Az 5A forrása a Marketing 4.0, 5. fejezet („The New Customer Path”), a Marketing 5.0-ra nem hivatkozunk. Az STDC Kaushik két eredeti blogbejegyzéséből van feldolgozva. Nyitott még: a tölcsér két könyvbeli olvasatából mi kell, a v9-ből mely diák kerülnek át, a tölcsérszámolás helye, a 32. dia idézete, és hogy az AIDA, Rucker, 5A időrend legyen-e az elméleti gerinc.

A 2. alkalom fájljai a projektmappában vannak, commitra várnak: `online-marketing-2026-evad-2-epizod.html` v1.15 · 2026. szeptember 24. (31 dia: a big shift négy dián mind a tizennégy gondolattal, See-Think-Do-Care csatornatérkép és Anna-demó, csatorna × fázis mátrix, Baptista STDC-sablonja), új fájl `journey-terkep.html` v1.10 (interaktív térkép: modellválasztás, fázisonként közönség, érzés, üzenet, KPI, csatorna-mátrix, lyuk; nyomtatható, és közvetlenül beküldi a nyolc blokkot az `ep2` Leadásba az api-n át; a böngészőben ment), `app.html` v2.3 (`ep2` nyolc mező, a Leadás nézet a térképre mutat), `index.html` v1.6 (2. sor élesítve), `.cpanel.yml` (két új `cp` sor: 2. deck és journey-térkép). Eldöntve 2026. szeptember 24.: a 2. alkalomnál a journey-térkép maga a leadás. Az indexen egy link van („Leadás: journey-térkép”), az app Leadás nézete csak a beküldött szöveg javítására szolgál. A térképen az Ügynökség (csapat) és a Márka is legördülő lista, a márka a csapat bejegyzéséből töltődik, a márkalista a bejegyzett csapatok márkáiból áll. A feladat dekonstrukció: az 1. alkalmon választott márka útját írják le megfigyelés alapján, nem kitalálják. Eldöntve 2026. szeptember 24. délelőtt: az AIDA mindenhonnan kikerült. A See-Think-Do-Care az alap, az 5A és az öt lépcső választható, de indoklással (mit mutat meg jobban a márkánál). A deckben új diák: „Ugyanaz az út, más kérdés” (a három modell mint döntési/szándék folyamat modell, mire válaszol), fordítókulcs Annával három modellben, a három lyuk példával, a megfigyelés négy lépése, a térkép kezelése képernyőképpel (36 dia). Új fájl: `journey-tippek.html` v1.0, megfigyelési útmutató élő linkekkel, a térképről és a deckből elérhető, `.cpanel.yml` sora megvan. A „Mit mérnénk” sor marad, a hallgatók tippelnek (a mérés későbbi alkalom). A vevő és a használó szétválasztása kikerült a feladatból (csak az e10 elméleti diáján maradt). 2026. szeptember 24., az oktató szövegmódosításai után (deck v1.8, 36 dia): a deckben a kulcsgondolat „A figyelem több helyen van. A konverzió egy cél és folyamat is egyben.” (a gondolati ív doksija még a régit tartalmazza). A ROPO-dia kikerült. A tölcsérszámolás helyén tölcsér és STDC-körök ábra, a sorrend-dia kártyákra bontva, új dia: „Honnan tudjuk, melyik fázisban van?”. A bővebb jegyzetek a `jegyzet-kutatas-2-alkalom.md` alapján készülnek. A 2. alkalom címe az oktató döntése szerint (2026. szeptember 24.): „Hogyan érjük el az embert és hogyan dönt?”, a deckben, az indexen, az appban, a térképen és a tippek oldalon átírva; az 1. alkalom deckjében még a régi cím áll. A deck 34 diás: a STDC-sablon dia kikerült, a tölcsér és körök dia az Anna-példa után áll, a „Honnan tudjuk” dia összevonva a „Melyik körrel hol találkozol” diával. Minden STDC-t érintő dián Kaushik színei (See kék, Think zöld, Do sárga, Care piros). A Sablon lap kikerült, a „mi keletkezik” dia a térkép szakaszait követi. Egy csapat egy böngészőben javasolt dolgozni (a térkép és a deck is kiírja); a beküldés figyelmeztet, ha már van leadás. A fejléc-csík diánként jelölve (`data-sec`): csak a lánc és a fázis-táblázat Évad, minden más 2.

## Források a 2. alkalomhoz

Minden forrás itt van a Projectben, egyik sem igényel mappa-hozzáférést.

- `konyvek/kotler-ch6-analyzing-consumer-markets.txt` – Kotler–Keller 14. kiadás, 6. fejezet, a vásárlási döntési folyamat
- `konyvek/chaffey-ch1-introducing-digital-marketing.txt` – Chaffey 6. kiadás, 1. fejezet, ebben a RACE
- `konyvek/chaffey-ch2-online-marketplace-customer-journeys.txt` – Chaffey 6. kiadás, 2. fejezet, customer journey és personák
- `gondolati-iv-7-epizod.md` – a gondolati ív teljes doksija, mind a hét alkalom
- `v9-deck-journey-blokk.md` – a „v9 deck" teljes szövege, diák és oktatói jegyzetek

A „v9 deck" a gondolati ív „Egy tény a már elkészült anyagról" szakaszában van meghatározva: a pivot előtti, 1. alkalomra készült deck („Élő műhely · 1. alkalom"), aminek a harmadik fázisa („Journey és tölcsér", a `ph:2` jelölésű diák) tartalmazza a vásárlói utat, a See-Think-Do-Care-t, a Kotler 5A-t, a ROPO-t és a tölcsérkritikát. Ez az anyag az epizódbeosztás szerint a 2. alkalomhoz tartozik. A szövege a `v9-deck-journey-blokk.md`-ben olvasható, az eredeti HTML az oktató gépén a `~/Downloads/10_Egyetem_oktatas/1-alkalom-hallgatoi-deck.html`. **Ez háttéranyag, nem a projekt fájlja**: nincs a gitben, nem kap `cp` sort, az `index.html` nem hivatkozik rá, és nem is kerül élesbe.

További ellenőrzött források: `konyvek/kotler-ch17-480-481-valaszhierarchia.md` (Kotler, Keller 480–481.) és `konyvek/kotler-5A-eredet.md` (Marketing 4.0, 5. fejezet). A Marketing 5.0 nincs meg, arra nem hivatkozunk. A 2026-os tematika ajánlott irodalma Chaffey 8. kiadás (2022), a feldolgozás a meglévő 6. kiadásból (2016) készült.

## Ami el van halasztva

- Csapatkódok a beadandók védelmére. Jelenleg bárki felülírhatja bármelyik csapat leadását, amíg az alkalom nincs lezárva; ezt ideiglenesen az oktatói zárolás kezeli. A csapatkódok a 2. alkalomnál jönnének.
- Saját vizsgakérdések kidolgozása. A jelenlegiek Nórától jött ötletek, nem véglegesek. A 2. alkalom után kerül elő.
- A deck közvetlen URL-lel Neptun-belépés nélkül is elérhető, a kapu csak az `index.html`-en van. Jelenleg csak a `noindex, nofollow` védi. Ha kell, szerveroldalon megoldható.
