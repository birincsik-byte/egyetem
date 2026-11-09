# 6. alkalom vázlata · Mit mutat a valóság · 2026. november 23.

Munkaanyag átnézésre. Készült: 2026. október 11. · v0.1

## Összefoglaló

A lánc kérdése: „Miből tudjuk meg, hogy működött”. A könyvek erősek a mérés logikájában (mérési folyamat, mutatók hierarchiája, lemorzsolódás, attribúció, hiúsági mutatók, kontrollcsoport), és mind a 2016 körüli állapotot írják: a GA4, a kulcsesemény, az elköteleződött munkamenet, a Consent Mode és a GDPR egyik könyvben sincs benne. Ezekhez a forrás a 3. alkalom webkutatása (`alkalom-3/webkutatas-3-alkalom.md`, elsődleges Google-, EUR-Lex- és EUB-források, 2026. október 5.) és öt mai ellenőrzés (2026. október 11.). A hirdetési fiók élő bemutatójához könyv nincs, az az oktató anyaga.

Berti mindhárom mondata forrásból alátámasztható. A kulcsgondolat („a szám nem válasz, hanem kérdés”) legtisztább könyvbeli párja Kingsnorth „So what?” kérdése és Kaushik „fok és fajta” különbsége. A tanulság sorrend-része Chaffey négy mérési kérdésében (10.2 ábra), Walker és Mullins „reappraisal is diagnostic” mondatában és Kotlernél Farris pilóta-hasonlatában van. A lánc szakadása Chaffey 8.8 ábráján (megjelenéstől az eladásig, minden lépésnél hatékonysággal), a 10.4 ábrán (lemorzsolódás okai szakaszonként), Kotler 17.5 ábráján (A és B márka) és a Marketing 4.0 PAR/BAR-számításában látszik. A „platformok cserélődnek” részhez két tiszta példa van: a minőségi mutató szerepe (Chaffey 2016 kontra a jelenlegi Google Ads súgó) és a GA4-ből 2023 novemberében kivett attribúciós modellek (Kingsnorth még tanítja őket).

A gyakorlat javaslata: a csapatok a saját márkájuk láncát kívülről fejtik vissza (hirdetéstár, kattintás, érkezés, mérőkódok és hozzájárulás, konverziós pont), és ebből írnak mérési tervet és hibakeresési sorrendet. Belső adathoz nem férnek hozzá, ezt a feladat nyíltan kezeli.

---

## Az alkalom szövege, szó szerint (gondolati ív)

> **A tematika szó szerint:**
> • Gyakorlati blokkok: belépés egy-egy hirdetési fiókba (Google Ads, social), a logika és összefüggések megértése
> • Webanalitika (GA4 fő mutatószámok) és GDPR / jogi vonatkozások

**Miről szól:** hirdetési fiók logikája élőben, GA4 fő mutatói, hibakeresés.

**Kulcsgondolat:** a szám nem válasz, hanem kérdés.

**Tanulság:** a diagnózis sorrend kérdése, nem tudásé. Végig kell menni a láncon a megjelenéstől a konverzióig, és megkeresni, hol szakad. Ez a készség többet ér, mint bármelyik platform ismerete, mert a platformok cserélődnek, a lánc nem.

**Fázis-sor:** Mit hoz magával: „Működött vagy nem működött.” Mire vált: „Hol szakad a lánc.” Mit tesz hozzá a végcélhoz: „A hallgató megtanulja ellenőrizni, és a saját döntését is megcáfolni.”

Jelölések lent: **K** = kulcsgondolat, **T1** = „a diagnózis sorrend kérdése, nem tudásé”, **T2** = „végig kell menni a láncon … hol szakad”, **T3** = „a platformok cserélődnek, a lánc nem”, **F** = fázis-sor („a saját döntését is megcáfolni”).

---

## 1. Forrástérkép

Az idézeteket a könyvek szövegfájljában géppel visszakerestem (saját keresővel a scratchpadben, a `findq.py` logikájával). Oldalszám: a nyomtatott oldalszám, ahol a fejlécből vagy láblécből kiolvasható; Neumeiernél és Abraham–Edelmannél nincs nyomtatott oldalszám a fájlban, ott PDF-oldal áll.

### Kulcsállítások (12)

| # | Állítás | Szó szerinti idézet | Hely | Kinek a mondatát támasztja |
|---|---|---|---|---|
| 1 | A mérés négy kérdése, sorrendben: mit akarunk, mi történik, miért, mit tegyünk. | „What is happening?” … „Why is it happening?” … „What should we do about it?” (10.2 ábra) | Chaffey, 10. fej., 555. o. | T1 |
| 2 | A diagnózis a mérés harmadik lépése, és az eltérés okát keresi. | „Stage 3, performance diagnosis, is the analysis of results to understand the reasons for variance from objectives and selection of marketing solutions to reduce variance.” | Chaffey, 10. fej., 554. o. | T1 |
| 3 | Ha nem érjük el a célt, meg kell keresni, hol van az ok: környezet, stratégia, terv vagy végrehajtás. | „When it is not, the firm determines whether the reason lies in the environment, the strategies employed, the action plans, the way the plans are being implemented” … „Thus, reappraisal is diagnostic” | Walker, Mullins, 13. fej., 335–336. o. | T1, T2 |
| 4 | A mutatóknak sorrendje van, mint a pilóta műszereinek. | „There is a sequence of knowing when to pay attention to which metrics” (Farris) | Kotler, Keller, 4. fej., 115. o. | T1 |
| 5 | A kommunikáció mérése megmutatja, hol szakad: az A márka ismert, de aki kipróbálta, elégedetlen. | „This indicates that the communications program is effective in creating awareness, but the product fails to meet consumer expectations.” (17.5 ábra) | Kotler, Keller, 17. fej., 494. o. | T2 |
| 6 | Minden konverziós arányt mérni kell a tudatosságtól az ajánlásig. | „Marketers should also measure every conversion rate from awareness to advocacy.” | Kotler, Kartajaya, Setiawan: Marketing 4.0, 6. fej., 77. o. | T2 (és visszamutatás a 2. alkalom 5A-jára) |
| 7 | A lemorzsolódás lépésenként mérhető a landingtől a pénztárig, és szakaszonként más az oka. | „A related concept is the attrition rate which describes how many visitors are lost at each step of a conversion funnel from landing page to checkout.” (558); „Potential reasons for causing attrition on an e-commerce site” (10.4 ábra, 559) | Chaffey, 10. fej., 558–559. o. | T2 |
| 8 | Egy hirdetés hozhat kattintást úgy, hogy a weboldalon nem lesz belőle eredmény. | „an ad could be effective in generating click-throughs or traffic, but not achieve the outcome required on the website” … „or the profile of the visitors is simply wrong” | Chaffey, 9. fej., 499. o. | T2 |
| 9 | Az analitika a fokot méri, nem a fajtát: 19 oldal lehet rossz navigáció és jó tartalom is. | „web analytics tools can measure the degree of engagement but they fall quite a bit short of measuring the kind of engagement.” | Chaffey, 10. fej., 551. o. (Kaushik-interjú) | K |
| 10 | Minden számra jön a „So what?” kérdés. | „So what? This is a question you should be asking yourself all the time.” | Kingsnorth, 14. fej., 281. o. | K |
| 11 | Az adat önmagában értéktelen, és minden lépésnél ember hibázhat: a termékben, a telepítésben, a beállításban, az értelmezésben. | „Data is in itself worthless.” … „So the product may be perfect but the set-up may be wrong.” | Kingsnorth, 14. fej., 261. o. | K, T1 (előbb a műszert kell ellenőrizni) |
| 12 | A kontrollcsoport és a teszt dönt, nem a megérzés. | „Data trumps intuition.” (Chaffey, 564. o.); „Instead of gut instinct or ‘hindsighting,’ multivariate testing became the accepted approach.” (Abraham, Edelman, PDF-oldal 156) | Chaffey, 10. fej.; Abraham, Edelman, 7. fej. (Sephora-eset) | F |

