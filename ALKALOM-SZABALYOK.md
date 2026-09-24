# Alkalom-szabályok · Online marketing 2026 ősz

Ez a doksi a tartalom és a nyelv szabályait tartja: hogyan épül fel egy alkalom deckje, mi kerül a jegyzetbe, hogyan jelöljük a forrásokat, mit tartalmaz a beadandó. A folyamat, a fájlok helye és a deploy nem itt van, hanem az `ALKALOM-INDITO-PROMPT.md`-ben. Ha a kettő ellentmond, az indító prompt nyer, mert az készül minden alkalomnál újra.

Utolsó frissítés: 2026. szeptember 24. Ez a változat az 1. és a 2. alkalom tapasztalataiból íródott, és felülírja a korábbi, szeptember 13-i verziót.

## Összefoglaló

A félév hét alkalom, hét kérdés, egy döntési lánc. Minden alkalom kérdése, kulcsgondolata és tanulsága az oktató szövege a gondolati ív doksiból, és változatlanul kerül a deckbe. A szakirodalom a mondatai mögé kerül forrásként, nem helyettük. A hallgatók ügynökségként dolgoznak egy valós magyar márkán, minden alkalom végén egy beadandóval, amire a többiek csillaggal és kötelező indoklással szavaznak.

## A sorrend

Először a téma feldolgozása, utána egy részletes, kidolgozott jegyzet, és csak utána a deck és a gyakorlat. Ebben a sorrendben, és a fázisokat nem vonjuk össze. Minden lépést az oktató átnéz, mielőtt a következő indul.

Először a könyvek feldolgozása egy `forrasfeldolgozas-[N]-alkalom.md` doksiba: könyvenként melyik fejezet mit ad az alkalom kérdéséhez, szó szerinti idézettel, és külön szakaszban, hogy az oktató kulcsgondolata és tanulsága melyik szerzőnél hogyan jelenik meg.

Utána a jegyzet-kutatás egy `jegyzet-kutatas-[N]-alkalom.md` doksiba, diánként tervezve: mi kerülhet a bővebb jegyzetbe (háttér, példák, magyar vagy helyi példák, források linkkel). Ez még nem a jegyzet, hanem az alapanyaga. Ehhez lehet inputot kérni az oktatótól, vagy keresni a már megadott forrásokban.

Utána a kidolgozott jegyzet egy `jegyzet-[N]-alkalom.md` doksiba, a tervezett diák sorrendjében: diánként cím, „Forrás:” sor és a teljes hallgatói jegyzet. Ez a deck alapja: ebből lesz a diák szövege, és ez kerül a diák mögé jegyzetként.

Csak a jóváhagyott kidolgozott jegyzetből készül a deck, utána a gyakorlat.

## A deck szerkezete

Az alkalom szerkezete fix: az első fele elmélet, a második fele gyakorlat. A deck témától függően rugalmas, de logikusan vezetett: építkezik, valahonnan eljut valahová.

Az első fele: visszamutatás a láncra és az előző alkalom beadandójára (ha még nem adták le, akkor csak a feladatra és a láncra, konkrét eredmény nélkül). Címlap, benne a hivatalos tematikai pont szó szerint idézve. A nap ritmusa. Az alkalom hármasa: miről szól, kulcsgondolat, tanulság. Utána az elméleti diák.

A második fele: a beadandó elmesélése a lehető legkevesebb dián, ismétlés nélkül; minden elmélet előtte van. Csapatmunka-szavazás. Zárás: a tanulság, és a következő alkalom kérdése cliffhangerként.

A diák kiscímén nincs „N. epizód” előtag. Forrásmegjelölés nem kerül a diára, az a jegyzetbe való.

## A beadandó

Fix, ami a félév végéig ugyanaz: a csapatok (ügynökségek), és a márka, amit az 1. alkalmon választottak.

A feladat alkalomfüggő, és mindig az adott alkalom előtt találjuk ki: mit néznek meg, milyen felületen adják le, milyen mezőkből áll, kell-e hozzá eszköz és segédlet. A mezők ezért alkalmanként mások. Egy kötöttség van: az `f3` mindig kötelező, és a leadás egymondatos lényege, mert ezt mutatja a szavazólista.

A feladat mindvégig dekonstrukció: a csapatok megfigyelnek és leírnak, nem kitalálnak. A hetedik alkalom az egyetlen konstrukció.

## Jegyzetek

Minden diához tartozik jegyzet (N billentyű): cím, „Forrás:” sor, és egy lapnyi hallgatói jegyzet, tegezve, a diára nem férő háttérrel és példákkal.

