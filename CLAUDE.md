# Egyetem · Online marketing 2026 ősz · szabályok Claude Code-nak

Ez a mappa három tárgy weboldalának forrása, tárgyanként egy almappában: `nappali/`, `levelezo/`, `ai-a-marketingben/`. Ez a fejezet a nappali tárgyról szól, élesben: https://egyetem.bemind.dev/om2026nappali/
A szerver egy cPanel Git-klónból és cronból frissül; a deploy a `.cpanel.yml`-ben felsorolt fájlokat másolja a `public_html/om2026nappali/` mappába, semmi mást.

A cron ütemezése a cPanel → Cron Jobs alatt áll, ez az egyetlen hiteles forrás. Jelenleg negyedóránként fut, a perc mezője `14-59/15`, vagyis a 14., 29., 44. és 59. percben. A push után tehát legfeljebb negyed óra az élesedés. A cron parancsa a `>/dev/null 2>&1` miatt a hibáit is eldobja, ezért egy elakadt deploy némán marad el; ha nem frissül az oldal, a cPanel Cron Jobs oldalán kell ellenőrizni az ütemezést.

Ne állítsd át `*/5`-re. 2026. szeptember 13-án és 14-én háromszor is át lett állítva, és mindannyiszor visszaíródott `14-59/15`-re néhány órán belül; a felülírás a szolgáltató oldalán történik, nem itt. Amíg ez nem tisztázódik velük, a negyedóra a valóság.

## Hogyan érkezik ide változás

A tartalmi munka a claude.ai chatben készül. Ha a chat a géphez van kötve, a kész fájlt közvetlenül ebbe a mappába írja, a régi helyére, ugyanazzal a fájlnévvel. Ha nincs a géphez kötve, a fájl a `~/Downloads` mappába kerül, és innen te viszed a helyére (lásd lent). A fájlnevek rögzítettek:

- `nappali/index.html` – gyűjtőoldal, a hét alkalom
- `nappali/alkalom-1/online-marketing-2026-evad-1-epizod.html` – 1. alkalom deck (a többi alkalom hasonló néven, a saját `nappali/alkalom-N/` mappájában)
- `nappali/app.html` – ügynökségi app (csapat, leadás, szavazás, eredmény)
- `nappali/api.php` – az app háttere (a `levelezo/` és az `ai-a-marketingben/` mappában bájtra azonos másolata van)
- `.cpanel.yml` – deploy lista
- az alkalmak beadandó-eszközei és segédletei, ha vannak, az alkalom mappájában (a 2. alkalomnál `nappali/alkalom-2/journey-terkep.html`, `nappali/alkalom-2/journey-tippek.html`, a 3.-nál `nappali/alkalom-3/oldal-anatomia.html`, `nappali/alkalom-3/oldal-vizsgalat.html`)

A munkadoksik a `nappali/` mappában vannak, almappákban: a `nappali/munkadoksik/` alatt a félév egészére vonatkozók (`HOL-TARTUNK.md`, `ALKALOM-SZABALYOK.md`, `ALKALOM-INDITO-PROMPT.md`, `gondolati-iv-7-epizod.md`, `forrasfeldolgozas-online-marketing-2026.md`, `findq.py`), a `nappali/alkalom-N/` alatt az adott alkalom forrásfeldolgozása és jegyzetei, a `nappali/` gyökerében az `UJ-FIOK-INDULAS.md`. Ezek nem kapnak `cp` sort, nem mennek ki a webre; ha ilyen új fájl jelenik meg, az nem ok a push leállítására. 2026. október 11. óta az alkalmakhoz tartozó webes fájlok (deck, eszköz, segédlet) is az `alkalom-N/` mappában vannak; a `.cpanel.yml` `cp` sora a mappával együtt adja meg őket, a szerveren a gyökérbe kerülnek, a webcím nem változik. 2026. november 9. óta minden tárgy a saját mappájában van; a repó gyökerében csak a közös fájlok maradnak: `.cpanel.yml`, `.gitignore`, `CLAUDE.md`, `README.md`.

## Mit csinálj, ha a tulajdonos azt mondja, „vidd fel a mai fájlokat”

A chatből letöltött fájlok a `~/Downloads` mappában vannak. A menet:

1. Keresd meg a `~/Downloads`-ban azokat a fájlokat, amiknek a neve szerepel a fenti listán. A böngésző a másodszori letöltésnél sorszámoz, tehát `app (1).html`, `app (2).html` is lehet; ilyenkor a legfrissebb módosítási idejű a jó, a neve pedig a sorszám nélküli alak.
2. Minden fájlnál olvasd ki a verziószámot a letöltött példányból és a mappában lévő régiből is (a deckben a bal alsó segédsor, az appban és az indexben a lábjegyzet, `v1.8 · 2026. szeptember 14.` alakban). Ha a letöltött verziója régebbi vagy ugyanaz, ne írd felül, hanem szólj, és kérdezd meg, mi legyen. Ha újabb, mozgasd a helyére, felülírva a régit.
3. Amelyik fájlt felvitted, azt töröld a `~/Downloads`-ból, hogy legközelebb ne keveredjen be egy régi példány.
4. A listán nem szereplő fájlt soha ne vidd fel a `~/Downloads`-ból, akkor sem, ha a neve idevalónak tűnik. Ha valami ismeretlen jött, sorold fel, és kérdezz.
5. Ha új deck fájl érkezett (új alkalom), ellenőrizd, hogy van rá `cp` sor a `.cpanel.yml`-ben és hivatkozik rá a tárgy `index.html`-je. Ha bármelyik hiányzik, mondd meg, és ne pusholj addig, amíg a tulajdonos nem dönt; ne találd ki magad a sort.
6. Ezután a szokásos menet: `git status`, commit rövid magyar üzenettel, push a `main` ágra. Írd ki a commit hasht, hogy melyik fájlok mentek fel milyen verzióval, és hogy a következő cron-körrel, legfeljebb negyed órán belül élesben lesz.

## Mit csinálj, ha a tulajdonos azt mondja, „commitold és pushold”

1. `git status`: nézd meg, mi változott, és mondd el egy mondatban.
2. Ha új fájl jelent meg (például egy új alkalom deckje), ellenőrizd, hogy a `.cpanel.yml`-ben van rá `cp` sor és az `index.html` hivatkozik rá. Ha bármelyik hiányzik, mondd meg, és ne pusholj addig, amíg a tulajdonos nem dönt; ne találd ki magad a sort.
3. Commit rövid magyar üzenettel (mi változott, melyik alkalom), push a `main` ágra.
4. Írd ki a commit hasht, és hogy a következő cron-körrel, legfeljebb negyed órán belül élesben lesz.

## Amit soha

- Ne kerüljön a repóba `data/` mappa, `key.php`, `neptun.php`, `BCKP/`, `.DS_Store`, `.claude/`, `konyvek/` vagy `_archiv/`. Mind a nyolc a `.gitignore`-ban van; ezekből egyiket se vedd ki. A `neptun.php` a hallgatók Neptun-kódjait tartalmazza, személyes adat, a repo pedig publikus. A `konyvek/` tankönyvszöveg, ezért nem mehet ki.
- A `.gitignore`-t 2026. szeptember 24-én a tulajdonos kérésére bővítették a `.claude/` és a `konyvek/` sorral. Ez a változás commitolható; ezen kívül a `.gitignore`-t ne módosítsd.
- Ne írd át a fájlok tartalmát saját kezdeményezésre; a tartalom a chatben készül, itt csak verziózás és feltöltés van.
- Ne hozz létre GitHub Actions workflow-t vagy más deploy mechanizmust; a deploy a szerveren fut.
- Ne nevezd át a fájlokat; a nevek a deploy listával és a szerverrel vannak összekötve.

## Verziószám

Minden fájl alján (a deckben a bal alsó segédsorban, az appban és az indexben a lábjegyzetben) egy verziószám áll, például `v1.0 · 2026. szeptember 13.`. Ezt a chat emeli minden átadott fájlnál. Amikor a tulajdonos megnézi a weboldalt, ebből látja, hogy a friss verzió van-e fent; ha a repóban lévő fájl verziója újabb, mint a weben látott, a deploy még nem futott le vagy elakadt.

## Új alkalom készítése

Egy új alkalom menetét a `nappali/munkadoksik/ALKALOM-INDITO-PROMPT.md` írja le, a tartalom és a nyelv szabályait a `nappali/munkadoksik/ALKALOM-SZABALYOK.md`. Ha a tulajdonos új alkalmat kér tőled, előbb ezt a kettőt olvasd el, és az ott leírt sorrendet tartsd: könyvek feldolgozása, jegyzet-kutatás, kidolgozott jegyzet, csak utána a deck és a gyakorlat, minden lépés után a tulajdonos jóváhagyásával, a tulajdonos mondatai változatlanul.

## AI a marketingben (2026. november 4. óta)

Az `ai-a-marketingben/` mappa egy másik tárgy, az AI a marketingben gyakorlatának oldala, élesben https://egyetem.bemind.dev/ai-in-marketing/. A `.cpanel.yml` végén saját blokkja van (`AIDEPLOY`): a kezdőlap az `ai-a-marketingben/index.html`, a hat diasor ugyanebben a mappában van, az `api.php` a közös. Az `ai-a-marketingben/forras/` a diasorok generátora, nem kap `cp` sort. Az `ai-a-marketingben/szerverre-kezzel/` két fájlja (`neptun.php`, `key.php`) titok, a `.gitignore` meglévő sorai kizárják, soha ne kerüljön a repóba. Részletek: `ai-a-marketingben/README.md`.