### Könyvenként

**Chaffey, Ellis-Chadwick: Digital Marketing, 6. kiadás (2016).** A fő forrás.

- *10. fejezet, Evaluation and improvement of digital channel performance (548–591. o.).* A 3. alkalom feldolgozása (`forrasfeldolgozas-3-alkalom.md`, „Mi marad a 6. alkalomra”) ide utalta a mérési folyamatot, a keretrendszert, a pontosságot és a tesztelést. Ezeket most olvastam el, és ezek kellenek:
  - 550. o., definíció: „Web analytics is the measurement, collection, analysis and reporting of Internet data for the purposes of understanding and optimising web usage.” A 10.1 ábra négy kérdése: mutató, eszköz, elemzés, cselekvés (a „cselekvés” oszlop kérdése: a mutatók alapján cselekszenek-e).
  - 553. o.: „You can’t manage what you can’t measure” (Napier). Háttér, nem dia.
  - 554. o., a WAA 2011-es felmérése: az első két gond az adatok cselekvésre váltása. Idézet: „The top two issues reported suggest the problems of performance management, taking action based on the data.” (K: a szám csak akkor ér valamit, ha kérdést és lépést vált ki; saját következtetés)
  - 555. o., makro- és mikroszintű mutatók, „performance drivers”. A 10.2 ábra (kulcsállítás 1).
  - 557. o., 10.3 ábra, WebInsights öt diagnosztikai kategóriája: üzleti hozzájárulás, marketingeredmények, elégedettség, viselkedés, promóció. A sorrend alulról felfelé épp a lánc (promóciótól az üzleti eredményig; saját következtetés). „Promotion is successful if traffic meets objectives of volume, quality, value and cost” (557).
  - 558–559. o., konverziós arány, lemorzsolódás, 10.4 ábra (kulcsállítás 7). Az ábra szakaszai: Acquisition, First impressions, Product selection, Payment and fulfilment, mindegyiknél konkrét okokkal (rossz közönség, lassú betöltés, homályos üzenet, ügyetlen navigáció, magas szállítási díj, kártyahiba).
  - 561. o., egyedi látogató = azonosító (IP, cookie, regisztráció), nem ember; 30 perces munkamenet (Universal-kori szabvány, jelölendő).
  - 564. o., A/B teszt, „Data trumps intuition.” (Amazon, Matt Round).
  - 566. o., clickstream: „Clickstream analysis refers to detailed analysis of visitor behaviour in order to identify improvements to the site.”
  - 568–569. o., pontosság: „The key benefit of the browser-based approach is that it is potentially more accurate than server-based approaches.” (568); mintavételezés a GA ingyenes változatában (568, Universal-kori állapot); „Web analytics systems store personal data.” (569) és „the latest laws about use of cookies.” (569). Ez a GDPR-blokk könyvbeli hídja.
  - 570. o.: „These tools measure the gap between what the user had hoped to do on the site and what they actually achieved.” (a „miért” kérdése a kérdőívvel)
  - 589. o., vizsgakérdés: „Measurement of websites concerns the recording of key events involving customers using a website.” Jó záró- vagy vizsgakérdés.
  - 562. o., Altimeter-keret a közösségi médiára: „Engagement KPIs to manage social media. These are the easiest measures to collect, but the least valuable” (562; a „valuable” szó sortöréssel). Hiúsági mutatókhoz.
- *8. fejezet, Campaign planning for digital media.*
  - 433. o., 8.7 ábra: a kampánymutatók hierarchiája a legegyszerűbbtől: volumen, minőség (konverziós arány), költség (CPC), CPA, ROI, márkamutatók, élettartamérték. Idézet: „Traffic volume measures give no indication of whether the audience referred to the site engages with it or leaves straight away” (433).
  - 434. o., visszafordulás: „since they don’t discover relevance!”; a visszafordulási arány szélesebb sávban mozog, mint a konverziós arány, ezért gyorsabban mutatja a hibás forrást vagy kulcsszót.
  - 436. o., 8.8 ábra: „An example of effectiveness measures for an online ad campaign”. A lánc egy dián: megjelenés, kattintás, látogatás, lead, eladás, és minden szint között hatékonysági mutató (CTR, CPC, konverziós arány, költség per eladás). A számok a könyv 2016-os brit biztosítási példájából valók, így idézhetők, de jelölni kell.
  - 456–458. o., attribúció: „It is seldom the case that a customer will go straight to a site and purchase” (456); a last-click modell „simplifies the reality of previous influence” (458, sortöréssel); 8.17 ábra (autóbérlés, több forrás egy eladás előtt).
  - 457. o., UTM-paraméterek (Digital marketing insight 8.4): „Defining a standard set of online marketing source codes is essential to determining the value of different referral sources”. Universal-kori leírás, a jelenlegi lista a GA4 súgójában bővebb (lásd webes források).
- *9. fejezet, Marketing communications using digital media channels.*
  - 497–498. o., minőségi mutató (quality score) 2016-os leírása: „Understanding quality score is the key to successful paid search marketing.” (497), „you can’t ‘buy your way to the top’ as many think” (498). A jelenlegi Google-súgó ezt másképp írja (T3, lásd lent).
  - 499. o., kulcsállítás 8, és a CPA képlete a konverziós arányból és a CPC-ből.
