# Egyetem · három tárgy forrása

Ebben a repóban három tárgy weboldala van, tárgyanként egy mappában. A deploy a
`.cpanel.yml` szerint fut: a szerver a felsorolt fájlokat másolja a célmappákba,
semmi mást, és soha nem töröl. A webcímek nem függnek a mappák nevétől.

| mappa | tárgy | élesben |
|---|---|---|
| `nappali/` | Online marketing, nappali tagozat | https://egyetem.bemind.dev/om2026nappali/ |
| `levelezo/` | Online marketing, levelező tagozat | https://egyetem.bemind.dev/om2026levelezo/ |
| `ai-a-marketingben/` | AI a marketingben | https://egyetem.bemind.dev/ai-in-marketing/ |

További mappák:

- `konyvek/` – tankönyvszöveg a felkészüléshez. Nincs a gitben, nem megy ki a webre.
- `_archiv/` – régi csomagok és mentések. Nincs a gitben, nem megy ki a webre.

## Amit tudni érdemes

**A `levelezo/` mappa befagyasztott.** A levelező tárgy webes fájljai (app, api,
az 1–7. deck és a segédletek) saját másolatban állnak ebben a mappában, laposan.
Korábban ugyanazokat a fájlokat kapta, mint a nappali; 2026. november 9. óta nem.
Ha a levelezőn kell változtatni, itt kell, és csak ide hat.

**A hallgatói adatok nincsenek a repóban.** A csapatok, a regisztrációk és a
leadott munkák a szerveren, a célmappák `data/` almappájában élnek. A deploy
ezeket nem érinti: csak `mkdir -p` és `cp` szerepel benne, egyetlen `rm`, `mv`
vagy `--delete` sincs.

**Titkok.** A `key.php` és a `neptun.php` (Neptun-kódok, személyes adat) soha nem
kerül a repóba, a `.gitignore` kizárja őket. Kézzel kell feltölteni a szerverre.
A levelezőhöz a `levelezo/szerverre-kezzel/`, az AI tárgyhoz az
`ai-a-marketingben/szerverre-kezzel/` mappában van a példány.

A munka menetét és a szabályokat a `CLAUDE.md` írja le, a nappali tárgy részletes
leírását a `nappali/README.md`.
