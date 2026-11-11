# Átadás a chatnek · AI a marketingben

Ebben a mappában néha közvetlenül a fájlokban írjuk át a szöveget, nem a claude.ai chatben. Ez a doksi gyűjti ezeket a kézi módosításokat, dátumozott szakaszokban, a legfrissebb elöl.

**Ha az `ai-a-marketingben/` bármelyik fájljából teljes új változat készül a chatben, előbb ezt a listát kell beépíteni**, különben a következő fájlátadás némán visszaírja a régi szöveget.

A doksi munkadoksi: nem kap `cp` sort a `.cpanel.yml`-ben, nem megy ki a webre.

---

## A generátor a hiteles forrás (2026. november 4. óta)

A kezdőlap és a hat diasor a `forras/` mappában lévő generátorból készül: a szövegek a `content.py`-ban, a HTML és a CSS a `build.py`-ban van. **Minden további szövegmódosítás a `forras/`-ban készüljön**, és onnan generálódjanak a fájlok. Ha valaki mégis kézzel javít egy HTML-t, azt vissza kell vezetni a generátorba, különben a következő futtatás eltörli.

2026. november 4-én a generátor szinkronba került a kézzel szerkesztett fájlokkal: a kimenete bájtra megegyezik a kinn lévő hét HTML-lel.

**A `build.py`-t soha ne futtasd a helyén.** A saját mappája szülőjébe ír, vagyis egyenesen az `ai-a-marketingben/` mappába: ott futtatva felülírja mind a hét fájlt. Ellenőrzéshez másold a `forras/` mappát egy ideiglenes helyre, ott futtasd, és md5-tel vesd össze a kimenetet.

### A heti nyitás egyetlen szám

A `content.py` tetején:

```python
NYITVA = 1   # eddig az alkalomig kattinthatók a linkek a kezdőlapon és a felső sávban
```

Ebből származik a kezdőlap gombjainak és a felső sáv elemeinek állapota is: ami `<= NYITVA`, az élő link, ami fölötte van, az szürke `off`. A diasor saját eleme a sávban akkor is `on` marad, ha a száma nagyobb a `NYITVA`-nál. A következő alkalom megnyitása tehát: a szám átírása és egy futtatás (ideiglenes másolatban, utána a fájlok másolása a helyükre), nem kézi szerkesztés nyolc fájlban.

---

## 2026. november 11., este: promptok rögzített kimeneti formátummal

Oktatói kérés: minden prompt mondja meg, milyen formában kérje vissza az eredményt, hogy a hallgató tovább tudja vinni, és legyen világos, melyik korábbi eredménnyel megy tovább. A 2. diasor (v2.2, 24 dia):

- Az 5. dia („Minden eredmény egy dokumentumba kerül”) oktatói kérésre kikerült (v2.3, 23 dia); a generátorban az `s2_doc()` megvan, de az `S2_SLIDES` nem használja. Helyette minden kis feladatnál „Ehhez kell” lista: minden szükséges előzmény külön sor, saját sárga TIPP gombbal („Ha nincs meg”), ami saját felugró ablakot nyit (`<dialog>`) egy önálló, helyben használható prompttal, ami a hiányzó előzményt most rögtön elkészíti. Visszautalás nincs (oktatói kérés: elvesznének). Adatok: `S2_NEED`, `TIP_PROMPTS` a `content.py` végén. A régi `S2_TIPS` már nincs használatban. 2. diasor v2.5.
- A „Ma kis lépésekben haladunk” dia menete négy lépés: rövid elmélet, kis feladat, márkadokumentum, továbbviszed.
- Minden kis feladat diáján „Ehhez kell:” sor (mit másoljon be) és „Eredmény, a márkadokumentumodba:” sor. Minden prompt a végén rögzített, nagybetűs mezőkből álló blokkot kér vissza („Csak ezt a blokkot add vissza: …”), és a bemásolandó részt szögletes zárójellel jelöli ([2. feladat eredménye]). Az adatok a `content.py` végén: `_FMT`.

---

## 2026. november 11., este: a márka neve és logója marad