- *3. fejezet, jogi környezet (a teljes könyvben megvan, 147–163. o.).* A GDPR szó nincs a könyvben (ellenőrizve 2026. október 11-én a teljes szövegben). A 3. alkalom feldolgozása (`forrasfeldolgozas-3-alkalom.md`, 449–554. sor) már kibontotta; a mérés szempontjából ezek kellenek, újra visszakeresve:
  - 147. o., 3.1 táblázat: az adatvédelem első sora az űrlapos adatgyűjtés és a webanalitikai követés együtt: „capture on forms and indirectly through tracking behaviour through web analytics”.
  - 149. o.: „The main issue to be considered by the marketer is disclosure of the types of information collection and tracking data used.”
  - 157. o.: „almost half of online shoppers are now deleting cookies” (a mérés pontatlanságának könyvbeli oka; a szám a könyvé, 2016-os, diára csak jelölve).
  - 158. o.: „explicit opt-in to cookies is required”; „This indicates that for an e-commerce service session cookies are legitimate without the need for opt-in.”
  - 159. o., tízpontos ellenőrzőlista: „Notify or inform the site visitor before asking for information on”.
  - Megkötés: a könyv a 95/46/EK irányelvet, a brit DPA-t és a PECR-t írja le. Jelenlegi jogot ebből tanítani nem szabad.

**Kingsnorth: Digital Marketing Strategy, 1. kiadás (Kogan Page, 2016).** A brief 2019-et ír kérdőjellel; a fájl kolofonja szerint 2016. Nincs benne GA4.

- *14. fejezet, Analytics and reporting (259–283. o.).* A legjobb forrás a kulcsgondolathoz és a hibakereséshez.
  - 260. o.: mérés nélkül a stratégia nem bizonyítható.
  - 261. o., „The human factor”: a Google Analytics négy emberi lépése (aki tervezte, aki telepítette, aki beállította, aki a riportból dönt). Kulcsállítás 11.
  - 262. o., „Data alignment”: „Even when using two very similar systems, sometimes ones produced by the same company, you will find discrepancies in the numbers.” A hibakeresés első kérdése: mit jelent ez a szám ebben a rendszerben (saját következtetés).
  - 267. o.: „Without web analytics you are blind to the activity on your site”.
  - 268. és 270–271. o., hiúsági mutatók (követők, social rank): „these metrics do not indicate that your content is engaging” (271).
  - 273. o., UX-eszközök (hőtérkép): „as they will show only the behaviour not the cause or intent”. Ez Kaushik „fok és fajta” gondolatának párja (K).
  - 274–276. o., címkekezelés (tag management): a címke elromolhat, ha az oldal változik. Hibakereséshez.
  - 277–279. o., attribúciós modellek: lineáris, első interakció, pozícióalapú, egyedi, adatvezérelt. Ezek közül a GA4-ben jelenleg csak az adatvezérelt és a last click érhető el (lásd webes források). T3 példája.
  - 280–282. o., riportolás: YoY, MoM, WoW hátrányai; „Tell a story” három kérdése: „what are we trying to achieve? Did we achieve it? What do we do next?” (281); „So what?” (281, kulcsállítás 10); „Hindsight by itself offers little value.” (281); „Check, check and check again.” (282).
- *6. fejezet, Paid search, Measurement and optimization (116–118. o.).*
  - 116. o.: „before looking into measurement it is essential to revisit your objectives”.
  - 116–117. o., a mutatók három csoportja: forgalmi (megjelenés, kattintás, CTR, CPC, átlagos pozíció, megjelenési arány, minőségi mutató), konverziós (bevétel, árrés, rendelés, lead, konverziós arány, AOV), hatékonysági (ROI, CPL/CPO, LTV). Ez a fiók oszlopainak lánc szerinti rendje (saját következtetés).
  - 117. o.: „It is as much a measure of your site’s ability to convert traffic as the ad itself.” (a konverziós arányról). Kié a hiba: a hirdetésé vagy az oldalé (T2).
  - 118. o., „Test, learn, refine, test...”.
- *8. fejezet, Social media, Measurement (160–161. o.).* Volumen és elérés kontra elköteleződés és minőség; a hangulat (sentiment) mérése. Rövid háttér a social fiókhoz.
- *2. fejezet, KPIs (42–43. o.).* A KPI-t az üzleti célhoz kell igazítani: „the more top-level metrics that determine the success of a business” (43).
- *3. fejezet, Regulation (56–63. o.).* „Implied consent is also possible” (57) a cookie-ról. **Ez jelenleg nem tanítható igazként**: a Planet49-ítélet (2019) és a GDPR 4. cikk 11. pontja szerint a hozzájárulás aktív cselekvés (webes forrás lent). Jó ellenpélda arra, hogy a könyv állapota elavult (T3, saját következtetés).

**Kotler, Keller: Marketing Management, 14. kiadás.**

- *4. fejezet, Marketing Metrics (114–115. o.).* Definíció: a marketingmutatók „the set of measures that helps them quantify, compare, and interpret their marketing performance” (114). Farris pilóta-hasonlata (115, kulcsállítás 4).
- *17. fejezet, Measuring Communication Results (494. o.).* „Too often, however, their communications directors supply only inputs and expenses” és „Ultimately, behavior-change measures capture the real payoff.” A 17.5 ábra A és B márkája (kulcsállítás 5): a legjobb órai interakció, mert a számok a könyvéi, és mindkét márkánál máshol szakad a lánc.

**Kotler, Kartajaya, Setiawan: Marketing 4.0, 6. fejezet, Marketing Productivity Metrics (73–78. o.).** PAR és BAR, az 5A-ra építve. 73. o.: a tudatosság és az ajánlás mint mutató „focus more on the outcome rather than the process”; 74. o.: a menedzserek nem értik, „why their scores go up or down in any given quarter”, és a példa: X márkát 90-en ismerik, 18-an veszik, 9-en ajánlják, vagyis „It fails to convert 80% of the high level of brand awareness into sales.” 77. o.: minden 5A-átmenet konverziós aránya mást jelez (alacsony aware→appeal: gyenge pozicionálás vagy végrehajtás; alacsony ask→act: a csatorna nem váltja vásárlásba az érdeklődést). Ez a 2. alkalom 5A-jának mérési folytatása, T2.

**Walker, Mullins: Marketing Strategy, 8. kiadás, 13. fejezet, Measuring and Delivering Marketing Performance.** 335–336. o., a teljesítménymérés öt lépése (13.2 ábra: standard, visszajelzés meghatározása, adat, értékelés, korrekció) és a diagnózis (kulcsállítás 3). 352. o., 13.13 ábra (Ambler tíz kérdése) és: „A key issue in developing a set of marketing metrics as part of an overall performance measurement system is getting the metrics aligned with the strategy.” Háttér a mérési tervhez.

