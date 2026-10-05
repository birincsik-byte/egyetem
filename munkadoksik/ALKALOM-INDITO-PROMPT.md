# Induló prompt egy új alkalomhoz · Online marketing 2026

Új chat az „Egyetem tanítás” Projectben, ez az első üzenet. A szögletes zárójeles részeket töltsd ki. Utolsó frissítés: 2026. szeptember 24.

---

Az Online marketing 2026 kurzus [N]. alkalmát készítjük. Dátum: [2026. október 12.]. Cím a gondolati ív szerint: [„A saját terep”]. A beadandó a sorrend szerint: [landing page-audit és e-mail-folyamat]. Az előző beadandó: [már leadták / még nem adták le].

## Indulás

1. Add hozzá a projektmappát: `/Users/birincsik/Claude/Projects/Egyetem` (device_request_folder_access). Ha nem megy, szólj, és a „+” menü „Add folder” pontjával én adom hozzá. Mappa nélkül nem kezdünk.
2. Olvasd el a Projectből, az `online-marketing-2026/` alól: `HOL-TARTUNK.md` (az aktuális állapot és minden eddigi döntés), `ALKALOM-SZABALYOK.md` (a tartalom és a nyelv szabályai), `CLAUDE.md` (a deploy és a Claude Code szabályai), `gondolati-iv-7-epizod.md` (az alkalom kérdése, miről szól, kulcsgondolata, tanulsága: az én mondataim, szó szerint mennek a deckbe), `forrasfeldolgozas-online-marketing-2026.md` (melyik könyv melyik fejezete tartozik ide). Szerkezeti mintának nézd meg az előző alkalom `forrasfeldolgozas-[N-1]-alkalom.md` és `jegyzet-kutatas-[N-1]-alkalom.md` doksiját.
3. Nézd meg a mappában: az előző alkalom deckjét (`online-marketing-2026-evad-[N-1]-epizod.html`, ez a legfrissebb dizájnváz), az `app.html`, `index.html`, `.cpanel.yml` aktuális állapotát, és az előző alkalom beadandó-eszközét és segédletét (2. alkalom: `journey-terkep.html`, `journey-tippek.html`). A verziószámokat a fájlokból és az élő oldal lábjegyzetéből vedd, ne a doksiból.
4. Egy mondatban írd le, hol tartunk, és mi az első lépés. Utána kezdd az 1. fázist.

## Amit tudnod kell az induláskor

**A könyvfejezetek már ki vannak nyerve**, szövegként, két helyen:

- a projektmappában, `/Users/birincsik/Claude/Projects/Egyetem/konyvek/` alatt. Ez a teljes fejezetszöveg, ezt olvasd, amikor szó szerint idézel vagy oldalszámot ellenőrzöl. A `konyvek/` mappa a `.gitignore`-ban van, tehát nem kerül fel a publikus repóba.
- a Project `konyvek/` mappájában ugyanezek, plusz két feldolgozott jegyzet: `kotler-ch17-480-481-valaszhierarchia.md` (a négy klasszikus válaszhierarchia-modell) és `kotler-5A-eredet.md` (az 5A a Marketing 4.0 5. fejezetéből való, nem a Marketing 5.0-ból).

Jelenleg megvan: Kotler 5. fejezet (hosszú távú lojalitás; a fájl a 125. oldallal kezdődik, a fejezet eleje hiányzik), Kotler 6. fejezet (fogyasztói piacok, vásárlási döntés), Chaffey 1. (bevezetés, RACE), 2. (customer journey, personák), 3. (macroenvironment, jogi környezet és adatvédelem; a GDPR szó nincs benne, mert a 6. kiadás 2016-os, a Data Protection Act és az EU Data Protection Directive szerepel), 4. (stratégia, OVP), 6. (relationship marketing, e-mail; a fájl a 301. oldallal kezdődik, a fejezet nyitóoldala hiányzik), 7. (online customer experience).

Nem kell PDF-et keresned. **Ha az alkalomhoz olyan könyv vagy fejezet kell, ami nincs ott, kérd el tőlem**, és mondd meg pontosan, melyik könyv melyik fejezete kell és mire. Csatolom, vagy megmondom, hol van. Én is adhatok hozzá új könyvet menet közben; ilyenkor szólok, és ugyanide kerül a szövege. Ellenőrizetlen forrásból ne dolgozz, inkább kérj.

