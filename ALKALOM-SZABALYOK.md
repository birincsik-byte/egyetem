# Új alkalom készítése · szabályok az 1. alkalom mintájára

Ez a doksi annak szól, aki a következő alkalom (epizód) anyagát készíti, akár a claude.ai chatben, akár Claude Code-ban, bármelyik modellel. Az 1. alkalom (`online-marketing-2026-evad-1-epizod.html`) a minta: szerkezet, hangnem, jegyzetek, forrásjelölés. Az itt leírtak a tulajdonos döntései, nem javaslatok.

## Összefoglaló

A félév hét alkalom, hét kérdés, egy döntési lánc. Minden alkalom kérdése, kulcsgondolata és tanulsága a tulajdonos szövege (a gondolati ív doksiban), és változatlanul kerül a deckbe. A szakirodalom a mondatai mögé kerül forrásként, nem helyettük. A hallgatók ügynökségként dolgoznak egy valós márkán, minden alkalom végén egy beadandóval, amire a többiek csillaggal és indoklással szavaznak.

## Kiindulás, minden alkalomnál

1. A gondolati ív doksija: az adott epizód kérdése, „miről szól", kulcsgondolat, tanulság. Ezek a tulajdonos mondatai, szó szerint mennek a deckbe.
2. A forrásfeldolgozás doksija (`forrasfeldolgozas-online-marketing-2026.md`): az adott epizódhoz melyik könyv melyik fejezete. Ha új könyv jön, ugyanebbe a formába kell feldolgozni.
3. Az 1. alkalom deckje mint minta: ugyanaz a HTML-váz, ugyanaz a CSS, ugyanazok a billentyűk és gombok.
4. Az app (`app.html`) és az index (`index.html`) aktuális állapota a repóból.

## Sorrend

Először a könyvek feldolgozása: egy forrásdoksi, amiben minden könyvnél ott van, melyik fejezet mit ad az alkalom kérdéséhez, és külön szakaszban, hogy a tulajdonos mondatai (kulcsgondolat, tanulság) melyik szerzőnél hogyan jelennek meg. Ezt a tulajdonos átnézi. Csak utána a deck. A kettőt nem szabad összevonni.

## A deck szerkezete

Visszamutatás a láncra és az előző alkalom beadandójára. Az alkalom címlapja (a hivatalos tematikai pont idézve). A nap ritmusa, négy blokk. Az epizód hármas diája: miről szól, kulcsgondolat, tanulság. Elméleti diák a forrásokkal, kettő és hat között, minden dián a forrás könyvcímmel és fejezettel. Summázás. A beadandó feladata, majd a „mi keletkezik" dia a nyolc blokkal (fejléc; amit néztünk; a márka; a célcsoport; a lényeg egy mondatban; bizonyíték; ítélet; ami hiányzik), terjedelem legfeljebb egy A4 oldal, a beküldés az app Leadás gombjával. A bizonyíték mindig külön blokk, mert az az érv: miből gondolják. A blokkok tartalma alkalmanként a beadandó témájához igazodik, de a szerkezet (források, tartalom, mondat, bizonyíték, ítélet, ami hiányzik) marad. Csapatmunka-szavazás dia a három szemponttal és az eredmény linkjével. Zárás: a tanulság, és a következő alkalom kérdése cliffhangerként.

## Jegyzetek

Minden diához tartozik jegyzet (N billentyű): cím, „Forrás:" sor, és egy lapnyi hallgatói jegyzet, tegezve, a diára nem férő háttérrel, példákkal. A forrás könyvcím és fejezet, oldalszám nélkül; ha a tulajdonos anyaga a forrás, akkor „oktató". Ha a szöveg a készítő saját következtetése, azt a jegyzetben jelölni kell: „az oktató következtetése". A tulajdonosnak szóló megjegyzés a jegyzetben nem maradhat, mert a hallgatók is látják.

## Nyelv és megfogalmazás

Magyarul, tegezve. Nincs gondolatjel a mondatokban. A deckben az „epizód" szó, a hallgatói felületen (app, index) az „alkalom". A szavazós kör neve „csapatmunka-szavazás". A pozicionálás három helye a tulajdonos szavaival: kinek szól, mi helyett választják, mi az értékajánlata. A diák kiscímén nincs „N. epizód" előtag. A tulajdonos mondatait nem szabad átfogalmazni, rövidíteni vagy „javítani"; ha valami nyelvtanilag sántít, kérdezni kell, nem cserélni.

## Technikai szabályok

A fejléc-csík sárgája az aktuális szakaszt követi: a keretező diákon „Évad", az alkalom diáin az alkalom száma (`data-sec` és `EP1_START` mintájára). A verziószám a deck bal alsó segédsorában, az app és az index lábjegyzetében; minden átadott fájlnál emelni kell. A deck nem használ külső függőséget a Google Fonts betűtípusokon kívül. A szófelhő és a javító mód (J) csak a böngészőben tárol.

## Ami egy új alkalommal együtt jár

Egy commitban: az új deck fájl (`online-marketing-2026-evad-N-epizod.html`), az `app.html` `EPISODES` listájában az `epN` bejegyzés a beadandó mezőivel (az `f3` mindig kötelező, ez a beadandó egymondatos lényege, ezt mutatja a szavazólista; a többi mező kulcsa `f1`, `f2`, `f4`–`f8`, a sorrendet a `fields` lista adja), az `index.html`-ben az alkalom sorának élesítése (az `off` osztály törlése, linkek), és a `.cpanel.yml`-ben egy új `cp` sor. Ha bármelyik hiányzik, a deploy vagy nem viszi fel, vagy a hallgató nem találja.

## A beadandók sorrendje

1. Pozicionálási mondat visszafejtve. 2. Journey-térkép. 3. Landing page-audit és e-mail-folyamat. 4. Csatornaterv üzenetenként. 5. POEM-terv és keretfelosztás. 6. Mérési terv és hibakeresés. 7. Brief és pitch. Hat alkalom dekonstrukció a valós márkán, a hetedik konstrukció.