**Neumeier: The Brand Gap, revised edition, Discipline 4 (Validate).** Nyomtatott oldalszám nincs, PDF-oldal szerint.
- PDF 103: „The standard model is an antique.” … „Companies need feedback. Feedback turns communication into something more like a theatre performance than a magazine.” A visszajelzés-hurok a kommunikáció negyedik eleme (F: a döntést a közönség igazolja vagy cáfolja).
- PDF 105: „creativity is subjective, but it’s only subjective until it reaches the marketplace” (K: a piacon már mérhető).
- PDF 109: „It’s usually better to get a rough answer to the right question than a detailed answer to the wrong question.” (K és T1)
- PDF 110–112: swap test, hand test, concept test; „It’s not about liking. It’s about understanding.” (PDF 112). A 7. alkalomhoz is.
- PDF 111: „When people talk to themselves, it’s called insanity. When companies talk to themselves, it’s called marketing.” (Bautista)
- Megjegyzés: Neumeier márkaelemek tesztelését írja, nem webanalitikát. A 6. alkalomhoz a gondolkodásmódot adja, a módszert nem.

**Abraham, Edelman: Personalized (HBR Press, 2024).** Nyomtatott oldalszám nincs, PDF-oldal szerint. Az egyetlen 2020 utáni könyv, és az egyetlen, amelyik a GDPR-t néven említi.
- 9. fejezet, Measuring Impact (PDF 180–193): kemény és vezető mutatók: „The hard metrics validate whether those interactions are of the right quality” (PDF 182); egy kampány hatása és a teljes hatás különbsége: „It’s one thing to measure the lift from individual email campaigns or the click-throughs and conversion rates across different experiences on the website.” (PDF 185); kettős számolás és márkás keresés: „you will see relatively higher response rates because customers who were searching for your brand were already likely to buy.” (PDF 186, attribúció, F); a zavaró felugró ablak „will quickly get flagged, even if it generates incremental sales.” (PDF 193).
- 4. és 6. fejezet, kontrollcsoport: „They withhold personalized interactions from a control group of customers” (PDF 84); univerzális kontrollcsoport, és hogy a kampányonkénti többletbevételek összeadása „grossly overstates their collective impact” (PDF 131).
- Sephora-eset (PDF 156): kulcsállítás 12.
- 10. fejezet, Navigating Risk and Privacy (PDF 194–196): „Customer data is the lifeblood of personalization.” (PDF 195); „Regulators worldwide uniformly hold that consumers have a right to know that their data is being collected.” (PDF 195), utána a GDPR átlátható hozzájárulási szabályai. Figyelem: a PDF 196 szerint „Google Chrome is phasing out third-party cookies”; a Google 2025. április 22-én bejelentette, hogy ezt nem vezeti be önálló kérdéssel, és marad a jelenlegi felhasználói választás (webes forrás lent). Ezt diára így nem szabad tenni.

**Nem dolgoztam fel ehhez az alkalomhoz:** Hooley, Piercy; Marketing 5.0 (a 2. alkalom döntése szerint nem hivatkozunk rá).

### Webes források (elsődleges [E], másodlagos [M])

A 3. alkalom webkutatásából (`alkalom-3/webkutatas-3-alkalom.md`, lekérve 2026. október 5., „Események, mérőeszközök, cookie és hozzájárulás” szakasz), amit a HOL-TARTUNK szerint az oktató 2026. október 6-án ide halasztott:
- GA4 eseménymodell, munkamenet (30 perc), automatikus és bővített mérésű események (page_view, session_start, user_engagement, scroll 90%, click, form_start, form_submit), elköteleződött munkamenet („Lasts longer than 10 seconds, Has a key event, Has 2 or more screen or page views”), visszafordulás („The percentage of sessions that were not engaged.”), elköteleződési idő, kulcsesemény, útvonal-felfedezés, CTR (Google Ads súgó) [E].
- Mikro- és makrokonverzió: Google „How to create a measurement plan” (support.google.com/analytics/answer/7165633) [E] és NN/g, Neusesser, 2024. július 19. [E].
- Cookie: Európai Bizottság [E]; ePrivacy 2002/58/EK 5. cikk (3), magyarul és angolul [E]; GDPR 4. cikk 11. pont, 7. cikk (1)–(4), (32) preambulumbekezdés angolul [E], magyarul csak részben; Planet49 (C-673/17), EUB magyar sajtóközlemény [E]; EDPB Cookie Banner Taskforce 2023 [E]; WP29 4/2012 vélemény az analitikai cookie-ról [E].
- Google Consent Mode, alap és haladó megvalósítás, a négy hirdetési és analitikai jelző [E].
- Microsoft Clarity hőtérkép, felvétel, rage és dead click, ingyenes, nyilvános élő demó [E]; Hotjar [E].
- Mit lát a kívülálló: Chrome DevTools Cookies és Network panel, Google Tag Assistant, Wappalyzer, BuiltWith, Ghostery [E].

Mai ellenőrzés (2026. október 11., WebFetch, elsődleges):
- **GA4 demófiók** [E] https://support.google.com/analytics/answer/6367342: „The Google Analytics demo account is a fully functional Google Analytics account that any Google user can access.” Két adatforrás: Google Merchandise Store (web) és Flood-It! (app és web). Mindenki Viewer szerepkörben lát; az adatok torzítottak (obfuscated); export nincs. A súgóoldal maga ellentmondásos a tulajdonok számában (2 vagy 3).
- **GA4 tölcsér-felfedezés** [E] https://support.google.com/analytics/answer/9327974: „visualize the steps your users take to complete a task”, és „quickly see how well they are succeeding or failing at each step” (a WebFetch kivonata, szemmel ellenőrizendő).
- **GA4 UTM-paraméterek** [E] https://support.google.com/analytics/answer/10917952: utm_id, utm_source, utm_medium, utm_campaign, utm_source_platform, utm_term, utm_content, utm_creative_format, utm_marketing_tactic; a source, medium és campaign mindig kell (összefoglalás, nem szó szerinti).
- **Google Ads minőségi mutató** [E] https://support.google.com/google-ads/answer/6167118: „Quality Score is a diagnostic tool meant to give you a sense of how well your ad quality compares to other advertisers.” „This score is measured on a scale from 1-10 and available at the keyword level.” Összetevők: „Expected clickthrough rate (CTR)”, „Ad relevance”, „Landing page experience”. „Quality Score is not an input in the ad auction.” (T3: Chaffey 2016-ban még a rangsor egyik meghatározójaként írta.)
- **Google Ads fiókszerkezet** [E] https://support.google.com/google-ads/answer/6372655: „A campaign consists of a collection of ad groups.”; kampányszinten költség, hálózat és földrajzi hely; hirdetéscsoportonként „pick a narrow theme”.
- **GA4 attribúció** [E] https://support.google.com/analytics/answer/10596866: „The first click, linear, time decay, and position-based attribution models are no longer available as of November 2023.” (T3, Kingsnorth 277–279. o. ellenpárja)
- **Google Hirdetési Átláthatósági Központ** [E] https://support.google.com/adspolicy/answer/13733850: „Google provides a searchable repository of advertisers and the ads they’ve served on Google platforms”; szűrés dátum és célzott hely szerint. Cím: https://adstransparency.google.com/
- **Chrome és a harmadik féltől származó cookie** [E] https://privacysandbox.google.com/blog/privacy-sandbox-next-steps (Anthony Chavez, 2025. április 22.): „we’ve made the decision to maintain our current approach to offering users third-party cookie choice in Chrome”.
- **Meta Hirdetéstár és Hirdetéskezelő szerkezete:** a Meta súgóoldalai robots-tiltás miatt nem töltődtek le. Nincs ellenőrzött forrásom, lásd hiányzó források.

