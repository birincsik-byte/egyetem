# Egyetem · Online marketing 2026 ősz · szabályok Claude Code-nak

Ez a mappa a kurzus weboldalának forrása. Élesben: https://egyetem.bemind.dev/om2026nappali/
A szerver egy cPanel Git-klónból és cronból frissül; a deploy a `.cpanel.yml`-ben felsorolt fájlokat másolja a `public_html/om2026nappali/` mappába, semmi mást.

A cron ütemezése a cPanel → Cron Jobs alatt áll, ez az egyetlen hiteles forrás. Jelenleg `*/5`, vagyis ötpercenként fut, tehát a push után legfeljebb öt perc az élesedés. A cron parancsa a `>/dev/null 2>&1` miatt a hibáit is eldobja, ezért egy elakadt deploy némán marad el; ha nem frissül az oldal, a cPanel Cron Jobs oldalán kell ellenőrizni az ütemezést.

## Hogyan érkezik ide változás

A tartalmi munka a claude.ai chatben készül. Onnan mindig teljes fájl jön, ugyanazzal a fájlnévvel, amit a tulajdonos bemásol ebbe a mappába a régi helyére. A fájlnevek rögzítettek:

- `index.html` – gyűjtőoldal, a hét alkalom
- `online-marketing-2026-evad-1-epizod.html` – 1. alkalom deck (a többi alkalom hasonló néven, saját fájlban)
- `app.html` – ügynökségi app (csapat, leadás, szavazás, eredmény)
- `api.php` – az app háttere
- `.cpanel.yml` – deploy lista

## Mit csinálj, ha a tulajdonos azt mondja, „commitold és pushold"

1. `git status`: nézd meg, mi változott, és mondd el egy mondatban.
2. Ha új fájl jelent meg (például egy új alkalom deckje), ellenőrizd, hogy a `.cpanel.yml`-ben van rá `cp` sor és az `index.html` hivatkozik rá. Ha bármelyik hiányzik, mondd meg, és ne pusholj addig, amíg a tulajdonos nem dönt; ne találd ki magad a sort.
3. Commit rövid magyar üzenettel (mi változott, melyik alkalom), push a `main` ágra.
4. Írd ki a commit hasht, és hogy a következő cron-körrel, legfeljebb öt percen belül élesben lesz.

## Amit soha

- Ne kerüljön a repóba `data/` mappa vagy `key.php` (a `.gitignore` kizárja; ne módosítsd).
- Ne írd át a fájlok tartalmát saját kezdeményezésre; a tartalom a chatben készül, itt csak verziózás és feltöltés van.
- Ne hozz létre GitHub Actions workflow-t vagy más deploy mechanizmust; a deploy a szerveren fut.
- Ne nevezd át a fájlokat; a nevek a deploy listával és a szerverrel vannak összekötve.

## Verziószám

Minden fájl alján (a deckben a bal alsó segédsorban, az appban és az indexben a lábjegyzetben) egy verziószám áll, például `v1.0 · 2026. szeptember 13.`. Ezt a chat emeli minden átadott fájlnál. Amikor a tulajdonos megnézi a weboldalt, ebből látja, hogy a friss verzió van-e fent; ha a repóban lévő fájl verziója újabb, mint a weben látott, a deploy még nem futott le vagy elakadt.

## Új alkalom készítése

A következő alkalmak anyagának készítési szabályai az `ALKALOM-SZABALYOK.md` fájlban vannak, az 1. alkalom mintájára. Ha a tulajdonos új alkalmat kér tőled (deck, forrásfeldolgozás, app-mezők), előbb azt olvasd el, és az ott leírt sorrendet tartsd: forrásdoksi először, deck utána, a tulajdonos mondatai változatlanul.
