# Levelező · Online marketing 2026 ősz

Élesben: https://egyetem.bemind.dev/om2026levelezo/ (külön mappa a szerveren, saját csapatlistával és leadással).

Két alkalom, ugyanaz a hét téma, mint a nappalin, témánként egy rövid órai gyakorlattal és az alkalom végén csapatmunka-szavazással:

- 1. alkalom, 2026. október 16., 14:30–19:00, A.2.A226: az 1–3. téma, a nappali deckjeivel.
- 2. alkalom, 2026. november 6., 14:30–19:00, A.2.A226: a 4–7. téma.

## Ami ebben a mappában van

- `index.html`: a levelezős kezdőlap. Deploykor a szerveren `index.html` néven a levelezős mappába kerül.

## Ami közös a nappalival

A deckek, az eszközök és az app ugyanazok a fájlok (`alkalom-N/` és a gyökér), a `.cpanel.yml` mindkét helyre kimásolja őket. Az `app.html` a címből ismeri fel, hogy a levelezős oldalon fut (`/om2026levelezo/`), és ott a rövid gyakorlatok mezőit mutatja.

## A szerveren, kézzel (nincs a gitben)

- `key.php`: az oktatói kulcs, egyelőre ugyanaz, mint a nappalin.
- `neptun.php`: a levelezős hallgatók Neptun-kódjai. Amíg nincs, csak az oktatói kulccsal lehet belépni.
- `data/`: az api.php magától létrehozza, a csapatlista üresen indul.