---

## 2. Deck-vázlat (32 dia)

A 3. alkalom szerkezete szerint. A diák fejlécében a „szempont” helyett **állomás** jelöli, melyik vizsgálati szemponthoz ad muníciót a dia a gyakorlatban (javaslat, lásd nyitott kérdések). A javasolt állomások, Berti „a megjelenéstől a konverzióig” láncából: **1. Megjelenés · 2. Kattintás · 3. Érkezés · 4. Haladás · 5. Konverzió**, és külön a **Műszer** (mér-e egyáltalán, és mit enged a hozzájárulás). A Műszer az én javaslatom, nem Berti láncának része. Forrás nem kerül a diára, a jegyzetbe megy.

### Keret

**1. Címlap.** „2026. november 23. · Mit mutat a valóság · Miből tudjuk meg, hogy működött”, alatta „A tematikából:” és a két tematikai pont szó szerint (fent). Forrás: gondolati ív.

**2. A lánc** (`data-sec` Évad). A hét kérdés, a 6. „ma”, mellette az eddigi beadandók (1–5.) neve. Forrás: gondolati ív.

**3. Visszamutatás · az 5. beadandó.** Ha leadták: a keretfelosztásokból egy-két tipikus döntés (hova ment a pénz). Átvezető mondat: most azt nézzük meg, miből derül ki, hogy jó helyre ment. Ha nincs még eredmény, csak a feladat és a lánc. Forrás: oktató.

**4. A mai alkalom.** Miről szól, kulcsgondolat, tanulság szó szerint; alatta a nap ritmusa (másfél óra elmélet benne az élő fiókbemutatóval, másfél óra csoportmunka). Forrás: gondolati ív.

**5. Egyéni feladat · 5 perc · írásban, magadnak.** Javaslat: „Gondolj egy hirdetésre, amire rákattintottál, de nem vettél semmit. Hol szakadt meg nálad?” A végén két-három választ felolvasunk, és a táblára állomásokhoz rendeljük. Ez a tanulság első tapasztalata. Interakció: igen.

### A. A lánc és a diagnózis (minden állomás)

**6. Egy szám, sok kérdés.** Kotler 17.5 ábrája két oszlopban: A márka (80% ismeri, 60% kipróbálta, 20% elégedett), B márka (40%, 30%, 80%). Kérdés a teremnek: hol szakad a lánc az egyiknél és a másiknál, és kinek a dolga megjavítani? A számok a könyvéi. Interakció: igen, ez tanítja a kulcsgondolatot. Forrás: Kotler, Keller 17. fej.; K, T2.

**7. A mérés négy kérdése.** Mit akarunk elérni? Mi történik? Miért történik? Mit tegyünk? Mellette Farris pilótája: minden fázisban más műszert néz. Egy mondat alul: az ok lehet a környezetben, a stratégiában, a tervben vagy a végrehajtásban. Forrás: Chaffey 10. fej. (10.2 ábra); Kotler, Keller 4. fej.; Walker, Mullins 13. fej.; T1.

**8. A mai nap módszere: a lánc állomásai.** Az öt állomás (és a Műszer) egy sávon, állomásonként a tipikus mutató (megjelenés, CTR, munkamenet és elköteleződési arány, események és mikrokonverzió, kulcsesemény és konverziós arány). Alatta a 3. alkalomról ismert három lépés: Mit látok? Miért így? Működik? Kiegészítés javaslatként: a „Működik?” itt azt jelenti, észrevenné-e a márka, ha ezen az állomáson szakadna a lánc. Forrás: Chaffey 8. fej. (8.8 ábra); Marketing 4.0, 6. fej.; oktató; T2.

### B. A hirdetési fiók logikája (1. Megjelenés, 2. Kattintás, 5. Konverzió)

**9. Hogyan épül fel egy fiók.** Google Ads: fiók (hozzáférés, számlázás), kampány (költségkeret, hálózat, hely), hirdetéscsoport (szűk téma, kulcsszavak), hirdetés. Meta: kampány, hirdetéskészlet, hirdetés (elsődleges forrás még kell). Az üzenet: minden szinten más döntés, és a hiba szintje megmondja, hol kell keresni (saját következtetés). Forrás: Google Ads súgó; 1–2. állomás.

**10. Élőben: a fiók.** Az oktató bemutatója (Google Ads és egy social fiók). A diáról csak a feladat: a hallgatók hívják be, melyik oszlop melyik állomás (megjelenés, kattintás, CTR, CPC, konverzió, CPA). Interakció: igen. Forrás: oktató; Kingsnorth 6. fej. (forgalmi, konverziós, hatékonysági mutatók).

**11. Ugyanaz a lánc, számokkal.** Chaffey 8.8 ábrája lépcsőként: megjelenés, kattintás, látogatás, lead, eladás, közte a hatékonysági mutatók. Kérdés: hol a legnagyobb veszteség, és az a hirdetés, az oldal vagy az értékesítés dolga? A számok a könyv 2016-os példájáé, a dián jelölve. Interakció: igen. Forrás: Chaffey 8. fej.; T2.

**12. Kié a hiba?** Két mondat egymás mellett: a konverziós arány ugyanannyira mutatja az oldalt, mint a hirdetést; egy hirdetés hozhat kattintást eredmény nélkül, mert a felhívás gyenge vagy rossz a közönség. Visszautalás a 3. alkalomra (az oldal, ahová érkezik). Forrás: Kingsnorth 6. fej.; Chaffey 9. fej.; 2–3. állomás.

