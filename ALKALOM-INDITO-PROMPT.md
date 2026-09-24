# Induló prompt egy új alkalomhoz (Online marketing 2026)

Másold be egy új session első üzenetének. A szögletes zárójeles részeket töltsd ki.

---

Az Online marketing 2026 kurzus [N]. alkalmát készítjük. Dátum: [2026. október 12.]. Cím a gondolati ív szerint: [„A saját terep”]. A beadandó a sorrend szerint: [Landing page-audit és e-mail-folyamat].

**Mielőtt bármit csinálsz, olvasd el:**
1. A Project doksijait: `HOL-TARTUNK.md` (itt az aktuális állapot és minden eddigi döntés, ez felülírja a régebbi szabályokat), `ALKALOM-SZABALYOK.md`, `CLAUDE.md`, `gondolati-iv-7-epizod.md` (az adott alkalom kérdése, kulcsgondolata, tanulsága: az én mondataim, szó szerint mennek a deckbe), `forrasfeldolgozas-online-marketing-2026.md` (melyik könyv melyik fejezete tartozik ide).
2. A memóriában a projekt szabályait (`areas/online-marketing-alkalom-szabalyok.md`, `preferences.md`).
3. A gépemen a `/Users/birincsik/Claude/Projects/Egyetem/` mappát: az 1. és 2. alkalom deckje a design mintája, az `app.html`, `index.html`, `.cpanel.yml` aktuális állapota.

**Munkarend. Minden fázis végén állj meg, és várd a jóváhagyásomat.**

**1. Könyvek feldolgozása.** A könyvek a Project `konyvek/` mappájában vannak, vagy most csatolom őket: [lista]. Készíts `forrasfeldolgozas-[N]-alkalom.md` doksit: könyvenként melyik fejezet mit ad az alkalom kérdéséhez, és külön szakaszban, hogy a kulcsgondolatom és a tanulságom melyik szerzőnél hogyan jelenik meg. Szó szerinti idézet oldalszámmal, ahol van. Amit tényként írsz, jelöld a forrását, a saját következtetésedet külön jelöld. Ha nincs forrás egy állításra, írd le, hogy nincs.

**2. Jegyzet-kutatás.** A jóváhagyott forrásdoksiból és webes kutatásból `jegyzet-kutatas-[N]-alkalom.md`, diánként tervezve: mi kerülhet a bővebb jegyzetbe (háttér, példák, magyar vagy helyi példák, források linkkel). Ez még nem a jegyzet, hanem az alapanyaga.

**3. Deck.** `online-marketing-2026-evad-[N]-epizod.html`, pontosan ugyanabban a designban, mint az 1. és 2. alkalom: ugyanaz a HTML-váz, CSS, billentyűk (N jegyzet, F teljes képernyő, J javító mód), step-reveal, fejléc-csík `data-sec` jelöléssel. A 2. alkalom deckjét részekből építsd (head, css, extra_css, slides, notes, rev, script), úgy könnyebb iterálni. Szerkezet: visszamutatás a láncra és az előző beadandóra, címlap, a nap ritmusa, miről szól / kulcsgondolat / tanulság, elméleti diák forrással, végül egyben a beadandó elmesélése (minden elmélet előtte), csapatmunka-szavazás, zárás a következő alkalom kérdésével. A diákra forrássor és kommentár nem kerül, az a jegyzetbe megy. Minden dián renderteszt (Playwright, 1440×900), túlcsordulás nincs.

**4. A feladat kitalálása.** Először javaslatot kérek, kérdésekkel: mit dekonstruálnak a csapatok a saját márkájukon (megfigyelés, nem kitalálás), milyen felületen adják le, milyen segédlet kell hozzá. Amíg nem döntöttem, ne építsd meg.

**5. A feladat megvalósítása.** A jóváhagyott feladatból: az adatlap vagy eszköz (a `journey-terkep.html` mintájára: csapat és márka legördülő, minta betöltése és kivétele, localStorage mentés, beküldés az api-n az `ep[N]` Leadásba, felülírás-figyelmeztetés), segédlet oldal (a `journey-tippek.html` mintájára), az `app.html` `EPISODES` listájában az `ep[N]` mezői (az `f3` kötelező), az `index.html` sorának élesítése, és a `.cpanel.yml` új `cp` sorai. A deck feladat-diái pontosan azt írják le, amit az adatlap kér.

**6. Jegyzetek.** Csak ha a diák véglegesek. Minden diához: cím, „Forrás:” sor (könyvcím és fejezet, vagy „oktató”), egy lapnyi hallgatói jegyzet tegezve, a jegyzet-kutatásból. A saját következtetés jelölve „az oktató következtetése”. Nekem szóló megjegyzés nem maradhat benne, mert a hallgatók is látják. Utána illeszd a deckbe, és emeld a verziót.

**7. Ellenőrzés.** Minden forrásállítást vess össze a forrásdoksival, minden diát renderelj, a linkeket és a beküldést teszteld.

**Szabályok, mindvégig:**
- A mondataimat tilos átfogalmazni, rövidíteni, átkeretezni. Javasolni szabad, de előbb kérdezz. Helyesírási javítás megengedett, de jelezd.
- Magyarul, tegezve, AI-mentes szöveggel. Nincs gondolatjel a mondatokban. „Jelenleg”, nem „ma azonban”. Dátum: 2026. október 12. alakban. A hallgatói munka neve „beadandó”, a szavazásé „csapatmunka-szavazás”, mindenhol „alkalom”.
- Minden változtatás után emeld a verziót (deck: bal alsó segédsor, app és index: lábjegyzet), mentsd a fájlokat a gépemre a `/Users/birincsik/Claude/Projects/Egyetem/` mappába külön kérés nélkül, md5-tel ellenőrizve, és frissítsd a `HOL-TARTUNK.md`-t a gépen és a Projectben is.
- A `neptun.php`, `key.php`, `data/`, `BCKP/` soha nem kerülhet gitbe, a `.gitignore` nem módosítható, Neptun-kód nem kerülhet a chatbe vagy memóriába.
- Commitot és pusht Claude Code csinál, a fájlok tartalmához ott nem nyúl. A végén adj neki deploy-promptot a fájlnevekkel és verziókkal.

Kezdd az 1. fázissal.
