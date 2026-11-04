# Átadás a chatnek · AI a marketingben

Ebben a mappában néha közvetlenül a fájlokban írjuk át a szöveget, nem a claude.ai chatben. Ez a doksi gyűjti ezeket a kézi módosításokat, dátumozott szakaszokban, a legfrissebb elöl.

**Ha az `AI-MARKETING/` bármelyik fájljából teljes új változat készül a chatben, előbb ezt a listát kell beépíteni**, különben a következő fájlátadás némán visszaírja a régi szöveget.

A doksi munkadoksi: nem kap `cp` sort a `.cpanel.yml`-ben, nem megy ki a webre.

---

## 2026. november 4.

Érintett fájlok: `AI-MARKETING/index.html` (v1.2) és a hat diasor, `AI-MARKETING/ai-marketing-2026-alkalom-1..6.html` (v1.1). Minden szövegnek a magyar és az angol változata is módosult.

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

### Verziószámok

`index.html` v1.2 és `ai-marketing-2026-alkalom-1.html` v1.2 · 2026. november 4. (angolul 4 November 2026), a 2–6. diasor v1.1 · 2026. november 4.

---

## Korábbi kézi módosítás, ami szintén érvényben van

A kezdőlap alcíme a főcím alatt kézzel került be, nem a chatből: **„Mi lenne, ha a Coca-Cola autómárka lenne.”** Ez maradjon a helyén, és ne kerüljön feljebb, a belépő doboz „Belépés” címe alá semmiképp.