**13. A platform cserélődik.** Két pár: a minőségi mutató 2016-ban a rangsor kulcsa volt (Chaffey), jelenleg diagnosztikai eszköz, ami nem bemenete az aukciónak (Google Ads súgó); Kingsnorth öt attribúciós modellt tanít, a GA4-ben 2023 novembere óta kettő maradt. A tanulság utolsó mondata alul, szó szerint. Forrás: Chaffey 9. fej.; Kingsnorth 14. fej.; Google súgó; T3.

### C. A GA4 fő mutatói (3. Érkezés, 4. Haladás, 5. Konverzió)

**14. Mit mér a webanalitika?** A definíció („megértés és optimalizálás”), és Kaushik: a 19 megnézett oldal lehet rossz navigáció és jó tartalom is. A szám a fokot mondja meg, a fajtát nem. Forrás: Chaffey 10. fej.; K.

**15. Minden esemény.** A GA4-ben az oldalmegtekintés is esemény. Egy oldal drótvázán jelölve, mi milyen eseményt vált ki: page_view, scroll (90%), click (kimenő), form_start, form_submit; a munkamenet 30 perc tétlenségig tart. Ez a 3. alkalomról halasztott anyag. Forrás: GA4 súgó (webkutatás); Chaffey 10. fej. 589. o. (a vizsgakérdés); 3–4. állomás.

**16. Elköteleződött vagy visszafordult.** Az elköteleződött munkamenet három feltétele (10 másodperc, kulcsesemény, két oldal), és hogy a visszafordulás ennek az ellentettje. Mellette a 2016-os definíció (egyoldalas látogatás). Ugyanaz a szó, más szám: ezért kell tudni, melyik rendszer mit ért alatta. Forrás: GA4 súgó; Chaffey 10. fej. 557. o.; Kingsnorth 14. fej. 262. o.; 3. állomás, T3.

**17. Honnan jött?** Forrás, médium, kampány; az UTM-paraméter a hirdetés és az oldal közötti híd. Ha hiányzik, a GA4 nem tudja, melyik kampány hozta a látogatót (összefoglalás a súgóból). Forrás: GA4 súgó; Chaffey 8. fej. 457. o.; 2–3. állomás.

**18. Kulcsesemény, mikro és makro.** A kulcsesemény definíciója; makrokonverzió a fő üzleti cél (vásárlás, foglalás), mikrokonverzió a lépés felé (kosárba tétel, feliratkozás). Kapcsolat a 3. alkalom konverziós pontjaival. Forrás: GA4 súgó; Google mérési terv; NN/g; Chaffey 10. fej. 555. o.; 4–5. állomás.

**19. Hol esnek ki?** A tölcsér-felfedezés képe (lépésenként hányan jutnak tovább), mellette Chaffey 10.4 ábrájának okai szakaszonként. Feladat: rendeld az okokat (lassú betöltés, homályos üzenet, magas szállítási díj, kártyahiba) az állomásokhoz. Interakció: igen. Forrás: GA4 súgó; Chaffey 10. fej.; T2.

**20. A szám mit, a felvétel miért.** Hőtérkép és munkamenet-felvétel (Clarity nyilvános demó), rage és dead click. A szám megmutatja, hol akad el, a felvétel, hogy mi történik ott; a szándékot egyik sem. Forrás: Clarity (webkutatás); Kingsnorth 14. fej. 273. o.; Chaffey 10. fej. 570. o.; 4. állomás, K.

### D. Amikor a szám téved (Műszer, 5. Konverzió)

**21. Négy ember a szám mögött.** Aki a terméket tervezte, aki telepítette, aki beállította, aki a riportból dönt: bármelyiknél lehet a hiba. Két rendszer ugyanarra mást mutat. Ezért az első hibakeresési lépés a műszer, nem a kampány (saját következtetés). Forrás: Kingsnorth 14. fej. 261–262. o.; Chaffey 10. fej. 568–569. o.; Műszer, T1.

**22. Kinek jár az érdem?** Chaffey autóbérlős ábrája (több forrás egy eladás előtt) és a last click; Abraham és Edelman: a márkás keresőhirdetés jól teljesít, mert aki a márkára keres, eleve venni akart. Kérdés: melyik csatorna kapna kevesebb pénzt, ha csak az utolsó kattintást néznénk? Forrás: Chaffey 8. fej.; Abraham, Edelman 9. fej.; 5. állomás, F.

**23. Ami jól mutat, és ami dönt.** Hiúsági mutatók (követők, lájk) kontra üzleti mutatók; a teszt és a kontrollcsoport („Data trumps intuition”); Neumeier visszajelzés-hurka. Egy mondat: a saját döntésedet akkor tudod megcáfolni, ha előre megmondod, melyik szám cáfolná (saját következtetés, a fázis-sorhoz). Forrás: Kingsnorth 14. fej.; Chaffey 10. fej. 562., 564. o.; Abraham, Edelman; Neumeier Discipline 4; F.

### E. GDPR és a mérés (Műszer)

**24. A mérés is adatkezelés.** Chaffey: az űrlap és a webanalitikai követés egy jogterület; „Web analytics systems store personal data.” Az ePrivacy 5. cikk (3) magyarul: a végberendezésen tárolt információhoz előzetes hozzájárulás kell, kivéve a feltétlenül szükségeset. A GDPR hozzájárulás-definíciója és hogy a visszavonás legyen olyan egyszerű, mint a megadás. Planet49: előre bejelölt négyzet nem elég. Lábjegyzetben: Kingsnorth 2016-ban még vélelmezett hozzájárulást írt, ez jelenleg nem tartható. Forrás: Chaffey 3. és 10. fej.; EUR-Lex; EUB (webkutatás); Műszer.

**25. Ami a sávon múlik.** A cookie-sáv döntése a lánc első kapuja: amit a látogató elutasít, azt a mérés nem vagy csak modellezve látja (Consent Mode alap és haladó módja). Élőben: Chrome DevTools, Network fül, szűrés a GA4 kéréseire, a sáv elfogadása előtt és után. Interakció: igen, ez a beadandó egyik lépése. Szám nincs a dián: a hozzájárulási arányra nincs ellenőrzött forrásunk. Forrás: Google Consent Mode súgó; Chrome DevTools dokumentáció; EDPB taskforce (webkutatás); Műszer.

### Bemutató (minden állomás)

Két valós, ellenőrizhető példa. Kívülről a **Tunki-Tunki** (tunkitunki.hu), mert a 3. alkalom bemutatója ugyanez volt, így a lánc folytatódik: akkor azt néztük, hogyan fogadja a látogatót, most azt, mit mér belőle. Belülről a **Google Merchandise Store** a Google hivatalos GA4 demófiókjában, mert ez az egyetlen valós GA4-fiók, amit bárki megnyithat. Adatot egyikről sem írok be: minden dia „Mit látunk?” sorát az óra előtt élőben kell kitölteni. A 3. deckből ismert tény a Tunki-oldalról: van sütisáv, ami mobilon takarja az első képernyő alját.