Oktatói döntés: a hallgatók a valódi márka nevével és logójával dolgoznak, csak az iparág új („Az IKEA marad IKEA, csak légitársaság lesz”). Ez órai játék, a kész anyagokat nem teszik közzé. A korábbi „saját név és logó, nem almárka” szabály ezzel megszűnt. Generátorban átvezetve:

- 1. diasor (v1.7): a „Mit csinálunk” dia kártyái (Megtartod · Áthelyezed · Elindítod) és alatta az órai játék szabálya; a Követelmények „Védjegyek” kártyája helyett „Órai játék”; a „Mi lenne, ha…” márkaválasztó alatti mondat; egy tipp („Erre épül a márkaplatform, az arculat és a kampány”).
- 2. diasor (v2.1, 23 dia): új 3. dia „Mi a feladat?” (Marad: név, logó, személyiség, értékek, vizuális kódok · Új: iparág, termék vagy szolgáltatás, célcsoport, ár, kampány); a névadás elmélete és a két névadó feladat kikerült, 9 kis feladat maradt; a promptok „[márka] mint [új kategória]” alakúak; a kitalált példa neve Twist helyett Rubik; az első tippdia „Mi marad, mi új”; „Mára elkészül: márkabrief (platform, personák)”. A kezdőlap „A feladat” gombja a 4. diára mutat. Kezdőlap v1.5.
- Még nincs átvezetve: a 3. alkalom logófeladata („3 logóirány… a kiinduló márka logóját ne másold”), a 3-6. alkalom többi szövege és a hallgatói feladatleírás (Claude-dokumentum). Ezeket a következő alkalmak előtt kell igazítani.

---

## 2026. november 11.

A változás a generátorban készült (`forras/content.py`, `forras/build.py`), nem kézzel; a hét HTML ebből lett újragenerálva.

- `NYITVA = 2`: a kezdőlapon és a felső sávban a 2. alkalom is kattintható.
- A 2. alkalom diasora (v2.0, 24 dia) kis feladatokra bontva, mert az 1. alkalmon a hallgatók nem nagyon értették a feladatot (oktatói visszajelzés). Szerkezet: címlap, „A mai nap” (11 kis feladat két blokkban, percekkel, a „Mára elkészül” sorral), utána témánként egy elméleti dia kitalált példával (Rubik-kocka mint cipőmárka, „Twist”), és minden kis feladatnál egy dia: mit csinálsz, eredmény, másolható promptjavaslat. Végén a 3 tippdia és a zárás. A sorrend a feladatleírás sorrendjét követi: név, márkaplatform, personák, opcionális árazás, plusz egy bemelegítés az elején és a márkabrief összerakása a végén.
- Az adatok a `content.py` végén: `S2_TASKS`, `S2_THEORY`, `S2_SLIDES`, `S2_BLOCKS`, `EXAMPLE`. A 2. alkalomnál a régi feladattáblázat és a régi promptdia nem jelenik meg (a `deck_slides` a 2. alkalomnál a `session2_slides()`-t használja).
- Verziók: 1. diasor v1.6, 2. diasor v2.0, a kezdőlap és a 3-6. diasor v1.4, mind 2026. november 11.
- A 2. diasor 2. diája új összefoglaló: mi volt a múlt heti feladat, és ki melyik márkát választotta 2026. november 5-én (`ROSTER`, `NOBRAND` a `content.py` végén). Oktatói döntés: a nevek teljes névvel kerülnek a fájlba és a repóba; Neptun-kód nem kerül bele. A diasor most 25 dia, a kezdőlap „A feladat” gombja a 3. diára („A mai nap”) mutat.
- A 3. dia („A mai nap”) oktatói kérésre nem sorolja fel a kis feladatokat: azt mondja el, hogy a mai témát kis feladatokra szedjük, és ezekből áll össze a márkabrief (név + pozicionálás + ígéret és értékek + személyiség és hangnem + célcsoport és persona + árazás = márkabrief), alatta a menet: rövid elmélet, kis feladat, eredmény.

---

## 2026. november 4.