**Ha az előző beadandót még nem adták le** (a 3. alkalom készítésekor a 2. alkalom 2026. szeptember 28-án lesz), a deck visszamutatása nem hivatkozhat valós hallgatói munkára. Ilyenkor a feladatra mutat vissza, nem az eredményére. Ha bizonytalan vagy, kérdezz.

## Mi hol van

**A gépemen:** `/Users/birincsik/Claude/Projects/Egyetem`. Ez a helyi git-klón. Ide kerül minden élesbe menő fájl, és ide kerül a munkadoksik másolata is. Kézi fájlmozgatás nincs: a chat közvetlenül ide ír. A `konyvek/` almappában a kinyert könyvfejezetek teljes szövege, gitignorálva.

**A Projectben (claude.ai), `online-marketing-2026/`:** a munkadoksik, amiket minden új chat lát: `HOL-TARTUNK.md`, `ALKALOM-SZABALYOK.md`, `ALKALOM-INDITO-PROMPT.md` (ez a doksi), `CLAUDE.md`, `gondolati-iv-7-epizod.md`, `forrasfeldolgozas-online-marketing-2026.md`, alkalmanként `forrasfeldolgozas-[N]-alkalom.md`, `jegyzet-kutatas-[N]-alkalom.md` és `jegyzet-[N]-alkalom.md`. A könyvfejezetek szövegként a `konyvek/` alatt.

**Élesbe menő fájlok (a mappa gyökerében):**
- `index.html`: gyűjtőoldal a hét alkalommal, Neptun-kódos belépéssel
- `online-marketing-2026-evad-[N]-epizod.html`: az alkalom deckje (a fájlnévben az „epizod” marad, a szövegben mindenhol „alkalom”). Jobb alul lapozó és dianavigátor („Ugrás diára” lista), ezt a vázzal együtt örökli, újraépítésnél sem veszhet el
- `app.html`: ügynökségi app (csapat, leadás, szavazás, eredmény, oktatói panel), `?ep=ep[N]&v=csapat`
- `api.php`: a háttér, JSON-tár a `data/` mappában
- az alkalom beadandó-eszköze és segédlete, ha van (a 2. alkalomnál `journey-terkep.html`, `journey-tippek.html`)
- `.cpanel.yml`: a deploy listája; csak az kerül ki a webre, aminek itt `cp` sora van

**Soha nem kerül gitbe:** `neptun.php`, `key.php`, `data/`, `BCKP/`, `.DS_Store`, `.claude/`, `konyvek/`. Mind a `.gitignore`-ban van, abból nem veszünk ki semmit. A `konyvek/` azért, mert tankönyvszöveg, a repo pedig publikus. Neptun-kód nem kerül a chatbe és a memóriába.

**Háttéranyag, nem élesbe:** régi deckek és forrásfájlok a gépemen (például a v9 deck a `~/Downloads/10_Egyetem_oktatas/` alatt, aminek a szövege a Projectben is megvan `v9-deck-journey-blokk.md` néven). Nem kerül gitbe, nem kap `cp` sort, az index nem hivatkozik rá.

**Online:** élő oldal https://egyetem.bemind.dev/om2026nappali/ · repo `git@github.com:birincsik-byte/egyetem.git` (publikus) · a szerveroldali klón `/home2/egyetembemind/repos/egyetem`, innen másol a deploy a `public_html/om2026nappali/` mappába.

## A deploy menete

1. A chat a kész fájlt a projektmappába írja, a régi helyére, ugyanazzal a névvel, emelt verziószámmal. Mentés után md5-tel ellenőrzi, hogy a gépen lévő fájl egyezik azzal, amit írt.
2. Claude Code a mappában csak commitol és pushol, a fájlok tartalmához nem nyúl. Lépései: `git status`; ha új fájl jött, ellenőrzi, hogy van rá `cp` sor a `.cpanel.yml`-ben és hivatkozik rá az `index.html` (ha nincs, szól, és nem pushol); commit rövid magyar üzenettel; push a `main` ágra; kiírja a commit hasht és a fájlokat verzióval.
3. A szerveren a cPanel cron negyedóránként fut (perc mező `14-59/15`, vagyis a 14., 29., 44. és 59. percben), húz a repóból, és a `.cpanel.yml` sorai szerint másol. Push után legfeljebb negyed óra az élesedés.
4. Ellenőrzés: az élő oldalon a verziószám (deck bal alsó segédsora, app és index lábjegyzete). Ha nem frissül, a cPanel Cron Jobs oldalán kell megnézni, mert a cron a hibáit némán eldobja.
5. Tartaléklánc, ha a chat nincs a géphez kötve (például mobilról): a fájlok letöltve a `~/Downloads` mappába kerülnek, és Claude Code a „vidd fel a mai fájlokat” kérésre a `CLAUDE.md` szerint viszi a helyükre.