**26. Bemutató · Tunki-Tunki kívülről · 1–2. állomás.** Fut-e hirdetése (Meta Hirdetéstár, Google Átláthatósági Központ), mit ígér, hova visz a link, van-e UTM a céloldal URL-jében. Mit látunk? Miért így? Működik? Óra előtt ellenőrizendő mind.

**27. Bemutató · Tunki-Tunki kívülről · 3. állomás és Műszer.** Egyezik-e az ígéret és az érkezés; a sütisávon van-e elutasító gomb; a DevTools szerint indul-e GA4- vagy Meta-kérés a döntés előtt; milyen konverziós pontok vannak (a 3. alkalom bemutatójából: regisztráció nélkül rendelhető, hírlevél-feliratkozás). Óra előtt ellenőrizendő.

**28. Bemutató · belülről · Google Merchandise Store, GA4 demófiók.** Élőben négy kattintás: forgalomszerzés (forrás és médium), események, kulcsesemények, tölcsér-felfedezés. A kérdés minden képernyőnél ugyanaz: mit kérdez ez a szám? Jelölve: az adatok a Google szerint torzítottak, ezért konkrét számot nem idézünk a jegyzetbe. Forrás: GA4 súgó (demófiók).

**29. Bemutató · a lánc egy dián.** A Tunki-Tunki útja kitöltve a beadandó szerkezetében: állomásonként mit látunk, melyik mutató mutatná a szakadást, hol látszana (Ads, Meta, GA4), és mi lenne a három legvalószínűbb szakadási pont sorrendben. Ez a minta, amit a csapatok az eszközben is betölthetnek.

### Gyakorlat és zárás

**30. A hatodik beadandó · csoportmunka.** Mérési terv és hibakeresés a márkátok láncán, kívülről. Nem javítotok, hanem visszafejtitek, mit mér a márka, mit nem, és hol nem venné észre, ha szakad a lánc. A végén egy mondat (sablon lent). Ha a márkának nincs hirdetése: az organikus belépési ponttal (keresés, közösségi profil) indul a lánc.

**31. A hatodik beadandó · hogyan töltitek ki.** Másfél óra, négy rész (lent). Eszköz: lánc-vizsgálat, a Tunki-Tunki minta betölthető. Laptop kell (DevTools telefonon nem megy). Valódi adatot nem adtok meg, nem fizettek, űrlapot nem küldtök be.

**32. Zárás.** A tanulság szó szerint. „Legközelebb, 2026. december 7-én: kikkel csináljuk?”

Csapatmunka-szavazás dia: a 3. alkalom eszköze szavazás nélkül ment; ha itt kell, a 31. után kerül be (lásd nyitott kérdések).

---

## 3. Gyakorlat és beadandó

**A beadandó eredeti címe:** 6. Mérési terv és hibakeresés.

**Igazítás a dekonstrukcióhoz (javaslat).** A csapatok nem látják a márka hirdetési fiókját és GA4-ét. Amit látnak, az a lánc nyoma kívülről: a hirdetés a nyilvános tárban, a kattintás URL-je, az érkező oldal, a böngészőbe letöltött mérőkódok és sütik, a konverziós pontok. Ebből fejtik vissza, mit mér a márka, és ebből írnak mérési tervet: állomásonként melyik szám mutatná, ha ott szakadna a lánc. Ez megfigyelés és leírás, nem kitalálás: a terv a meglévő láncra szól, nem újra. A hibakeresés itt azt jelenti, hogy sorrendbe teszik a lehetséges szakadási pontokat, és mindegyikhez megmondják, mi cáfolná.

**Hogyan illeszkedik a „Mit látok? Miért így? Működik?” (javaslat).**
- *Mit látok?* Az állomás nyoma, bizonyítékkal: képernyőkép, URL, a hálózati kérés neve, a sütisáv szövege.
- *Miért így?* Mit akar a márka mérni ezzel, és mit tart eredménynek (melyik konverziós pont a makro, melyik a mikro).
- *Működik?* Ha ezen az állomáson szakadna a lánc, észrevenné-e a márka, és melyik számból. Itt kerül elő a fázis-sor második fele: melyik korábbi saját döntésünket (4. csatornaterv, 5. keretfelosztás) cáfolná meg ez a szám.

**Idő: 90 perc, csapatban, négy rész.**
1. Bejárás kívülről, 1–3. állomás · 25 perc. Hirdetéstár és Átláthatósági Központ, kattintás, céloldal, UTM, ígéret és érkezés egyezése.
2. A műszer · 20 perc. Sütisáv (van-e elutasítás, olyan egyszerű-e, mint az elfogadás), DevTools Network és Cookies panel vagy Tag Assistant: milyen mérőkódok futnak, a döntés előtt vagy után.
3. Mérési terv és hibakeresés · 30 perc. Állomásonként egy mutató és hogy hol látszana; a három legvalószínűbb szakadási pont sorrendben, bizonyítékkal és cáfolattal; a saját korábbi döntés próbája.
4. Összegzés és leadás · 15 perc. Az egy mondat, ki mit csinált.

**Eszköz ötlete: `lanc-vizsgalat.html`** (az `oldal-vizsgalat.html` mintájára: lépések fülekkel, böngészőben ment, betölthető minta, a végén beküldi a mezőket az `ep6` leadásba).

Lépések: Az út kiválasztása · Megjelenés · Kattintás · Érkezés · Műszer · Konverzió · Mérési terv · Hibakeresés és összegzés.

| Mező | Tartalom |
|---|---|
| f1 | A vizsgált út: belépési pont (melyik hirdetés vagy organikus forrás), céloldal, makro- és mikrokonverzió. |
| f2 | Mit láttok állomásonként (megjelenés, kattintás, érkezés, konverziós pont), bizonyítékkal. |
| **f3** | **Egymondatos lényeg (kötelező, ezt mutatja a szavazólista).** |
| f4 | Miért így: mit mér a márka valószínűleg, mit tart eredménynek, és mit nem mér. |
| f5 | Mérési terv: állomásonként egy mutató, hol látszana (Google Ads, Meta, GA4), és milyen kérdést vet fel. |
| f6 | Hibakeresés: a három legvalószínűbb szakadási pont sorrendben, bizonyítékkal, és mindegyiknél, mi cáfolná. |
| f7 | A műszer: sütisáv és hozzájárulás, mérőkódok a döntés előtt és után, mit nem lát emiatt a márka. |
| f8 | A saját döntés próbája (melyik 4. vagy 5. beadandóbeli döntést melyik szám cáfolná), és ki mit csinált. |