Érintett fájlok: `ai-a-marketingben/index.html` (v1.2) és a hat diasor, `ai-a-marketingben/ai-marketing-2026-alkalom-1..6.html` (v1.1). Minden szövegnek a magyar és az angol változata is módosult.

### 1. Nincs óráról órára leadás

A hallgatók a félév alatt órán dolgoznak, részfeladatot nem adnak le, a végén mutatják be a decket.

- A feladatdiák alján és a záródiák címében a **„Leadandó:”** helyett **„Mára elkészül:”** áll. Angolul **„Deliverable:”** helyett **„Done by today:”**. Ugyanez a kezdőlap hat alkalom-kártyáján is.
- A záródiákról törölve: „A leadás helyét és határidejét az oktató adja meg.” (angolul „The instructor will tell you where and when to upload.”) — **az 1–5. alkalomból**. A 6. alkalomban szándékosan maradt, mert ott valós a végleges deck és a portfólió átadása.
- A feladattáblázatok „Részfeladat” és „Eredménytermék” oszlopa változatlan.

### 2. Az 1. alkalom Követelmények diája

A „Leadás” kártya helyén:

> **Munka és bemutató** · A félév alatt órán dolgozol, részleadás nincs. Az aláírás feltétele a december 10-i tenderprezentáció és a végleges deck.

Angolul:

> **Work and presentation** · You work in class through the semester; there are no interim submissions. The condition for the course signature is the pitch presentation on 10 December and the final deck.

### 3. Apró szövegjavítások, ahol még leadásra utalt a szöveg

| Hol | Régi | Új |
|---|---|---|
| 1. alkalom, Féléves terv részfeladat | „a deck öt blokkját és a leadandókat” | „a deck öt blokkját és az eredménytermékeket” |
| 1. alkalom, tipp (Egy mappa a félévre) | „ments bele mindent, amit leadsz” | „ments bele mindent, ami elkészül” |
| 1. alkalom, AI-használat kártya | „A leadott anyagban írd oda” | „A kész anyagban írd oda” |
| 3. alkalom, tipp | „A leadáshoz és a deckhez is ezek kellenek.” | „A deckhez ezek kellenek.” |
| 5. alkalom, tipp (Válogass) | „Nem kell minden leadandó a deckbe.” | „Nem kell minden eredménytermék a deckbe.” |

Angol párjaik: „the five blocks of the deck and the deliverables” → „the five blocks of the deck and the outputs”; „save everything you hand in” → „save everything you produce”; „In the material you hand in, note which tool” → „In the finished material, note which tool”; „You need them for submission and for the deck.” → „You need them for the deck.”; „Not every deliverable needs to be in the deck.” → „Not every output needs to be in the deck.”

A magyar „eredménytermék” angol párja mindenütt **output**, ez a feladattáblázat oszlopfejléce is („Sub-task · Output · Where it goes in the deck”). A „deliverable” szó nem szerepel többé a mappában.

### 4. Kezdőlap: egyszerre csak a soron következő alkalom nyitható

Jelenleg csak az 1. alkalom gombjai élnek. A 2–6. alkalom „Prezentáció” és „A feladat” gombja szürke és nem kattintható, és alkalomról alkalomra nyitjuk ki őket.

- A halott gombokon nincs `href` és nincs `data-href`; helyettük `class="off"` (a fő gombon `class="main off"`), `aria-disabled="true"`, a cél pedig `data-off="ai-marketing-2026-alkalom-N.html"` és `data-off-hash="#d2"` attribútumban van eltéve.
- Új CSS-sor közvetlenül a `.links a.main` szabály után:
  `.links a.off,.links a.main.off{background:transparent;border-color:var(--line);color:var(--soft);cursor:default}`
- A nyelvváltó JS csak az `a[data-href]` elemeket írja át, a halott gombokhoz nem nyúl.
- A diasorok fájljai URL-ről továbbra is elérhetők, csak a kezdőlapról nem lehet rájuk kattintani.

### 5. Új főcím

A kezdőlap `<h1>`-e és az 1. diasor „Mit csinálunk” diájának `<h2>`-je:

- magyarul: „Egy ismert márka, egy új kategória” → **„Marketing tender: valós márka egy elképzelt iparágban”**
- angolul: „A well-known brand, a new category” → **„Marketing pitch: a real brand in an imagined industry”** („pitch”, mert a deck neve is „pitch deck”, a 6. alkalom pedig „Pitch presentation”.)

Az 1. diasorban a cím alatti mondat („Például: mi lenne, ha a Coca-Cola autómárka lenne?”) változatlan.

### 6. Felső témasáv: csak a soron következő alkalom él

A diasorok tetején lévő `<nav class="strip">` sávban ugyanaz a logika, mint a kezdőlap gombjainál: most csak az 1. alkalom és a kezdőlap kattintható, a 2–6. alkalom szürke, és alkalomról alkalomra nyitjuk ki őket. Mind a hat diasorban.

- A letiltott sávelemeken nincs `href` és `data-href`; helyettük `class="off"`, `aria-disabled="true"`, a cél `data-off="ai-marketing-2026-alkalom-N.html"`.
- Az aktuális diasor saját eleme marad `class="on" aria-current="page"` és élő, az nem navigációs link.
- Új CSS-sorok közvetlenül a `.strip a.on` szabály után:
  `.strip a.off{opacity:.45;cursor:default}` és `.strip a.off b{color:var(--ink-soft)}`
- Az 1. diasor két `<div class="season">` blokkjában (a „Hat csütörtök, 8:00 és 12:00 között” dia magyar és angol változata) a 2–6. alkalomra mutató linkek **szándékosan élők maradtak**, oda nem nyúltunk.

### 7. A sáv nyitott magassága a tartalomhoz igazodik

A sáv korábban fix 64 pixelre nyílt ki, és a leghosszabb feliratoknál (2., 4., 5. alkalom) ez kevés volt: a `overflow:hidden` miatt a szám és a felirat alja levágódott. Most a magasságot a tartalom adja:

- `.strip{…height:auto;max-height:10px;…;transition:max-height .2s,box-shadow .2s}` — csukva továbbra is 10 pixeles csík
- `.strip:hover,.strip:focus-within{max-height:240px;…}` — nyitva annyi, amennyi a felirat, a 240 pixel csak felső korlát

Így keskenyebb ablakban és nagyobb böngésző-nagyítás mellett sem vág le semmit. Mind a hat diasorban.

### 8. A 8. dia kártyái nem kattinthatók

Az 1. diasor 8. diáján („Hat csütörtök, 8:00 és 12:00 között”) a hat kártya korábban linkelt a diasorokra. Berti kérésére ez megszűnt:

- a kártya `<a class="ep">` helyett `<div class="ep">`, `href` és `data-href` nélkül, a tartalma változatlan
- CSS: `.slide a.ep` → `.slide .ep`, `.slide a.ep.now` → `.slide .ep.now`, a `:hover` emelkedés törölve (ha nem kattintható, ne is viselkedjen úgy). A `.ep .n`, `.ep .d`, `.ep b`, `.ep .o` érintetlen.
- A dia alatti mondatból kimaradt az „Az alkalmakra kattintva megnyílik a saját diasoruk.” / „Click a session to open its own slides.” tagmondat, mert kattinthatatlan kártyák mellett valótlan lenne.
- A `.ep` CSS közös, ezért a 2–6. diasor stíluslapja is ezt kapta. Látható változás nincs bennük (nincs season kártyájuk), ezért a verziójuk nem emelkedett.

### Verziószámok

`ai-marketing-2026-alkalom-1.html` **v1.4**, `index.html` és a 2–6. diasor **v1.3** · 2026. november 4. (angolul 4 November 2026). A fájlonkénti eltérést a `content.py` `VER_KIVETEL` táblája kezeli.

---

## Korábbi kézi módosítás, ami szintén érvényben van

A kezdőlap alcíme a főcím alatt kézzel került be, nem a chatből: **„Mi lenne, ha a Coca-Cola autómárka lenne.”** Ez maradjon a helyén, és ne kerüljön feljebb, a belépő doboz „Belépés” címe alá semmiképp.