A forrás könyvcím és fejezet, oldalszám nélkül. Ha az oktató anyaga a forrás, akkor csak annyi, hogy „oktató”. Ha a szöveg a készítő saját következtetése, azt jelölni kell: „az oktató következtetése”. Az oktatónak szóló megjegyzés nem maradhat a jegyzetben, mert a hallgatók is látják.

## Források

Tényt csak forrással írunk. A saját következtetést jelöljük. Amit nem találunk, azt kimondjuk.

Oldalszámra csak akkor hivatkozunk, ha a szöveg megvan és ellenőrizhető. Másodkézből vett oldalszám nem kerül se a munkadoksiba, se a deckbe. Ha egy hivatkozást nem lehet ellenőrizni, meg kell keresni az eredeti forrást, vagy ki kell hagyni.

A munkadoksikban (forrásfeldolgozás, jegyzet) az idézet mellé oldalszám vagy URL jár, webes forrásnál dátummal és azzal, hogy elsődleges vagy másodlagos. A deckbe ebből csak a könyvcím és a fejezet megy át.

## Nyelv és megfogalmazás

Magyarul, tegezve, AI-mentes szöveggel. Nincs gondolatjel a mondatokban. „Jelenleg”, nem „ma azonban”. Dátum: 2026. október 12. alakban.

A hallgatói munka neve mindenhol „beadandó”, a szavazós köré „csapatmunka-szavazás”. A hallgatói felületeken és a deck szövegében mindenhol „alkalom”. Az „évad” és az „epizód” csak analógiaként marad a keretező diákon; a deck fájlnevében az „epizod” szó marad, mert a név a deploy listához van kötve.

A pozicionálás három helye az oktató szavaival: kinek szól, mi helyett választják, mi az értékajánlata.

Az oktató mondatait tilos átfogalmazni, rövidíteni, átkeretezni vagy „javítani”. Javasolni szabad, de előbb kérdezni kell. Ha valami nyelvtanilag sántít, kérdezni kell, nem cserélni.

## Technikai szabályok

A deck dizájnja pontosan ugyanaz minden alkalomnál: ugyanaz a HTML-váz és CSS, Fraunces és Source Sans 3 betűtípus, papírháttér, kobalt kiemelés. Step-reveal. Fejléc-csík `data-sec` jelöléssel diánként: a keretező diákon „Évad”, az alkalom diáin az alkalom száma. Billentyűk: nyilak, szóköz, N jegyzet, J javító mód, F teljes képernyő. Jobb alul lapozó és dianavigátor („Ugrás diára” lista). Verziószám a bal alsó segédsorban.

Külső függőség csak a Google Fonts. A szófelhő és a javító mód csak a böngészőben tárol.

Az új deck az előző deckből épül, részekben (head, css, extra_css, slides, notes, rev, script), mert úgy könnyebb iterálni. Minden dián renderteszt 1440×900-on, túlcsordulás nincs.

Verziószám minden átadott fájlnál emelkedik: a deckben a bal alsó segédsorban, az appban és az indexben a lábjegyzetben.

## Ami egy új alkalommal együtt jár

Egy commitban megy ki:

1. az új deck fájl (`online-marketing-2026-evad-[N]-epizod.html`)
2. az alkalom beadandó-eszköze és segédlete, ha van (a 2. alkalomnál `journey-terkep.html` és `journey-tippek.html`)
3. az `app.html` `EPISODES` listájában az `ep[N]` bejegyzés a beadandó mezőivel; az `f3` mindig kötelező, ez a leadás egymondatos lényege, ezt mutatja a szavazólista
4. az `index.html`-ben az alkalom sorának élesítése (az `off` osztály törlése, linkek)
5. a `.cpanel.yml`-ben minden új fájlhoz egy `cp` sor

Ha bármelyik hiányzik, a deploy vagy nem viszi fel, vagy a hallgató nem találja. Az `app.html`, az `index.html` és az `api.php` mind a hét alkalmat kiszolgálja, ezeket mindig a projektmappában lévő állapotukból kell módosítani.

Ha egy cím vagy egy név változik, mindenhol át kell írni: deck, index, app, eszköz, segédlet.

Helyi tesztnél a Python-szerveren a PHP nem fut: a belépés és a beküldés csak `php -S`-sel vagy az élő oldalon tesztelhető. Az élő oldalon a beküldést csak az oktató jóváhagyásával szabad tesztelni, mert a valós adatba ír.

## A beadandók sorrendje

1. Pozicionálási mondat visszafejtve. 2. Journey-térkép. 3. Landing page-audit és e-mail-folyamat. 4. Csatornaterv üzenetenként. 5. POEM-terv és keretfelosztás. 6. Mérési terv és hibakeresés. 7. Brief és pitch.

Hat alkalom dekonstrukció a valós márkán, a hetedik konstrukció.