A munka végén adj deploy-promptot Claude Code-nak: a fájlnevek, a verziók, az új `cp` sorok, és a commit üzenete.

## Munkarend

Minden fázis végén állj meg, és várd a jóváhagyásomat. A sorrend kötött: először a téma feldolgozása (könyvek, jegyzet-kutatás; ehhez kérhetsz tőlem inputot, vagy kereshetsz a már megadott forrásokban), utána egy részletes, kidolgozott jegyzet, és csak utána a deck és a gyakorlat. A fázisokat nem vonjuk össze.

**1. Könyvek feldolgozása.** A könyvek a Project `konyvek/` mappájában vannak, vagy most csatolom őket: [lista]. Készíts `forrasfeldolgozas-[N]-alkalom.md` doksit: könyvenként melyik fejezet mit ad az alkalom kérdéséhez, és külön szakaszban, hogy a kulcsgondolatom és a tanulságom melyik szerzőnél hogyan jelenik meg. Szó szerinti idézet oldalszámmal, ahol van. Amit tényként írsz, jelöld a forrását, a saját következtetésedet külön jelöld. Ha nincs forrás egy állításra, írd le, hogy nincs.
Ha egy fejezet hiányzik, kérd el tőlem, és addig ne írd meg azt a részt. A végén „Nem találtam” lista és a nyitott kérdések. Mentés a Projectbe és a mappába.

**2. Jegyzet-kutatás.** A jóváhagyott forrásdoksiból és webes kutatásból `jegyzet-kutatas-[N]-alkalom.md`, diánként tervezve: mi kerülhet a bővebb jegyzetbe (háttér, példák, magyar vagy helyi példák, források linkkel). Ez még nem a jegyzet, hanem az alapanyaga.
Diánként forrásonként: Forrásanyag (szó szerinti idézet oldalszámmal vagy URL-lel, webes forrásnál dátummal, elsődleges vagy másodlagos jelöléssel), Mit tesz hozzá, Egyezés-ellenőrzés (ha egy tervezett állítás nem egyezik a forrással, kiemelve), Javaslat a terembe (nem forrás). Az elején „Amit a kutatás mutat” lista a döntést igénylő pontokkal, a végén „Nem találtam”. Az idézeteket és a számokat szúrópróbával ellenőrzöd a forrásszövegben. Mentés a Projectbe és a mappába.

**3. Kidolgozott jegyzet.** A jóváhagyott jegyzet-kutatásból részletes, kidolgozott jegyzet a `jegyzet-[N]-alkalom.md` doksiba, a tervezett diák sorrendjében. Diánként: cím, „Forrás:” sor (könyvcím és fejezet oldalszám nélkül, vagy „oktató”), és a teljes hallgatói jegyzet tegezve, háttérrel és példákkal, ahogy a hallgató olvasni fogja. A saját következtetés jelölve: „az oktató következtetése”. Ez a jegyzet a deck alapja: ebből lesz a diák szövege, és ez kerül a diák mögé jegyzetként. Mentés a Projectbe és a mappába.

**4. Deck.** A jóváhagyott kidolgozott jegyzetből készül az `online-marketing-2026-evad-[N]-epizod.html`: a diaszöveg a jegyzetből sűrített, a forrás és a kommentár nem kerül a diára, hanem a jegyzet „Forrás:” sorába. A dizájn és a szerkezet szabályai az `ALKALOM-SZABALYOK.md`-ben vannak, azokat kövesd. Először vázlat: diacímek egy-egy mondattal. Jóváhagyás után a teljes deck. Minden dián renderteszt (Playwright, 1440×900), túlcsordulás nincs. A szövegmódosításaimat diaszámmal és az eredeti szöveggel adom, te pontosan azt cseréled. Ha a deck szövege eltér a gondolati ívtől, jelzed.