**Sablonmondat f3-hoz (javaslat):** „A [márka] láncán a(z) [állomás] a leggyengébb pont, mert [amit láttunk], és ezt a(z) [mutató] mutatná meg.”

**Segédlet ötlete:** egy oldal a kívülről használható eszközökről (Hirdetéstár, Átláthatósági Központ, DevTools Cookies és Network, Tag Assistant, Wappalyzer), mindegyikhez egy képernyőkép és egy mondat, mit lehet belőle megtudni és mit nem. Forrás: webkutatás, „Mit lát a kívülálló”.

---

## 4. Levelezős rövid változat (60–65 perc, 11 dia)

**Ami marad:** 1. Címlap és a mai alkalom (a hármas egy dián). 2. Egy szám, sok kérdés (Kotler A és B márka, interakció). 3. A mérés négy kérdése és a lánc állomásai egy dián. 4. Hogyan épül fel egy fiók. 5. Élőben: a fiók (10 perc, az oktató). 6. Ugyanaz a lánc, számokkal (Chaffey 8.8) és „kié a hiba” egy dián. 7. Minden esemény és az elköteleződött munkamenet egy dián. 8. Honnan jött, és hol esnek ki (UTM és tölcsér). 9. Négy ember a szám mögött és a platform cserélődik egy dián. 10. Ami a sávon múlik (GDPR és Consent Mode egy dián, DevTools élőben). 11. Mini-gyakorlat és zárás.

**Ami kimarad vagy jegyzetbe megy:** hőtérkép és felvétel, attribúció részletesen, hiúsági mutatók és kontrollcsoport, a teljes bemutató (csak a Tunki-Tunki sütisáv és DevTools része marad élőben, a GA4 demófiók kimarad vagy 3 percre rövidül).

**Mini-gyakorlat (20–25 perc), „Három állomás kívülről”, csapatban a saját márkán, laptopon:**
1. Megjelenés · 5 perc: fut-e hirdetés a Hirdetéstárban vagy az Átláthatósági Központban, és mit ígér.
2. Kattintás és érkezés · 5 perc: hova visz, van-e UTM, egyezik-e az ígéret az oldallal.
3. A műszer · 10 perc: sütisáv elutasítással, DevTools Network, indul-e mérőkérés a döntés előtt.
4. Egy mondat · 5 perc: f3 a sablon szerint, és egy mutató, ami a leggyengébb pontot mutatná.

---

## 5. Nyitott kérdések Bertinek

1. **A GDPR helye.** A gondolati ív lefedettségi táblája a GDPR-t a 3. alkalomhoz rendeli, a 3. deck vázlatának nyitott kérdése volt, hogy a 6.-ra megy-e, és a kész 3. deckben a címlapon kívül nincs róla dia. A HOL-TARTUNK szerint a cookie és a hozzájárulás 2026. október 6-án ide került. Itt marad-e, és milyen mélységben: csak a mérés jogi lába (24–25. dia, javaslat), vagy teljes blokk (jogalapok, adatkezelési tájékoztató, érintetti jogok)?
2. **Melyik fiókot mutatod élőben?** Saját BEMIND-fiók, ügyfélfiók engedéllyel, vagy csak a GA4 demófiók? Ha ügyfélé, a képernyőn látszó adatokat anonimizálni kell-e.
3. **Az állomások.** Az öt állomás neve (Megjelenés, Kattintás, Érkezés, Haladás, Konverzió) az én javaslatom a te „megjelenéstől a konverzióig” mondatodra. A külön **Műszer** (mér-e egyáltalán, mit enged a hozzájárulás) szintén az enyém, és túlmegy a láncodon. Maradhat így, vagy más neveket, más számot szeretnél? A szempont helyett állomás-jelölés a diákon rendben van?
4. **A „Működik?” értelmezése.** Javaslatom: itt azt jelentse, „észrevenné-e a márka, ha ezen az állomáson szakadna”. Elfogadod, vagy maradjon a 3. alkalom jelentése?
5. **A sablonmondat és a nyolc mező** (fent) jó-e így. A fázis-sor „a saját döntését is megcáfolni” részét az f8-ba tettem (a 4. és 5. beadandó döntésének próbája). Ez kell-e, vagy túl sok?
6. **A bemutató márkája.** Tunki-Tunki a folytonosság miatt; nem ellenőriztem, fut-e hirdetése és milyen mérőkódok vannak az oldalán. Ha nincs hirdetése, kell egy másik magyar márka a kívülről nézett részhez. Megfelel-e a Google Merchandise Store a belső nézethez?
7. **Laptop.** A 3. alkalom telefonon ment, ez a feladat laptopot kér (DevTools). Ez megoldható a teremben?
8. **Csapatmunka-szavazás** legyen-e ennél az alkalomnál.
9. **Clarity-demó:** a hivatalos nyilvános demó, vagy a saját oldalad Clarity-képe.

## Hiányzó források

- **NAIH** saját tájékoztatója vagy ajánlása a sütikről és a webanalitikáról: a 3. alkalom webkutatása sem találta, mai keresés sem hozta. Kell, ha a GDPR-blokk magyar hatósági nézőpontot ad.
- **A magyar jogszabályi hely**, ahová az ePrivacy 5. cikk (3) átültetése került: nem ellenőriztem. Emlékezetből az elektronikus hírközlési törvény egyik bekezdése, de ezt forrás nélkül nem írnám le, és változhatott.
- **A GDPR 7. cikk (2)–(4) és a (32) preambulumbekezdés magyar szövege**: az EUR-Lexről kézzel kell kimásolni (a webkutatás csonkát kapott).
- **Meta**: a Hirdetéskezelő szerkezete (kampány, hirdetéskészlet, hirdetés) és a Hirdetéstár hivatalos leírása; a súgóoldalak letöltését robots-szabály tiltotta. A Meta Pixel és a Conversions API viszonya a hozzájáruláshoz szintén nincs meg.
- **Google Ads attribúció**: a GA4-ről van elsődleges forrás (2023. november), a Google Ads fiók jelenlegi modelljeiről külön ellenőrizni kell.
- **Consent Mode**: hogy a haladó mód modellezése mennyit pótol, arra nincs számom, és nem is kell a diára.
- **Google Merchandise Store** jelenlegi bolt-URL-je (a demófiók súgója nem adja meg).
- **Chaffey 8. kiadás (2022)**: a tematika ajánlott irodalma; a feldolgozás a 6. kiadásból (2016) készült, a 8. kiadás mérési fejezetét nem láttam.
- A tölcsér-felfedezés és a Google Ads súgó idézeteit a WebFetch kivonatolta: diára kerülés előtt szemmel ellenőrizendő az eredeti oldalon.