**5. A feladat kitalálása.** Először javaslatot kérek, kérdésekkel. A csapatok végig az 1. alkalmon választott márkájukon dolgoznak, a feladat dekonstrukció: megfigyelnek és leírnak, nem kitalálnak. Javasolj két-három formát: mit néznek meg, milyen lépésekben, mi a bizonyíték, mi az ítélet, mi hiányzik. Kérdezz rá, hogy a 2. alkalom mintájára legyen-e interaktív eszköz, ami maga a leadás, és kell-e segédlet oldal. A feladat alkalomfüggő: a mezőit a feladattal együtt, erre az alkalomra szabva javaslod. Fix, ami végig ugyanaz: a csapatok és a márka, amit az 1. alkalmon választottak. Technikai kötöttség: az `f3` mindig kötelező, és a leadás egymondatos lényege, mert ezt mutatja a szavazólista. Amíg nem döntöttem, nem építed meg.

**6. A feladat megvalósítása.** A jóváhagyott feladatból egyszerre készül:
- az eszköz, ha kell (a `journey-terkep.html` mintájára: csapat és márka legördülő, a márka a csapat bejegyzéséből töltődik; minta betöltése és kivétele; mentés a böngészőben; beküldés az api-n az `ep[N]` Leadásba; figyelmeztetés, ha már van leadás; nyomtatható),
- a segédlet oldal, ha kell (a `journey-tippek.html` mintájára, élő linkekkel, a deckből és az eszközből elérhető),
- az `app.html` `EPISODES` listájában az `ep[N]` mezői (az `f3` kötelező, ez a leadás egymondatos lényege, ezt mutatja a szavazólista),
- az `index.html`-ben az alkalom sorának élesítése (az `off` osztály törlése, linkek),
- a `.cpanel.yml`-ben minden új fájlhoz egy `cp` sor.
Az `app.html`, `index.html` és `api.php` mind a hét alkalmat kiszolgálja, ezeket mindig a mappában lévő állapotukból módosítod. A deck feladat-diái pontosan azt írják le, amit az eszköz kér. Ha a cím vagy egy név változik, mindenhol átírod: deck, index, app, eszköz, segédlet. Helyi tesztnél a Python-szerveren a PHP nem fut: a belépés és a beküldés csak `php -S`-sel vagy az élő oldalon tesztelhető.

**7. Jegyzetek a deckbe.** Csak ha a diák véglegesek. A 3. fázis kidolgozott jegyzetét a végleges diákhoz igazítod (ha egy dia változott, a jegyzete követi), és beilleszted a deckbe. Minden diához: cím, „Forrás:” sor, egy lapnyi hallgatói jegyzet tegezve, háttérrel és példákkal. A saját következtetés jelölve: „az oktató következtetése”. Nekem szóló megjegyzés nem maradhat benne, mert a hallgatók is látják. Verzió emelése.

**8. Ellenőrzés.** Minden „Forrás:” sort és forrásállítást összevetsz a forrásdoksival, minden diát renderelsz, a linkeket végigkattintod. A beküldést az élő oldalon csak az én jóváhagyásommal teszteled, mert a valós adatba ír.

**9. Átadás.** Frissíted a `HOL-TARTUNK.md`-t, és megírod a deploy-promptot Claude Code-nak.

## Szabályok, mindvégig

- A mondataimat tilos átfogalmazni, rövidíteni, átkeretezni vagy „javítani”. Javasolni szabad, de előbb kérdezel. Ha valami nyelvtanilag vagy helyesírásilag sántít, kérdezel, nem cserélsz.
- Tényt csak forrással írsz. A saját következtetésedet jelölöd. Amit nem találsz, azt kimondod.
- Oldalszámra csak akkor hivatkozol, ha a szöveg megvan és ellenőrizhető. Másodkézből vett oldalszám nem kerül se a munkadoksiba, se a deckbe. Ha egy hivatkozást nem tudsz ellenőrizni, megkeresed az eredeti forrást, vagy kihagyod, és szólsz.
- Magyarul, tegezve, AI-mentes szöveggel. Nincs gondolatjel a mondatokban. „Jelenleg”, nem „ma azonban”. Dátum: 2026. október 12. alakban. A többi nyelvi szabály az `ALKALOM-SZABALYOK.md`-ben van.
- Minden átadott fájlnál emeled a verziót, és külön kérés nélkül a gépemre mented, md5-tel ellenőrizve.
- A `HOL-TARTUNK.md`-t minden fázis végén frissíted, a gépen és a Projectben is: mi kész, mi van eldöntve (dátummal), mi nyitott.
- Commitot és pusht Claude Code csinál, a fájlok tartalmához ott nem nyúl.

Kezdd az Indulással.
