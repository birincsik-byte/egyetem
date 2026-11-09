---
title: "Forrásfeldolgozás · 3. alkalom · A saját terep"
subtitle: "Online marketing, Pannon Egyetem, 2026 őszi félév · munkaanyag átnézésre"
date: "2026. október 5. · v3"
---

# Összefoglaló

v3 · 2026. október 5. A v3-ban bekerült Chaffey 9. és 10. fejezete. Az első változat egy korábbi sessionből beemelt kulcsgondolathoz és tanulsághoz rendelt forrást. Ezek nem az oktató mondatai voltak, ezért elengedtük őket. Ez a változat az oktató 2026. október 5-i keretezését és az általa választott hármast követi.

A 3. alkalomhoz (2026. október 12., „A saját terep”) tíz forrást dolgoztam fel: Chaffey 7., 6., 3., 4., 9. és 10. fejezetét, Kotler, Keller 5. fejezetét és a 6. fejezetből az észlelt kockázatot, valamint a 2026. október 5-én hozott három UX-könyvet (Krug, Weinschenk, Yablonski). Minden angol idézet szó szerinti, és mindegyiket géppel visszakerestem a forrásszövegben: a Chaffey- és Kotler-fájlokban a `munkadoksik/findq.py`, az új könyvekben a `munkadoksik/findq_pdf.py` adta az oldalszámot.

A könyvek erősek abban, ami a látogatóval az oldalon történik: első benyomás, landing, akadályok, bizalom, regisztráció, e-mail-folyamat. A 2026. október 5-én hozott teljes Chaffey-könyvből a 9. és a 10. fejezet is bekerült. A 10. fejezet adja a webanalitika alapfogalmait (látogatás, oldalmegtekintés, bounce rate, clickstream, útvonal), és van benne egy vizsgakérdés, ami a tanulsághoz áll a legközelebb: „Measurement of websites concerns the recording of key events involving customers using a website.” (589). Továbbra is hiányzik a könyvekből a klasztermodell, a hőtérkép, a munkamenet-felvétel, a jelenlegi (GA4) eseménymodell és a jelenlegi cookie-szabályozás. Ezekhez a forrás a `webkutatas-3-alkalom.md` (elsődleges webes források).

A deckvázlat (v0.3) még a régi hármasra épült. A diánkénti ellenőrzést lent meghagytam, mert a forrásállítások pontosítása (TurboTax 6%, WHSmith, Fogg 46,1%, „öt másodperc”) az új deckben is érvényes, a vázlatot magát a 4. fázisban az új keret szerint kell újraírni.

---

# A források ehhez az alkalomhoz

**Chaffey, Ellis-Chadwick: Digital Marketing, Strategy, Implementation and Practice, 6. kiadás (2016), 7. fejezet (Delivering the online customer experience), 354–417. oldal.** A saját felület gerince: forgalom és teljesítés, landing page, hitelesség, használhatóság, betöltési idő, bizalom, szolgáltatásminőség. Végigolvasva. Sok adata 2000 és 2014 közötti.

**Chaffey, Ellis-Chadwick, 6. fejezet (Relationship marketing using digital platforms), 301–350. oldal.** Engedélyalapú marketing, űrlap és ösztönző, e-CRM, az üdvözlő sorozat (Table 6.1), right touching, a WHSmith-eset, e-mail kontra közösségi platform. A fájl a 301. oldallal kezdődik, a fejezet nyitóoldala (tanulási célok, bevezető, a Zappos-eset eleje) hiányzik.

**Chaffey, Ellis-Chadwick, 3. fejezet (Online marketplace analysis: macro-environment), csak a jogi és adatvédelmi rész, 147–159. és 163. oldal.** A 2016-os állapot: a 95/46/EK irányelv, a brit Data Protection Act és a PECR. A GDPR szó nincs benne. Ami a fejezetben jogi szabályként áll, az nem a jelenleg érvényes jog.

**Chaffey, Ellis-Chadwick, 4. fejezet (Digital marketing strategy), az OVP és a saját felület, 193–241. oldal között.** Az online értékajánlat definíciója és példái (222–223.), a saját felület szerepe, a Tesco eseményvezérelt levelei (240–241.).

**Chaffey, Ellis-Chadwick, 9. fejezet (Marketing communications using digital media channels), 476–547. oldal, csak a saját terepet érintő részek.** Új forrás, 2026. október 5., a teljes könyvből kinyerve (`konyvek/chaffey-ch9-marketing-communications.txt`). A saját oldal mint középpont, on-page SEO, belső linkelés, a landing oldal a csatornák szemszögéből (quality score, dedikált landing), opt-in e-mail és a házon belüli lista. A csatornák részletei a 4. alkalomé.

**Chaffey, Ellis-Chadwick, 10. fejezet (Evaluation and improvement of digital channel performance), 548–591. oldal.** Új forrás, 2026. október 5. (`konyvek/chaffey-ch10-evaluation-improvement.txt`). Webanalitikai alapfogalmak (látogatás, oldalmegtekintés, egyedi látogató, bounce rate, clickstream, útvonalelemzés), mikro- és makroszintű mérőszámok, A/B teszt, mérőeszközök. A 2016-os, Universal Analytics korabeli állapot. A mérési terv a 6. alkalomé.

**Kotler, Keller: Marketing Management, 14. kiadás, 5. fejezet (Creating Long-Term Loyalty Relationships), 125–150. oldal.** Az észlelt vevőérték és a teljes vevői költség, a TurboTax-eset, megtartás, Godin, loyalty programok és klubok, adatbázis és adatvédelmi aggályok. A fájl a 125. oldallal, egy bekezdés közepén kezdődik, a fejezet eleje hiányzik.

**Kotler, Keller, 6. fejezet (Analyzing Consumer Markets), csak a 170–171. oldal.** A hat észlelt kockázat, a v9 deck 25. diájának forrása.

**Krug: Don't Make Me Think, Revisited, 3. kiadás (New Riders, 2014).** Új forrás, 2026. október 5. Az első törvény, a szkennelés, a kezdőlap feladatai, a goodwill-tartály, a saját kezű usability teszt. A PDF-ben nincs nyomtatott oldalszám, ezért fejezettel hivatkozom. Krug maga írja az előszóban, hogy a könyv egy része elavult, és azt is, mi marad érvényes (lent).

**Weinschenk: 100 Things Every Designer Needs to Know About People (New Riders, 2011).** Új forrás, 2026. október 5. Pszichológiai pontok egy-egy kutatásra építve: kognitív terhelés, döntési túlterhelés, bizalom, társas bizonyíték, motiváció, űrlapok. A példái a 2010 körüli webet mutatják, a kutatások érvényességét nem ítélem meg.

**Yablonski: Laws of UX, 2. kiadás (O'Reilly, 2024).** Új forrás, 2026. október 5., a legfrissebb. Tíz UX-törvény (Jakob, Fitts, Miller, Hick, Postel, peak–end, aesthetic–usability, von Restorff, Tesler, Doherty), egy etikai fejezet a dark patternekről. A kiadás éve a copyright-oldalról: „Copyright © 2024”, „February 2024: Second Edition”.

**A 2026-os tematika ajánlott irodalma** Chaffey, Ellis-Chadwick 8. kiadása (2022); a feldolgozás a meglévő 6. kiadásból készült, az oldalszámok arra érvényesek.

**Az új könyvek szövege.** A három PDF-ből `pdftotext`-tel szövegfájl készült ugyanabba a mappába (`konyvek/3ik alkalom/krug-dont-make-me-think.txt`, `weinschenk-100-things.txt`, `yablonski-laws-of-ux.txt`). A `konyvek/` gitignorált, ezek sem kerülnek a repóba. Az idézetellenőrző: `munkadoksik/findq_pdf.py`. Weinschenknél a nyomtatott oldal a PDF-lap mínusz 13, Yablonskinál mínusz 20; ezt a feldolgozás során lapról lapra ellenőriztük.

---

# 3. alkalom: A saját terep

**A tematika pontjai, szó szerint:**
• Weboldal és UX/UI mint forgalomterelő felület, loyalty/regisztrációs logika
• (és a „Platformok és eszközök” pontból: automatizált email marketing)
• (és a „Webanalitika és GDPR” pontból: a GDPR / jogi vonatkozások)

**Az oktató keretezése (2026. október 5.).** Az 1. alkalom arról szólt, hogy azonosítani tudják a márkát, az üzeneteit és a célcsoportját. A 2. a journeyről: milyen folyamaton keresztül lesz az érdeklődőből vásárló. A 3. arról, hogy amikor megérkezett hozzánk az előszobába, mit tehetünk, hogy a legjobban érezze magát: milyen legyen a weboldal, mi a landing oldal és mi nem, milyen oldaltípusok vannak, tartalommodellek (a klasztermodell is), mikro- és makrokonverzió, belső folyamatok, a weboldal kulcs- és fontossági eseményei (látogatás, oldalmegtekintés, oldalon eltöltött idő, átkattintás, navigációs térkép, hogyan használják az oldalt) és a mérés eszközei (mit jelent a cookie, mit jelent a hőtérkép). A mérési terv és a hibakeresés a 6. alkalomé.

**A hármas (javaslat, az oktató az A változatot választotta, 2026. október 5.):**
Miről szól: weboldal és oldaltípusok, landing oldal, tartalommodellek, regisztráció és e-mail, a weboldal eseményei és mérőeszközei, adatkezelés.
Kulcsgondolat: amikor megérkezik, már nem mi keressük őt, hanem ő keres minket. Az előszobában dől el, hogy beljebb jön-e.
Tanulság: az oldalon minden lépés egy esemény, és minden esemény elárulja, hol érezte jól magát a látogató, és hol akadt el.

**A beadandó (az oktató döntése, 2026. október 5.):** a saját márka oldalának elemzése és egy külső márka oldalának elemzése ugyanazon szempontok szerint. Javító javaslat nincs, az a 7. alkalom konstrukciója. A külső oldalt minden csapat egy előre összeállított listából választja. A nap: másfél óra elmélet, utána másfél óra csoportmunka.

A könyvek sorrendje lent: előbb a három Chaffey-fejezet és a Kotler, utána a három új UX-könyv. Fejezetenként témákra bontva, mindegyiknél oldal, magyar összefoglaló, szó szerinti idézet, és hogy mit ad az alkalomhoz. A hármas és a témák forrásai, a diánkénti ellenőrzés és a „Nem találtam” lista a végén, összevonva.


# A könyvek fejezetenként

## Chaffey, Ellis-Chadwick, 7. fejezet (Delivering the online customer experience)

Digital Marketing, 6. kiadás (2016), 354–417. oldal. Feldolgozva 2026. október 5-én a `konyvek/chaffey-ch7-online-customer-experience.txt` fájlból, végigolvasva. Minden idézet és oldalszám a `findq.py` kimenete. A fejezet első oldala (355.) a szövegfájlban futófej nélkül áll, ezért a fejezet eleji tanulási célokból nem idézek. A fejezet sok adata 2000 és 2014 közötti; ahol ez számít, jelzem.

### A saját felület és a forgalom

**356. oldal, hol zajlik az interakció.** A bevezetés szerint a márka digitális élménye jelenleg sok érintkezési pontból áll (oldal, app, közösségi oldalak), a fejezet mégis a weboldalra fókuszál, mert a legtöbb interakció ott történik. Ugyanitt áll, hogy a közösségi média kevéssé hoz látogatást az oldalra.
Idézet: "For most businesses, the majority of interactions still occur on desktop and mobile websites, so this is where we focus in this chapter." (356) és "Although social media have grown in importance, they are relatively unimportant in prompting website visits." (356)
Mit ad az alkalomhoz: háttér ahhoz, miért a weboldallal kezd az alkalom: Chaffey szerint az interakciók többsége a weboldalon történik, ezért a fejezet is erre fókuszál.

**362. oldal, a weboldal a kommunikáció közepén.** A tervezésről szóló rész első mondata kimondja, hogy a közösségi média térnyerése ellenére a céges weboldal maradt az online kommunikáció középpontja.
Idézet: "Despite the growth in social media, the company website, which today must be effective for users accessing via desktop, smartphone and tablet devices, is still at the heart of online communications." (362)
Mit ad az alkalomhoz: a 9. diához („Mi a tiéd”) használható mondat a saját felület súlyáról.

**356. oldal, mit vár a vevő az oldaltól.** Alison Lancaster (John Lewis Direct, Charles Tyrwhitt) szerint a jó oldal a felhasználóval kezdődik, és a vevő kényelmet, gyors, áttekinthető, könnyen bejárható oldalt akar.
Idézet: "A good site should always begin with the user." (356) és "They want a site that is quick to download, well-structured and easy to navigate." (356)

**360. oldal, CRO: több bevétel ugyanabból a forgalomból.** A fejezetet nyitó Smart Insights-interjúban Karl Blanks (Conversion Rate Experts) úgy érvel a konverzióoptimalizálás mellett, hogy az nem több hirdetési költést, hanem a meglévő költés jobb megtérülését jelenti. Ben Jesson szerint a cél azt megtalálni, a tölcsér melyik része hozza a legtöbbet a legkevesebb munkával.
Idézet: "We explain that CRO allows companies to generate more" (360), "It's about getting a higher return from the existing ad spend." (360) és "The real goal is to identify which parts of the sales funnel will yield the greatest wins with the least work." (360)
Mit ad az alkalomhoz: a CRO gyakorlati kerete: a meglévő forgalom jobb teljesítése a feladat, nem több hirdetés. Ehhez kapcsolódik az alkalom kiindulópontja, hogy a látogató már megérkezett (saját következtetés).

### Blocked arteries és a konverziógyilkosok

**361. oldal, a „blocked arteries”.** Ben Jesson módszere: fel kell rajzolni a teljes konverziós tölcsért, mérni minden lépését, és a legnagyobb lemorzsolódást keresni. Ezeket „blocked arteries” néven nevezi: olyan oldalak vagy oldalelemek, amelyekre sokan jutnak el, de gyengén teljesítenek. A jeleket analitikából, használhatósági tesztből, kérdőívből, ügyfélszolgálati visszajelzésből és megérzésből veszik.
Idézet: "Then you should look for the biggest drop-offs from one step to the next." (361) és "We like to say that we look for the 'blocked arteries' (that is, pages – or page elements – that get loads of visitors but are underperforming)." (361)
Mit ad az alkalomhoz: a 8. dia forrása, és jó auditkérdés a beadandóhoz: hol sok a látogató és kevés a továbblépés.

**361. oldal, a leggyakoribb konverziógyilkosok.** Karl Blanks hármat sorol fel. Az első a tesztelés hiánya: egy másutt bevált „best practice” elem akár csökkentheti is a konverziót, a Google egyik oldalán például a videó rontotta. A második a „meek tweaking”, vagyis olyan apró változtatás, ami nem hozhat érdemi hatást. A harmadik, hogy már az első látogatáskor eladást kérnek; jobb több lépcsős utat tesztelni, ahol előbb értéket adnak (összehasonlító táblázat, fórum, e-mail), és csak utána kérik a rendelést.
Idézet: "Installing a 'best practice' magic button that another site swears by might actually lower conversions." (361), "Despite the popularity of video, Google once discovered through tests that video reduced conversions on one of its pages." (361), "Killer #2 is 'meek tweaking' – in other words, making changes that are never likely to have a significant effect." (361), "Killer #3 is asking for the sale on the first visit." (361) és "in which you provide great value before you ask for the order." (361)
Mit ad az alkalomhoz: a videós példa azt mutatja, hogy egy oldalra tett új elem nem biztos, hogy hoz, és teszt nélkül nem derül ki; az oldalelemzésnél jó óvatossági pont (saját következtetés).

**360–361. oldal, tesztelés és a design szerepe.** Jesson szerint a bevált gyakorlat csak kiindulópont a teszteléshez, nem válasz. Blanks szerint a kiváló design előfeltétele a konverziónak, de az igazi áttörést a látogató gondolkodásának megismerése hozza.
Idézet: "Best practices should not be the answer to optimising a website, but merely one starting point for formulating a test strategy." (360) és "Excellent design is a prerequisite for conversion" (361)

### Hova érkezik a látogató: landing page és deep linking

**386–387. oldal, landing page.** A fejezet margódefiníciója szerint a landing page az a belépő oldal, ahová a látogató egy hirdetésre vagy más oldalon lévő linkre kattintva érkezik; lehet a kezdőlap is, de jobb, ha olyan oldal, amelynek üzenete a hirdetés ajánlatára fókuszál (a definíció vége a szövegfájlban a főszöveggel összekeveredett, ezért csak az eleje idézhető). A főszöveg szerint sok első látogató nem a kezdőlapra érkezik, hanem mélyebbre, keresőből vagy más oldal linkjéről.
Idézet: "an ad or other form of link from a referring site. It can be a home page but more typically, and desirably, a landing page is a page" (386) és "they arrive deeper in the site from search engines or links from other sites." (386–387)
Mit ad az alkalomhoz: a 11. dia forrása; a hirdetés és az érkezőoldal egyezésének könyvbeli alapja a definíció „offer in the ad” része.

**387. oldal, a landing page hat célja (Chaffey és Smith, 2012).** Hat cél, mindegyikhez kérdések: válasz kiváltása (feltűnő call-to-action a hajtás felett), a különböző közönségek megszólítása (címsor, ami megmutatja, hogy jó helyen van), a márkaüzenet átadása (ki vagy, mit csinálsz, hol, miben más), a látogató kérdéseinek megválaszolása, a kínálat bemutatása, keresőoptimalizálás. A második célnál áll, hogy az oldalon lévő űrlap gyakran hatékonyabb egy plusz kattintásnál.
Idézet: "Does the page have a prominent call-to-action, such as a prominent button above the fold; and repeated in text and image form?" (387), "Does the page have a prominent headline and subheads showing the visitor is in the right place?" (387), "A landing page containing form fields to fill in is often more effective than an additional click since it starts committed visitors on their journey." (387) és "Different audiences will want to know different things." (387)
Mit ad az alkalomhoz: a landing page-audit kérdéslistájának kész váza, a 10., 11. és 15. dia forrása.

**397. oldal, deep linking (Nielsen).** Nielsen arra figyelmeztet, hogy sok felhasználó nem a kezdőlapon érkezik, hanem egy másik oldalról vagy nyomtatott, tévés hirdetésből egy belső oldalra. Ezt deep linkingnek hívja, és az ilyen oldalakon is megfelelő navigáció és kontextus kell.
Idézet: "that many users will not arrive on the home page, but may be referred from another site or according to a" (397)

**404. oldal, forgalomterelés és az érkezőoldal.** A forgalomépítésről szóló rövid rész szerint az oldal tervezésekor a keresőoptimalizálást és a landing page-en nyújtott élményt kell különösen figyelembe venni, ahol a látogató mélyebben érkezik.
Idézet: "the experience delivered on landing pages where the visitor arrives not on the home page, but deeper within the site." (404)

### Mit lát, amikor megérkezik: OVP és alapkérdések

**381. oldal, a hiányzó alapinformáció.** A versenytársak oldalainak áttekintésénél Chaffey megjegyzi, hogy sok oldalról hiányzik az, amit egy céget nem ismerő látogató tudni akar: ki vagy, mit csinálsz, hol, és miben vagy más. Az utolsó kérdés az online értékajánlat (OVP) átadása.
Idézet: "some sites miss out the basic information that someone who is unfamiliar with a company may want to know" (381), "Who are you? 'About Us' is now a standard menu option." (381) és "What makes you different? Why should I use your site/services compared to your" (381)

**387. oldal, a márkaüzenet a landing page-en.** A harmadik cél ugyanezt a négy kérdést teszi fel az érkezőoldalra, és rákérdez, meggyőző-e az OVP, és van-e vásárlói vélemény vagy értékelés a független hitelességhez.
Idézet: "Does the page clearly explain who you are, what you do, where you operate and what makes you different?" (387) és "Is your online value proposition compelling? Do you use customer testimonials or ratings to show independent credibility?" (387)
Mit ad az alkalomhoz: a 10. dia „who you are, what you do” kérdése szó szerint itt van.

**374–375. oldal, marketingvezérelt oldaltervezés.** Az elemzési fázis kérdései között szerepel a célközönség (perszóna), a szolgáltatások (értékajánlat) és a várt marketingeredmény (regisztráció, lead, eladás). A marketingvezérelt tervezésnél az ügyfélszerzéshez világos OVP kell, a konverzióhoz pedig az, hogy az oldal megszólítsa az első látogatót.
Idézet: "What should the content of site be? Which services will be provided (value proposition)?" (374), "Customer acquisition – the online value proposition must be clear." (375) és "Customer conversion – the site must engage first-time visitors." (375)

**376–377. oldal, egy kezdőlap elemenként (Ultralase).** A 7.2 mini esettanulmány egy lézeres szemműtéti cég kezdőlapját bontja kilenc elemre: karusszel a márkaüzenettel, call-to-action gombok az ügyfélút lépéseihez, bevezető szöveg, ösztönzővel ellátott űrlap, a gyakori kérdések kiemelve a kezdőlapon, feltűnő telefonszám, social proof (klinikatérkép, vélemények), és a MyUltralase regisztráció.
Idézet: "Customer journey highlighted (buttons below carousel)." (376), "These 'points of resolution' are often hidden in a FAQ, but it is interesting that Ultralase highlights them on the home page." (377), "Prominent phone response (top right). Vital for high-value, complex products since conversion tends to be higher via the phone channel." (377) és "Social proof (right sidebar)." (377)
Mit ad az alkalomhoz: mintapélda a beadandóhoz, hogyan lehet egy oldalt elemenként végignézni; a kiemelt GYIK az akadályelvétel konkrét esete (saját következtetés).

### Hitelesség és percepció

**389–390. oldal, Fogg et al. (2003): mi alapján ítélik hitelesnek az oldalt.** Fogg és kollégái diákokkal értékeltettek oldalakat, és azt vizsgálták, mi alapján ítélik meg a szolgáltató hitelességét. A lista élén a design look áll (46,1%), utána az információ szerkezete (28,5%) és fókusza (25,1%). Chaffey két megszorítást tesz: a bevallott viselkedés eltérhet a megfigyelttől, és bár a kinézet áll az élen, a többi tényező nagy része az információ minőségéről szól.
Idézet: "et al. (2003) asked students to review sites to assess the credibility of different suppliers based on the website design." (389), "Design look 46.1%" (389), "Reported behaviour (e.g. through questionnaires or focus groups) may be quite different from actual observed behaviour." (390) és "you can see that many of the other factors are based on the quality of information." (390)
Mit ad az alkalomhoz: a 12. dia forrása. A százalékok összege jóval 100 fölött van, tehát nem részesedés, hanem azt mutatja, hány értékelésben került elő az adott tényező (saját következtetés, a könyv a módszert nem írja le).

**389–390. oldal, egyszerűség és az oldal személyisége.** Rosen és Purinton (2004) szerint az egyszerű design számít. Az oldal stílusa (szín, kép, tipográfia, elrendezés) személyiséget ad, aminek a célközönséghez kell illenie.
Idézet: "You can see that these authors suggest that simplicity in design is important." (389) és "This personality has to be consistent with the needs of the target audience." (390)

**357. oldal, racionális és érzelmi értékek.** De Chernatony (2001) nyomán az online márkaélmény racionális és érzelmi értékekből, valamint az ezekre épülő ígért élményből áll; ez a 7.2 ábra piramisának alapja.
Idézet: "delivering the online experience promised by a brand requires delivering rational values, emotional values and promised experience" (357)

**404. oldal, a szolgáltatásminőségi rés mint percepció.** A szolgáltatásminőség keretei a vevő elvárt és észlelt szolgáltatásszintje közötti résen alapulnak. Az elvárás korábbi tapasztalatból és szájhagyományból jön.
Idézet: "between the customer's expected level of service (from previous experience and word-of-mouth communication) and their perception of the actual level of service delivery." (404)
Mit ad az alkalomhoz: keretet ad a márkáról kialakuló képhez: ez az elvárás és az oldalon tapasztalt élmény különbsége (saját következtetés).

### Használhatóság és akadályok

**377. oldal, Nielsen: az emberek elmennek.** Nielsen „Usability 101” cikke szerint a használhatóság a túlélés feltétele: ha az oldal nehezen használható, ha a kezdőlap nem mondja meg világosan, mit kínál a cég, ha eltévednek, ha nem kapnak választ a kérdéseikre, akkor elmennek. Nielsen a tervezési költségvetés kb. 10%-át szánná használhatóságra.
Idézet: "On the web, usability is a necessary condition for survival. If a website is difficult to use, people leave. If the homepage fails to clearly state what a company offers and what users can do on the site, people leave." (377), "If users get lost on a website, they leave." (377) és "If a website's information is hard to read or doesn't answer users' key questions, they leave. Note a pattern here?" (377)
Mit ad az alkalomhoz: a 15. dia Nielsen-idézete; az elakadás és a kilépés okainak egyik legerősebb könyvbeli támasza.

**377. oldal, hatékonyság és eredményesség.** A használhatósági szakemberek a feladat teljesülését mérik: lehet, hogy a látogatók közül csak tízből három találja meg a telefonszámot. A hatékonyságot az időből és a kattintások számából mérik.
Idézet: "out of ten visitors to a website may be able to find a telephone number" (377)

**375. oldal, a Fogg-féle viselkedésmodell.** Fogg (2009) modellje szerint egy célviselkedéshez három dolog kell egyszerre: elég motiváció, a viselkedés végrehajtásának képessége, és egy kiváltó jel. Ha a három nem esik egybe, a viselkedés elmarad.
Idézet: "they must (1) be sufficiently motivated, (2) have the ability to perform the behaviour and (3) be triggered to perform the behaviour. These three factors must occur at the same moment, otherwise the behaviour will not happen." (375)
Mit ad az alkalomhoz: a súrlódás elméleti kerete: a meggyőzés a motivációra hat, az akadály elvétele a képességre (saját következtetés).

**375. oldal, a konverzió legyen minél egyszerűbb.** A marketingvezérelt tervezés konverziós pontja szerint az ajánlat vagy vásárlás teljesítését a lehető legegyszerűbbé kell tenni, hogy közben ne morzsolódjanak le.
Idézet: "The fulfilment of the offer or purchase must be as simple as possible to avoid attrition during this process." (375)
Mit ad az alkalomhoz: a súrlódás témájának legközelebbi szó szerinti könyvi mondata: a konverziós lépés legyen a lehető legegyszerűbb.

**399–400. oldal, Hofacker öt akadálya.** Hofacker (2000) az információfeldolgozás öt szakaszát írja le (expozíció, figyelem, megértés, elfogadás, megjegyzés). Mindegyik akadály: ha a design vagy a tartalom túl nehezen feldolgozható, a látogató nem jut tovább a következő szakaszba. Az elfogadáshoz a szövegnek hiteles forrásra kell hivatkoznia.
Idézet: "Each of the five stages summarised in Table 7.3 acts as a hurdle, since if the site design or content is too difficult to process then the customer cannot progress to the next stage." (399) és "Copy should refer to credible sources and present" (400)
Mit ad az alkalomhoz: a beadandó akadálylistájához egy sorrendi keret is van: melyik szakaszban akad el a látogató (saját következtetés).

**396. oldal, flow és űrlapok.** A flow azt írja le, mennyire könnyen találja meg a felhasználó, amit keres, ahogy oldalról oldalra halad, és ide tartozik az űrlapok kitöltése is. Rettie (2001) szerint a flow feltételei közé tartozik a gyors letöltés és az űrlapok automatikus kitöltése.
Idézet: "'flow' essentially describes how easy it is for users to find the information or experiences they need as they move from one page of the site to the next, but it also includes other interactions such as filling in on-screen forms." (396) és "They include quick download time, alternative versions, auto-completion of forms" (396)

**399. oldal, szövegírási hibák.** A leggyakoribb hiba, hogy az oldal túl sokat feltételez a látogató tudásáról a cégről és a termékekről, és belső zsargont használ.
Idézet: "too much knowledge assumed of the visitor about the company, its products and" (399)

### Betöltési idő és elérhetőség

**372. oldal, a letöltési idő.** A letöltési teljesítmény a siker feltétele szélessávú kapcsolat mellett is. A Strangeloop (2011) kutatása szerint az elfogadható letöltési idő átlagosan három másodperc; a Trilibis (2014) szerint a vizsgált reszponzív oldalaknak csak 21%-a töltött be négy másodperc alatt okostelefonon. A lassúság fő oka a képek mérete.
Idézet: "page download performance is essential to the success of a site" (372), "average user perception of acceptable download time is three seconds" (372) és "only 21 per cent of these modern websites were loading in less than four seconds on a smartphone" (372)
Mit ad az alkalomhoz: a 15. dia betöltési adata; a számok 2011-es és 2014-es mérésből valók, jelenlegi adatnak külső forrás kell.

**373–374. oldal, elérhetőség és kampánykudarc.** A SciVisum (2005) szerint az internetes kampányok háromnegyedét érintik az oldal hibái. A marketingesek 37%-a nem tudta megmondani, mennyit veszítenek a megszakított tranzakciókon.
Idézet: "three-quarters of Internet marketing campaigns are impacted by website failures" (373) és "Thirty-seven per cent could not put a monetary value on losses caused by customers abandoning web transactions." (374)

**407. oldal, a nem elérhető oldal.** A megbízhatóság az oldal elérhetőségén múlik; aki akkor próbálkozik, amikor az oldal nem elérhető, végleg elveszhet.
Idézet: "potential customers may be lost for ever if they attempt to use the site when it is unavailable." (407)

### Bizalom, biztonság és adatkezelés

**358–359. oldal, az online márkaérték öt dimenziója.** Christodoulides et al. (2006) öt dimenzióval mérik az online márkaértéket: érzelmi kötődés, online élmény, válaszkészség, bizalom, teljesítés. A kérdések kész auditszempontként használhatók.
Idézet: "Q5: I never feel lost when navigating through [X]'s website." (358), "Q9: I trust [X] to keep my personal information safe." (359) és "Q10: I feel safe in my transactions with [X]." (359)
Mit ad az alkalomhoz: a bizalom itt mérhető kérdésként jelenik meg, a beadandóban átvehető állításként (saját következtetés).

**408. oldal, assurance: magánszféra és biztonság.** Az e-kereskedelmi oldal egyik bizalmi kérdése a vevői adatok védelme és biztonsága; Chaffey itt a 3. fejezetre utal. Chaffey és Smith (2012) teendői: világos adatvédelmi nyilatkozat, a helyi adatvédelmi és fogyasztóvédelmi szabályok követése, az adatbiztonság elsőbbsége, független tanúsítás.
Idézet: "provide clear and effective privacy statements;" (408) és "make security of customer data a priority;" (408)
Mit ad az alkalomhoz: az adatkezelés mint bizalmi elem a felületen; a GDPR maga nincs a fejezetben.

**409. oldal, opt-in és opt-out (7.5 táblázat).** Chaffey és Edgar (2000) követelménylistája szerint promóciós e-mailnél opt-in és opt-out lehetőség kell, és megfelelő ajánlat a vevő adataiért cserébe. A táblázat a beérkező levelekre automatikus visszaigazolást is előír.
Idézet: "Opt-in and opt-out options must be" (409) és "Use of autoresponders to confirm query" (409)
Mit ad az alkalomhoz: a 21. diához csak régi (2000-es) háttér; a táblázat oszlopai a szövegfájlban összekeveredtek, ezért csak rövid részlet idézhető.

**379. oldal, akadálymentesség mint jogi kötelezettség.** Sok országban akadálymentességi jogszabály vonatkozik a weboldalakra; Chaffey az Egyesült Királyság 1995-ös DDA-ját hozza példának, és a W3C WAI irányelveit.
Idézet: "legislation to which website owners are subject." (379)

### Regisztráció és e-mail a fejezetben

**377. oldal, regisztráció mint OVP (MyUltralase).** Az Ultralase oldalán a regisztráció maga is az értékajánlat része, célja a mélyebb kapcsolat és a visszatérés.
Idézet: "This site registration facility again shows the online value" (377) és "This is intended to encourage a deeper relationship and return visits." (377)

**394. oldal, a regisztráció elhagyása mint előny (FT.com).** Az FT a HTML5-ös webappja előnyei között sorolja fel, hogy a meglévő fiókkal működik, nem kell újra regisztrálni.
Idézet: "Use your existing account – no additional registration required." (394)
Mit ad az alkalomhoz: kis, kézzelfogható példa arra, hogy egy akadály (újabb regisztráció) elhagyását a cég maga hirdeti előnyként (saját következtetés).

**361. oldal, értéket adni a név elkérése előtt.** Blanks harmadik gyilkosánál az összehasonlító táblázat, fórum, különjelentés és e-mail marketing arra szolgál, hogy jó információt adjanak, nevet kérjenek, kapcsolatot építsenek, és így nőjön az eladás esélye.
Idézet: "allow you to provide good information, ask for names, cultivate a relationship and thereby improve the chances of a sale." (361)
Mit ad az alkalomhoz: híd a regisztrációs logika és az e-mail-folyamat között.

**360. oldal, autoresponder.** Jesson szerint az oldalon tesztelten működő előnyállítások átvihetők direkt levélbe vagy e-mail autoresponder kampányba, ott is teszteléssel.
Idézet: "might be transferable to direct mail or email autoresponder" (360)

**411–412. oldal, egy nyelvoktatási eset (i-to-i).** A 7. esettanulmány egy online TEFL-tanfolyamokat kínáló cégé. Külön landing page-eket használ a fizetett keresésből és affiliate-ekből érkezőknek, több lead-gyűjtő eszközt (brosúra, „TEFL taster”, e-mail útmutató, nyereményjáték), a leadeket üdvözlő e-mail-sorozat követi, telefonos utókövetés nincs.
Idézet: "Specific landing pages are used" (411) és "proactively followed up on. There is no phone follow-up" (412)
Mit ad az alkalomhoz: nyelvoktatási példa, Anna nyelviskolás történetéhez közel áll (saját következtetés). Az üdvözlő levelekről szóló mondat elválasztás miatt nem idézhető.

### Merchandising és értékelések

**402–403. oldal, online merchandising.** Az online bolt célja minden látogatónál a lehető legtöbb eladás: releváns termékek és promóciók, szinonimák a keresésben, szűrhető (faceted) navigáció, bestsellerek, csomagajánlat. A kapcsolódó termékek felajánlása a termékoldalon vagy a pénztárban óvatosságot kíván, mert csökkentheti a konverziót. A vásárlói értékelések befolyásolják az eladást: a CompUSA-nál 60%-kal magasabb konverziót hoztak.
Idézet: "Online, this means presenting relevant products and promotions" (402), "product page or in checkout, although care has to be taken here since this can reduce" (402), "Reviews can be important in influencing sales." (403) és "60 per cent higher conversion;" (403)
Mit ad az alkalomhoz: a pénztárban felkínált plusz termék olyan hozzáadott elem, ami ronthatja a konverziót (saját következtetés).

**403–404. oldal, figleaves.com (7.6 mini esettanulmány).** A fehérneműket árusító figleaves.com OVP-je elemenként: kínálat, könnyű keresés, „no hassle” visszaküldés (az Egyesült Királyságban a postaköltséget is állják), otthoni felpróbálás próbafülke helyett, ajándékozás, 24 órán belüli feladás. A Bazaarvoice adatai szerint az értékeléssel rendelkező termékek konverziója 12,5%-kal magasabb.
Idézet: "You can easily return goods if they don't fit or if they don't meet your expectation." (404), "What's more, you can check out your purchases at home – no queuing for or embarrassing moments in luridly lit changing rooms." (404) és "Overall, products with reviews have a 12.5 per cent higher conversion rate than those without." (404)
Mit ad az alkalomhoz: a 12. dia „mások értékelése” része, és a figleaves OVP-je szinte minden pontjában egy kockázatot vagy kellemetlenséget vesz le (visszaküldés, kínos próbafülke), ami a 14. diához is jó példa (saját következtetés).

### Szolgáltatásminőség és lojalitás

**404–406. oldal, SERVQUAL, WEBQUAL, E-SERVQUAL.** Parasuraman et al. (1985) öt dimenziója (kézzelfoghatóság, megbízhatóság, válaszkészség, biztosíték, empátia), a WEBQUAL 14 dimenziója és az E-SERVQUAL hét dimenziója. Chaffey szerint mindkettő jelenleg is használható, de kimarad belőlük az akadálymentesség, a megtalálhatóság, a többcsatornás integráció és a vásárlói értékelés.
Idézet: "Both are useful frameworks which can still be applied to evaluate online service quality today, although arguably they omit the importance of accessibility, findability techniques, multichannel integration and customer reviews and ratings" (406)

**407. oldal, elérhetőség a kapcsolatfelvételhez.** Upton (2008) kutatásában tízből három brit fogyasztó nehezen találta meg a kapcsolati adatokat a weboldalon.
Idézet: "they found it difficult to locate contact details on websites." (407)

**408–409. oldal, a szolgáltatási ígéret.** A SERVQUAL alkalmazásának három lépése: az elvárások megértése, az ígéret megfogalmazása és kommunikálása, az ígéret teljesítése. Jobb kevesebbet ígérni, mint többet; ha az ígéret nem teljesül, az online hitelesség elvész.
Idézet: "It is better to under-promise than over-promise." (408–409), "A book retailer who delivers a book in two days when three days were promised will earn the customer's loyalty better than the retailer who promises one day but delivers in two!" (409) és "Otherwise, online credibility is destroyed and a customer may never return." (409)
Mit ad az alkalomhoz: a bizalom témájához: az oldal ígér, és az oldalnak kell teljesítenie, különben a hitelesség elvész.

**410. oldal, lojalitás.** Rigby et al. (2000) szerint az ismételt vásárlás fő mozgatói a pontos kiszállítás mellett az ár, a könnyű használat és az ügyfélszolgálat.
Idézet: "including correct delivery of order, but other factors such as price, ease of use and" (410)
Mit ad az alkalomhoz: a loyalty logikához a fejezet csak ennyit ad; a programokról (pontgyűjtés, klub) nem ír.

## Chaffey, Ellis-Chadwick, 6. fejezet (Relationship marketing using digital platforms)

Digital Marketing, 6. kiadás. Forrásfájl: `konyvek/chaffey-ch6-relationship-marketing.txt`. Feldolgozva: 2026. október 5. Minden idézetet és oldalszámot a `findq.py` adott vissza.

**A fájl hiányos az elején.** A szöveg a 301. oldallal kezdődik, a fejezet nyitóoldala (vagy nyitóoldalai) hiányzik: a tanulási célok, a bevezető és a Zappos-eset (Mini case study 6.1) eleje. Az első sor („Repeat customers spend more.”) még a 300. oldal maradéka, a futófej előtt áll, ezért a `findq.py` nem ad rá oldalszámot. A fájl a 350. oldal után a 3. rész nyitószövegével zárul.

**Kinyerési hibák, amikre figyelni kell.** A margón álló definíciós dobozok szövege sok helyen a főszöveg sorai közé került, ezért több hosszabb mondat csak rövidebb részletben ellenőrizhető. A Table 6.1 (321. oldal) két cellája sérült, lásd lent.

### Az engedélyalapú marketing és az opt-in

**313–314. oldal, Godin és az engedély.** A fogalmat Seth Godin vezette be 1999-ben, és Chaffey szerint ez az online CRM alapja az ügyfél életciklusában. Godin a hagyományos megközelítést „interruption marketing” néven írja le, az engedélyalapú marketing ezzel szemben engedélyt kér, mielőtt kapcsolatba lép, és ad valamit cserébe. A klasszikus csere információ vagy szórakozás: B2B oldalon egy ingyenes riport az e-mail-címért. Az opt-in az, amikor a látogató egy jelölőnégyzettel maga kéri a további leveleket; Chaffey szerint ez jobb az opt-outnál.
Idézet: „anticipated, relevant and personal [and timely].” (313.) · „seeking the customer’s permission before engaging them in a relationship” (313.) · „and providing something in exchange. The classic exchange is based on information or entertainment” (314.) · „This approach is widely known as opt-in.” (314.) · „is preferable to opt-out” (314.)
Mit ad az alkalomhoz: a regisztrációs dia (17.) elméleti alapja, a feliratkozás mint csere.

**313. oldal, a megszakítás ára.** Godin szerint a napi 500 marketingüzenetből a web és a digitális tévé után napi 3000 fölötti lett, és ettől minden egyes üzenet hatása hígul.
Idézet: „we were bombarded by 500 marketing messages a day” (313.) · „Godin refers to the traditional approach as interruption marketing.” (313.)
Mit ad az alkalomhoz: magyarázat arra, miért nem elég a forgalmat megvenni, és miért ér többet az engedély.

**314. oldal, a randevú-hasonlat öt lépése.** Godin az ügyfélszerzést és megtartást randevúhoz hasonlítja. Az öt lépés: ösztönzőt adni, hogy a vevő önként jelentkezzen; a figyelmét egy időben elnyújtott „tananyaggal” használni; az ösztönzőt megerősíteni, hogy az engedély megmaradjon; újabb ösztönzővel több engedélyt kérni; idővel az engedélyt nyereséges viselkedésre váltani. Chaffey hozzáteszi, hogy a gyakorlatban a látogatót továbbra is valamilyen „megszakítással” kell az oldalra hozni (keresés, közösségi média, remarketing).
Idézet: „Godin (1999) suggests that dating the customer involves:” (314.) · „offering the prospect an incentive to volunteer;” (314.) · „using the attention offered by the prospect, offering a curriculum over time” (314.) · „reinforcing the incentive to guarantee that the prospect maintains the permission;” (314.) · „offering additional incentives to get even more permission from the consumer;” (314.) · „over time, using the permission to change consumer behaviour towards profits.” (314.) · „In practice, new forms of ‘interruption’ are required.” (314.)
Mit ad az alkalomhoz: az e-mail-folyamat (beadandó) gerince lehet: először ösztönző, aztán fokozatos tartalom, aztán további engedély.

**309. oldal, az előminősített lista.** Az engedélyalapú (inbound) marketing előnye, hogy a kontaktlista önkiválasztott, és levelet csak annak kell küldeni, aki kérte.
Idézet: „self-selecting or pre-qualified.” (309.) · „information needs to be sent only to those customers who have expressed a preference for it” (309.)
Mit ad az alkalomhoz: érv arra, hogy a saját lista minősége fontosabb a méreténél.

### Mit adsz cserébe: ösztönző, űrlap, WIFM

**314. oldal, a folyamat 1., 2a. és 2b. lépése (Figure 6.5).** Az engedélyalapú kapcsolatépítés lépései: 1. a látogatót a saját felületre hozni; 2a. ösztönözni a cselekvésre; 2b. adatot gyűjteni a kapcsolat fenntartásához. Az ösztönző kétféle lehet: leadgeneráló ajánlat vagy eladásgeneráló ajánlat. Az ajánlat típusai: információs érték, szórakoztató érték, pénzbeli érték és kiváltságos hozzáférés, és ezeket A/B teszttel lehet finomítani. A Facebookon a cégek „kapus” oldalakat használtak, ahol előbb lájkolni kellett.
Idézet: „Stage 1. Attract new and existing customers to online presence.” (314.) · „Stage 2a. Prompt and incentivise visitors to action.” (314.) · „lead generation offers and sales generation offers.” (314.) · „monetary value and privileged access to information” (314.) · „Stage 2b: Capture customer information to maintain relationship.” (314.)
Mit ad az alkalomhoz: a landing page-audit egyik kérdése: mit kínál az oldal az adatért cserébe.

**316. oldal, az űrlap tervezése.** Az űrlapot úgy kell megtervezni, hogy minél többen kitöltsék. Chaffey hét szempontot sorol: márkajelzés a megnyugtatásra, csak a legfontosabb profilmezők (ne legyen túl sok kérdés), a kötelező mezők jelölése, adatvédelem („we will not share”), KISS, WIFM (miért kéred az adatot, mit kap érte), és az adatok ellenőrzése.
Idézet: „It is important to design these forms to maximise their completion.” (316.) · „branding to reassure the customer;” (316.) · „(not too many questions should be asked);” (316.) · „mandatory fields – mark fields which must be completed” (316.) · „privacy – ‘we will not share’ is the magic phrase to counter the customer’s main fear of their details being passed on;” (316.) · „a full privacy statement should be available for those who need it;” (316.) · „KISS – ‘Keep it simple, stupid’ is a well-known American phrase;” (316.) · „WIFM – ‘What’s in it for me?’ Explain why the customer’s data is being captured; what benefits it will give them?” (316.) · „validation – of email, postcode etc., checking data as far as possible to make it accurate.” (316.)
Mit ad az alkalomhoz: ez a hét szempont szinte változtatás nélkül használható ellenőrzőlista a beadandó űrlap-részéhez.

**319. oldal, többféle ösztönző.** A 3. e-permission elv: sok oldalon egyetlen „free–win–save” ösztönző van mindenkinek, pedig a különböző közönségeknek szóló különböző ösztönzők több engedélyt hoznak.
Idézet: „Principle 3 – Offer a range of opt-in incentives.” (319.) · „Different incentives for different audiences will generate a higher volume of permission” (319.)
Mit ad az alkalomhoz: a See és a Do fázisból érkező látogatónak más ösztönző kell; ez a szöveg a 11. dia saját következtetését támasztja alá, ha óvatosan használjuk (saját következtetés).

### Adatgyűjtés fokozatosan: „Watch, don’t ask”

**319. oldal, figyelj, ne kérdezz.** Az 5. e-permission elv: a megszakító kérdések száma csökkenthető, ha a kattintásokat figyeled, és ezekből indítod a következő levelet. Példák: melyik tartalomra vagy ajánlatra kattint, mennyire foglalkozik a levelekkel, és emlékeztető annak, aki elsőre nem nyitotta meg. A 3. elvnél Chaffey ugyanezt mondja az ösztönzőkről: abból, hogy ki milyen ösztönzőt kért, kérdezés nélkül is lehet következtetni.
Idézet: „Principle 5 – Watch, don’t ask (or ‘Sense and Respond’).” (319.) · „The need to ask interruptive questions can be reduced through the use of monitoring clicks to better understand customer needs and to trigger follow-up communications.” (319.) · „follow-up reminder to those who don’t open the email first time.” (319.) · „We can also gauge the characteristics of the respondent by the type of incentives or communications they have requested, without the need to ask them.” (319.)
Mit ad az alkalomhoz: a 17. dia „ne kérdezz meg mindent az elején” mondatának pontos forrása.

**316–317. oldal, a profil bővítése később.** Az első adatgyűjtés után az adatot bővíteni kell, és minden érintkezési pontot (online és offline) érdemes erre használni. A 3. és 4. lépés további célja az adatminőség javítása.
Idézet: „As well as online data capture, it is important to use all customer touchpoints to capture” (316.) · „Once data has been initially collected, it should be added to gain a better understanding” (317.) · „A further objective in stage 3 and stage 4 is to improve customer information quality.” (317.)
Mit ad az alkalomhoz: a regisztráció nem egyszeri űrlap, hanem lépcsőzetes adatgyűjtés, ami a súrlódás csökkentésének egyik módja (saját következtetés).

**319. oldal, a közös ügyfélprofil.** A 2. elv: kell egy előre definiált adatkör, különben kimarad valami. A példa egy közműcég, amely 80 000 e-mail-címet gyűjtött, de elfelejtette elkérni az irányítószámot.
Idézet: „Principle 2 – Create a ‘common customer profile’.” (319.) · „forgot to ask for the post- code for geo-targeting!” (319.)
Mit ad az alkalomhoz: ellenpont a „kérdezz kevesebbet” elvhez: a kevés kérdésnek a jó kérdésnek kell lennie.

### Az e-CRM és az ügyfél életciklusa

**302. és 308–309. oldal, az e-CRM mint „sense and respond”.** Chaffey szerint az e-CRM érzékelő és reagáló kommunikáció, a klasszikus példa az Amazon személyre szabott ajánlása e-mailben és az oldalon. A digitális kapcsolatmarketing az ügyféladatbázist köti össze a weboldallal és az üzenetekkel. Az egyik előny az alacsonyabb költség: a személyre szabó technológia megvétele után a célzás és a kommunikáció nagy része automatikusan fut.
Idézet: „E-CRM, can be characterised as sense and respond communications.” (302.) · „Once personalisation technology has been purchased, much of the targeting and communications can be implemented automatically.” (309.)
Mit ad az alkalomhoz: az „automatizált e-mail” tematikai pont könyvbeli definíciója.

**311–312. oldal, az életciklus négy szakasza (Figure 6.4).** A klasszikus életciklus: kiválasztás, megszerzés, megtartás, bővítés. Online a megszerzés lehet egylépéses (első látogatásra vásárol), de jellemzően többlépéses, a látogató visszatér. A konverziót úgy lehet segíteni, hogy az első kapcsolatot egy elérhetőség elkérésével alakítod ki; Chaffey ezt nevezi engedélyalapú megközelítésnek.
Idézet: „A high-level view of the classic customer lifecycle of select, acquire, retain, extend” (311.) · „For an online business, acquisition may involve a single-step conversion” (312.) · „Typically, a longer, multi-step process is needed for conversion to sale where a visitor returns to the site.” (312.) · „To facilitate conversion, customer lifecycle marketing should seek to form an initial relationship through asking for contact details” (312.)
Mit ad az alkalomhoz: ez köti össze a landing page-et és az e-mailt: aki most nem vesz, annak az elérhetőségét kell megszerezni.

**308. oldal, az elköteleződés nem egy érintési pont.** Az engagement szót néha egyetlen érintési pontra használják (mennyi időt tölt az oldalon, konvertál-e), Chaffey szerint viszont a márka hosszú távú képességét jelenti, hogy újra és újra megszerezze a figyelmet. Az elköteleződés üzleti célja az ügyfélérték maximalizálása.
Idézet: „whether someone dwells on” (308.) · „really refers to the long-term ability of a brand to gain a customer’s attention” (308.) · „The commercial aim of engagement is to maximise customer value” (308.)
Mit ad az alkalomhoz: a weboldal eseményeihez ad ellenpontot: az oldalon töltött idő vagy egy konverzió egyetlen érintési pont, az elköteleződés ennél hosszabb távú.

**329. oldal, aktivitás szerinti szegmentálás (Figure 6.14).** Regisztrációs oldalaknál négy csoport: új, aktív, alvó és inaktív (regisztrált, de nem használta). A célok: több aktív, kevesebb alvó és kevesebb inaktív felhasználó.
Idézet: „Increasing the percentage of active users” (329.) · „Decreasing the percentage of inactive users (or non-activated) users.” (329.)
Mit ad az alkalomhoz: a regisztráció nem a cél vége; az inaktív regisztrált a regisztrációs logika vakfoltja.

### Az üdvözlő sorozat és az automatizált életciklus-levelek

**320–321. oldal, Table 6.1 (Example welcome contact strategy).** Chaffey a táblát olyan kapcsolati stratégiának vagy e-mail-sorozatnak mutatja be, amelyben viselkedési triggerek indítják a személyre szabott levelet. A tábla oszlopai: Message type, Interval/trigger condition, Outcomes required, Medium for message/sequence. A sorok, szó szerint a fájlból:

| | Message type | Interval/trigger condition | Outcomes required | Medium for message/sequence |
|---|---|---|---|---|
| 1 | Welcome message | Guest site membership signup, Immediate | Encourage trial of site services; Increase awareness of range of commercial and informational offerings | Email, post transaction pa [a cella a nyomtatott könyvben is így, csonkán áll] |
| 2 | Engagement message | 1 month inactive (i.e. <3 visits) | Encourage use of forum (good enabler of membership); Highlight top content | Email, home page, side panels deep in site |
| 3 | Initial cross-sell message | 1 month active | Encourage membership; Ask for feedback | Email |
| 4 | Conversion | 2 days after browsing content | Use for range of services for guest members or full [a cella a nyomtatott könyvben is így, csonkán áll] | Phone or email |

Megjegyzés a táblához: a 2026. október 5-én kapott teljes könyv PDF-jének 321. oldalán ellenőrizve. A szövegfájl „(i.e. 63 visits)” cellája a könyvben „(i.e. <3 visits)”, a kinyeréskor sérült. Az 1. sor médium-cellája („Email, post transaction pa”) és a 4. sor eredmény-cellája („Use for range of services for guest members or full”) a könyvben is csonkán áll, ez szedési hiba a kiadásban; a dián ezek nem idézhetők teljes mondatként.
Idézet: „Table 6.1 shows a recommended approach for developing a contact strategy or email communications sequence involving different behavioural trigger events which prompt broadcast of a personalised email.” (320.) · „Example welcome contact strategy” (321.) · „Encourage trial of site services” (321.) · „1 month inactive” (321.) · „(i.e. 63 visits)” (321.) · „2 days after browsing” (321.)
Mit ad az alkalomhoz: a 19. dia és a beadandó e-mail-folyamatának mintája, triggerrel, céllal és csatornával.

**322. oldal, automatizált életciklus-levelek.** Az „érzelmileg leiratkozottak” kezelésének egyik lépése: automatizált életciklus-leveleket kell a kapcsolati stratégia részévé tenni, az előfizető érdeklődéséhez szabva. Ide tartozik az üdvözlő sorozat, a visszaaktiváló sorozat és a szolgáltatási üzenetek, például az elégedettségi kérdőív.
Idézet: „Develop automated customer lifecycle emails as part of the contact strategy” (322.) · „relevant and tailored according to the interests of the subscriber.” (322.) · „Lifecycle emails will include welcome email contact strategies, reactivation email strategies and other service messages such as customer feedback surveys.” (322.)
Mit ad az alkalomhoz: az életciklus-levelek három típusa, amit a beadandó e-mail-folyamata lefedhet.

**320–322. oldal, az érzelmileg leiratkozottak.** A leiratkozási arány alacsony (kampányonként 0,1% alatt), de a lista akár több mint fele „érzelmileg leiratkozott”: nem iratkozott le, csak ritkán nyit vagy kattint. Chaffey javaslatai: finomabb aktivitásmérés, a gyakoriság tesztelése (akár csökkentése), életciklus-levelek, és olyan mezők a személyre szabáshoz, amelyek tényleg relevánsak. Ezek gyakran nem a nem, hanem a nemrég nézett tartalom vagy termék.
Idézet: „there can be upwards of 50 per cent of a list who are ‘emotionally unsubscribed’” (320.) · „they are not actually unsubscribed but rarely open or click” (320.) · „It may be appropriate to reduce frequency if customers” (321.) · „Often these won’t be the obvious fields such as gender” (322.)
Mit ad az alkalomhoz: figyelmeztetés a beadandóhoz: a feliratkozás után a lista csendben elhalhat, ha a folyamat nem releváns.

### „Right touching”: a kapcsolati stratégia

**319–320. oldal, right touching (Digital marketing insight 6.1).** A szakasz címe a 319. oldalon kezdődik: a médiafragmentáció miatt strukturált, csatornákon átívelő kapcsolati stratégia kell. A 320. oldali keret szerint ez olyan többcsatornás stratégia, amely a meghatározott életciklus mentén a megfelelő üzenetet, értékajánlatot, hangnemet, időzítést, gyakoriságot és csatornát adja, és a cél a két fél közti érték egyensúlya. Minden interakciót releváns üzenetsornak kell követnie; Chaffey ezt kontextuális marketingnek hívja.
Idézet: „‘Right touching’ through developing online contact strategies” (319.) · „Right touching can be summarised as:” (320.) · „Delivers the Right Message” (320.) · „At the Right Time or context” (320.) · „With the Right Frequency and Interval” (320.) · „Right balance of value between both parties” (320.) · „Every customer interaction or response to a communication should be followed up by a series of relevant communications delivered by the right combinations of channel” (320.) · „where the aim is to deliver relevant messages which fit the current context of” (320.)
Mit ad az alkalomhoz: a 19. dia „right touching” elve, a 2. alkalom „jó üzenet rossz időben” gondolatának folytatása (saját következtetés).

**319–320. oldal, a kapcsolati szabályzat.** A 6. elv szerint kell egy kimenő kapcsolati stratégia a levelek számáról, gyakoriságáról és típusáról. A szabályzat elemei: gyakoriság (például legalább negyedévente, legfeljebb havonta), intervallum (legalább egy hét vagy egy hónap két üzenet között), tartalom és ajánlat, az online és offline kapcsolat összekötése, és egy ellenőrzési pont.
Idézet: „Principle 6 – Create an outbound contact strategy.” (319.) · „A contact policy should be developed to manage and control communications so that they are at an acceptable level.” (320.) · „Frequency – e.g. minimum once per quarter and maximum once per month.” (320.) · „Interval – e.g. there must be a gap of at least one week or one month between communications.” (320.)
Mit ad az alkalomhoz: a beadandó e-mail-folyamatában a gyakoriság és az intervallum kötelező mező lehet.

**341. oldal, Guess: „batch and blast” helyett relevancia (Mini case study 6.7).** A Guess három éve heti három-négy levelet küldött mindenkinek, és tudta, hogy ezzel valószínűleg irritálja a vevőit. A gyakoriság csökkentése helyett a relevanciát növelte: a kiegészítőket kedvelő perszóna kiegészítő-fókuszú levelet kapott, és ennek a csoportnak a CTR-je és konverziója messze meghaladta a sima levelet kapókét.
Idézet: „Three years ago we were emailing customers three, possibly four times a week.” (341.) · „We were very much ‘batch and blast’” (341.) · „One option was to cut back on emails.” (341.) · „The CTR and conversion rate of group A far exceeded those of” (341.)
Mit ad az alkalomhoz: második eset a 20. dia mellé, ha egy WHSmith-példa kevés.

### Kosárelhagyás és esetek: WHSmith

**321. oldal, Mini case study 6.4 (WHSmith use behavioural email to encourage engagement).** Klasszikus kosárelhagyó utánkövető levél, három változatban tesztelve. 1. általános, márkázott levél: +10% konverzió. 2. személyre szabott levél 5%-os, 72 órára szóló kuponkóddal: +100%. 3. ugyanez 48 órás határidővel: +200%. Egy utólagos felmérés azokat kérdezte, akik a levélből visszakattintottak és vásároltak, de a kódot nem használták. Ők a levelet emlékeztetőnek vették a visszatérésre, és a határidő hozta vissza őket, bár a kedvezményt végül nem vették igénybe.
Idézet: „Behavioural email marketing or remarketing is a classic ‘sense and respond’ e-CRM approach.” (321.) · „a classic abandoned shopping cart follow-up email, but with three alternative communications which were tested with these results:” (321.) · „Generic branded follow-up email: + 10 per cent conversion rate.” (321.) · „Personalised remarketing email with a promotional code for a 5 per cent discount time-limited to 72 hours: + 100 per cent conversion rate.” (321.) · „time-limited to 48 hours: + 200 per cent conversion rate.” (321.) · „These customers had still reacted to the remarketing email as a prompt to return to the WHSmith website.” (321.) · „It was the expiry date of the call to action that had prompted them to return, even though they then did not take advantage of the 5 per cent discount promo code.” (321.)
Mit ad az alkalomhoz: a 20. dia esete, azzal a pontosítással, hogy a felmérés csak a kódot nem használó vásárlókra szól, és náluk a határidő volt a visszahozó tényező.

### Pop-up: több lead, több bosszúság

**314. oldal, Figure 6.6.** A feltűnő cselekvésre hívás vagy pop-up növeli a konverziót. Chaffey évekig ellenállt a pop-upnak, de a Smart Insights oldalon bevezetve 40%-kal nőtt a leadkonverzió. Sok felhasználót bosszant, az oldaltulajdonosnak viszont több leadet hoz, ezért a pop-upok száma nő, és valószínűleg nőni is fog.
Idézet: „prominent calls-to-action or pop-ups can boost” (314.) · „which was resisted by Dave” (314.) · „Chaffey for several years, increased lead conversion by 40 per cent” (314.) · „Many web users will be annoyed by pop-ups, yet for site owners they do increase the number of leads” (314.) · „so the number of pop-ups is now increasing and is likely to do so further.” (314.)
Mit ad az alkalomhoz: a vitapont forrása: a pop-up akadály a látogatónak, mégis több leadet hoz, ami feszül azzal, hogy az akadályokat el kell venni.

### Leiratkozás: szándékos súrlódás

**319. oldal, a 4. elv (Don’t make opt-out too easy).** Chaffey szerint a marketingesek gyakran túl könnyűvé teszik a leiratkozást. A leiratkozás lehetősége sok országban jogi kötelezettség, de az egykattintásos leiratkozás szerinte túl könnyű. Helyette egy beállítási oldalt javasol (Amazon: „My Profile”), ahol a vevő ritkíthatja a leveleket, és sokan ezt választják a teljes leiratkozás helyett.
Idézet: „Principle 4 – Don’t make opt-out too easy.” (319.) · „Although offering some form of opt-out is now a legal requirement in many countries due to privacy laws” (319.) · „a single click to unsubscribe is making it too easy.” (319.) · „offer a link to a ‘communications preferences’ or ‘customer centre’ web form” (319.) · „which may be the option taken rather than unsubscribing” (319.)
Mit ad az alkalomhoz: második vitapont a súrlódásról; ez a 2016-os szöveg, és a jelenlegi jogi helyzettel külön forrásból kell összevetni (lásd a 21. diánál).

**317–319. oldal, választható opt-in.** Az 1. elv: a vevő választhasson tartalmat, gyakoriságot, csatornát és formátumot. Chaffey itt is jelzi, hogy az opt-in sok országban jogi kötelezettség.
Idézet: „Principle 1 – Consider selective opt-in to communications.” (317.) · „Some customers may not want a weekly e-newsletter; rather, they may only want to hear about new product releases.” (317.) · „Remember opt-in is a legal requirement in many countries.” (317.) · „Content – news, products, offers, events.” (317.) · „Channel – email, social network, direct mail, phone or SMS.” (319.)
Mit ad az alkalomhoz: a feliratkozási űrlap és a beállítási központ mint a saját felület része.

### Adatkezelés, bizalom, kontroll

**313. oldal, Integrity (Peppers és Rogers 5I modellje).** Az ötödik I: minden kapcsolat bizalomra épül, ezért a vevő bizalmát nem szabad elveszíteni. A tanulás a vevőről nem lehet tolakodó, és a magánszférát meg kell őrizni. Az adatvédelmi kérdéseket Chaffey a 3. fejezetre utalja.
Idézet: „Integrity. Since all relationships are built on trust” (313.) · „Efforts to learn from the customer should not be seen as intrusive, and privacy should be maintained.” (313.) · „(See Chapter 3 for coverage of privacy issues related to e-CRM.)” (313.)
Mit ad az alkalomhoz: a bizalom témájához kapcsolható könyvbeli mondat, és átvezet az adatkezeléshez.

**322. oldal, Tucker (2014): több kontroll, jobb válasz.** Nem mindenki fogadja jól a személyre szabást, egyesek a személyes adatok biztonsága miatti félelem miatt negatívan reagálnak. Tucker Facebook-hirdetéseken azt találta, hogy akik több kontrollt kaptak az adatvédelmi beállítások felett, azok pozitívabban reagáltak a személyre szabott üzenetekre. Chaffey következtetése: érdemes több kontrollt adni a vevőnek az adatai felett.
Idézet: „due to fears over security of personal data” (322.) · „Tucker (2014) found that when” (322.) · „individuals were given more control over privacy settings they were more likely to respond” (322.) · „positively to personalised communications.” (322.) · „should consider giving individuals more control over how” (322.)
Mit ad az alkalomhoz: a 21. dia „ez is bizalom” mondatának könyvbeli alátámasztása.

**347–348. oldal, gyakorló kérdések.** A fejezet végi kérdések között szerepel az adatvédelmi aggályok kezelése, a jogi és etikai korlátok, és három intézkedés a magánszféra védelmére.
Idézet: „How can customer concerns about privacy be responded to when conducting one-to-one marketing using the Internet?” (347.) · „Explore the legal and ethical constraints on implementing relationship marketing using the digital media.” (348.) · „Suggest three measures a company can take to ensure that a customer’s privacy is not infringed when conducting one-to-one marketing.” (348.)
Mit ad az alkalomhoz: kész vitakérdések a GDPR-blokkhoz; a válaszhoz a fejezet önmagában nem elég.

### E-mail kontra közösségi platform, saját kontra kölcsönzött felület

**317. oldal, az e-mail személyre szabható, a közösségi háló nem.** A 3. lépés digitális csatornái: személyre szabott e-mail, személyre szabott tartalom belépés után, és tartalomterjesztés RSS-en vagy közösségi hálón. A közösségi hálóknak az a korlátja, hogy nincs olyan szintű engedély, amellyel a profiladat elérhető, és az üzenet nem szabható személyre. Az engedélyalapú marketing a közösségi hálón a lájk vagy a követés, de az e-mail előnye, hogy egyénre szabható.
Idézet: „Social networks have the limitation currently of not having a level of permission where profile information can be accessed, and messages can’t be personalised.” (317.) · „Of course, email offers a key benefit over social media channels since it can be tailored to the individual.” (317.)
Mit ad az alkalomhoz: a 9. dia pontos forrása.

**342–343. oldal, közösség saját oldalon vagy más platformon.** A cégnek két útja van: a közösséget más oldalakon építi (earned media), vagy a saját oldalán (owned media). A saját közösség jobban illeszkedik a márka céljaihoz, és mivel a regisztrált tagok a cég adatbázisában vannak, e-mail-marketingre és kutatásra is lehetőséget ad. A független közösségi hálókon a hirdetésekre adott válasz alacsony, mert a felhasználók figyelme az interakción van.
Idézet: „They can either create community through other sites (earned media, Chapter 1) or provide community facilities on their own site (owned media).” (342.) · „Since registered members of the community will be on the company database, the community will provide opportunities for email marketing” (343.) · „for the advertisers responses tend to be low because the focus of users is on interacting, not on the ads.” (343.)
Mit ad az alkalomhoz: az owned media fogalma itt van meg: a saját oldalon a regisztrált tag a cég adatbázisába kerül, ez a regisztráció és az e-mail témájához kapcsolódik. A „bérelt figyelem” szó nem Chaffeyé.

**304–305. oldal, ellenpont: szolgálj ott, ahol a vevő van (Guy Stephens-interjú).** Stephens szerint a cégek régen minél hamarabb vissza akarták hozni az interakciót a saját weboldalukra vagy ügyfélszolgálatukra, jelenleg viszont a „service at source” felé tolódnak. A Best Buy idézett mondata szerint nem akarják, hogy a vevőnek el kelljen hagynia a Facebookot egy kérdés miatt.
Idézet: „Traditionally, companies would have looked to bring the interaction back to their website or into the contact centre as soon as possible.” (304–305.) · „‘service at source’ for customers.” (304.) · „we want them to ask it there.” (305.)
Mit ad az alkalomhoz: ellenpont a weboldal központi szerepéhez, a 9. diához jó vitakérdés (a Zing Burger és a Wolt esete mellé).

### Loyalty és megtartás

**309. oldal, hűségprogramok az e-CRM-ben.** A hűségprogramok (Tesco Clubcard, Nectar, légitársaságok, szállodaláncok) a bővítést és a megtartást ösztönzik. E-CRM-ben így használják őket: kezdő bónuszpont a regisztrációért, több pont a második vagy harmadik online vásárlásért, extra pont a visszaaktiválásért, és népszerű termékek kevés pontért az ismételt vásárlás ösztönzésére.
Idézet: „Loyalty schemes are often used to encourage customer extension and retention.” (309.) · „initial bonus points for sign-up to online services or initial registration;” (309.) · „points for customer development or extension” (309.) · „Popular products are offered for a relatively low number of points to encourage repeat purchases.” (309.)
Mit ad az alkalomhoz: a 18. dia „regisztrációs és loyalty logika” pontjának Chaffey-féle kiegészítése a Kotler-forrás mellé.

**324–325. oldal, érzelmi és viselkedési hűség (Figure 6.11).** Chaffey kétféle hűséget különít el: az érzelmit (kedvező megítélés, vélemény, ajánlás) és a viselkedésit (ismételt vásárlás, visszatérés, válasz a kampányokra). Az érzelmi hűséget leginkább az online élmény befolyásolja; a Figure 6.11 elégedettségi tényezői között ott van az értékajánlat, a könnyű használat, a teljesítmény, a vizuális dizájn és a megnyugtatás. Az elégedettség és a hűség nem feltétlenül jár együtt.
Idézet: „where loyalty to a brand is demonstrated by” (324.) · „favourable perceptions, opinions and recommendations including social sharing.” (324.) · „The second type of loyalty is behavioural loyalty” (324.) · „how many online sites have you continued to use after a poor level of service was delivered?” (324.) · „Value proposition” (325.) · „Ease of use” (325.) · „Reassurance” (325.) · „there may be customers with a high degree of satisfaction who don’t exhibit behavioural loyalty” (325.)
Mit ad az alkalomhoz: a márkáról kialakuló képhez: az érzelmi hűség a megítélésen múlik, és azt az oldal élménye formálja.

**343. oldal, a hiányzó elem: az ügyfélélmény.** A fejezet zárógondolata: a legrelevánsabb kommunikáció is kudarcot vall, ha az élmény rossz. Ha az első vagy visszatérő látogatás lassan betöltő, nehezen használható oldalon történik, nem alakul ki hűség. Ezt Chaffey a 7. fejezetben tárgyalja.
Idézet: „Customer experience – the missing element required” (343.) · „even the most relevant communications will fail if another key factor is not taken into account – this is the customer experience.” (343.) · „If a first-time or repeat customer experience is poor due to a slow-to-download difficult-to-use site, then it is unlikely that loyalty from the online customer will develop.” (343.) · „In the next chapter we review techniques used to help develop this experience.” (343.)
Mit ad az alkalomhoz: híd a 6. és a 7. fejezet között, és az alkalom két felének (felület és e-mail) összekötése.

### Ami még releváns

**301. oldal, Zappos (Mini case study 6.1 vége).** A Zappos-eset második pontja szerint a vásárlás kockázatát le kell venni a vevőről, a visszaküldés legyen ingyenes és egyszerű, a gyors és pontos teljesítés pedig szájreklámot hoz. Az eset eleje hiányzik a fájlból.
Idézet: „Make it easy for customers to build your brand” (301.) · „Remove the risk of purchase and make it easy to return products for free.” (301.) · „Fast, accurate fulfilment is worth talking about.” (301.)
Mit ad az alkalomhoz: példa egy akadály elvételére (a vásárlás kockázata, ingyenes visszaküldés), és a Printa csapat visszaküldési aggályához is kapcsolódik.

**307. oldal, integráció a csatornák között (Guy Stephens).** Stephens szerint a holisztikus élménynek abban kell segítenie a vevőt, hogy elérje, amit akart, anélkül, hogy közben feldühítenék.
Idézet: „ensuring the holistic customer experience helps them achieve what they set out to achieve without, bluntly, ‘pissing them off’ along the way.” (307.)
Mit ad az alkalomhoz: egy gyakorló szakember mondata a súrlódásról, a vevő céljából nézve.

**317. oldal, a 4. lépés: offline csatornák.** A postai levél vagy a telefon még költséghatékony lehet, és jobban átütheti a figyelmet, mint egy e-mail.
Idézet: „may have more ‘cut-through’ compared to an email.” (317.)
Mit ad az alkalomhoz: a Levendula-esethez (offline márka): az e-mail-folyamat nem az egyetlen út.

**335. oldal, recency (Novo).** Az utolsó cselekvés óta eltelt napok száma a legerősebb előrejelzője annak, hogy a vevő megismétli a cselekvést; ezért jön újabb katalógus rögtön az első vásárlás után.
Idézet: „Recency, or the number of days that have gone by since a customer completed an action (purchase, log-in, download, etc.), is the most powerful predictor of the customer repeating an action” (335.) · „Recency is why you receive another catalogue from the company shortly after you make your first purchase from them.” (335.)
Mit ad az alkalomhoz: érv arra, hogy az üdvözlő és az első vásárlás utáni levél azonnal menjen.

**331. oldal, élettartamérték.** Az LTV az a teljes nettó haszon, amit egy vevő a teljes kapcsolat alatt hoz; szegmensszinten arra felel, mennyit érdemes egy új vevő megszerzésére költeni.
Idézet: „How much can I afford to invest in acquiring a new customer?” (331.)
Mit ad az alkalomhoz: háttér a megtartás értékéhez; a deckbe valószínűleg nem kell (saját következtetés).

## Chaffey, Ellis-Chadwick, 3. és 4. fejezet: bevezető megjegyzés

A 3. alkalomhoz (A saját terep, „Hol fogadjuk, amikor megérkezik hozzánk”, beadandó: landing page-audit és e-mail-folyamat) két fejezetet dolgoztam fel. Forrás: Chaffey, Ellis-Chadwick: Digital Marketing, 6. kiadás, 2016. A 3. fejezetből csak a jogi és adatvédelmi részt (147–159. és 163. oldal), a 4. fejezetből az online értékajánlatot és a saját felületről szóló részeket. Minden idézet szó szerinti, mindegyiket a `findq.py`-val kerestem vissza, az oldalszám a findq kimenete.

Fontos megkötés: a könyv 2016-os, a jogi rész a 95/46/EK irányelvre, a brit Data Protection Actre és a PECR-re épül. A GDPR nem szerepel benne (lásd a végén). A jelenlegi jogi állapotot a könyv nem írja le, ehhez külső hivatalos forrás kell, ezt a 2. fázis keresi meg. Ami lent jogi szabályként szerepel, az a könyv 2016-os leírása, nem a jelenleg érvényes jog.

## Chaffey, Ellis-Chadwick, 3. fejezet, jogi környezet és adatvédelem

### Az adatvédelem mint a marketing kerete

**147. oldal, a hat jogterület (Table 3.1).** Chaffey hat jogi területet sorol fel, ami a digitális marketinget szabályozza. Az első az adatvédelem és a magánszféra, és ennek első sora pont a saját felület: az adatgyűjtés űrlapon és a követés webanalitikával. Ugyanebben a sorban szerepel az e-mail- és SMS-marketing, valamint a cookie-k használata.
Idézet: „Collection, storage, usage and deletion of personal information directly through data” … „capture on forms and indirectly through tracking behaviour through web analytics” (147. oldal)
Mit ad az alkalomhoz: a regisztrációs űrlap, a hírlevél-feliratkozás és a mérés egy jogterület alá tartozik. A beadandó adatkezelési része ezt a hármat nézheti egyben.

**148. oldal, a magánszféra és a mérlegelés.** A magánszféra definíciója erkölcsi jog. Chaffey dilemmaként írja le: a személyes adat a célzáshoz kell, a vevő viszont csak bizonyos mennyiségű adatot ad szívesen. A törvények értelmezése 2016-ban még bizonytalan volt, a cégek kockázatmérlegelés alapján döntöttek.
Idézet: „Privacy refers to a moral right of individuals to avoid intrusion into their personal affairs” (148. oldal)
Idézet: „Effective e-commerce requires establishing a balance between the benefits the individual customer will add to their online experience through providing personal information and the amount and type of information that they are prepared for companies to hold about them.” (148. oldal)
Idézet: „different interpretations of the law are possible and since these are new laws they have not been tested in court.” (148. oldal)
Mit ad az alkalomhoz: a „mennyit kérsz és mit adsz érte” kérdés könyvbeli alapja. Az űrlap minden mezője ennek a mérlegnek az egyik serpenyőjébe kerül.

**148–149. oldal, az adattípusok (Table 3.2).** Öt adattípus: kapcsolati adat, profiladat, platformhasználat, viselkedés egy oldalon, viselkedés több oldalon. Az első kettőt az űrlap gyűjti, ezekről az adatgyűjtés pontján adatvédelmi tájékoztató szól. A többiről a felhasználó általában nem tud.
Idézet: „The first two types of information in the table are usually readily explained through a privacy statement at the point of data collection and, as we will see, this is usually a legal requirement.” (149. oldal)
Idézet: „The main issue to be considered by the marketer is disclosure of the types of information collection and tracking data used.” (149. oldal)
Mit ad az alkalomhoz: az audit egyik kérdése: az űrlap mellett ott van-e, mire kéri az adatot.

### Adatvédelmi törvény és a nyolc elv (2016-os brit állapot)

**149–150. oldal, irányelv és DPA.** A jogi alap a 95/46/EK irányelv, Nagy-Britanniában a Data Protection Act 1984 és 1998. A felügyelet az ICO. A könyv innen a DPA nyolc elvét veszi sorra.
Idézet: „Member states shall protect the fundamental rights and freedoms of natural persons” (149. oldal)
Idézet: „In the UK, the enactment of the European legislation is the Data Protection Acts 1984 and 1998 (DPA)” (150. oldal)
Mit ad az alkalomhoz: történeti keret. A deckben csak annyi, hogy a könyv ezt a régi rendszert írja le (saját következtetés).

**150. oldal, hozzájárulás és célhoz kötöttség (1. és 2. elv).** Az adatkezeléshez hozzájárulás vagy szerződés, illetve jogszabály kell. A hozzájárulás definíciója: önkéntes, konkrét, tájékozott. Az adatgyűjtés pontján meg kell mondani, miért és hogyan kezelik az adatot, a további megkereséshez külön hozzájárulás kell.
Idézet: „any freely given specific and informed indication of his wishes by which the data subject signifies his agreement to personal data relating to him being processed” (150. oldal)
Idézet: „Personal data shall be obtained only for one or more specified and lawful purposes” (150. oldal)
Idézet: „This implies that the organisation must make it clear why and how the data will be” (150. oldal)
Idézet: „You would also have to agree (give consent) for further communications from the company.” (150. oldal)
Mit ad az alkalomhoz: a nyereményjáték-példa jó tanórai eset: a játékra jelentkezés és a hírlevél két külön döntés.

**151. oldal, a tájékoztatás három kérdése és az adattakarékosság (3. elv).** A Figure 3.10 utáni lista: küldenek-e később üzenetet, továbbadják-e az adatot, meddig őrzik. Az első kettőhöz online kifejezett hozzájárulás kell. A 3. elv szerint csak a szükséges minimumot szabad kérni. Chaffey maga mondja ki a feszültséget: a cégnek minél több adat kellene.
Idézet: „whether future communications will be sent to the individual (explicit consent is” (151. oldal)
Idézet: „whether the data will be passed on to third parties (again explicit consent is required);” (151. oldal)
Idézet: „This specifies that the minimum necessary amount of data is requested for processing.” (151. oldal)
Idézet: „There is difficulty in reconciling this provision between the needs of the individual and the needs of the company.” (151. oldal)
Mit ad az alkalomhoz: a „kevesebb kötelező mező” könyvbeli alapja. A regisztrációs űrlap súrlódásához is kapcsolódik: a jog és a súrlódás csökkentése itt ugyanabba az irányba mutat (saját következtetés).

**152–153. oldal, megőrzés, jogok, biztonság, adattovábbítás (4–8. elv).** Pontosság, a szükségesnél tovább nem őrzött adat, az érintett jogai (betekintés, direkt marketing tiltása), biztonság, EGT-n kívüli továbbítás. A könyv az USA felé a Safe Harbor rendszert említi.
Idézet: „Personal data processed for any purpose or purposes shall not be kept for longer than is necessary for that purpose or those purposes.” (152. oldal)
Idézet: „Data transfer with the US is possible through companies registered through the Safe Harbor Scheme” (153. oldal)
Mit ad az alkalomhoz: háttér. A Safe Harbor jelenlegi állapotát a könyv nem írja le, ezt sem szabad belőle tanítani.

### Engedély, opt-in, opt-out

**153. oldal, spam és engedélyalapú e-mail.** Az e-mail marketingeszköz marad, de a címzettnek bele kell egyeznie. Chaffey definiálja az opt-int és az opt-outot, és szerinte a leiratkozás lehetősége a sikeres e-mail-marketing kulcsa. Itt jelenik meg a cold list és a house list is.
Idézet: „Anti-spam laws do not mean that email cannot be used as a marketing tool, but the” … „recipient has to agree to receive the mailing. This approach is called Permissive Marketing.” (153. oldal)
Idézet: „Permissive email marketing is based on consent or opt-in by customers, and the option” … „to unsubscribe or opt-out is the key to successful email marketing.” (153. oldal)
Mit ad az alkalomhoz: az e-mail-folyamat beadandó kiinduló pontja. Az első levél előtt ott a feliratkozás, és minden levélben ott a leiratkozás.

**153–154. oldal, a 2002/58/EK irányelv és a PECR.** A 95/46-os irányelvet a technológia és a spam gyorsan meghaladta, ezért jött 2002-ben az elektronikus hírközlési irányelv. Nagy-Britanniában ez a PECR, 2003. december 11-től. A 22–24. cikk szól az e-mailről.
Idézet: „Data Protection Directive 95/46 and Data Protection Act afford a reasonable level of protection for consumers, they were quickly superseded by advances in technology and the rapid growth in spam.” (153. oldal)
Idézet: „as the Privacy and Electronic Communications Regulations (PECR) Act.” (154. oldal)
Idézet: „Clauses 22 to 24 are the main clauses relevant to email communications.” (154. oldal)
Mit ad az alkalomhoz: háttér. A deckre legfeljebb annyi, hogy az e-mailre külön szabály vonatkozik, nem csak az általános adatvédelem (saját következtetés).

**155. oldal, a PECR pontjai.** Opt-in rendszer: a címzett előre hozzájárul, online általában jelölőnégyzettel. Minden levélben kell leiratkozási lehetőség, már az adatgyűjtéskor is. Meglévő vevőnek hasonló termékről hozzájárulás nélkül is lehet írni (soft opt-in), de ezt több ország nem fogadja el. Kell valós elérhetőség és felismerhető feladó. A vírusmarketinget a biztos rossz szemmel nézi.
Idézet: „The relevant phrase is part of 22(2) where the recipient must have ‘previously notified the sender that he consents’ or has proactively agreed to receive commercial email. This is opt-in.” (155. oldal)
Idézet: „Opt-in can be achieved online or offline through asking people whether they want to receive email. Online this is often done through a tick-box.” (155. oldal)
Idézet: „The law states that a ‘simple means of refusing’ future communications is required both when the details were first collected and in each subsequent communication.” (155. oldal)
Idézet: „previous opt-in is not required if the contact details were obtained during the course of the sale or negotiations for the sale of a product or service.” (155. oldal)
Idézet: „The law requires a name, address or phone number where recipients can direct complaints.” (155. oldal)
Mit ad az alkalomhoz: kész ellenőrzőlista az e-mail-folyamat minden levelére: van-e leiratkozás, felismerhető-e a feladó, van-e elérhetőség. A jelenlegi érvényességét a 2. fázisnak kell ellenőriznie.

### Cookie-k

**156–157. oldal, mi a cookie.** A cookie-szakasz a 156. oldalon kezdődik (Digital marketing insight 3.5): típusok (tartós, munkameneti, first-party, third-party) és felhasználás (személyre szabás, visszatérő látogató, követés oldalak között, konverziókövetés). A 157. oldalon: a vásárlók közel fele törli a cookie-kat, ezért a mérés pontatlan lesz.
Idézet: „Some privacy campaigners consider that the user’s privacy is invaded by planting” (156. oldal)
Idézet: „almost half of online shoppers are now deleting cookies” (157. oldal)
Mit ad az alkalomhoz: a landing page-audit mérési oldala: amit az oldal mér, az a cookie-n múlik.

**158. oldal, a cookie-k jogi korlátai.** A PECR 2003-as szövege szerint tárolni csak világos tájékoztatás után és visszautasítási lehetőséggel lehet. Chaffey ebből kifejezett opt-int olvas ki, és ezt látjuk a weboldalakon. A feltétlenül szükséges cookie (például kosár) kivétel. A „remember me” jelölőnégyzet ezt oldja meg a belépésnél. A 2012-es szigorítás érinti a display hirdetést, a viselkedésalapú célzást és a webanalitikát. A szövegben két évszám áll: a szabályt 2012. május 25-től alkalmazzák, a weboldalakon „2013-as bevezetés” után látjuk; ezt a könyv nem oldja fel.
Idézet: „a person shall not use an electronic communications network to store information, or to gain access to information stored, in the terminal equipment of a subscriber or user unless the following requirements are met.” (158. oldal)
Idézet: „given the opportunity to refuse the storage of or access to that information;” (158. oldal)
Idézet: „explicit opt-in to cookies is required” (158. oldal)
Idézet: „This indicates that for an e-commerce service session cookies are legitimate without the need for opt-in.” (158. oldal)
Idézet: „It is arguable whether the identification of return visitors is ‘strictly necessary’ and this is why some sites have a ‘remember me’ tick box next to the log-in.” (158. oldal)
Mit ad az alkalomhoz: a cookie-sáv könyvbeli eredete. A sáv az első dolog, amit a látogató az oldalon lát, tehát a fogadás része (saját következtetés).

### Ellenőrzőlista a megfeleléshez

**158–159. oldal, tíz lépés.** A jogi rész egy tízpontos listával zárul, ami a saját felület auditjára szinte változtatás nélkül használható: tájékoztatás az adatkérés előtt, hozzájárulás, világos adatvédelmi nyilatkozat, cookie-tájékoztatás, csak a szükséges adat, a marketingcélú adat legyen opcionális, opt-in és opt-out, biztonság.
Idézet: „Notify or inform the site visitor before asking for information on:” (159. oldal)
Idézet: „how the site visitor can opt out (be unsubscribed from email lists or cookies);” (159. oldal)
Idézet: „Reassure customers by providing clear and effective privacy statements and explaining the purpose of data collection.” (159. oldal)
Idézet: „For example, a person’s name and full address should not be required to provide an online quotation.” (159. oldal)
Idézet: „If extra information is required for marketing purposes this should be made clear and the provision of such information should be optional.” (159. oldal)
Idézet: „Only use data for marketing (by the company or third parties) when a user has been informed this is the case and has agreed to this. (This is opt-in.)” (159. oldal)
Idézet: „Provide the option for customers to stop receiving information. (This is opt-out.)” (159. oldal)
Mit ad az alkalomhoz: a regisztráció és az adatkezelés legerősebb könyvbeli példája ebben a fejezetben: árajánlathoz ne kérj teljes nevet és címet. Ez egyszerre adatvédelmi és súrlódási szabály.

### Előre bepipált doboz

**163. oldal, fogyasztóvédelmi szabályok.** Ez nem az adatvédelmi, hanem a szerződési jogi (távértékesítési) részben áll. Az új uniós fogyasztói jogok (2011, Nagy-Britanniában 2014-től) a vásárlás közben felkínált kiegészítő szolgáltatásoknál (utasbiztosítás, autóbérlés) tiltják az előre bepipált dobozt. Ugyanitt: a rejtett költség tilalma és az ár kifejezett elfogadása. A 163. oldalon az online reklámjogban az is szerepel, hogy a kéretlen marketinglevélnek felismerhetőnek kell lennie.
Idézet: „These additional services may be offered through ‘pre-ticked’ boxes. With the new Directive, pre-ticked boxes will be banned across the European Union.” (163. oldal)
Idézet: „Consumers must explicitly confirm that they understand that they have to pay a price.” (163. oldal)
Idézet: „Online shoppers will not have to pay charges or other costs if they were not properly informed before they place an order.” (163. oldal)
Mit ad az alkalomhoz: a könyvben az előre bepipált doboz a fizetős kiegészítőkről szól, nem a hírlevél-hozzájárulásról. Ha a 21. dián a hozzájárulásnál szerepel, ahhoz a 2. fázis külső forrása kell. Chaffey a 155. oldalon csak annyit mond, hogy az opt-in online jelölőnégyzettel történik (saját következtetés).

## Chaffey, Ellis-Chadwick, 4. fejezet, az online értékajánlat (OVP)

### Az OVP definíciója és elemei

**222. oldal, mi az OVP.** A 4. döntésben (pozicionálás és megkülönböztetés) jön elő. Az OVP a megkülönböztető előnyt teszi világossá és kommunikálja. Két eleme van: online tartalom és szolgáltatás, amit üzenetekkel magyarázunk, és ezeknek az üzeneteknek az eljuttatása minden érintkezési ponton, a szlogentől a weboldal részletes tartalmáig. Az üzenet erősítse a márka alapajánlatát, és mondja meg, mit kap online a látogató, amit offline vagy a versenytársnál nem.
Idézet: „In a digital marketing context, differential advantage and positioning can be clarified” … „and communicated by developing an online value proposition (OVP).” (222. oldal)
Idézet: „reinforce core brand proposition and credibility;” (222. oldal)
Idézet: „communicate what a visitor can get from an online brand that they can’t get from” … „the brand offline and they can’t get from competitors or intermediaries.” (222. oldal)
Mit ad az alkalomhoz: a 10. dia gerince. A két kérdés, amit a landing page-nek meg kell válaszolnia: mit kapok itt, és miért nem máshol.

**222. oldal, az OVP az oldalon.** Az oldalon kommunikált OVP vevőközpontúvá teszi a weboldalt. A Webuyanycar.com példája a 223. oldali 4.20 ábra. Chaffey szerint nem csak az ár különböztet meg, a márkaélmény és a szolgáltatás minősége ugyanannyit számít.
Idézet: „Communicating the OVP on the site can help create a customer-centric website.” (222. oldal)
Idézet: „It is important to note that price is not the only way to stand out online, quality of brand experience and quality of service is equally important for creating differential advantage.” (222. oldal)
Mit ad az alkalomhoz: az audit első kérdése a márka saját oldalán: hol áll az OVP, és látszik-e azonnal.

### Az OVP példái és haszna

**222. oldal, Virgin Wines.** A Virgin Wines OVP-je négy „és ha…” kérdésre felel: nem vagy otthon, máshol olcsóbb, messze laksz, sietsz. Mindegyikre egy ígéret a válasz.
Idézet: „We promise that our drivers will find a safe place to leave your wine; but if it does get stolen, we just replace it.” (222. oldal)
Idézet: „We deliver within seven days, or your delivery is free.” (222. oldal)
Mit ad az alkalomhoz: a Virgin Wines minden pontja egy aggodalmat vesz le a látogatóról. Ez az akadályok elvételének szép könyvbeli példája, és közvetlenül illik a Printa csapat Do fázisához (szállítási költség és idő, visszaküldés) (saját következtetés).

**222. oldal, interaktív elemek és a négy haszon.** Az OVP interaktív elemekkel is építhető: vásárlói értékelések, blog, vásárlási útmutató, videós értékelés. Ezek a konverziót és az újravásárlást segítik. A világos OVP négy haszna: megkülönböztet a versenytársaktól (ez a weboldaltervezés célja legyen), fókuszt ad, PR-ban és szájhagyományban terjed (Amazon: akár 40% kedvezmény, 3 millió cím), és illeszkedik a termékajánlathoz.
Idézet: „Interactive Web 2.0 features can be particularly important for transactional sites in that they may enhance the user’s experience and so encourage conversion and repeat sales.” (222. oldal)
Idézet: „It helps distinguish an e-commerce site from its competitors (this should be a website design objective).” (222. oldal)
Idézet: „It helps provide a focus to marketing efforts so that company staff are clear about the purpose of the site.” (222. oldal)
Mit ad az alkalomhoz: az értékelések szerepe a 12. dia (percepció) felé visz.

**223. oldal, Activity 4.5.** A könyv feladata: öt cég weboldalán egy-két mondatban összefoglalni az értékajánlatot, és megmutatni, hogyan jelzi a weboldal tartalma.
Idézet: „summarise their Internet value proposition. You should also explain how they use the content of the website to indicate their value proposition to customers.” (223. oldal)
Mit ad az alkalomhoz: majdnem kész beadandó-lépés. A landing page-audit első kérdése lehet ugyanez a márka saját oldalán.

**Kérdéslista.** Az OVP-hez a 4. fejezetben nincs kérdéslista. A 224–225. oldalon van tizenkét kérdés, de az a közösségi média stratégiájához tartozik, nem az OVP-hez. Lásd a Nem találtam részt.

### Az OVP a stratégiában

**186., 199., 211., 239. oldal, ahol még előkerül.** Porter hat elvéből a második az egyedi, de teljesíthető értékajánlat (186. oldal). A Sizzle célnál az OVP tájékoztat vagy szórakoztat (199. oldal). A lojalitás növelése az OVP-n keresztül (211. oldal). A 239. oldalon az OVP-stratégia a megszerzés és a megtartás értékajánlata, és mellette áll az online értékesítési hatékonyság stratégiája: a látogatóból hírlevél-feliratkozás vagy első kosárba tett termék által lesz lead.
Idézet: „Define a value proposition, which is unique but, importantly, deliverable.” (186. oldal)
Idézet: „defining the value proposition for acquisition and retention to engage with customers online.” (239. oldal)
Idézet: „become leads (e.g. through registering for an e-newsletter or placing the first item in the shopping basket)” (239. oldal)
Mit ad az alkalomhoz: a regisztráció és a hírlevél itt az oldal konverziós célja. Ez köti össze a landing page-et és az e-mail-folyamatot.

### A saját felület és a weboldal szerepe

**193. oldal, a jelenlét szintjei.** A kisvállalkozás digitális jelenlétének öt szintje: 0. nincs weboldal, 1. katalógusbejegyzés (Yelp, Google My Business), 2. statikus „brochureware” oldal vagy csak Facebook-oldal, 3. kereshető, űrlapos oldal, 4. tranzakciós oldal, 5. teljesen interaktív oldal marketing-automatizációval.
Idézet: „Level 2. Simple static website created containing basic company contact and product” (193. oldal)
Idézet: „Level 5. Fully interactive site and marketing automation providing relationship” (193. oldal)
Mit ad az alkalomhoz: a csapatok elhelyezhetik a márkájukat ezen a skálán. A Levendula („teljes mértékben offline nyomja”) valószínűleg alacsony szinten áll (saját következtetés).

**204. oldal, paid, owned, earned.** A 4. fejezetben az owned media csak egyszer, a költségeknél szerepel. Definíció nincs, az az 1. fejezetben van (11–12. oldal, a 2. alkalom forrásfeldolgozása szerint).
Idézet: „paid, owned and earned media costs” (204. oldal)
Mit ad az alkalomhoz: a 9. diához ebből a fejezetből nincs anyag.

**224–225. oldal, ellenpont: az elköteleződés a közösségi oldalon könnyebb.** Chaffey szerint egyre inkább nem a céges weboldalon, hanem a közösségi jelenléten a legegyszerűbb az online elköteleződés. Ugyanakkor a közösségi tartalom gyakran a weboldal vagy a blog mélyebb tartalmára mutat. Az Asda példájánál a feliratkozáshoz e-mail-cím kell.
Idézet: „Increasingly, it’s most straightforward to achieve online engagement not on a company” (224. oldal)
Idézet: „Often the content will need to link to more in-depth content on the company website or blog.” (225. oldal)
Mit ad az alkalomhoz: vitapont a weboldal szerepéhez. Az elköteleződés lehet a bérelt felületen, de a mélyebb tartalom és az e-mail-cím a sajáton van (saját következtetés).

**233. oldal, gyors győzelmek a konverzióban.** A 10. lépés: a landing page üzenete és használhatósága, a kezdőlap, kategória- és termékoldal, a kosár, a regisztráció és a fizetés javítása, A/B teszttel.
Idézet: „conversion (improvements to landing page messaging and usability through small findability improvements to navigation or search labelling” (233. oldal)
Mit ad az alkalomhoz: a landing page-audit tárgyainak listája egy mondatban, a könyv szavaival.

### Tesco-eset: eseményvezérelt levelek

**240–241. oldal, a fejezet záró esete.** A Tesco automatizált, eseményvezérelt levelekkel dolgozik. Három trigger: regisztrált, de nem vásárolt (két nap múlva levél segítséggel és kedvezménnyel), első vásárlás (azonnali visszaigazolás, elégedettségi kérdőív, tippek, hírlevél, személyre szabott ajánlat), hosszú ideje nem vásárolt (reaktiváló levél kérdőívvel és ösztönzővel). Mögötte a Clubcard és a hat életciklus-kategória áll. A 241. oldal futófeje a könyvben tévesen „Chapter 2”, az oldalszám a findq szerint helyes.
Idézet: „Tesco then uses automated event-triggered messaging” (240. oldal)
Idézet: „Auto-response (AR) 1: Two days after registration” (241. oldal)
Idézet: „AR1: Immediate order confirmation.” (241. oldal)
Idézet: „AR1: Dormancy detected – reactivation email with” (241. oldal)
Mit ad az alkalomhoz: az e-mail-folyamat beadandó mintája triggerrel, időzítéssel és céllal. Kiegészíti a 19. dia Table 6.1-ét.

## Chaffey, Ellis-Chadwick, 9. fejezet (Marketing communications using digital media channels)

Digital Marketing, 6. kiadás (2016), 476–547. oldal. Feldolgozva 2026. október 5-én a `konyvek/chaffey-ch9-marketing-communications.txt` fájlból. A keresőmarketing (484–501), a display céloldalra vonatkozó része (515–521) és az e-mail szakasz (522–528) ténylegesen végigolvasva, az e-PR, az affiliate, a social és az offline rész futtában. Minden idézet és oldalszám a `findq.py` kimenete. Csak a saját terephez tartozó részeket dolgoztam fel; a csatornák maguk a 4. alkalomé. A fejezet 2016-os, a Google-eszközök nevei és több adat elavult; ahol ez számít, jelzem.

### A saját oldal mint középpont

**482. oldal, a márka oldala előbb van, mint a social.** A fejezetet nyitó interjúban Katie Webb (Vision Express) arról beszél, hogy sok márka a Facebook- és Twitter-jelenlétét hirdeti, a weboldalát nem. Szerinte fordítva kellene: a közösségi jelenlét a weboldal üzenetét egészíti ki, és az oldalra terel.
Idézet: "To me, a brands website should take precedence, and social media presences should complement the website messaging and be aimed at engaging customers with the website." (482)
Mit ad az alkalomhoz: 1. és 9. blokk. Egy gyakorló marketinges mondata arról, hogy a csatornák a saját terep felé dolgoznak.

**504. oldal, a saját oldal mint saját média.** Az online PR-ról szóló részben Chaffey azt írja, hogy a cégnek saját oldala, sajtószobája, feedje és blogja van, ezért részben megkerülheti a médiatulajdonosokat.
Idézet: "Since a company will have its own site, press centre, feeds and blogs, it is possible to bypass other media owners to some extent." (504)
Mit ad az alkalomhoz: 1. blokk. A saját terep a fizetett és a szerzett média mellett az a felület, ahol a cég maga mondja el a történetét.

**483. oldal, 9.2 ábra, mennyire bíznak a forrásokban.** A Nielsen (2013) adatai szerint a válaszadók 58%-a az ismerősei ajánlását tartja fontosnak vásárlás előtt, 45% az online véleményeket, 36% a feliratkozással kapott e-maileket, 34% a márkák weboldalát. A keresőhirdetés 19%, a banner 14%.
Idézet: "E-mails I signed up for" (483), a 9.2 ábra egyik sora. Az ábra címe: "Percentage who consider different information sources as" (483)
Mit ad az alkalomhoz: 6. és 7. blokk. A feliratkozott e-mail és a márka saját oldala a bizalmi sorban a fizetett hirdetések előtt áll. A felmérés 2013-as.

### SEO a saját oldalon: on-page tényezők

**487–488. oldal, a két fő rangsorolási tényező.** Chaffey szerint a jó helyezés két legfontosabb tényezője az oldal szövegének egyezése a keresett kifejezéssel (ennek javítása az on-page optimalizálás) és az oldalra mutató linkek. Ugyanitt: a belső linkeket a kereső hasonlóan értékeli, a javítás eszköze a belső linkarchitektúra.
Idézet: "Matching between web page copy and the key phrases searched." (487) és "The processes to improve this aspect of SEO are external link building and internal link architecture." (488)
Mit ad az alkalomhoz: 5. blokk. A belső linkelés a könyvben SEO-fogalom, nem csak navigáció.

**488. oldal, tartalommarketing és linkszerzés.** A szerzők megjegyzik, hogy az első kiadáskor a tartalommarketing fogalma még nem létezett, jelenleg viszont ez a minőségi linkek megszerzésének legjobb módja. Szerintük a SEO mindig is technikai munka, tartalomfejlesztés és más oldaltulajdonosokkal való együttműködés volt.
Idézet: "gain quality backlinks is through content marketing" (488)
Mit ad az alkalomhoz: 5. blokk, tartalomstratégia. A tartalom a saját terepen van, a hatása a linkeken keresztül kívülről jön vissza.

**489. oldal, a SEO gyenge pontja és a szövegírók.** A SEO hátrányai között szerepel, hogy ismertséget építeni rosszul tud, mert a keresőnek már ismernie kell a márkát vagy a szolgáltatást. A bevált gyakorlat része, hogy a tartalomszerkesztőket meg kell tanítani az on-page tényezőkre.
Idézet: "Searchers already have to be familiar with a brand or service to find it." (489) és "Content editors and reviewers within a company therefore need to be trained to understand these factors and incorporate them into their copywriting." (489)
Mit ad az alkalomhoz: 5. blokk. Az on-page SEO szövegírói feladat, nem csak technikai.

**489. oldal, indexelés és duplikált tartalom.** Az index inclusion azt jelenti, hogy a releváns oldalak bekerülnek-e a kereső indexébe. Ennek akadálya lehet a bonyolult URL-eket gyártó tartalomkezelő, illetve a duplikált tartalom. Utóbbira a canonical címke a megoldás.
Idézet: "‘canonical’ meta tag which tells the search engine which the primary page is." (489)
Mit ad az alkalomhoz: 5. blokk. Az információs architektúra hibája (sok hasonló oldal) SEO-hibaként jelenik meg. A könyv a Google Webmaster Toolst említi, ennek jelenlegi neve Google Search Console (saját megjegyzés, nem a könyvből).

**491. oldal, Panda: a vékony tartalom büntetése.** A Panda 2011-től a gyenge minőségű, „thin” tartalmú oldalak láthatóságát csökkentette, a Penguin az agresszív linképítést.
Idézet: "aimed at reducing the visibility of low-quality sites with ‘thin’ content." (491)
Mit ad az alkalomhoz: 5. blokk. Érv a tartalomstratégia mellett: a sok, de üres oldal kár. Az algoritmusfrissítések listája 2015-tel zárul.

**491–492. oldal, kulcskifejezés és céloldal.** A keresőmarketing kulcsa a kulcskifejezés relevanciája: a keresőmezőbe írt szavak és a legrelevánsabb céloldal egyezése. Chaffey ezért beszél kulcskifejezésről (keyphrase) és nem kulcsszóról. A minősítők típusai a „car insurance” példán: összehasonlítás, ár vagy termékjellemző, felhasználási cél, terméktípus, gyártó, hely, cselekvés („buy”).
Idézet: "search box to the most relevant destination content page." (491)
Mit ad az alkalomhoz: 3. és 5. blokk. Minden fontos kifejezéshez kell egy oldal, ami pontosan arra válaszol. A minősítők listája jó gyakorlat a tartalommodellhez.

**492–493. oldal, az on-page tényezők listája.** Chaffey felsorolja: a kifejezés gyakorisága (nem túlzottan, 2–4% alatt), előfordulás a title-ben és a címsorokban, a link anchor szövegében, kiemelés, közelség a dokumentum elejéhez, kimenő linkek, alt szöveg, metaadatok. A Google saját irányelve szerint az oldal teljes tartalmát nézi. A title a legfontosabb metaadat, mert ez a kattintható sor a találati oldalon. A title és a description legyen egyedi minden oldalon.
Idézet: "Google goes far beyond the number of times a term appears on a page and examines all aspects of the page’s content (and the content of the pages linking to it) to determine if it’s a good match for your query." (492), "If it contains powerful, relevant copy, you will get more clicks" (493) és "These need to be unique for each page on a site, otherwise the search engine may assess the content as duplicate and some pages may be down-weighted in importance." (493)
Mit ad az alkalomhoz: 4. és 5. blokk. A title és a description a találati oldalon az első benyomás része, még az oldal előtt. A kulcsszósűrűség számszerű határa és a keywords meta tárgyalása 2016-os gyakorlat; a könyv maga is jelzi, hogy a keywords metát a Google sosem használta.

### Belső linkelés és hubhoz hasonló szerkezet

**494. oldal, Resource Centre és authority/hub oldalak.** A linkszerzés első lépése Chaffey és Smith (2012) szerint értékes tartalmat létrehozni, és azt a navigációban kiemelni, vagy néhány oldalon csoportosítani („Useful Resources”, „Resource Centre”). Így mások közvetlenül az eszközökre linkelnek, nem csak a főoldalra. Ugyanezen az oldalon a „hub” szó is előfordul, de a PageRank kapcsán: a Google az adott keresésben tekintélyes, „authority” vagy „hub” oldalakat azonosítja.
Idézet: "By creating more valuable content and then showcasing them within your navigation, or grouping it within a few pages such as a ‘Useful Resources’ or a more extensive ‘Resource Centre’" (494) és "‘authority sites’ or hub sites for a particular type of search." (494)
Mit ad az alkalomhoz: 5. blokk. A Resource Centre a könyvben a legközelebbi rokona a hub vagy pillar oldalnak: egy helyre gyűjtött, navigációból elérhető tartalom. A „hub sites” viszont külső tekintélyt jelent, nem az oldalon belüli gyűjtőoldalt. A klasztermodellt Chaffey nem tárgyalja (lásd Nem találtam).

**495. oldal, belső linkelés.** A külső linképítés elvei az oldalon belül is érvényesek. A legfontosabb: a keresők által használt kifejezés kerüljön a link anchor szövegébe, és a releváns tartalomra mutasson. Azokra az oldalakra, amelyeknek jól kell rangsorolniuk, több belső link mutasson. A sűrűn összekötött, hálós szerkezet jobb lehet az egyszerű hierarchiánál.
Idézet: "Many of the principles of external link-building can also be applied to links within sites." (495), "The most important principle is to include keyphrases used by searchers within the anchor text of a hyperlink to point to relevant content." (495) és "A meshed structure with lots of interlinks can work better than a simple hierarchy." (495)
Mit ad az alkalomhoz: 5. blokk. Ez a fejezet legerősebb mondata a belső linkelésről. A hálós szerkezet és a hierarchia szembeállítása jól illeszkedik a klasztermodellhez, de Chaffey nem nevezi így (saját következtetés).

**507–508. oldal, a blog mint tartalomszerkezet.** A blogformátum lehetővé teszi, hogy ugyanaz a tartalom többféleképpen legyen elérhető. A Smart Insights blogja példáján: téma (kategória), címke, szerző és idő szerint. Chaffey szerint a blogok a közösségi platformok mellett is fontosak maradtak, mert mélyebb témafeldolgozást adnak.
Idézet: "The blogging format enables the content on a website to be delivered in different ways." (507) és "Although some forecast that blogs would become less important" (508)
Mit ad az alkalomhoz: 5. blokk, tartalommodell. A kategória és a címke a könyvben a legközelebbi példa a témák szerinti rendezésre. A 9.12 ábra (509. oldal) a Smart Insights folyamatát mutatja: a blogbejegyzés a „hub”, innen megy hírlevélbe, RSS-be és közösségi oldalakra. Ezt az ábra feliratából olvasom, idézni nem tudom, mert az ábraszöveg a kinyert fájlban szétesett.

### A landing oldal a csatornák szemszögéből

**497. oldal, quality score és landing page relevance.** A fizetett keresésben nem az nyer, aki a legtöbbet fizeti. A Google a hirdetés relevanciáját is méri, ennek eszköze a quality score. A képlet egyik eleme a landing oldal relevanciája; a Google robotokkal ellenőrzi a céloldalakat.
Idézet: "Quality score = (keyword’s click-through rate, ad text relevance, keyword relevance, landing page relevance, speed and other methods of assessing relevance)" (497) és "as is relevance of the landing page (Google now sends out AdBots-Google to check them out)." (497)
Mit ad az alkalomhoz: 3. blokk, a hirdetés és az oldal egyezése. A landing oldal minősége közvetlenül a hirdetés árát és helyét befolyásolja. A képlet a 2016-os leírás; a Google jelenleg a „landing page experience” megnevezést használja (saját megjegyzés, nem a könyvből).

**498. oldal, a hely nem vásárolható meg.** Hogy a természetes találatok fölött nulla vagy három hirdetés jelenik meg, az a quality score-on múlik.
Idézet: "you can’t ‘buy your way to the top’ as many think." (498)
Mit ad az alkalomhoz: 3. blokk. Jó mondat arra, hogy a rossz landing oldal pénzbe kerül.

**499. oldal, a kattintás még nem eredmény; dedikált landing.** A hirdetés hozhat kattintást úgy is, hogy az oldalon nem lesz belőle lead vagy eladás. Ennek oka lehet gyenge cselekvésre ösztönzés vagy rossz közönség. Ezért gyakran olcsóbb, ha adott kulcskifejezésekre külön microsite vagy landing oldal készül. Ez lehet a site szerkezetének része is: a „car insurance” hirdetés a gépjármű-biztosítás oldalra visz, nem a főoldalra. Az ügyfélszerzési költség képlete: 100 osztva a konverziós arány százalékával, szorozva a kattintásonkénti költséggel. A 9.3 táblázat szerint ugyanannál a kattintásárnál 25% helyett 10% konverzió 2,5-szeres CPA-t jelent.
Idézet: "Clearly, an ad could be effective in generating click-throughs or traffic, but not achieve the outcome required on the website such as generating a lead or online sale." (499), "it will often be more cost-effective if targeted microsites or landing pages are created" (499) és "clicking on a ‘car insurance’ ad will take the visitor through to the car insurance page on a site rather than a home page." (499)
Mit ad az alkalomhoz: 3. blokk, mi a landing és mi nem. A főoldal nem landing; a landing az az oldal, ami a hirdetés kérdésére válaszol. A CPA-képlet számolós feladatnak is jó.

**500–501. oldal, kampánystruktúra és üzenetegyezés.** A kampánystruktúra azért fontos, hogy az adott keresés a hozzá illő hirdetésszöveget váltsa ki. A PPC-ellenőrzőlistában külön tétel a céloldal-stratégia.
Idézet: "Are AdGroups small enough to deliver a message relevant for the keyphrase entered?" (500) és "Destination or landing page strategy. How are landing pages improved?" (501)
Mit ad az alkalomhoz: 3. blokk. A „message match” kifejezés nem szerepel a fejezetben; a gondolat a keresés, a hirdetésszöveg (ad text relevance, 497) és a landing relevanciája láncában van meg. A hirdetés és az oldal egyezését a könyv a relevancia fogalmával írja le (saját következtetés).

**515. oldal, a display hirdetés céloldala.** A bannerről érkező látogató céloldala általában külön erre készült, direkt válaszra épülő oldal. A Huggies példája: a gyermekgondozási oldalon elhelyezett hirdetés részletes információhoz vitt, és a hűségprogramba való feliratkozásra ösztönzött.
Idézet: "The destination page from a banner ad will usually be designed as" (515), "a specifically created direct-response page to encourage further action." (515) és "encouraging them to opt in to a loyalty programme." (515)
Mit ad az alkalomhoz: 3. és 7. blokk. A landing típusai közé: tájékoztató és feliratkoztató (loyalty) céloldal.

**526. oldal, az e-mail landing oldala.** A CRITICAL utolsó betűje a landing oldal: az e-mailből érkezőt jellemzően űrlap fogadja, és az űrlap kitölthetősége a kampány egész sikerére hat.
Idézet: "Designing the page so the form is easy to complete can affect the overall success of the campaign." (526)
Mit ad az alkalomhoz: 3. és 6. blokk. A súrlódás a könyvben az űrlapnál jelenik meg.

### Opt-in e-mail és a házon belüli lista

**523–524. oldal, opt-in és house list.** Az e-mailt leginkább a prospectek konvertálására és az ügyfelek megtartására használják, saját, engedélyen alapuló listával (house list). A Lastminute.com listája több mint 10 millió címet tartalmazott. Az opt-in e-mail kontrollált push üzenet, ami válaszra ösztönöz.
Idézet: "opt-in house list of prospects and customers that have given permission to an organisation" (523) és "communications provide a controlled push message which encourages response." (524)
Mit ad az alkalomhoz: 7. blokk. A házon belüli lista a saját terep része: a cég birtokolja, nem bérli.

**524. oldal, a házon belüli e-mail típusai.** Konverziós e-mail (regisztrált, de nem vásárolt látogatónak automatikus követés), rendszeres hírlevél, house-list kampány, eseményre induló e-mail, e-mail-sorozat. A William Hill fogadóiroda tapasztalata: az automatikus követő e-mailek kétszer annyi regisztrálót vittek el az első fogadásig, mint ahányan e-mail nélkül eljutottak oda.
Idézet: "Someone visits a website and expresses interest in a product or" (524), "William Hill found that automated follow-up emails" (524) és "twice as many registrants to place their first bet compared to registrants who did not receive an email." (524)
Mit ad az alkalomhoz: 7. blokk, regisztráció és automatizált e-mail. A William Hill-példa számszerű érv az automatizált követés mellett.

**525. oldal, ESP és a válaszkészség lecsengése.** Az e-mail szolgáltató (ESP) négy képességet ad, ezek között a feliratkozó űrlapok és a landing oldalak kezelését. Az e-mail hátrányai között: a címzett feliratkozáskor a legaktívabb, utána nehéz megtartani.
Idézet: "hosting of forms for managing email subscriptions and landing pages" (525) és "Email recipients are most responsive when they first subscribe to an email. It is difficult to keep them engaged." (525)
Mit ad az alkalomhoz: 7. blokk. Érv az üdvözlő sorozat mellett: az első hetek a legértékesebbek.

**526. oldal, e-mail mutatók.** Kézbesítési arány (non-bounce rate), megnyitási arány, kattintási arány. A megnyitás a letöltött képekből mérhető, ezért pontatlan. A kattintás a kézbesítettekhez viszonyított egyedi kattintás, ennek szintje Chaffey szerint 10% körül van. A legfontosabb mégis az, hogy a kattintás után mi történik az oldalon (eladás, lead).
Idézet: "how many customers open an email, but is not accurate" (526), "This is the number of people who click through on the email of those delivered (strictly unique clicks rather than total clicks)." (526) és "Additionally, and most important, are the marketing outcomes or value events" (526)
Mit ad az alkalomhoz: 7. és 8. blokk. Az e-mail eredménye a saját oldalon születik, ott kell mérni. A megnyitási arány 2016 óta még kevésbé megbízható (például az Apple 2021-es Mail Privacy Protection funkciója miatt; saját megjegyzés, nem a könyvből). A 10%-os kattintási szint is régi adat.

**526. oldal, CRITICAL.** Chaffey (2006) ellenőrzőlistája: Creative, Relevance, Incentive, Targeting and timing, Integration, Conversation, Attributes, Landing page. A relevancia a lista minőségén és a célzáson múlik. A feliratkozáshoz releváns ösztönző kell, például ingyenes információ vagy kedvezmény az e-mail-címért cserébe.
Idézet: "Does the offer and creative of the email meet the needs of the recipients?" (526) és "A relevant incentive, such as free information or a discount, is offered in exchange for a prospect providing their email address by filling in an online form." (526)
Mit ad az alkalomhoz: 6. és 7. blokk. Az ösztönző a regisztrációs súrlódás ellensúlya (saját következtetés).

**527–528. oldal, üdvözlő program és a lista építése.** A lista aktivitásának fenntartására: üdvözlő program az első három–hat hónapban automatikus, célzott e-mailekkel, újraaktiváló ajánlatok, szegmentálás aktivitás szerint. A DMA (2008) felmérésében a legtöbb cég az organikus webes forgalomból gyűjti az új címeket.
Idézet: "Develop a welcome programme where over the first three to six months targeted," (527) és "the majority of respondents gather new email addresses through organic website traffic" (528)
Mit ad az alkalomhoz: 7. blokk. A lista a saját oldalon épül, tehát a feliratkozási pont az oldal tervezési kérdése. A DMA-adat 2008-as.

### Mérés és cookie

**480. oldal, a forgalmi források és a mérés hézaga.** A 9.1 ábra a Google Analytics átlagos forrásmegoszlását mutatja (Smart Insights, 2011): direkt 36,5%, kereső 27%, hivatkozó 21%, egyéb 15,5%. A direkt forgalomba kerül az is, ha az e-mail linkjei nincsenek felcímkézve, illetve az appokból jövő social forgalom („Dark Social”). A könyv maga jelzi, hogy ezt a benchmarkot a Google már nem frissíti.
Idézet: "direct traffic results from URL type-ins, bookmarks or when email marketing isn’t tracked by marketers adding specific link tracking to their email so that they show up in analytics." (480)
Mit ad az alkalomhoz: 8. blokk. Kampánycímkézés nélkül a forrás elvész. Az arányok 2011-esek, nem használhatók jelenlegi viszonyításra.

**498. oldal, remarketing cookie-val.** A Google a keresőhirdetésre kattintó vagy egy adott oldalt meglátogató felhasználó gépére cookie-t helyez, és ezzel a display hálózaton újra megjeleníti neki a hirdetést.
Idézet: "Google offers retargeting through cookies placed on the searchers" (498) és "to display ads on the content network after someone has clicked on a paid search ad or visited a specific page on a site as a reminder to act." (498)
Mit ad az alkalomhoz: 8. blokk. Az oldalmegtekintés eseményként a remarketing alapja.

**510. oldal, affiliate cookie.** Az affiliate oldalról átkattintó látogatót cookie követi; ha a megállapodott időn belül (1, 7, 30, 60 vagy 90 nap) vásárol, az affiliate kapja a jutalékot.
Idézet: "this prospect will be tracked through a cookie placed on the visitor’s PC." (510)
Mit ad az alkalomhoz: 8. blokk. A cookie mint attribúciós eszköz egyszerű példája.

**518. és 520. oldal, view-through, viselkedésalapú célzás, banner és keresés.** A viselkedésalapú újracélzás cookie-val követi a felhasználót. A hirdetésszerverek a kattintás mellett a view-through-t is mérik: a felhasználó látta a hirdetést, és egy időn belül (például 30 nap) felkereste az oldalt. A MAD (2007) utazási felmérésében kétszer annyian mentek a bannertől a keresőbe, mint ahányan a bannerre kattintottak.
Idézet: "Tracking of individuals is achieved through use of cookies." (518), "subsequently visits a website within a defined period, such as 30 days." (520) és "more than twice as many people are being driven to a search engine by banner advertising than by clicking directly on the banner!" (518)
Mit ad az alkalomhoz: 8. blokk, átkattintás és cookie. Az átkattintás alulbecsüli a hatást, a látogató gyakran más úton érkezik az oldalra. A könyv a cookie-k adatvédelmi és hozzájárulási oldalát ebben a fejezetben nem tárgyalja (lásd Nem találtam).

### Mi marad a 4. alkalomra

A csatornák önmagukban: a SEO folyamata (crawl, index, rank), a külső linképítés és a Penguin, a PPC licitálása, kulcsszóegyezési típusai és optimalizálása, az online PR és az influencer outreach, az affiliate modellek, a display formátumok és vásárlása, a social és a virális marketing, az offline promóció, valamint a 9.4 táblázat a csatornák erősségeiről és gyengeségeiről (541–542. oldal). Az e-mailből a hidegebb, akvizíciós formák (bérelt lista, co-branded e-mail, harmadik fél hírlevele), a deliverability és a renderability.

## Chaffey, Ellis-Chadwick, 10. fejezet (Evaluation and improvement of digital channel performance)

Digital Marketing, 6. kiadás, 2016, 548–591. oldal. A fejezet két részből áll: teljesítménymenedzsment (mérőszámok, eszközök, tesztelés) és a webes jelenlét karbantartása (tartalomfrissítés, felelősségek, CMS). A 3. alkalomhoz az első rész kell, a második részből csak a tartalomtípusok és a sablonok. A könyv 2016-os, a Google Analytics akkori (Universal) állapotát írja: munkamenet-alapú mérés, 30 perces session, bounce rate, Google Website Optimiser. Ahol ez számít, jelzem.

**Módszertani megjegyzés az oldalszámokhoz.** A kinyert szövegben a páratlan oldalak futófeje két sorra törik („…improvement of d” / „igital channel performance 551”). A `munkadoksik/findq.py` ezt 2026. október 5-től felismeri, az oldalszámok a javított findq kimenetei. A margón futó glosszárium miatt a több soron átnyúló mondatokat soronként ellenőriztem, ezeknél „ / ” választja el a sorokat.

### Webanalitika: mit mér egyáltalán

**550. oldal, a webanalitika definíciója.** A Digital Analytics Association definíciója szerint a webanalitika internetes adatok mérése, gyűjtése, elemzése és riportolása a webhasználat megértése és optimalizálása céljából. A szerzők szerint ez „catch-all” definíció, hiányzik belőle a kereskedelmi cél és a többcsatornás használat mérése.
Idézet: „Web analytics is the measurement, collection, analysis and reporting of Internet data for” / „the purposes of understanding and optimising web usage.” (550, soronként ellenőrizve)
Mit ad az alkalomhoz: 8. blokk, bevezető mondat. A „megértése és optimalizálása” pár jól illeszkedik a tanulsághoz: nem a szám a cél, hanem hogy hol érezte jól magát és hol akadt el (saját következtetés).

**551. oldal, Kaushik: az elköteleződés foka és fajtája.** Kaushik szerint az „engagement” szót annyira elkoptatták, hogy semmit nem jelent. Az analitikai eszköz a fokát méri (hány oldalt nézett meg), a fajtáját nem (bosszús volt vagy elégedett).
Idézet: „web analytics tools can measure the degree of engagement but they fall quite a bit short of measuring the kind of engagement.” (551)
Idézet: „So they can report that visitors saw 19 pages on your site (degree) but they can’t tell you if that was because the visitors were frustrated with your crappy navigation or thrilled with your content.” (551)
Mit ad az alkalomhoz: 8. blokk (elköteleződési idő, oldalmegtekintés) és 9. összegzés. Ez a legerősebb ellenpont a tanulsághoz: az esemény elárulja, hol akadt el, de azt nem, hogy miért. Ehhez kell a hőtérkép, a munkamenet-felvétel vagy a felhasználói teszt (saját következtetés). A 19 oldal példája a 2. és 5. blokkhoz is jó: a sok oldalmegtekintés jelenthet rossz navigációt.

**551. oldal, Kaushik: az elköteleződés egyszerű mérőszámai.** A legegyszerűbb példa a fő landing oldalak visszafordulási aránya. Két kattintással elérhető a visszatérés (recency), a gyakoriság, a látogatás hossza és mélysége.
Idézet: „Perhaps the simplest example is using the bounce rate for the core landing pages to identify pages that won’t even entice visitors to make one click!” (551)
Idézet: „In two clicks you can also get loyalty (recency), frequency, length of visit and” (551)
Mit ad az alkalomhoz: 3. blokk (landing) és 4. blokk (első benyomás). A „won’t even entice visitors to make one click” az előszoba-kép mérhető változata: ha egyet sem kattint, be sem jött (saját következtetés). A recency és frequency a 7. blokkhoz (loyalty) is kapcsolódik.

**552. oldal, Kaushik: hol kezdjük a tesztelést.** Gyakorlati recept: a 25 leglátogatottabb belépő oldal közül a három legmagasabb visszafordulásút kell először tesztelni. Kaushik az A/B tesztet javasolja kezdésnek, nagy különbségű változatokkal. Kell egy „customer listening channel” is: távoli felhasználói teszt, kutatás, call center, kérdőív.
Idézet: „Run a report for your top 25 landing pages (entry pages) on your site, then look at the bounce rates for each of them.” (552)
Idézet: „Pick three with the highest bounce rates, these are the pages letting you down the most.” (552)
Idézet: „The best focus points about what is not working on your site come from your customers (sadly not you)” (552)
Mit ad az alkalomhoz: 3. és 4. blokk (landing, első benyomás), 6. blokk (súrlódás). A harmadik idézet a kulcsgondolathoz illik: a látogató mondja meg, mi nem működik, nem mi (saját következtetés). A 2016-os szöveg a Google Website Optimisert említi ingyenes A/B eszközként; ez az eszköz jelenleg nem érhető el (nem a könyvből van, ellenőrizendő).

**553. oldal, Kaushik: eseménynaplózás.** Kaushik a jövő analitikájáról beszélve megemlíti, hogy az eszközök többet fognak tudni az oldalmegtekintés-riportnál, és az eseménynaplózást már meglévő, „cool” dolognak tartja.
Idézet: „I don’t mean doing clever things like event logging to measure Web 2.0 experiences” (553)
Mit ad az alkalomhoz: 8. blokk, történeti háttér. 2016-ban az oldalmegtekintés volt az alapegység, az esemény kiegészítő. Jelenleg a GA4-ben fordított a helyzet: minden esemény, az oldalmegtekintés is (saját következtetés, a GA4 nem szerepel a könyvben).

### Mikro- és makroszintű mérőszámok

**555. oldal, makro- és mikroszintű mérőszámok.** Chaffey (2000) szerint a mérési keretrendszerben kell lennie makroszintű hatékonysági mérőszámoknak (elérte-e a stratégiai célt, mennyit hoz az üzletnek) és mikroszintű mérőszámoknak (mennyire hatékony a taktika). A mikroszintűeket „performance drivers” néven is hívják, mert ezek teljesülése viszi a stratégiai célt.
Idézet: „Include macro-level effectiveness metrics which assess whether strategic goals are achieved” (555)
Idézet: „Include micro-level metrics which assess the efficiency of digital marketing tactics and implementation.” (555)
Idézet: „Such measures are often referred to as performance drivers” (555)
Mit ad az alkalomhoz: 8. blokk (mikro- és makrokonverzió). Figyelem: a könyv itt mérőszám-szinteket ír, nem konverziótípusokat. A „mikrokonverzió” szó nem szerepel a fejezetben. A „macro-conversion rates” kifejezés egyszer előfordul, az AB testing margószócikkében (564. oldal, példaként az eladás vagy a feliratkozás konverziós arányát hozza), de a margó tördelése miatt ezt a findq egyben nem találja, ezért idézetként nem használom. A mikro- és makrokonverzió jelenlegi értelmezése (kisebb lépések a fő cél felé) ebből csak levezethető (saját következtetés).

### A látogató viselkedése: mit lehet nyomon követni

**557. oldal, honnan jön (referrer, channel promotion).** A forgalom forrását a referrer mutatja: melyik oldalról vagy kulcsszóval érkezett. A promóció akkor sikeres, ha a forgalom volumene, minősége, értéke és költsége megfelel a célnak. A minőséget az mutatja, hogy a célpiacból jön-e (konverzió, visszafordulás, akvizíciós költség forrásonként). A közösségi oldalakra érkező látogatásnál hasonló referrer-adat általában nincs.
Idézet: „Promotion is successful if traffic meets” (557)
Idézet: „determined by whether visitors are in the target market” (557)
Idézet: „typically available for visits to social media sites.” (557)
Mit ad az alkalomhoz: 1. blokk (visszamutatás: honnan jön, kit hoztunk be), 8. blokk (mi látszik kívülről). A kulcsgondolat első fele itt mérhető: a referrer megmutatja, mit keresett, amikor megtalált minket (saját következtetés).

**557. oldal, mit csinál az oldalon (channel buyer behaviour).** Ha már az oldalon van, követni lehet, milyen tartalmat néz, mikor jön és meddig marad, és ebből lesz-e lead vagy vásárlás. Regisztrációval viselkedési profil építhető. A visszatérő látogatót cookie vagy bejelentkezés ismeri fel.
Idézet: „Once customers have been attracted to the site we can monitor content accessed, when” (557)
Idézet: „It is also important to recognise return visitors for whom cookies or login are used.” (557)
Mit ad az alkalomhoz: 8. blokk (cookie, oldalon töltött idő), 7. blokk (a regisztráció mérési haszna is: profil, visszatérés). A kulcsgondolat második fele („beljebb jön-e”) itt kezd mérhetővé válni (saját következtetés).

**557–558. oldal, kulcsarányok: bounce rate, stickiness.** Visszafordulási arány oldalanként (egyoldalas látogatások aránya), kezdőlap-megtekintés az összeshez képest, stickiness (oldalmegtekintés per munkamenet), visszatérés (munkamenet per látogató). Mind munkamenet-alapú, a Universal Analytics logikája.
Idézet: „Bounce rates for different pages, i.e. proportion of single page visits.” (557)
Idézet: „Stickiness: page views/visitor sessions” (558)
Mit ad az alkalomhoz: 4. blokk (első benyomás: visszafordulás), 8. blokk. Jelölendő: a GA4-ben a bounce rate más definícióval él (a nem elkötelezett munkamenetek aránya), a könyv a régi, egyoldalas definíciót adja (a GA4-es definíció nem a könyvből van).

**558. oldal, konverziós arány és kulcseredmények.** A csatorna eredményei: regisztráció vagy hírlevél-feliratkozás, információkérés (brosúra, visszahívás), promócióra reagálás, offline lead vagy vásárlás, online vásárlás. A konverziós arány a látogatók azon aránya, akik egy adott eredményt elérnek; példa: 10 000 látogatóból 500 regisztrál, ez 5 százalék.
Idézet: „A widely used method of assessing channel outcomes is to review the conversion rate, which gives an indication of the percentage of site visitors who take a particular outcome.” (558)
Idézet: „registration to site or subscriptions to an email newsletter;” (558)
Idézet: „Conversion rate, visitors to registration = 5 per cent (10,000 visitors, of which 500” (558)
Mit ad az alkalomhoz: 7. blokk (regisztráció, e-mail mint mérhető eredmény) és 8. blokk (mikro- és makrokonverzió). A lista elemei a jelenlegi szóhasználattal részben mikrokonverziók (feliratkozás, információkérés), részben makrokonverzió (vásárlás); ezt a felosztást a könyv nem teszi meg (saját következtetés).

**558–559. oldal, lemorzsolódás (attrition rate) és okai.** Az attrition rate megmutatja, hány látogató vész el a konverziós tölcsér egyes lépései között a landing oldaltól a fizetésig. A 10.4 ábra szakaszonként sorolja az okokat: akvizíció (rossz közönség), első benyomás (lassú betöltés, homályos üzenet, nem megnyerő külső), termékválasztás (ügyetlen navigáció, nehézkes választás, nem versenyképes ár, nincs valós idejű készletinfó), fizetés és teljesítés (kártyahiba, magas szállítási költség, nincs e-mail értesítés, sikertelen kézbesítés). A kosárba tétel és a vásárlás közötti lemorzsolódás különösen magas.
Idézet: „A related concept is the attrition rate which describes how many visitors are lost at each” / „step of a conversion funnel from landing page to checkout.” (558, soronként ellenőrizve)
Idézet: „A key feature of e-commerce sites is that there is a high attrition rate between a customer adding an item to a basket and subsequently making a purchase.” (558)
Idézet: „Potential reasons for causing attrition on an e-commerce site” (559, a 10.4 ábra címe)
Mit ad az alkalomhoz: 4. blokk (az ábrán szó szerint „First impressions” szakasz van), 6. blokk (súrlódás és bizalom: a kártyabiztonsági félelem a könyv szerint a magas kosárelhagyás egyik feltételezett oka), 8. blokk (navigációs útvonal). A 10.4 ábra szinte a tanulság képi változata: minden lépésnél megmutatja, hol akadt el a látogató (saját következtetés). Ez az ábra diának is jó.

### Mennyiségi mérőszámok: hit, oldalmegtekintés, látogatás, egyedi látogató

**560–561. oldal, log fájl, hit, oldalmegtekintés, egyedi látogató.** A látogatói aktivitás adatai rögzítik a látogatók számát és az útvonalakat (clickstream). Az 1990-es években ezt szerveroldali log fájlból mérték, ahol minden letöltött fájl egy „hit”. A hit félrevezető (egy tíz képből és szövegből álló oldal 11 hit), az oldalmegtekintés és az egyedi látogató jobb mérőszám. A 10.1 táblázat (ABCe) definíciói: egyedi felhasználó (IP és user agent, cookie vagy regisztrációs azonosító alapján), látogatás (30 perc inaktivitásig tartó oldalmegtekintés-sorozat), oldalmegtekintés, hirdetésmegjelenés, hirdetéskattintás.
Idézet: „on the site and the paths or clickstreams they take through the site as they visit different” (560)
Idézet: „Despite their wide use in the media, hits are not a useful measure of website effective-” (560)
Idézet: „A unique and valid identifier [for a site visitor].” (561)
Idézet: „Sites may use (i) IP + User – Agent, (ii) cookie and/or (iii) registration ID” (561)
Idézet: „gap of 30 minutes or more between successive page impressions for that user” (561)
Mit ad az alkalomhoz: 8. blokk (oldalmegtekintés, cookie). Az egyedi látogató definíciójából látszik, hogy a „látogató” valójában egy azonosító (cookie, IP, login), nem egy ember (saját következtetés). A 30 perces munkamenet a Universal Analytics korának szabványa, jelöld.

**561. oldal, oldal per látogatás és az oldalon töltött idő torzítása.** A PPV (pages per visit) a szerzők szerint pontosabb jelzője a „ragadósságnak”, mint az oldalon töltött idő, mert az időt felfelé torzítják azok, akik megérkeznek, nem csinálnak semmit, és csak a 30 perces időtúllépéskor ér véget a munkamenetük.
Idézet: „PPV is a more accurate indication of stickiness than duration on a site in minutes since this figure is skewed upwards by visitors who arrive on a site and are inactive before their session times out at 30 minutes.” (561)
Mit ad az alkalomhoz: 8. blokk (elköteleződési idő, oldalon töltött idő). Ez a régi „time on site” mutató gyengéje, és pont ezt a problémát kezeli a GA4 elköteleződési ideje (csak akkor számol, ha az oldal előtérben van). A GA4-es megoldás nem a könyvből van (saját következtetés).

**562. oldal, a szokásos riportok.** Minden analitikai csomag tud: top oldalak, belépő és kilépő oldalak, útvonal- vagy clickstream-elemzés, ország, böngésző és operációs rendszer, hivatkozó URL és domain.
Idézet: „entry and exit pages;” (562)
Idézet: „path or clickstream analysis showing the sequence of pages viewed;” (562)
Idézet: „referring URL and domain (where the visitor came from).” (562)
Mit ad az alkalomhoz: 8. blokk (navigációs útvonal, mi látszik kívülről), 3. blokk (belépő oldal mint landing).

### Tervezés a méréshez

**563–564. oldal, design for analysis (DFA).** A mérést gyakran utólag építik be, amikor már kérdezik, hány látogató és vásárlás van. Jobb, ha a mérést az oldal tervezésébe építik, hogy látsszon a közönség típusa és a döntési pontjaik. Példa: a Dell kezdőlapján a fő navigáció ügyféltípus szerint van, így a választásból becsülhető a közönség megoszlása. További példák: hosszú oldal vagy űrlap darabolása, tartalomcsoportok közönség vagy döntési szakasz szerint, lemorzsolódás mérése a vásárlási lépéseknél.
Idézet: „a technique known as design for analysis (DFA) is designed into” (563)
Idézet: „the primary navigation on the home page is by cus-” / „tomer type.” (563, soronként ellenőrizve)
Idézet: „Breaking up a long page or form into different parts, so you can see which parts people are interested in.” (564)
Idézet: „Group content by audience type or buying decision and setting up content groups of related content within web analytics systems.” (564)
Idézet: „Measure attrition at different points in a customer journey, e.g. exit points on a five- page buying cycle.” (564)
Mit ad az alkalomhoz: 5. blokk (információs architektúra és tartalommodell: a tartalomcsoport közönség vagy döntési szakasz szerint közel áll a klasztermodellhez), 2. blokk (navigáció), 6. blokk (űrlap darabolása), 8. blokk (esemény, útvonal). A DFA a tanulság gyakorlati feltétele: csak az a lépés árulkodik, amelyiket mérhetőre terveztük (saját következtetés).

### Tesztelés: A/B és multivariáns

**564. oldal, A/B teszt.** Ha vita van, melyik változat jobb, csak kísérlet dönthet. Az Amazon elve (Matt Round): „Data trumps intuition.” Az A/B teszt egy oldal vagy oldalelem (címsor, kép, gomb) két változatát teszteli, a látogatókat véletlenszerűen osztva szét. A cél az átkattintási arány, a konverzió és a látogatásonkénti bevétel javítása. A kontrolloldal jellemzően a meglévő landing oldal. Skype példa: a menüpontok átnevezése („Call Phones” helyett „Skype Credit”, „Shop” helyett „Accessories”) 18,75 százalékkal növelte a látogatásonkénti bevételt.
Idézet: „Data trumps intuition.” (564)
Idézet: „In its simplest form, A/B or AB testing refers to testing two different versions of a page or a” (564)
Idézet: „The goal is to increase page or site effectiveness against key” (564)
Idézet: „tion and simply describing the offer available rather than the activity.” (564, a Skype példa tanulsága)
Mit ad az alkalomhoz: 2. blokk (UI: gomb, címsor), 3. blokk (landing mint kontrolloldal), 8. blokk (átkattintás). A Skype példa az 5. blokkhoz is: a navigációs címke az ajánlatot nevezze meg, ne a tevékenységet. A tesztelés módszertana inkább a 6. alkalomra tartozik.

**564–566. oldal, multivariáns teszt.** Az A/B teszt kifinomultabb formája, egyszerre több oldalelem kombinációit teszteli. National Express mini esettanulmány: a foglalás utolsó előtti lépésén 3500 kombinációt próbáltak, a legjobb 14,11 százalékkal növelte a konverziót.
Idézet: „Multivariate testing is a more sophisticated form of AB testing which enables simultane-” (564)
Mit ad az alkalomhoz: 6. blokk (súrlódás egy foglalási lépésen), 8. blokk röviden. Részletesen a 6. alkalomra.

### Clickstream és útvonalelemzés

**566–567. oldal, clickstream és path analysis.** A clickstream-elemzés a látogatói viselkedés részletes elemzése a javítás érdekében. Az összesített „top paths” riport ritkán hasznos, mert a várt utakat mutatja (kezdőlap, kilépés). Akkor lesz cselekvésre váltható, ha egy oldal szemszögéből nézzük: forward path (merre mennek egy oldalról) és reverse path (honnan jutnak egy oldalra, például az első pénztároldalra).
Idézet: „Clickstream analysis refers to detailed analysis of visitor behaviour in order to identify improvements to the site.” (566)
Idézet: „you seek to learn from the most popular paths.” (566)
Idézet: „It highlights typically paths which are expected and can’t really be influenced.” (566)
Mit ad az alkalomhoz: 8. blokk (navigációs útvonal), 9. összegzés. A tanulsághoz: az útvonal akkor beszél, ha egy konkrét oldalról kérdezzük (saját következtetés).

**567. oldal, 10.3 táblázat: az elemző kérdései.** Kérdés és riport párok: hol lépnek be (top landing pages), honnan jönnek (referrers), mi a legnépszerűbb tartalom (gond-e a navigációs címkék miatti megtalálhatóság), hogyan keresnek (site search), hol lépnek ki (van-e 404 hibaoldal), milyen útvonalakat járnak. A táblázat GA-terminológiát használ (Universal kori elnevezések).
Idézet: „Are there problems with findability caused by navigation labelling?” (567)
Idézet: „Are there error pages (e.g. 404 not found) which cause visitors to leave?” (567)
Idézet: „How popular are different forms of navigation, e.g. top” (567)
Mit ad az alkalomhoz: 5. blokk (információs architektúra, címkézés), 2. blokk (navigáció), 6. blokk (hibaoldal mint súrlódás). A táblázat diára vagy hallgatói feladatlapnak alkalmas.

**567–568. oldal, belső keresés.** A belső keresés a tartalom megtalálásának fő útja, ezért elemzése megtérül. Mérőszámok: keresések száma, keresés per látogató, nulla találatos keresések aránya, keresési találatoldalról kilépés, a találatokra kattintás és konverzió aránya, legnépszerűbb keresőkifejezések.
Idézet: „On-site search is another crucial part of clickstream analysis on many sites since it is a key” (567)
Idézet: „percentage of searches returning zero results;” (567)
Mit ad az alkalomhoz: 5. blokk és a kulcsgondolat: az oldalon belül is ő keres minket, a belső keresés szó szerint megmutatja, mit keres (saját következtetés). 8. blokk: a keresés mint esemény.

**568. oldal, szegmentálás.** Nehéz a vevőszegmenseket a webes viselkedéshez kötni, mert az analitikai adat nincs összekötve a vevő- vagy vásárlási adattal. Viselkedési szegmensek viszont készíthetők: új és visszatérő, forrás szerint, konvertáló és nem konvertáló, ország, megnézett tartalom. MyTravel példa: „site flirt” (legfeljebb két oldal), „site browse”, látott keresési találatot, ajánlatot, fizetési adatokat, visszaigazolást.
Idézet: „site flirt (two pages or fewer);” (568)
Mit ad az alkalomhoz: 4. blokk (a „site flirt” az előszobában maradó látogató), 7. blokk (a regisztráció köti össze a viselkedést a vevőadattal, ez a könyvből levezethető, saját következtetés), 8. blokk (navigációs útvonal mint szegmens).

### Mérőeszközök és pontosság

**568–569. oldal, log fájl kontra page tagging, pontosság.** A böngészőalapú (tag-alapú) mérés egy rövid szkriptet futtat minden oldalbetöltéskor, és potenciálisan pontosabb a szerveroldalinál. A Google Analytics ingyenes változata nagy oldalakon mintavételez, ami csökkenti a pontosságot (Universal kori állapot). A 10.4 táblázat a log fájl hibáit sorolja: alulszámlálás (böngésző- és proxy-gyorsítótár, tűzfal közös IP-vel, dinamikus oldalak), túlszámlálás (keretek, keresőrobotok, futtatható fájlok). Adatvédelem: az analitikai rendszer személyes adatot tárol, a cookie-szabályokat követni kell.
Idézet: „tional log file analysis to the more common browser-based or tag-based measurement” / „system that records access to web pages every time a page is loaded into a user’s web” (568, soronként ellenőrizve)
Idézet: „The key benefit of the browser-based approach is that it is potentially more accurate than server-based approaches.” (568)
Idézet: „The free version of Google Analytics uses sampling on large sites which can” (568)
Idézet: „Caching in user’s web browsers (when a user” (569)
Idézet: „Web analytics systems store personal data.” (569)
Idézet: „the latest laws about use of cookies.” (569)
Mit ad az alkalomhoz: 8. blokk (cookie, mi látszik kívülről, eszközök). A cookie-k saját pontossági gondjairól (törlés, több eszköz, elutasítás) a fejezet nem ír, lásd Nem találtam. A pontosság részletei a 6. alkalomra.

**568. oldal, attribúció.** A „last-click-wins” modell pontatlan, a teljes vásárlói utat súlyozó modellek pontosabbak.
Idézet: „referral source to sale is inaccurate” (568)
Mit ad az alkalomhoz: 1. blokk (visszamutatás a journey-re), röviden. Részletesen nem ide tartozik.

### Kvalitatív eszközök: kérdőív, fókuszcsoport, teszt

**570–571. oldal, visszajelző eszközök és a 10.5 táblázat.** Öt online visszajelző eszköztípus: folyamatos oldalvisszajelzés, szándék és elégedettség felmérése (mit akart tenni a látogató és mit sikerült), crowdsourcing, oldal- vagy koncepcióvisszajelzés panelről, általános kérdőív. A 10.5 táblázat erősségek és gyengeségek szerint veti össze a módszereket (log fájl, böngészőalapú mérés, A/B és MVT, panel, kérdőív, fókuszcsoport, próbavásárló).
Idézet: „These tools measure the gap between what the user had hoped to do on the site and what they actually achieved.” (570)
Idézet: „Most site analytics tools are now” / „browser based” (571, soronként ellenőrizve)
Mit ad az alkalomhoz: 8. blokk (az esemény a „mit csinált”, a kérdőív a „mit akart”), 6. blokk. A szándék és eredmény közti rés a tanulság kiegészítése: az esemény megmutatja, hol akadt el, a kérdőív, hogy mit keresett (saját következtetés).

**572–573. oldal, fókuszcsoport és felhasználói teszt.** Hagyományos fókuszcsoportban a vásárlók egy teremben értékelik az oldalt, jellemzően indulás előtt, a prototípus-szakaszban. Hasznosabb, ha forgatókönyveket kapnak. A valós helyzet előnye, hogy látszik a reakció.
Idézet: „the users will be given different scenarios to follow.” (572–573)
Idézet: „Conducting real-world focus groups has the benefit that the reactions of site users can be monitored; the scratch or slap of the head cannot be monitored in the virtual world!” (573)
Mit ad az alkalomhoz: 2. blokk (UX), 8. blokk. A fejezetben ez a legközelebb álló rész a felhasználói teszthez (usability testing); önálló usability-módszertan nincs benne. A „scratch or slap of the head” jól mutatja, mit nem lát az analitika, és mit pótol részben jelenleg a munkamenet-felvétel (saját következtetés, a munkamenet-felvétel nem szerepel a könyvben).

**573. oldal, próbavásárló.** Az internetes csatorna nem önmagában létezik, az offline kiszolgálásnak is tartania kell, amit az online ígér. A próbavásárló az oldal használhatóságát, a teljesítést, az e-mail és telefonos válaszidőt és a márkahatást teszteli.
Idézet: „the Internet channel does not exist in” / „isolation.” (573, soronként ellenőrizve)
Mit ad az alkalomhoz: 6. blokk (bizalom: az ígéret és a teljesítés egyezése), 7. blokk (e-mail válasz).

### Tartalomtípusok és sablonok (a fejezet második része)

**575. oldal, tartalomtípusok egy online kereskedőnél.** Termékinformáció (termék- és kategóriaoldalak), termékmárka-tartalom, kereskedőmárka-tartalom (értékajánlat, bizalom, történet), promóciós, támogató (rendelés, visszaküldés), közösségi (vélemények, értékelések) és blogtartalom.
Idézet: „Brand content (retailer brand) – content about the company, such as its value proposi-” (575)
Idézet: „Community content – user-generated content which may be in a community area or” (575)
Mit ad az alkalomhoz: 5. blokk (tartalommodell), 3. blokk (oldaltípusok), 6. blokk (bizalmi tartalom: a kereskedőmárka-tartalomban szerepel a „trust”, a közösségi tartalomban a vélemények).

**579–580. oldal, oldalsablonok.** Oldaltípusonként (kategória, termék, blog) egységes sablon kell: könnyebb használni, az elemek hasonlók, a márka egységes. A 10.6 táblázat szabványai: oldalstruktúra, navigáció (főmenü helye, kezdőlap gomb minden oldalon), szöveg és oldalszerkezet (a webes szöveg rövidebb, emészthető darabokban), tesztelés, arculat, teljesítmény (letöltési sebesség).
Idézet: „The site will be easier to use – a customer who has become familiar with using one area” (579)
Mit ad az alkalomhoz: 2. blokk (UI-konzisztencia), 3. blokk (oldaltípusok). Rövid háttér, nem kulcsrész.

### Amazon esettanulmány: a mérés kultúrája

**583–585. oldal, „Culture of Metrics”.** Bezos 1997-ben vezette be a mérési kultúrát. Marcus (2004) szerint az Amazon minden mozdulatot rögzített. A „customer enjoyment” mérőszám kitalálásakor az első ötlet az oldalon töltött idő volt, Bezos szerint ez nem elég konkrét; aztán szóba került a vásárlás és a gyakoriság (az RFM elemei). A „Creator Metrics” eszköz tartalmanként konverziót, oldalmegtekintést, kosárba tételt és „repelt” (a tartalmat megnyitották, majd visszagomb) mért. Az A/B teszteknél munkamenet-időt és -hosszt is mértek.
Idézet: „A company like Amazon” / „could (and did) record every move a visitor made,” / „every last click and twitch of the mouse.” (584, soronként ellenőrizve)
Idézet: „much time each customer spends on the site?’” (584)
Idézet: „‘Not specific enough’, Jeff said.” (584)
Idézet: „back button then used” (584, a „repel” definíciójának vége)
Mit ad az alkalomhoz: 8. blokk (oldalon töltött idő mint gyenge mutató, esemény), 9. összegzés. Az „every last click and twitch of the mouse” a tanulság erős, szerzői megfelelője: minden mozdulat adat. A „repel” pedig egy korai, saját fejlesztésű esemény: megnyitotta, de visszalépett, vagyis elakadt (saját következtetés).

### Vizsgakérdés az eseményről

**589. oldal, vizsgakérdés.** A fejezet egyetlen olyan mondata, amely a mérést kifejezetten eseményként írja le.
Idézet: „Measurement of websites concerns the recording of key events involving custom-” / „ers using a website. Briefly explain five different types of event.” (589, soronként ellenőrizve)
Mit ad az alkalomhoz: 8. blokk és a tanulság. Nagyon közel áll a tanulsághoz („az oldalon minden lépés egy esemény”), de a fejezet magát az eseményt sehol nem definiálja; a kérdésre a válasz a fejezetből csak összerakható (saját következtetés). Hallgatói kérdésnek is használható.

### Mi marad a 6. alkalomra

- A mérési folyamat négy lépése (célkitűzés, mérés, diagnózis, beavatkozás), 10.2 ábra, 554–555. oldal.
- A mérési keretrendszer öt diagnosztikai kategóriája (WebInsights), 10.3 ábra, 557. oldal; többcsatornás scorecard, 10.5 ábra, 560. oldal.
- A mérési akadályok és a WAA 2011-es felmérése (az adatok cselekvésre váltása a fő gond), 554. oldal.
- Eszközválasztás szempontjai (integráció, pontosság, attribúció, vizualizáció, testreszabás, adatvédelem), 568–569. oldal; a 10.11 ábra adattípusai.
- A log fájl alul- és túlszámlálási hibái részletesen (10.4 táblázat, 569. oldal) és a 10.5 módszer-összevetés (571. oldal), hibakereséshez.
- A/B és MVT módszertan (kontrolloldal, ABC teszt, statisztikai szignifikancia, az Amazon tesztelési nehézségei), 564–566. és 584. oldal.
- Kérdőív-tervezés (Grossnickle és Raskin), 572. oldal.
- Közösségi média mérése (Altimeter-piramis), 562–563. oldal.

## Kotler, Keller: megjegyzés a forrásfájlról

**Kotler, Keller: Marketing Management, 14. kiadás.** Az 5. fejezet fájlja (`konyvek/kotler-ch5-long-term-loyalty.txt`) a 125. oldallal kezdődik, egy bekezdés közepén („How then do customers ultimately make choices?”). A fejezet eleje hiányzik: a fejezetnyitó, a kérdéslista és a vevőérték-alszakasz kezdete. A szöveg a 125. oldalon az 5.2 ábrára és a 9. végjegyzetre hivatkozik, tehát az 5.1 ábra és az 1–8. végjegyzet a hiányzó részben van. Hogy pontosan hány oldal hiányzik, a fájlból nem tudom megállapítani. A fájl a 150. oldalon a 6. fejezet nyitóoldalával és a 151–152. oldallal ér véget.

A kinyert szöveg több helyen két hasábot fésül össze soronként (a 125. oldalon az 5.2 ábra feliratai, a 129. oldalon a Net Promoter keretes írás). Ezeknél a mondatot soronként ellenőriztem a `findq.py`-val, és az idézetben „[…]” jelzi, hol szakítja meg a másik hasáb. Minden idézet és oldalszám a `munkadoksik/findq.py` kimenete. A 6. fejezetből csak a 170–171. oldalt dolgoztam fel.


## Kotler, Keller, 5. fejezet (Creating Long-Term Loyalty Relationships)

### Az észlelt vevőérték és a teljes vevői költség

**125. oldal, customer-perceived value (CPV).** A vevő értékmaximalizáló, a keresés költségein, a tudásán, a mobilitásán és a jövedelmén belül. Azt az ajánlatot választja, amelyről úgy hiszi, a legnagyobb észlelt értéket adja. Az észlelt érték a teljes vevői haszon és a teljes vevői költség különbsége, a versenytárs ajánlatához mérve. A haszon négy forrása a termék, a szolgáltatás, a személyzet és az imázs (5.2 ábra).

Idézet (125. oldal): „Customer-perceived value (CPV) is the difference between the prospective customer’s evaluation of […] all the benefits and all the costs of an offering and the perceived alternatives.”

Idézet (125. oldal): „Customers estimate […] which offer they believe—for whatever reason—will deliver the most perceived value and act on it”

Mit ad az alkalomhoz: a weboldal az a hely, ahol a vevő ezt a kivonást ténylegesen elvégzi. Az érték nem csak attól nő, amit a márka hozzátesz, hanem attól is, amit elvesz (saját következtetés).

**125. oldal, total customer cost: pénz, idő, energia, pszichés költség.** A teljes vevői költség nem csak az ár. Benne van az az idő, energia és pszichés teher is, amit a vevő a kiértékelésre, a megszerzésre, a használatra és a megszabadulásra fordít. Kotler Adam Smitht idézi: a dolgok valódi ára a megszerzésük fáradsága. A marketinges kétféleképpen növelheti az értéket: a hasznot emeli, vagy egy vagy több költséget csökkent.

Idézet (125. oldal): „Total customer cost is the perceived bundle of costs customers expect to incur in evaluating, obtaining, using, […] and disposing of the given market offering, including monetary, time, energy, and psychological costs.”

Idézet (125. oldal): „The real price of anything is the toil and trouble of acquir-”

Idézet (125. oldal): „The marketer can increase the value of the customer […] offering by raising economic, functional, or emotional benefits and/or reducing one or more costs.”

Mit ad az alkalomhoz: ez az akadályok és a súrlódás könyvbeli kerete. Az idő, az energia és a pszichés költség mind a felületen keletkezik: a kitöltendő mező, a keresgélés, a bizonytalanság. A „kevesebb költség” út pontosan az akadály elvétele (saját következtetés).

### A Caterpillar-példa és a hátrányban lévő eladó két útja

**125–126. oldal, Caterpillar kontra Komatsu.** Egy építőipari cég beszerzője traktort választ. A Caterpillart látja jobbnak termékben, szolgáltatásban, személyzetben és imázsban, de ettől még nem biztos, hogy megveszi: a teljes költséget is mérlegeli. A Caterpillar három módon javíthat az ajánlatán: több haszon, kevesebb nem pénzbeli költség (idő, energia, pszichés ráfordítás), alacsonyabb ár. A cég a jobb értékért 10–20%-kal magasabb árat tud kérni. A fejezetrész végén a szöveg általánosít: a hátrányban lévő eladónak két útja van. Fontos: a „két út” nem a Caterpillar-eset, hanem az abból levont általános tanulság (126. oldal), a Caterpillar-esetben három mód szerepel (125. oldal).

Idézet (125. oldal): „Second, it can reduce the buyer’s nonmonetary costs by reducing the time, energy, and psychological investment.”

Idézet (125. oldal): „The buyer will choose whichever source delivers the highest perceived value.”

Idézet (126. oldal): „It also implies that the seller at a disadvantage has two alternatives: increase total customer benefit or […] decrease total customer cost.”

Idézet (126. oldal): „The latter calls for reducing the buyer’s costs by reducing the price or cost of ownership and maintenance, […] simplifying the ordering and delivery process, or absorbing some buyer risk by offering a warranty.”

Idézet (126. oldal): „allowing the firm to command a premium price 10 percent to 20 percent higher than”

Mit ad az alkalomhoz: a 13. dia gerince. A „kevesebb költség” út Kotlernél három konkrét eszközt nevez meg: alacsonyabb ár vagy fenntartási költség, egyszerűbb rendelés és szállítás, a kockázat átvállalása garanciával. A második és a harmadik weboldal-feladat. Az utolsó elem (a kockázat átvállalása) átvezet a 6. fejezet hat kockázatához.

### Ígéret és értékszállítási rendszer

**127. oldal, value proposition, value delivery system, loyalty.** Az értékajánlat több a pozicionálásnál: ígéret arról, milyen élményre számíthat a vevő. Hogy az ígéret teljesül-e, az az értékszállítási rendszeren múlik, ami minden élményt magában foglal a megszerzéstől a használatig. Kotler Oliver lojalitás-definícióját idézi: mélyen gyökerező elköteleződés az újravásárlásra, a váltásra csábító helyzetek és marketingerőfeszítések ellenére.

Idézet (127. oldal): „The value delivery system includes all the experiences the customer will have on the […] way to obtaining and using the offering.”

Idézet (127. oldal): „Oliver defines loyalty as “a deeply held commitment to […] rebuy or repatronize a preferred product or service in the future despite situational influences and”

Mit ad az alkalomhoz: a weboldal az értékszállítási rendszer része, nem a hirdetésé. Ehhez kapcsolódik, hogy a megérkezés után az oldalon dől el, beljebb jön-e a látogató (saját következtetés).

### Elégedettség és elvárás

**128. oldal, Total Customer Satisfaction.** Az elégedettség az észlelt teljesítmény és az elvárás összevetéséből születik. Az elvárás a korábbi tapasztalatból, ismerősök tanácsából és a marketinges ígéreteiből jön. Ha a marketinges túl magasra teszi az elvárást, a vevő csalódik; ha túl alacsonyra, kevés vevőt vonz. A Xerox „teljesen elégedett” vevői hatszor nagyobb eséllyel vásároltak újra, mint a „nagyon elégedettek”. A Kia 10 éves, 100 000 mérföldes garanciával vált sikeressé az Egyesült Államokban.

Idézet (128. oldal): „If marketer raise expectations too high, the”

Idézet (128. oldal): „Xerox’s senior management found its “completely satisfied” customers […] were six times more likely to repurchase Xerox products over the following 18 months than even its”

Idézet (128. oldal): „100,000 mile warranties.”

Mit ad az alkalomhoz: a landing page ígérete elvárást állít be. Ha a hirdetés mást ígér, mint amit az oldal mutat, az elégedetlenség már az érkezéskor kezdődik (saját következtetés, a 11. diához).

### Panasz és a néma távozás

**131. oldal, Customer Complaints.** A vevők kb. 25%-ban elégedetlenek a vásárlással, de csak kb. 5%-uk panaszkodik. A többi úgy érzi, nem éri meg a fáradságot, vagy nem tudja, hol tehetné. Egyszerűen nem vásárol többé. A legjobb, amit a cég tehet, hogy könnyűvé teszi a panaszt: űrlap, ingyenes szám, weboldal, e-mail-cím.

Idézet (131. oldal): „their purchases about 25 percent of the time, only about 5 percent complain.”

Idézet (131. oldal): „just stop buying.”

Idézet (131. oldal): „The best thing a company can do is make it easy for customers to complain.”

Mit ad az alkalomhoz: a súrlódás a vásárlás után is súrlódás. Itt maga a panasz nehézsége a költség, és a vevő ugyanúgy szó nélkül megy el, mint a kosárnál (saját következtetés).

### A TurboTax-eset

**129. oldal, „Marketing Insight: Net Promoter and Customer Satisfaction”.** A keretes írás Reichheld Net Promoter-módszeréről szól. Ebben szerepel: amikor az Intuit a TurboTax termékre alkalmazta a Net Promotert, a visszajelzésből kiderült, hogy a vevők elégedetlenek a szoftver visszatérítési (rebate) eljárásával. Miután az Intuit eltörölte a vásárlás igazolásának követelményét, az eladások 6%-kal nőttek. A pontos szám: **6 percent**. Az eset tehát egy mérésből (NPS-visszajelzés) kiderült akadály elhagyásáról szól, és nem a vásárlás előtti, hanem a vásárlás utáni visszatérítési lépésről.

Idézet (129. oldal), a mondat soronként ellenőrizve, mert a kinyert szövegben a keretes írás sorai a főszöveg soraival váltakoznak: „When Intuit applied Net Promoter to its […] TurboTax product, feedback revealed dissatisfaction with the soft- […] ware’s rebate procedure. After Intuit dropped the proof-of-purchase […] requirement, sales jumped 6 percent.”

Idézet (129. oldal): „Reichheld says he developed NPS in response to overly”

Mit ad az alkalomhoz: a 16. dia tényanyaga, és egy akadály elvételének legközelebbi példája a fejezetben. A könyv nem állítja, hogy az akadály elvétele többet hozott volna bármilyen új érvnél; ez az összehasonlítás nem a könyvé. A vázlat mondata („több eladást hozott, mint bármilyen új érv”) ezért így nem tulajdonítható Kotlernek.

### Megtartás: „five times more”

**139–140. oldal, Attracting and Retaining Customers, Reducing Defection, Retention Dynamics.** Új vevőt szerezni drága, és a megszerzés módja is számít: egy vizsgálatban a 35%-os kedvezménnyel szerzett vevők hosszú távú értéke kb. fele volt a kedvezmény nélkül szerzettekének. Ha a cég nem tartja meg a vevőt, olyan, mintha lyukas vödörbe öntene vizet. A 140. oldali felsorolás: új vevőt szerezni akár ötször többe kerülhet, mint a meglévőt elégedetten megtartani; az átlagos cég évente vevői 10%-át elveszíti; a lemorzsolódás 5%-os csökkentése iparágtól függően 25–85%-kal növelheti a profitot. A marketing-tölcsér (5.4 ábra) a szakaszok közti konverziós arányokkal megmutatja a szűk keresztmetszetet. Az összefoglalóban (147. oldal) ugyanez határozottabban: a becslés szerint ötször annyiba kerül.

Idézet (140. oldal): „Acquiring new customers can cost five times more than satisfying and retaining current ones.”

Idézet (140. oldal): „The average company loses 10 percent of its customers each year.”

Idézet (140. oldal): „A 5 percent reduction in the customer defection rate can increase profits by 25 percent to”

Idézet (139. oldal): „Adding customers here is like adding water to a leaking bucket.”

Idézet (139. oldal): „One study showed that cus- tomers acquired through the offer of a 35 percent discount had about one-half the long-term value […] of customers acquired without any discount.”

Idézet (140. oldal): „the funnel allows marketers to identify any bottleneck stage or barrier to building a loyal”

Idézet (147. oldal): „The cost of attracting a new customer is […] estimated to be five times the cost of keeping a current”

Mit ad az alkalomhoz: a 18. dia. A „five times” a 140. oldalon „can cost”, vagyis feltételes; a szöveg forrása a 74. végjegyzet, ami nincs a fájlban. A lyukas vödör jó kép arra, miért kevés látogatót hozni, ha az oldal nem tartja meg (saját következtetés). A 35%-os kedvezmény adata vitapont: a kedvezmény mint ösztönző gyengébb vevőt hoz.

### CRM és érintkezési pont

**135. oldal, Customer Relationship Management.** A CRM az egyes vevőkről szóló részletes információ és minden érintkezési pont gondos kezelése a lojalitás maximalizálására. Érintkezési pont minden alkalom, amikor a vevő találkozik a márkával: a tényleges élménytől a kommunikáción át a futó megfigyelésig. A szálloda példáján: foglalás, bejelentkezés, kijelentkezés, törzsvendég-program.

Idézet (135. oldal): „Customer relationship management (CRM) is the process of carefully managing detailed […] information about individual customers and all customer “touch points” to maximize loyalty.”

Idézet (135. oldal): „A customer touch point is any occasion on which a customer encounters the brand and product—”

Mit ad az alkalomhoz: a 2. alkalom touchpoint-fogalmának folytatása. A saját felület az a touchpoint, amelyről a márka a legtöbbet tudhat és a legtöbbet dönthet (saját következtetés).

### Személyre szabás a weben: Domino's

**136. oldal, Personalizing Marketing.** A cégek e-mailt, weboldalt, ügyfélszolgálatot és adatbázist használnak a folyamatos kapcsolathoz. A Domino's weboldalán a vevő minden lépést maga irányít: látja a pizzája képét összeállítás közben, látja a pontos árat, és követheti a rendelést a sütőtől a kiszállításig.

Idézet (136. oldal): „Companies are using e-mail, Web sites, call centers, […] databases, and database software to foster continuous contact between company and customer.”

Idézet (136. oldal): „Domino’s has put the customer in charge of ordering a pizza delivery every step”

Idézet (136. oldal): „The Web site also shows exactly what the com-”

Mit ad az alkalomhoz: a weboldalas súrlódáscsökkentés egyetlen részletes példája a fejezetben. Az ár azonnali mutatása és a rendeléskövetés a pénzbeli és a pszichés költség (bizonytalanság) csökkentése (saját következtetés).

### Engedélyalapú marketing (Godin)

**136–137. oldal, Permission marketing.** Az engedélyalapú marketing csak a vevő kifejezett engedélye után keresi meg őt, abból kiindulva, hogy a tömegmédiás „megszakító marketing” már nem működik. Seth Godin szerint erősebb a kapcsolat, ha a márka tiszteli a vevő kívánságát, és csak akkor küld üzenetet, amikor ő hajlandóságot mutat a mélyebb kapcsolatra. Godin szerint ez azért működik, mert „anticipated, personal, and relevant”. Kotler hozzáteszi a korlátját: feltételezi, hogy a vevő tudja, mit akar, pedig sokszor nem; a „participatory marketing” talán jobb fogalom.

Idézet (136. oldal): „Permission marketing, the practice of marketing to consumers only after gaining their expressed […] permission, is based on the premise that marketers can no longer use “interruption marketing””

Idézet (137. oldal): „develop stronger consumer relationships by respecting consumers’ wishes and sending messages […] only when they express a willingness to become more involved with the brand.”

Idézet (137. oldal): „permission marketing works because it is “anticipated, personal, and relevant.””

Idézet (137. oldal): „Permission marketing, like other personalization approaches, presumes consumers know”

Idézet (137. oldal): „“Participatory marketing” may be a more appropriate concept than permission market-”

Mit ad az alkalomhoz: a 17. dia Kotler-része. A WIFM és a „Watch, don't ask” Kotlernél nincs meg, azok Chaffey 6. fejezetéből jönnek. Az „anticipated, personal, and relevant” hármas jó mérce az e-mail-folyamat beadandóhoz: a levelet várja-e, neki szól-e, érdekli-e (saját következtetés).

### Vélemények, ajánlások, és amikor a személyre szabás visszaüt

**138–139. oldal, Customer Reviews and Recommendations.** A vásárlói értékelések egyre fontosabb döntési tényezők. A PETCO az értékeléseket e-mailekbe és bannerekbe tette, és az átkattintási arány jelentősen nőtt. Egy Forrester-vizsgálatban a vevők 50%-a hasznosnak tartotta a negatív értékeléseket. A szöveg figyelmeztet: a gépi ajánlások visszaüthetnek, ha rendre mellélőnek. A 138. oldalon az is áll, hogy a vevőknek saját életük van, és csak néhányan, csak néha akarnak bevonódni a márkába.

Idézet (138. oldal): „Online pet food retailer PETCO actually started using consumer product ratings and reviews […] in e-mails and banner ads, finding the click-through rate increased considerably as a result.”

Idézet (139. oldal): „found negative reviews helpful.”

Idézet (139. oldal): „when customers are bombarded by computer-generated recom-”

Idézet (138. oldal): „Consumers have lives, jobs, families, hobbies, goals, and commitments, and many things”

Mit ad az alkalomhoz: a vélemény a weboldalon a társas és funkcionális kockázat csökkentője (lásd a 6. fejezetet). A „Consumers have lives” mondat ellensúly a loyalty-lelkesedéshez: a regisztráció és a klub a vevőnek is költség (saját következtetés).

### Loyalty programok és klubok

**141–142. oldal, Building Loyalty, Developing Loyalty Programs.** A megtartást építő tevékenységek pénzügyi, társas vagy strukturális kötődést adnak. Az 5.5 ábra egyik pontja: legyen könnyű a vevőnek elérni a megfelelő munkatársat; egy másik: mérlegelni kell a gyakorisági és klubprogramokat. A gyakorisági program (FP) a gyakran és sokat vásárlót jutalmazza. Az iparágban az első nyer a legtöbbet, utána a program mindenkinek pénzügyi teher lehet. Egyes programok bezárják a vevőt, és magas váltási költséget teremtenek; pszichés lökést és kiváltságérzetet is adnak. A nyitott klub jó adatbázis-építésre és vevőszerzésre, a zárt (tagdíjas, feltételhez kötött) klub erősebben épít hosszú távú lojalitást, mert a tagdíj és a feltételek kiszűrik a futó érdeklődőket. Példák: Chicken of the Sea Mermaid Club (80 000 tag, hírlevél, visszajelzés), Apple felhasználói csoportok.

Idézet (141. oldal): „adding financial benefits, social benefits, or structural ties.”

Idézet (141. oldal): „Make it easy for customers to reach appropriate company staff and express their needs, perceptions, and complaints.”

Idézet (142. oldal): „Frequency programs (FPs) are designed to reward […] customers who buy frequently and in substantial amounts.”

Idézet (142. oldal): „Typically, the first company to introduce a FP in an industry gains the most benefit, especially if”

Idézet (142. oldal): „Some FPs generate rewards in a way that locks customers in and creates significant costs to switching.”

Idézet (142. oldal): „also produce a psychological boost and a feeling of being special and elite that customers value.”

Idézet (142. oldal): „building a database or snagging customers from competitors, limited-membership clubs are […] more powerful long-term loyalty builders. Fees and membership conditions prevent those with […] only a fleeting interest in a company’s products from joining.”

Idézet (141. oldal): „Chicken of the Sea has 80,000 members in its Mermaid Club”

Mit ad az alkalomhoz: a 18. dia, és a vázlat vitapontja szó szerint itt van: a zárt klub belépési feltétele szándékos akadály, és Kotler szerint épp ettől erősebb. Ez nem cáfolja, hogy az akadályokat el kell venni, hanem pontosítja: az akadály elvétele a belépni akarónak segít, a kiszűrés a márkának (saját következtetés).

### Visszahódítás

**143. oldal, Win-Backs.** Gyakran könnyebb a volt vevőt visszahozni, mint újat találni, mert a cég ismeri a nevét és az előzményeit. A kilépési interjú és az elvesztett vevők felmérése feltárja az elégedetlenség okait.

Idézet (143. oldal): „ex-customers (because the company knows their names and histories) than to find new ones.”

Mit ad az alkalomhoz: az e-mail-folyamat utolsó szakasza (újraaktiválás) Kotlernél ezzel indokolható.

### Adatbázis és automatizált levelezés

**143–145. oldal, Customer Databases and Database Marketing.** A levelezőlista csak név, cím, telefonszám. A vevői adatbázis ennél sokkal több: tranzakciók, regisztrációs adatok, telefonos megkeresések, cookie-k és minden érintkezés. A Fingerhut háztartásonként kb. 1400 adatot tart nyilván. Az adatbázis öt felhasználása közül kettő az automatizált levelezés: a vásárlás után automatikus sorozat (egy hét múlva köszönőlevél, öt hét múlva új ajánlat, tíz hét múlva, ha nem reagált, telefon és kedvezmény), és az automatikus levelezőprogramok (születésnap, évforduló, ünnepi emlékeztető, szezonon kívüli ajánlat).

Idézet (143. oldal): „Many companies confuse a customer mailing list with a customer database.”

Idézet (143. oldal): „much more information, accumulated through customer transactions, registration information, […] telephone queries, cookies, and every customer contact.”

Idézet (143. oldal): „Fingerhut possesses some 1,400 pieces of information about each of the 30 million households”

Idézet (145. oldal): „Following a sale, it can set up an automatic sequence of activities: One week later send a thank-you note; […] five weeks later send a new offer; ten weeks later (if customer has not responded) phone and”

Idézet (145. oldal): „Automatic mailing programs (automatic marketing) can […] send out birthday or anniversary cards, holiday shopping reminders, or off-season promo-”

Mit ad az alkalomhoz: a 19. dia Kotler-kiegészítése. A háromlépéses sorozat (1., 5., 10. hét, feltétellel) egy kész e-mail-folyamat minta triggerrel és időzítéssel; a beadandó e-mail-folyamatának egyszerű kiindulópontja lehet. A regisztráció Kotlernél az adatbázis egyik forrása.

### Az adatbázis árnyoldala és az adatvédelem

**145–146. oldal, The Downside of Database Marketing and CRM, Marketing Insight: The Behavioral Targeting Controversy.** Öt probléma közül a negyedik az adatvédelem: nem minden vevő akar kapcsolatot a céggel, és van, akit zavar, hogy a cég ennyi személyes adatot gyűjtött róla. Az online cégeknek el kell magyarázniuk az adatvédelmi szabályaikat, és meg kell adniuk a jogot, hogy a vevő adatait ne tárolják. Az európai országok nem nézik jó szemmel az adatbázis-marketinget, az EU törvényt hozott, ami 27 tagállamban fékezi. A Deloitte szerint a cégek 70%-a alig vagy egyáltalán nem látott javulást a CRM bevezetésétől. A keretes írás a cookie-alapú viselkedési célzásról: egy 2009-es amerikai felmérésben a válaszadók kb. kétharmada ellenezte, és kétharmaduk szerint joguk volna tudni mindent, amit egy weboldal tud róluk. A Hotmail-regisztrációnál nevet, életkort, nemet és irányítószámot kellett megadni. A fejezet záró mondata: a feltárt összefüggéseknek a vevő számára is elfogadhatónak kell lenniük.

Idézet (145. oldal): „Not all customers want a relationship with the company. Some may resent knowing the […] company has collected that much personal information about them. Online companies […] should explain their privacy policies and give consumers the right not to have their informa-”

Idézet (145. oldal): „European countries do not look favorably on database marketing and are protec-”

Idézet (145–146. oldal): „The European Union passed a law handicapping the […] growth of database marketing in its 27 member countries.”

Idézet (145. oldal): „Deloitte Consulting found that 70 percent of”

Idézet (146. oldal): „In one 2009 U.S. survey, about two-thirds of respondents”

Idézet (146. oldal): „Two-thirds of respondents also believed laws should give people the right to”

Idézet (146. oldal): „account, for example, is required to give the company his or her name,”

Idézet (146. oldal): „the discovered relationships must be valid and acceptable to consumers.”

Mit ad az alkalomhoz: a 21. dia háttere, de csak háttér. A könyv a GDPR előtti (2012-es) állapotot írja le, a törvényt nem nevezi meg, hozzájárulásról, opt-inről vagy cookie-sávról nem szól. A jelenlegi szabályokhoz a vázlat szerint külső hivatalos forrás kell (EUR-Lex, NAIH). A 147. oldali Marketing Debate („Online versus Offline Privacy”) vitakérdésnek használható.


## Kotler, Keller, 6. fejezet, az észlelt kockázat (csak ez a rész)

**170–171. oldal, Intervening factors, perceived risk.** A vásárlási szándék és a döntés közé két tényező léphet (6.6 ábra): mások attitűdje (170. oldal) és a váratlan helyzeti tényezők (171. oldal). A döntés módosítását, elhalasztását vagy elkerülését erősen befolyásolja az észlelt kockázat egy vagy több fajtája. A hat típus (171. oldal):

| Angol név | A könyv meghatározása |
|---|---|
| Functional risk | „The product does not perform to expectations.” |
| Physical risk | „The product poses a threat to the physical well-being or health of the user or others.” |
| Financial risk | „The product is not worth the price paid.” |
| Social risk | „The product results in embarrassment in front of others.” |
| Psychological risk | „The product affects the mental well-being of the user.” |
| Time risk | „The failure of the product results in an opportunity cost of finding another satis- factory product.” |

A kockázat mértéke függ a tét összegétől, a tulajdonságok bizonytalanságától és a vevő önbizalmától. A vevőknek saját rutinjaik vannak a kockázat csökkentésére: elkerülik a döntést, barátoktól kérnek információt, ismert márkát és garanciát választanak. A marketinges feladata a könyv szerint: megérteni, mi váltja ki a kockázatérzetet, és olyan információt és támogatást adni, ami csökkenti. Konkrét eszközt (oldalelemet) a könyv itt nem sorol fel; a vevői rutinok között a garancia és a nemzeti márka szerepel.

Idézet (171. oldal): „A consumer’s decision to modify, postpone, or avoid a purchase decision is heavily influenced […] by one or more types of perceived risk:”

Idézet (171. oldal): „Functional risk—The product does not perform to expectations.”

Idézet (171. oldal): „Physical risk—The product poses a threat to the physical well-being or health of the user or others.”

Idézet (171. oldal): „Financial risk—The product is not worth the price paid.”

Idézet (171. oldal): „Social risk—The product results in embarrassment in front of others.”

Idézet (171. oldal): „Psychological risk—The product affects the mental well-being of the user.”

Idézet (171. oldal): „Time risk—The failure of the product results in an opportunity cost of finding another satis- factory product.”

Idézet (171. oldal): „The degree of perceived risk varies with the amount of money at stake, the amount of attribute […] uncertainty, and the level of consumer self-confidence.”

Idézet (171. oldal): „Consumers develop routines for reducing the uncertainty and negative consequences of risk, such as avoiding decisions, gathering informa- tion from friends, and developing preferences for national brand names and warranties.”

Idézet (171. oldal): „Marketers must understand the factors that provoke a feeling of risk in consumers and provide information and support to reduce it.”

Idézet (170. oldal): „The first factor is the attitudes of others.”

Idézet (171. oldal): „The second factor is unanticipated situational factors that may erupt to change the purchase”

Idézet (171. oldal): „Preferences and even purchase intentions are not completely reliable”

Mit ad az alkalomhoz: a 14. dia. A kockázat ott jelentkezik, ahol a szándék már megvan, vagyis a saját felületen, a döntés előtti utolsó lépésben. Ez az akadályok megszüntetésének könyvbeli helye az oldalon (saját következtetés). A 5. fejezet 126. oldali mondata („absorbing some buyer risk by offering a warranty”) a két fejezetet összeköti.

### A v9 deck 25. diája és a könyv

A v9 deck (`konyvek/v9-deck-journey-blokk.md`) 25. diája (`ph:2`, 13:59, „Pszichológia”), szó szerint:

> Amit a fejében mérlegel, mielőtt fizet
> Hat kockázat
> Nem fog működni · árt nekem · nem ér annyit · ciki lesz mások előtt · rosszul érzem magam tőle · újra kell keresnem
> Küszöb
> Minden szempontra van egy minimum. Ami nem éri el, kiesik, bármilyen jó máshol.
> Egy szempont
> A legfontosabb szempont dönt, a többit meg sem nézi.
> Mások
> Az utolsó pillanatban is elveheti a döntést egy vélemény vagy egy váratlan helyzet.
> Kotler & Keller, 170–171. oldal. Minden kockázathoz tartozik egy weboldalelem, ami leveszi. Ez lesz a harmadik alkalom.

Az oktatói jegyzetből ide tartozó mondatok: „A vásárló nem előnyöket mérlegel, hanem kockázatokat zár ki. Hatféle kockázat van, és ebből csak egy a pénz.” és „A jó ajánlat mellé kockázatot kell levenni: garancia, vélemény, ingyenes visszaküldés, méretsegéd, arc és név a weboldalon.”

Összevetés a könyvvel:
- A hat kockázat sorrendje és tartalma egyezik a 171. oldallal: functional = nem fog működni, physical = árt nekem, financial = nem ér annyit, social = ciki lesz mások előtt, psychological = rosszul érzem magam tőle, time = újra kell keresnem.
- Pontatlanság: a physical risk a könyvben „the user or others”, a dia csak a felhasználót („árt nekem”) mondja.
- A time risk a könyvben a termék kudarcából eredő alternatív költség (egy másik megfelelő termék megkeresése). Az „újra kell keresnem” ezt jól adja vissza.
- Az oldalszám: a hat kockázat csak a 171. oldalon van. A dia egészére a 170–171. jó, mert a „Küszöb” (conjunctive heuristic) és az „Egy szempont” (lexicographic heuristic) a 170. oldalon, a „Mások” (attitudes of others, unanticipated situational factors) a 170–171. oldalon van.
- „Minden kockázathoz tartozik egy weboldalelem, ami leveszi”: ez nincs a könyvben. Kotler csak annyit mond, hogy a marketinges adjon információt és támogatást a kockázat csökkentésére. Az oldalelemekhez rendelés az oktatóé.
- A jegyzet eszközlistájából a könyvben csak a garancia szerepel (171. oldal a vevői rutinok között, 126. oldal a hátrányban lévő eladó eszközeként). A vélemény a könyvben az „attitudes of others” mellett, az infomediárok értékeléseként jelenik meg (171. oldal), nem kockázatcsökkentő eszközként. Az ingyenes visszaküldés, a méretsegéd és az „arc és név” nincs a 6. fejezetnek ebben a részében. Az 5. fejezetben a Nordstrom „hassle-free return policy” (148. oldal) a visszaküldés legközelebbi említése.
- „Hatféle kockázat van, és ebből csak egy a pénz”: egyezik a listával. „A vásárló nem előnyöket mérlegel, hanem kockázatokat zár ki”: ez a szó szerint így nincs a könyvben; a 170. oldalon a nem kompenzáló döntési modellek mondanak hasonlót, a kockázattal való összekötés az oktatóé.

Idézet (170. oldal): „the consumer sets a minimum acceptable cutoff level for each at-”

Idézet (170. oldal): „the consumer chooses the best brand on the basis of its per-”

## Krug: Don't Make Me Think, Revisited (3. kiadás, 2014)

Feldolgozva: 2026. október 5. Forrás: `konyvek/uj/krug-dont-make-me-think.txt` (pdftotext kimenet). A PDF-ben nincs nyomtatott oldalszám, ezért minden hivatkozás fejezetszintű. Minden idézetet a `findq_pdf.py`-val kerestem vissza; a fejezetet a fájlban elfoglalt helyük alapján magam állapítottam meg, mert az ellenőrző a 3. fejezet egyik „Chapter 10.” kereszthivatkozása után tévesen 10. fejezetet ír.

A könyv első kiadása 2000-es, a második 2006-os, ez a harmadik 2013 novemberében zárult (az előszó dátuma), a kolofón szerint 2014-es. Krug maga írja, hogy a könyv elavultnak hat: „It feels dated. After all, it’s thirteen years old, which is like a hundred years in Internet time.” (Preface). Azt is ő mondja, mi marad érvényes: „usability is about people and how they understand and use things, not about technology. And while technology often changes quickly, people change very slowly.” (Preface). Ami jelenleg is használható: az első törvény, a szkennelés és a satisficing, a kezdőlap szerepe, a goodwill-tartály és a saját kezű usability teszt menete. Ami elavult, azt a szöveg maga jelzi: a mobilról azt írja, hogy „Web and app design for mobile devices is still in its formative “Wild West” days” (Chapter 10), a mobil képernyőfelvételről pedig, hogy „As of this writing, robust mobile screen recording and screen sharing apps aren’t available” (Chapter 10). A flat designról: „which may have waned by the time you read this” (Chapter 10). A felsorolt eszközök (GoToMeeting, WebEx, Camtasia, UserTesting.com) és a résztvevői díjak dollárban a 2013-as állapotot mutatják. A UserTesting.com ajánlásánál Krug közli, hogy kapcsolatban áll velük: „Full disclosure: I receive some compensation from UserTesting.com for letting them use my name.” (Chapter 9). E-mail-automatizálásról, loyalty-programról és adatvédelmi szabályozásról a könyv nem szól (lásd: Nem találtam).

### Az első törvény

**Chapter 1 (Don't make me think!), Krug első törvénye.** A legfontosabb szabály: egy oldalnak ránézésre érthetőnek kell lennie, a felhasználónak nem kell gondolkodnia azon, mi ez és hogyan használja. Minden kérdőjel a fejben kognitív teher, és ezek összeadódnak. Krug szerint a felesleges gondolkodtatás a bizalmat is rontja, nem csak az időt viszi. Ha valami nem lehet magától értetődő, legalább magyarázza meg önmagát.
Idézet: „If you have room in your head for only one usability rule, make this the one.” (Chapter 1)
Idézet: „When you’re creating a site, your job is to get rid of the question marks.” (Chapter 1)
Idézet: „The fact that the people who built the site didn’t care enough to make things obvious—and easy—can erode our confidence in the site and the organization behind it.” (Chapter 1)
Mit ad az alkalomhoz: a súrlódás legegyszerűbb mértékegysége a kérdőjel. A csapatok a márka oldalán megszámolhatják, hol áll meg a látogató egy pillanatra. A harmadik idézet a bizalomhoz köti: a súrlódás nem semleges, a márka megítélését is rontja.

**Introduction (Read me first), a usability definíciója.** Krug definíciója szerint használható az, amit egy átlagos vagy átlag alatti képességű ember ki tud ismerni annyira, hogy elvégezzen vele valamit, és közben ne kerüljön több fáradságba, mint amennyit megér.
Idézet: „can figure out how to use the thing to accomplish something without it being more trouble than it’s worth.” (Introduction)
Mit ad az alkalomhoz: a „more trouble than it’s worth” a Kotler-féle költségoldal (idő, energia) usability-nyelven (saját következtetés). Jól összeköti a 13. diát a súrlódás diáival.

### Szkennelés, satisficing, muddling through

**Chapter 2 (How we really use the Web), a három tény.** A felhasználó nem olvas, hanem szkennel; nem a legjobb lehetőséget választja, hanem az első elfogadhatót (satisficing, Herbert Simon kifejezése); és nem érti meg, hogyan működik az oldal, hanem átvergődik rajta. Krug szerint a tervezők racionális, figyelmes olvasót képzelnek el, a valóság egy 60 mérföldes sebességgel elsuhanó óriásplakát. Ha a látogató „érti”, nagyobb eséllyel találja meg, amit keres, és visszajön.
Idézet: „the user’s reality is much closer to “billboard going by at 60 miles an hour.”” (Chapter 2)
Idézet: „We don’t read pages. We scan them.” (Chapter 2)
Idézet: „we choose the first reasonable option, a strategy known as satisficing.” (Chapter 2)
Idézet: „You can get away with a site that people muddle through only until someone builds one down the street that makes them feel smart.” (Chapter 2)
Mit ad az alkalomhoz: a landing page-auditnál nem az a kérdés, mit ír az oldal, hanem az, mit lát belőle az, aki átfut rajta. A satisficing azt is jelenti, hogy az első kattintható dolog nyer, vagyis a fő cselekvésnek ott kell lennie, ahová először néz.

**Chapter 1 (Don't make me think!), aki magát hibáztatja.** Krug megjegyzi, hogy sokan meglepően sokáig kitartanak egy frusztráló oldalon, és nem az oldalt, hanem magukat okolják.
Idézet: „often blaming themselves and not the site.” (Chapter 1)
Mit ad az alkalomhoz: ha a látogató magát hibáztatja, az elakadás oka mégis az oldalon van; az oldal dolga ezt magára venni (saját következtetés).

### Plakáttervezés: konvenció, hierarchia, kattinthatóság, zaj

**Chapter 3 (Billboard Design 101), tervezés szkennelésre.** Krug hat dolgot javasol: konvenciók követése, világos vizuális hierarchia, jól elkülönülő oldalterületek, egyértelmű kattinthatóság, a zaj csökkentése és szkennelhető szöveg. A kattinthatóságról már az 1. fejezetben is kimondja, hogy azon egy ezredmásodpercet sem kellene gondolkodni. A zajnál azt javasolja, hogy szerkesztéskor mindent zajnak tekintsünk, amíg be nem bizonyosodik az ellenkezője.
Idézet: „As a user, I should never have to devote a millisecond of thought to whether things are clickable—or not.” (Chapter 1)
Idézet: „start with the assumption that everything is visual noise” (Chapter 3)
Idézet: „In the face of limited time and attention, everything that’s not part of the solution must go.” (Chapter 3)
Mit ad az alkalomhoz: kész szempontlista a landing page-audithoz (konvenció, hierarchia, kattinthatóság, zaj). A „must go” mondat az akadályok elvételének egyik legtisztább könyvbeli megfelelője: elvenni, nem hozzátenni.

### Kattintások és nehéz döntések, űrlapok

**Chapter 4 (Animal, Vegetable, or Mineral?), Krug második törvénye.** Nem a kattintások száma számít, hanem az, hogy egy-egy kattintás mennyi gondolkodást és bizonytalanságot kíván. Krug példája egy cikkoldal, ahol el kell döntenie, előfizető, tag vagy egyik sem, és közben a kérdés átfordul: megéri-e egyáltalán a cikk. A nehéz kérdésekről az űrlapoknál is beszél, Caroline Jarrett könyvére hivatkozva; a szükséges segítség legyen rövid, időben érkező és megkerülhetetlen.
Idézet: „It doesn’t matter how many times I have to click, as long as each click is a mindless, unambiguous choice.” (Chapter 4)
Idézet: „At this point, the question I’m asking myself is probably changing from “How do I answer this question?” to “Just how interested am I in this article?”” (Chapter 4)
Mit ad az alkalomhoz: a második idézet a regisztrációs akadály pontos esete. Egy regisztrációs vagy előfizetési lépés a látogató saját motivációját teszi próbára, és ott veszít a márka (saját következtetés). Jó példa a Printa-csapat „fizetési folyamat elakadása” megfigyeléséhez.

### Felesleges szavak

**Chapter 5 (Omit needless words), Krug harmadik törvénye.** Minden oldalon a szavak fele elhagyható, aztán a maradék fele is. Két fő bűnös: a „happy talk” (üdvözlő, öndicsérő szöveg, ami nem mond semmit) és az utasítások, amiket senki nem olvas el, csak ha már minden más kudarcot vallott.
Idézet: „Get rid of half the words on each page, then get rid of half of what’s left.” (Chapter 5)
Idézet: „it focuses on saying how great we are, as opposed to explaining what makes us great.” (Chapter 5)
Idézet: „no one is going to read them—at least not until after repeated attempts at “muddling through” have failed.” (Chapter 5)
Mit ad az alkalomhoz: az audit egyik kérdése lehet, hogy a márka oldalán az első képernyő szövege azt mondja-e el, mitől jó, vagy csak azt, hogy jó. Ez közvetlenül kapcsolódik az 1. beadandó értékajánlatához (saját következtetés).

### Navigáció és mélyen érkező látogató

**Chapter 6 (Street signs and Breadcrumbs), navigáció, bizalom, űrlapoldal.** Krug szerint a navigáció nem az oldal egyik eleme, hanem maga az oldal. Három kevésbé nyilvánvaló szerepe: megmutatja, mi van itt, megmutatja, hogyan kell használni, és bizalmat ad azok iránt, akik készítették. Űrlapoldalon (fizetés, regisztráció, feliratkozás) a teljes navigáció zavaró lehet, ott elég a logó, a Home és a kitöltést segítő linkek. A link és az oldal neve közti egyezést „social contract”-nak hívja.
Idézet: „Navigation isn’t just a feature of a Web site; it is the Web site” (Chapter 6)
Idézet: „It gives us confidence in the people who built it. Every moment we’re in a Web site, we’re keeping a mental running tally: “Do these guys know what they’re doing?”” (Chapter 6)
Idézet: „On pages where a form needs to be filled in, the persistent navigation can sometimes be an unnecessary distraction.” (Chapter 6)
Idézet: „The name of the page will match the words I clicked to get there.” (Chapter 6)
Mit ad az alkalomhoz: az utolsó idézet a 11. dia (a hirdetés ígérete és a céloldal egyezése) usability-oldali párja: ha a kattintott szó és az oldal címe eltér, a bizalom csökken.

**Chapter 6 (Street signs and Breadcrumbs), a trunk test.** Krug „csomagtartó-tesztje”: valakit bekötött szemmel letesznek az oldal egy mély pontján, és azonnal meg kell tudnia mondani, milyen oldalon van, melyik aloldalon, mik a fő részek, hol tart, és hogyan kereshet. A teszt alapgondolata, hogy a látogató ritkán a kezdőlapon érkezik, hanem keresőből, közösségi oldalról vagy e-mailből egyenesen egy belső oldalra.
Idézet: „it’s so easy to forget that the Web experience is often more like being abducted than following a garden path.” (Chapter 6)
Idézet: „What site is this? (Site ID)” (Chapter 6)
Mit ad az alkalomhoz: a trunk test öt perc alatt elvégezhető a márka bármelyik landing oldalán, és pontosan arra a helyzetre szól, amikor Anna egy Reelsből vagy Google-keresésből egy tanfolyamoldalra érkezik.

### A kezdőlap és a landing: mit kell megmondania

**Chapter 7 (The Big Bang Theory of Web Design), a nagy kép.** A kezdőlapnak rengeteg feladata van, de az egyetlen, ami nem veszhet el, és ami a leggyakrabban elvész: annak elmondása, mi ez az oldal. Az első néhány másodperc döntő, mert az első benyomás tartósnak bizonyul, és aki rosszul indul, egyre jobban eltéved. A kezdőlap egyben a hitelesség és a bizalom megteremtésének helye; egyes látogatóknak ez az egyetlen esély.
Idézet: „Right off the bat, the Home page has to tell me what site this is and what it’s for—and if possible, why I should be here and not at some other site.” (Chapter 7)
Idézet: „They haven’t made it clear enough what the site is.” (Chapter 7)
Idézet: „the first few seconds you spend on a new Web site or Web page are critical.” (Chapter 7)
Idézet: „we make snap judgments, but they tend to be a pretty reliable predictor of our more reasoned assessments.” (Chapter 7)
Idézet: „If people are lost when they start out, they usually just keep getting...loster.” (Chapter 7)
Idézet: „For some visitors, the Home page will be the only chance your site gets to create a good impression.” (Chapter 7)
Mit ad az alkalomhoz: ez a 10. dia („Mit lát, amikor megérkezik”) Krug-forrása. Az „öt másodperc” így nem szerepel, Krug „first few seconds”-ot ír, és egy 50 ezredmásodperces kísérletre utal (cím szerint: „Attention Web Designers: You Have 50 Milliseconds to Make a Good First Impression!”). Ha a dián szám kell, ez a két megfogalmazás forrásolható.

**Chapter 7 (The Big Bang Theory of Web Design), minden oldal belépési pont.** Krug elfogadja, hogy a látogatók sokszor nem a kezdőlapon lépnek be, hanem e-mailből, blogból vagy közösségi oldalról egy mély oldalra. Ezért minden oldalnak orientálnia kell, és sokan ezután felugranak a kezdőlapra tájékozódni.
Idézet: „Now people are just as likely—or more likely—to enter your site by clicking on a link in an email, a blog, or something from a social network that takes them directly to a page deep in your site.” (Chapter 7)
Idézet: „every page of your site should do as much as it can to orient them properly: to give them the right idea about who you are, what you do, and what your site has to offer.” (Chapter 7)
Mit ad az alkalomhoz: a 11. dia („Landing page, nem kezdőlap”) Krug-oldali forrása. Chaffey „who you are, what you do…” kérdése és Krug mondata szinte szóról szóra egyezik.

**Chapter 7 (The Big Bang Theory of Web Design), tagline, regisztráció, belépési pontok.** A jó tagline világos, rövid (hat-nyolc szó), megkülönböztet és előnyt mond; nem mottó. A kezdőlapon azonnal látszania kell, hol lehet keresni, böngészni, és ha van regisztráció, hol lehet regisztrálni vagy belépni. Krug figyelmeztet, hogy a misszió-nyilatkozat nem jó bevezető szöveg, és hogy a fő üzenet hiányát a szervezeten belül senki nem veszi észre.
Idézet: „a really good tagline is one that no one else in the world could use except you” (Chapter 7)
Idézet: „motto expresses a guiding principle, a goal, or an ideal, but a tagline conveys a value proposition.” (Chapter 7)
Idézet: „the places where I register or sign in should be prominent.” (Chapter 7)
Idézet: „the “main point” is the one thing nobody inside the organization will notice is missing.” (Chapter 7)
Mit ad az alkalomhoz: a tagline-kritérium közvetlen mérce a csapatoknak (Nielsen nyomán): használhatná-e ugyanezt a mondatot a versenytárs? Az utolsó idézet indokolja, miért kívülállóként, megfigyelőként kell auditálni.

**Chapter 7 (The Big Bang Theory of Web Design), a forgalom mint csapda.** A „golden goose” részben Krug leírja, hogy a kezdőlapi kiemelés túl jól működik: amit kiemelnek, az forgalmat kap, ezért mindenki kiemelést akar, a túlzsúfolt kezdőlap vesztesége viszont mindenkire szétterül (a közlegelő tragédiája).
Idézet: „The section that’s being promoted gets a huge gain in traffic, while the overall loss in effectiveness of the Home page as it gets more cluttered is shared by all sections.” (Chapter 7)
Mit ad az alkalomhoz: könyvbeli példa arra, hogy egy rész forgalma nőhet úgy, hogy az egész oldal teljesítménye romlik (saját következtetés). A 8. diához Chaffey mellé kiegészítésnek jó.

### Vita helyett megfigyelés

**Chapter 8 ("The Farmer and the Cowman Should Be Friends"), nincs átlagos felhasználó.** A csapatok azon vitatkoznak, mit szeretnek a felhasználók, pedig nincs átlagfelhasználó, és a kérdés rosszul van feltéve. A helyes kérdés, hogy egy adott elem adott helyen működik-e, és erre csak a teszt felel. Krug azt is leírja, hogy a „hype” kultúra (vezetés, marketing) ígéreteit a „craft” kultúra (tervezők, fejlesztők) kénytelen teljesíteni.
Idézet: „ALL WEB USERS ARE UNIQUE AND ALL WEB USE IS BASICALLY IDIOSYNCRATIC” (Chapter 8)
Idézet: „the realm of what works or doesn’t work.” (Chapter 8)
Idézet: „the burden of delivering on those promises lands on the shoulders of the craft culture artisans” (Chapter 8)
Mit ad az alkalomhoz: a beadandó műfajának indoklása: nem „szerintünk szép vagy csúnya”, hanem „működik vagy nem működik”. A hype és craft szétválás jól mutatja, hogy a hirdetés ígéretét az oldal váltja be vagy nem.

### A usability teszt mint olcsó megfigyelés

**Chapter 9 (Usability testing on 10 cents a day), mi a teszt és mi nem.** A fókuszcsoport arról szól, mit mondanak az emberek, a usability teszt arról, mit csinálnak: egyszerre egy embert figyelünk, ahogy tipikus feladatokat végez. Krug szerint egy felhasználó tesztelése száz százalékkal jobb, mint egy sem, és a saját kezű teszt kvalitatív módszer, nem bizonyít, hanem javítható problémákat talál. Gyakran az derül ki, hogy a vitatott részletek mellékesek, mert az értékajánlatot sem értik.
Idézet: „The main difference is that in usability tests, you watch people actually use things, instead of just listening to them talk about them.” (Chapter 9)
Idézet: „Testing one user is 100 percent better than testing none.” (Chapter 9)
Idézet: „The process isn’t rigorous at all: You give them tasks to do, you observe, and you learn. The result is actionable insights, not proof.” (Chapter 9)
Idézet: „it doesn’t make much difference whether you go with cascading menus or mega menus if nobody understands the value proposition of your site.” (Chapter 9)
Mit ad az alkalomhoz: a beadandó módszertani alapja. A „megfigyelnek, nem kitalálnak” elvet Krug szavaival lehet indokolni.

**Chapter 9 (Usability testing on 10 cents a day), a teszt menete.** Három résztvevő fordulónként elég, lazán toborozva („grade on a curve”). Egy órás menet: üdvözlés, néhány kérdés, a kezdőlap körbejárása (mit lát, kié az oldal, mit lehet itt csinálni, mire való), feladatok hangos gondolkodással, utólagos kérdések. A facilitátor nem segít; ha kérdeznek, visszakérdez. Már tervezés előtt érdemes versenytársak oldalait tesztelni.
Idézet: „RECRUIT LOOSELY AND GRADE ON A CURVE” (Chapter 9)
Idézet: „look at this page and tell me what you make of it: what strikes you about it, whose site you think it is, what you can do here, and what it’s for.” (Chapter 9)
Idézet: „encourage them to think out loud as much as possible.” (Chapter 9)
Idézet: „“What would you do if I wasn’t here?”” (Chapter 9)
Idézet: „we’re testing the site, not you.” (Chapter 9)
Idézet: „it’s a good idea to do a test of competitive sites.” (Chapter 9)
Mit ad az alkalomhoz: a „Home page tour” kérdései szó szerint használhatók a beadandó első lépésének. A versenytárs-teszt pontosan a csapatok helyzete: nem a saját oldalukat vizsgálják (saját következtetés).

**Chapter 9 (Usability testing on 10 cents a day), kiértékelés és javítás.** A megfigyelők ülésenként leírják a három legsúlyosabb problémát, csak ténylegesen megtörtént eseteket. A legsúlyosabbakat kell előbb javítani. A gyakori hiba, hogy a csapat ilyenkor hozzátesz (magyarázatot, utasítást), pedig gyakran elvenni kellene. A „kajak-problémák” (a felhasználó egy pillanatra eltéved, de segítség nélkül visszatalál) figyelmen kívül hagyhatók. Három tipikus probléma: nem értik a koncepciót, nincs ott a szó, amit keresnek, túl sok minden van az oldalon.
Idézet: „And they have to be observed problems; things that actually happened during one of the test sessions.” (Chapter 9)
Idézet: „FOCUS RUTHLESSLY ON FIXING THE MOST SERIOUS PROBLEMS FIRST” (Chapter 9)
Idézet: „But very often the right solution is to take something (or some things) away that are obscuring the meaning, rather than adding yet another distraction.” (Chapter 9)
Idézet: „Ignore “kayak” problems.” (Chapter 9)
Idézet: „Users are unclear on the concept.” (Chapter 9)
Mit ad az alkalomhoz: a harmadik idézet az akadályok elvételének legközelebbi szerzői megfelelője a könyvben.

### Mobil

**Chapter 10 (Mobile: It's not just a city in Alabama anymore), kis képernyő, sebesség, affordanciák.** Az alapelvek ugyanazok, de mobilon még gyorsabban mennek és még kevesebbet olvasnak. A helyhiány kezelése nem mehet a használhatóság rovására. Krug kifejezetten bosszantónak tartja, ha egy e-mailből vagy közösségi oldalról érkező linkre koppintva a mobil kezdőlapra kerül a látogató a keresett tartalom helyett. A lassúság frusztrációt és goodwill-vesztést okoz. Az affordanciák (vizuális jelek arra, hogyan használható valami) mobilon, hover nélkül és flat designnal könnyen eltűnnek.
Idézet: „If anything, people are moving faster and reading even less on small screens.” (Chapter 10)
Idézet: „MANAGING REAL ESTATE CHALLENGES SHOULDN’T BE DONE AT THE COST OF USABILITY” (Chapter 10)
Idézet: „Don’t leave me standing at the front door.” (Chapter 10)
Idézet: „Slow performance equals frustration for users and loss of goodwill for publishers.” (Chapter 10)
Idézet: „Affordances are visual clues in an object’s design that suggest how we can use it.” (Chapter 10)
Mit ad az alkalomhoz: a csapatok auditja mobilon is készüljön, mert a See fázisból (Reels, Instagram) érkezők jellemzően telefonon jönnek (saját következtetés). A „front door” mondat a 11. diához és a 15. dia betöltési idejéhez ad Krug-forrást. A mobil tesztelés technikai részei (kamera a készüléken, tükrözés helyett) 2013-as állapotot írnak le, és maga Krug is átmenetinek tartja őket.

### A goodwill-tartály

**Chapter 11 (Usability as common courtesy), mi a tartály.** Krug szerint minden látogató egy jóindulat-tartállyal érkezik, és minden probléma csökkenti a szintjét. Ha kiürül, a látogató elmegy, vagy rosszabb véleménye lesz a szervezetről. A tartály egyéni és helyzetfüggő (aki siet vagy egy rossz élményből jön, alacsonyabb szinttel érkezik), újratölthető, és egyetlen hiba is kiürítheti. Saját példája egy légitársaság oldala egy esetleges sztrájk reggelén: semmi információ, csak promóció. A fejezet kérdése a világosság mellett: „mensch”-ként viselkedik-e az oldal.
Idézet: „every time we enter a Web site, we start out with a reservoir of goodwill. Each problem we encounter on the site lowers the level of that reservoir.” (Chapter 11)
Idézet: „It’s idiosyncratic.” (Chapter 11)
Idézet: „It’s situational.” (Chapter 11)
Idézet: „You can refill it.” (Chapter 11)
Idézet: „just opening up a registration form with tons of fields may be enough to cause some people’s reserve to plunge instantly to zero.” (Chapter 11)
Idézet: „they did an outstanding job of depleting my goodwill towards both the airline and their Web site.” (Chapter 11)
Idézet: „Does my site behave like a mensch?” (Chapter 11)
Mit ad az alkalomhoz: a súrlódás mérhetővé tett képe. Krug a légitársasági látogatást lépésről lépésre, a tartály szintjével együtt írja le; ez a forma átvehető a beadandó naplójához.

**Chapter 11 (Usability as common courtesy), mi fogyasztja.** Az információ elrejtése (ügyfélszolgálati telefonszám, szállítási díj, ár), büntetés azért, mert nem az oldal által várt formában írom be az adatot, a feladathoz nem szükséges személyes adat kérése, hamis kedvesség, „sizzle” (hangulatfotók az utamban) és amatőr kinézet. Krug szerint a kinézet miatt ritkán megy el valaki. A pop-upról azt írja, hogy ha a statisztika szerint tíz százalékkal több bevételt hoz, és ez megéri a bosszúságot, üzleti döntésként vállalható, csak tudatosan.
Idézet: „The most common things to hide are customer support phone numbers, shipping rates, and prices.” (Chapter 11)
Idézet: „Don’t make me jump through hoops just because you don’t want to write a little bit of code.” (Chapter 11)
Idézet: „Most users are very skeptical of requests for personal information and find it annoying if a site asks for more than what’s needed for the task at hand.” (Chapter 11)
Idézet: „Having to wade through pages bloated with feel-good marketing photos makes it clear that you don’t understand—or care—that I’m in a hurry.” (Chapter 11)
Idézet: „almost no one is going to leave a site just because it doesn’t look great.” (Chapter 11)
Idézet: „if your statistics show you can get 10 percent more revenue by using pop-ups and you think it’s worth annoying your users, you can do it. It’s a business decision.” (Chapter 11)
Mit ad az alkalomhoz: kész akadálylista az audithoz. A szükségtelen személyes adat kérése egyszerre usability- és adatkezelési kérdés, ez híd a 21. diához (saját következtetés; Krug a jogi oldalt nem tárgyalja). A „kinézet miatt ritkán megy el” mondat feszültségben áll Chaffey Fogg-adatával (46,1%, a kinézet a hitelesség megítélésében), ez a 12. diánál vitapont lehet. A pop-up mondat az 5. kérdés (pop-up vitapont) Krug-oldali párja.

**Chapter 11 (Usability as common courtesy), mi tölti.** A fő feladatok legyenek nyilvánvalók és könnyűek; légy nyílt a kellemetlen dolgokról is (szállítási díj, parkolás, leállás); spórolj lépéseket a látogatónak; tegyél munkát bele; válaszolj a várható kérdésekre őszinte, friss GYIK-kel; tedd könnyűvé a hibából való visszatérést; ha nem tudod megadni, amit kér, legalább kérj elnézést. A lépésspórolás példája egy e-mailes visszaigazolás, amelyben a link egyből a csomagkövetést nyitja meg.
Idézet: „nothing should get in the way of making it dead easy to apply for a mortgage.” (Chapter 11)
Idézet: „Be upfront about things like shipping costs, hotel daily parking fees, service outages—anything you’d rather not be upfront about.” (Chapter 11)
Idézet: „Save me steps wherever you can.” (Chapter 11)
Idézet: „put a link in my email receipt that opens their site and submits my tracking number when I click it.” (Chapter 11)
Idézet: „If you can’t do what they want, at least let them know that you know you’re inconveniencing them.” (Chapter 11)
Mit ad az alkalomhoz: a Printa-csapat megfigyelése (aggódnak a szállítási költség és a visszaküldés miatt) szinte szó szerint Krug listája: a szállítási díj nyílt közlése tölti a tartályt, az elrejtése üríti. A visszaigazoló levél példája az e-mail-folyamat egyetlen konkrét Krug-esete.

### Manipuláció kontra meggyőzés

**Chapter 13 (Guide for the perplexed), a sötét oldal.** Krug elfogadja a meggyőzést, ha nem megtévesztő, de figyelmeztet a manipulációra. Enyhe példája az alapból bepipált, félig elrejtett hírlevél-feliratkozás. Azt is írja, hogy a usability teszt nem alkalmas annak mérésére, hogy valami kívánatos-e; az piackutatási kérdés. A végén néhány határozott szabályt ad, köztük: ne tegyél címkét az űrlapmezőbe.
Idézet: „I don’t have a problem with helping to persuade people to do things, either, as long as it’s not deceptive.” (Chapter 13)
Idézet: „using a slightly hidden checkbox checked by default to automatically sign you up for a newsletter.” (Chapter 13)
Idézet: „Whether something is desirable is a market research question, best answered by using market research tools and instruments.” (Chapter 13)
Idézet: „Don’t put labels inside form fields.” (Chapter 13)
Mit ad az alkalomhoz: az előre bepipált hírlevél-doboz a 21. dia (Chaffey 3. fejezet, előre bepipált doboz) usability-oldali párja; Krug „manipulációnak” nevezi. A jogi minősítéshez külső forrás kell, Krug nem jogi forrás.

**Chapter 13 (Guide for the perplexed), UX a teljes életcikluson.** Krug a UX-et úgy írja le, hogy a felhasználó igényeit a termék életciklusának minden szakaszában figyelembe veszi, a tévéreklámtól a vásárláson és a szállításkövetésen át a visszaküldésig.
Idézet: „UX sees its role as taking the users’ needs into account at every stage of the product life cycle” (Chapter 13)
Mit ad az alkalomhoz: összekötő mondat a 2. alkalom journey-térképe és a 3. alkalom saját terepe között.

## Weinschenk: 100 Things Every Designer Needs to Know About People (2011)

Susan Weinschenk, New Riders, 2011. Feldolgozva 2026. október 5-én a `konyvek/uj/weinschenk-100-things.txt` fájlból: a tartalomjegyzék végig, a releváns pontok teljes szövege lapról lapra. Minden idézet a `findq_pdf.py` kimenete, és szó szerint áll, a fájl „ﬁ” és „ﬂ” ligatúráival együtt (enélkül az ellenőrző nem találja meg). Az oldalszám a nyomtatott oldal. A könyvben a nyomtatott oldal a PDF-lap mínusz 13; ahol az ellenőrző None-t adott, a lap lábsorából olvastam ki, és mindenhol egyezett ezzel. A könyv 15 éves: a példái (MailChimp, Dropbox, LinkedIn, Livemocha, amerikai állami weboldalak, a Twitter 140 karaktere) a 2010 körüli webet mutatják. A pontok nagy része egy-egy pszichológiai kutatásra épül; ezeket a könyv szerinti szerzővel és évszámmal jelölöm, de hogy a kutatás jelenleg is megállja-e a helyét, azt nem ítélem meg. A könyv a tervezőnek szól, a weboldal és a felület felől beszél; e-mail-automatizálásról, regisztrációs folyamatról és adatkezelésről alig van benne valami (lásd a Nem találtam listát).

### Figyelem és szkennelés

**6. pont, 13–14. oldal, hová néz a látogató.** Az ember a képernyő közepére néz, a széleket (logó, üres tér, navigáció) átugorja, aztán a saját olvasási irányában halad. Egy nagy kép, egy arc vagy mozgás elhúzza ettől. Ha hiba vagy váratlan akadály jön, a figyelme beszűkül a problémás részre.
Idézet: "they tend to look at the center of the screen and avoid the edges." (13), "Put the most important information (or things you want people to focus on) in the top third of the screen or in the middle." (14) és "If there is an error or unexpected problem with the task people are trying to accomplish, then they stop looking at other parts of the screen and focus on the problem area." (14)
Mit ad az alkalomhoz: konkrét auditkérdés a beadandóhoz: mi van az érkezőoldal felső harmadában és középen, és mi szorult a szélekre.

**57. pont, 132–135. oldal, szkennelés és gyors benyomás.** Az ember a lehető legkevesebb munkával akarja elvégezni a feladatot, és a „jó elég” megoldást keresi, nem a legjobbat (Herbert Simon „satisficing” fogalma). Weinschenk Steve Krug Don’t Make Me Think (2005) című könyvét idézi: a weboldalt nem olvassák, hanem átfutják. Négy amerikai állami weboldal példáján mutatja meg, hogy az ember egy-két másodperc alatt eldönti, könnyű lesz-e használni az oldalt, és ez az első benyomás dönthet arról, marad-e.
Idézet: "people will do the least amount of work possible to get a task done." (132), "You make a decision that a particular Web site will be easy to use based on the impression the site provides in one or two seconds of viewing." (134) és "People will satisﬁce, that is, look for the good-enough solution rather than the optimal solution." (135)
Mit ad az alkalomhoz: könyvbeli forrás a gyors ítéletre (egy-két másodperc). A deckvázlat 10. diájáról hiányzó „öt másodperc” helyett ez idézhető, de ez nem kutatási adat, hanem a szerző példája (saját következtetés).

**41. pont, 98. oldal, szűrés.** Az ember azt veszi észre, ami a meglévő meggyőződését erősíti, a többit kiszűri. A szerző szerint ami a tervezőnek nyilvánvaló, az a látogatónak nem biztos.
Idézet: "If it’s critical that people pay attention to certain information, make that information stand out 10 times more than you think is necessary." (98)
Mit ad az alkalomhoz: ha a fő gomb vagy ajánlat nem ugrik ki, a látogató nem találja; ez súrlódás, nem érvhiány (saját következtetés).

**45. pont, 104. oldal, kiugró jelek.** Az ember csak arra figyel, ami az adott feladathoz kell (salient cues); a pénzérme részleteit sem tudja felidézni, csak a színét és a méretét.
Idézet: "You only pay attention to what you need for the task at hand." (104)
Mit ad az alkalomhoz: a látogató azzal a feladattal érkezik, amit a hirdetés vagy a keresés adott neki; az oldalnak ehhez kell jelet adnia (saját következtetés).

### Kognitív terhelés és progresszív felfedés

**28. pont, 65–67. oldal, a háromféle terhelés.** A szerző a human factors szakirodalom szerint három terhelést különít el: kognitív (gondolkodás, emlékezés), vizuális (keresés a képernyőn) és motoros (kattintás, gépelés). A kognitív a legdrágább, a motoros a legolcsóbb, ezért megéri néhány kattintással több, ha cserébe kevesebbet kell gondolkodni. Saját kutatására hivatkozik, ahol tíznél több kattintás után is „könnyű volt” a válasz.
Idézet: "Clicking is less of a load than thinking." (65)
Mit ad az alkalomhoz: a súrlódás nem a kattintások száma, hanem a gondolkodás és a bizonytalanság; ez árnyalja a „kevesebb lépés” szabályt (saját következtetés).

**27. pont, 62–64. oldal, progresszív felfedés (MailChimp).** Egyszerre csak annyi információt kell adni, amennyi abban a pillanatban kell. A MailChimp példáján mutatja: az első oldalon lista és kép, kattintásra több részlet, egy szinttel lejjebb még több. A kattintások számát nem kell számolni, ha minden lépés annyit ad, amennyi továbbviszi a látogatót. A módszer csak akkor működik, ha tudod, mit keres az ember az út egyes pontjain. A fogalom eredetét J. M. Keller ARCS-modelljéhez köti (1980-as évek eleje).
Idézet: "Progressive disclosure means providing only the information people need at the moment." (62), "Think progressive disclosure; don’t count clicks." (64) és "Progressive disclosure only works if you know what most people will be looking for at each part of the path." (64)
Mit ad az alkalomhoz: a landing page és az üdvözlő e-mail-sorozat közös elve: nem mindent az elején. A „Know who needs what when” mondat összeköti a 2. alkalom journey-térképével (saját következtetés).

**20. pont, 48–50. oldal, négy elem.** A „hét plusz-mínusz kettő” szerinte városi legenda; George A. Miller (1956) előadására, Baddeley (1986, 1994) és Cowan (2001) munkáira hivatkozik, ezek szerint a szám négy. Csoportosítással (chunking) több is befogadható.
Idézet: "If you could limit the information you give people to four items, that would actually be a great idea, but you don’t have to be that drastic." (50)
Mit ad az alkalomhoz: menüpontok, csomagok, űrlapblokkok számlálásához ad mércét az audithoz.

**19. pont, 46–47. oldal, munkamemória.** A munkamemória gyorsan felejt, és a stressz tovább rontja. A szerző szerint ne kelljen az egyik oldalon látott adatot egy másikon beírni.
Idézet: "Don’t ask people to remember information from one place to another, such as reading letters or numbers on one page and then entering them on another page; if you do, they’ll probably forget the information and get frustrated." (47)
Mit ad az alkalomhoz: tipikus űrlap-súrlódás (kuponkód, rendelésszám, megerősítő kód másik ablakból).

### Döntési túlterhelés

**92. pont, 206–207. oldal, a lekvár-kísérlet.** Az ember azt mondja, sok választást akar, de sok közül nehezebben dönt. A könyv Iyengar és Lepper (2000) kísérletét idézi: a 24 lekváros asztalnál többen álltak meg (60 és 40 százalék), de a 6 lekvárosnál a megállók 31 százaléka vásárolt, a 24-esnél 3 százaléka. A szerző ezt a négyelemes memóriakorláttal köti össze.
Idézet: "Resist the impulse to provide your customers with a large number of choices." (207) és "If possible, limit the number of choices to three or four." (207)
Mit ad az alkalomhoz: a látogatás és a vásárlás közti különbség egyik legtisztább példája: több megálló, kevesebb vásárlás (saját következtetés). A kevesebb opció egy akadály elvétele.

**93. pont, 208–209. oldal, a választás mint kontroll.** Ugyanakkor az ember a választást kontrollként éli meg, és rosszul viseli, ha elveszik tőle. Iyengar The Art of Choosing (2010) könyvéből patkány-, majom- és kaszinókísérleteket idéz.
Idézet: "People need to feel that they’re in control and that they have choices." (209)
Mit ad az alkalomhoz: vitapont a 92. ponttal szemben: kevés opció, de legyen érzés, hogy választ (saját következtetés).

### Bizalom és első benyomás

**79. pont, 177–178. oldal, a kinézet az első szűrő.** A szerző szerint kevés a valódi kutatás a weboldal és a bizalom kapcsolatáról. Elizabeth Sillence (2004) egészségügyi weboldalakon végzett kutatását idézi: amikor a résztvevők elutasítottak egy oldalt, a megjegyzéseik 83 százaléka a designra vonatkozott (első benyomás, navigáció, szín, betűméret, név), amikor megbíztak benne, 74 százalékuk a tartalomra. A szerző kétlépcsős folyamatot ír le: előbb gyors elutasítás a kinézet alapján, utána a tartalom és a hitelesség dönt.
Idézet: "83 percent of their comments were related to design factors" (177), "People make quick decisions about what is not trustworthy. So they reject a Web site ﬁrst, and then decide after that whether or not to actually trust it." (178) és "If a Web site makes it through the ﬁrst rejection cut, then content and credibility become the determining factors as to whether the person trusts the site." (178)
Mit ad az alkalomhoz: az első benyomáshoz és a bizalomhoz; a 12. dián Chaffey Fogg-adata mellé második forrásként. A kutatás egészségügyi oldalakon készült, ezt a dián érdemes jelezni.

**66. pont, 151–153. oldal, az oldal is társas helyzet.** A szerző szerint minden online interakció társas interakció, és ugyanazok a szabályok érvényesek rá. A lassú oldal olyan, mint aki nem néz rád; ha túl korán kér személyes adatot, olyan, mint aki túl közel jön; ha nem emlékszik rád, olyan, mint aki nem ismer meg. Az Organizing for America oldal példája: a kezdőlap e-mail-címet és irányítószámot kér, mielőtt bármit mutatna, és a kihagyás gomb már későn jön.
Idézet: "Just the act of going to a Web site is a social interaction." (151), "If the site asks for personal information too early in the interaction, that’s like the other person getting too personal." (152), "If the Web site does not save your information from session to session, that’s like the other person not recognizing you or remembering that you know each other." (152) és "But by now you don’t trust him and don’t want to interact." (153)
Mit ad az alkalomhoz: a regisztráció és az adatkérés legerősebb pontja a könyvben. A deckvázlat 17. diájához (ne kérdezz meg mindent az elején) és a 21. diához (adatkezelés mint bizalom) jó párhuzam. A „nem ismer meg” mondat a loyalty és a bejelentkezés felé is mutat (saját következtetés).

### Társas bizonyíték és vélemények

**98. pont, 217–218. oldal, bizonytalanságban mások döntenek.** Ha az ember bizonytalan (például ismeretlen márkánál), megnézi mások értékelését, még idegenekét is. A könyv Latane és Darley (1970) füstös szobás kísérletét és Yi-Fen Chen (2008) könyvesbolti kutatását idézi: a három értékeléstípus (rendszeres látogató, szakértő, az oldal ajánlása) közül a rendszeres látogatóké hatott a legjobban.
Idézet: "When we’re unsure about what to do or buy, we look to testimonials, ratings, and reviews to tell us how to behave." (217), "but the reviews by regular visitors were the most inﬂuential." (218) és "The more information you provide in the rating and review about the person who left it, the more inﬂuential the rating or review will be." (218)
Mit ad az alkalomhoz: a 14. dia hat kockázatához („nem fog működni”, „ciki lesz”) a vélemény mint oldalelem; auditkérdés: van-e értékelés, és látszik-e, ki írta.

**90. pont, 202–203. oldal, nem tudatos döntés.** A döntés nagy része nem tudatos. A szerző tényezői között ott van, mit vesznek mások (értékelések), a következetesség, a viszonosság és a veszteségtől való félelem. Ugyanakkor az embernek racionális indok is kell a döntéséhez.
Idézet: "What other people are deciding to buy" (202), "Fear of loss" (202) és "So you still need to provide the rational, logical reasons, even though they’re unlikely to be the actual reasons that people decided to take action." (203)
Mit ad az alkalomhoz: árnyalja a meggyőzés szerepét: a racionális érv nem tűnik el, de nem az érv dönt (saját következtetés).

**74. pont, 168. oldal, történet az adat helyett.** Az anekdota jobban meggyőz, mint az adat, mert érzelmet és empátiát kelt; még jobb, ha videón a vevő mondja el.
Idézet: "Use anecdotes in addition to, or in place of, factual data." (168)
Mit ad az alkalomhoz: az ügyféltörténet és a videós vélemény mint oldalelem.

### Motiváció, progress és jutalom (loyalty)

**50. pont, 116–117. oldal, a cél közelsége (pecsétkártya).** A goal-gradient hatás: minél közelebb a cél, annál gyorsabban halad az ember. A könyv Clark Hull (1934) patkánykísérletét és Ran Kivetz (2006) kávézós kutatását idézi: a 12 mezős, két pecséttel induló kártyát gyorsabban töltik meg, mint a 10 mezős üreset, pedig mindkettőhöz 10 kávé kell. Koo és Fishbach (2010) szerint a hátralévő rész jobban motivál, mint a már elvégzett. A jutalom után a motiváció és a vásárlás visszaesik.
Idézet: "The goal-gradient effect says that you will accelerate your behavior as you progress closer to your goal." (116), "You can get this extra motivation even with the illusion of progress" (117), "People enjoy being part of a reward program." (117) és "You’re most at risk of losing your customer right after a reward is reached." (117)
Mit ad az alkalomhoz: a deckvázlat 18. diájához (loyalty logika) a legjobb könyvbeli példa; az utolsó mondat az e-mail-folyamathoz: a jutalom utáni levél a kritikus pont (saját következtetés).

**55. pont, 127–130. oldal, progress (MailChimp, LinkedIn).** A haladás érzése akkor is motivál, ha kicsi. A LinkedIn a profil kitöltöttségét mutatja, a MailChimp azt, hány lépés van hátra a kampány elkészítéséig, a Livemocha pontot és irányítópultot ad. A loyalty-hoz a szerző szerint olyan tevékenység kell, amit az ember magától is szívesen csinál, nem csak jutalomért. Daniel Pink Drive (2009) könyvére hivatkozik.
Idézet: "even small signs of progress can have a large effect in motivating people to move forward to the next step in a task." (127), "MailChimp shows you how many steps you have left to create an e-mail campaign" (127) és "If you want to build loyalty and have repeat customers (for example, repeat visitors to your Web site), you’ll need to have activities that people inherently want to do" (130)
Mit ad az alkalomhoz: a regisztrációs és rendelési folyamat lépésjelzője mint súrlódáscsökkentő elem; auditkérdés: látja-e a látogató, hol tart.

**54. pont, 125–126. oldal, belső és külső jutalom.** Lepper, Greene és Nisbett (1973) rajzoló gyerekes kísérlete: az előre megígért jutalom után kevesebbet rajzoltak, mint a váratlanul jutalmazottak és a kontrollcsoport. Brian Knutson (2001) szerint a pénzjutalom ígérete dopamint szabadít fel.
Idézet: "If you’re going to give an extrinsic reward, it will be more motivating if it is unexpected." (126)
Mit ad az alkalomhoz: az e-mail-folyamatban a váratlan ajándék vagy kedvezmény erősebb, mint az előre beígért (saját következtetés). Kapcsolódik Chaffey WHSmith-esetéhez, ahol nem a kedvezmény hozta vissza a vevőt.

**51. pont, 118–120. oldal, jutalomütemezés.** Skinner operáns kondicionálása: négy jutalmazási ütem, a változó arányú hozza a legtöbb ismétlést. A szerző szerint a kávézós pecsétkártya fix arányú, a Dropbox meghívásos tárhelybónusza folyamatos jutalmazás. A jutalomnak annak kell lennie, amit az adott közönség akar.
Idézet: "For operant conditioning to work, the reinforcement (reward) must be something that particular audience wants." (120)
Mit ad az alkalomhoz: a loyalty-program jutalmának megválasztásához; a WIFM kérdés pszichológiai oldala (saját következtetés).

**53. pont, 123. oldal, az e-mail mint kiszámíthatatlan jutalom.** A kiszámíthatatlanság a dopaminrendszert ingerli; a szerző szerint az e-mail és a közösségi média változó arányú jutalmazásként működik, és az értesítés hangja vagy ikonja pavlovi jel.
Idézet: "Basically e-mail, Twitter, and most social media run on the variable ratio schedule discussed earlier in this chapter." (123)
Mit ad az alkalomhoz: háttér ahhoz, miért nyitja meg az ember a levelet; a könyv itt a felhasználó szemszögéből beszél, nem hírlevél-marketingről.

**60. pont, 139–140. oldal, kis lépés, szokás.** Philippa Lally (2010) kutatása szerint egy szokás kialakulása átlagosan 66 nap, 18 és 254 nap között. Aki nagy elköteleződést akar, előbb kicsit kérjen. A 30. pont (71. oldal) ugyanezt mondja meggyőződésről.
Idézet: "If you want people to commit to something big, you ﬁrst need to get them to commit to something that is related, but very small." (140), "Give people a reason to come back and do the task every day or almost every day." (140) és "The best way to change a belief is to get someone to commit to something very small." (71)
Mit ad az alkalomhoz: a regisztráció lépcsőzése (előbb csak e-mail, később a többi adat) és a próbaóra, szintfelmérő típusú első lépés (Katedra) könyvbeli háttere (saját következtetés).

**81. pont, 180. oldal, a nehéz belépés.** Elliot Aronson (1959) beavatási kísérlete és Festinger (1956) kognitív disszonancia elmélete: minél nehezebb bekerülni egy csoportba, annál jobban szeretik a tagok. A szerző ehhez saját véleményként a szűkösséget teszi hozzá. Közösségnél a belépési lépések akadálynak tűnnek, de a belépők jobban kötődhetnek.
Idézet: "but they may also mean that the people who do join care more about the group." (180)
Mit ad az alkalomhoz: a deckvázlat 18. diájának vitapontja (zárt klub mint szándékos akadály) itt könyvbeli forrást kap. Feszültségben áll azzal, hogy az akadályokat el kell venni; a szerző maga is jelzi, hogy nem azt javasolja, hogy az oldal legyen nehéz.

### Szűkösség és üzenet

**56. pont, 131. oldal, szűkösség.** Walter Mischel késleltetett jutalom kísérleteire (1960-as évek vége, 1970-es évek eleje) épül. A tanulságban a szerző kimondja, hogy aki nehezen vár, arra a szűkösség üzenete jobban hat.
Idézet: "People who are not good at delaying gratiﬁcation will be more suggestible to images and messages of scarcity (for example, “only three left in stock” or “only available till the end of the month”)." (131)
Mit ad az alkalomhoz: a kosárelhagyó és határidős e-mail egyik eszköze (saját következtetés); a könyvben ez egy tanulságmondat, nem külön kutatás a szűkösségről.

**94. pont, 210–211. oldal, idő a pénz előtt.** Mogilner és Aaker (2009) limonádés kísérlete: az idő említése („Spend a little time”) több vásárlót és magasabb árat hozott, mint a pénzé. A szerző szerint a legtöbb termékénél az élményre kell fókuszálni, presztízstermékeknél viszont a pénz említése hat.
Idézet: "delay the mention of money as long as possible." (211)
Mit ad az alkalomhoz: az érkezőoldal és az üdvözlő levél sorrendjéhez: előbb az élmény, aztán az ár (saját következtetés).

### Űrlapok, alapértékek és hibák

**58. pont, 136. oldal, alapértékek.** Az előre kitöltött mező csökkenti a munkát, de az ember nem mindig veszi észre, és elfogadja akaratlanul is. A szerző saját esetét írja le: a webshop a lánya címét hagyta szállítási címnek.
Idézet: "Defaults reduce the amount of work needed to complete a task." (136) és "If it takes a lot of work to change the result of accepting “wrong” defaults, then think twice about using them in your design." (136)
Mit ad az alkalomhoz: az alapérték egyszerre súrlódáscsökkentő és kockázat. Az előre bepipált hozzájárulásos doboz ugyanez a mechanizmus (saját következtetés; a könyv nem beszél hozzájárulásról, a jogi oldal Chaffeyből és a GDPR-ból jön).

**85. pont, 188–189. oldal, hibaüzenet.** Hiba mindig lesz. A legjobb hibaüzenet az, ami meg sem jelenik; ha mégis kell, mondja meg, mit csinált az ember, mi a baj, hogyan javítsa, egyszerű, cselekvő nyelven, példával.
Idézet: "the best error message is no error message" (188) és "Instructs the person how to correct it" (189)
Mit ad az alkalomhoz: auditkérdés a beadandóhoz: mi történik, ha a látogató rosszul tölti ki az űrlapot.

**86. pont, 190–193. oldal, stressz és űrlap.** A szerző saját esete: beteg lányával egy biztosítói oldalon kellett orvost keresnie, és az első mező (milyen biztosítása van) megakasztotta; minél stresszesebb volt, annál kevésbé boldogult az űrlappal. A Yerkes-Dodson-törvényre (1908) és Sonia Lupien (2007) kutatására hivatkozik. Stressz alatt az ember beszűkül, és ugyanazt próbálja újra.
Idézet: "The more stressed I got, the more trouble I had ﬁlling in the form." (190) és "Trying to ﬁll out a form on a screen when a customer is present on the phone or in person is stressful." (192)
Mit ad az alkalomhoz: a látogató ritkán ül nyugodtan az oldalon; egy érthetetlen kötelező mező az egyik legtisztább súrlódás (saját következtetés).

## Yablonski: Laws of UX (2. kiadás, 2024)

Jon Yablonski: Laws of UX. Using Psychology to Design Better Products & Services. Második kiadás, O'Reilly Media, Sebastopol. A copyright-oldalon (PDF 6. lap, oldalszám nélkül) ez áll: „Copyright © 2024 Jon Yablonski. All rights reserved.”, a kiadástörténet „May 2020: First Edition”, „February 2024: Second Edition”, az első megjelenés „2024-01-23”. ISBN 978-1-098-14696-2. A könyv 12 fejezet: tíz törvény (Jakob, Fitts, Miller, Hick, Postel, peak–end, aesthetic–usability, von Restorff, Tesler, Doherty), egy alkalmazási fejezet (11.) és egy etikai fejezet (12., „With Power Comes Responsibility”). Minden törvényfejezet azonos szerkezetű: Key Takeaways, Overview, Origins, egy pszichológiai fogalom, Examples, egy kutatási technika, egy Key Consideration, Conclusion. A goal-gradient hatásnak, a choice overloadnak, a chunkingnak, a working memorynak, a cognitive loadnak és a flow-nak nincs saját fejezete, ezek más törvények alfejezeteiben szerepelnek (lent jelölve). Zeigarnik-hatás nincs a könyvben. A 2. kiadás AI-részei rövidek (Tesler-fejezet, 110. és 113–114. oldal). Az oldalszámok a nyomtatott oldalak, a findq_pdf.py-val ellenőrizve; a fejezetnyitó oldalaknál a szkript a fejezetszámot adta vissza, ott a lap alján álló oldalszámot a PDF-lapról olvastam le (PDF-lap mínusz 20). Feldolgozva: 2026. október 5.

### Jakob-törvény

**1. fejezet, 1–2. oldal, ismerős minták és súrlódás.** A felhasználó az idejét főleg más oldalakon tölti, és azt várja, hogy a te oldalad is úgy működjön. Az ismerősség csökkenti a kognitív terhelést, a szerző szerint a tervező célja a fölösleges súrlódás eltávolítása. A szokatlan megoldás frusztrációhoz és a feladat feladásához vezet.
Idézet: „Users spend most of their time on other sites, and they prefer your site to work the same way as all the other sites they already know.” (1. oldal)
Idézet: „As designers, it is our objective to ensure people successfully achieve their goals when using the interfaces we’ve built by eliminating as much friction as possible.” (2. oldal)
Idézet: „In contrast, uncommon conventions can lead to people becoming frustrated, confused, and more likely to abandon their tasks and leave because the interface does not match up with their understanding of how things should work.” (2. oldal)
Mit ad az alkalomhoz: a súrlódás szó maga a könyvben áll, már az első fejezet második oldalán. Az audit első kérdése lehet: ott van-e a kosár, a kereső, a menü, ahol a látogató keresi.

**1. fejezet, 6. és 12. oldal, webshop-folyamat.** A webshopok (példa: Etsy) a megszokott termékválasztás, kosár, fizetés sorrendet követik, így a vevő a korábbi tapasztalatát viszi tovább. A szerző tanácsa: mindig a bevett mintákból indulj, és csak indokkal térj el.
Idézet: „By conforming to users’ expectations about the process of selecting products, adding them to the virtual cart, and checking out, designers can ensure users are able to apply their accumulated knowledge from previous ecommerce experiences” (6. oldal)
Idézet: „The best piece of advice I can give in regard to Jakob’s law is to always begin with common patterns and conventions” (12. oldal)
Mit ad az alkalomhoz: a csapatok a valós márka kosarát és pénztárát a megszokott mintához mérhetik. Ellenpélda a 4. oldalon: a Snapchat 2018-as újratervezése, amely elrontotta a felhasználók mentális modelljét.

### Fitts-törvény

**2. fejezet, 15., 18. és 21. oldal, gombméret és elhelyezés.** A cél elérésének ideje a távolságtól és a mérettől függ. A kis érintési felület a szerző szerint akkor is rontja a használhatóság érzetét, ha a felhasználó nem hibázik. Az űrlap küldőgombja az utolsó mező közelébe kerül.
Idézet: „The time to acquire a target is a function of the distance to and size of the target.” (15. oldal)
Idézet: „Small touch targets add to the perception that an interface is less usable, even if the user is able to avoid errors when attempting to select a target.” (18. oldal)
Idézet: „buttons that are intended to complete an action (such as filling out a form) should be close to the active element.” (21. oldal)
Mit ad az alkalomhoz: mobilon megfigyelhető audit-szempont (elérhető-e hüvelykujjal a fő gomb, elég nagy-e). A 18. oldali mondat a percepcióhoz is kapcsolódik: a kis gomb rosszabb képet ad a márkáról (saját következtetés).

### Miller-törvény, munkamemória, kognitív terhelés, chunking

**3. fejezet, 29–37. oldal, a munkamemória korlátja.** A „7 ± 2” a szerző szerint gyakran félreértett szabály, a lényeg a chunking, vagyis a tartalom csoportosítása. A kognitív terhelés az a mentális erőforrás, ami a felület megértéséhez kell; ha túllépi a munkamemóriát, a felhasználó frusztrált lesz vagy feladja. Újabb kutatás négy elem körüli korlátot is említ.
Idézet: „The amount of mental resources needed to understand and interact with an interface is known as cognitive load.” (31. oldal)
Idézet: „Our working memory, the buffer space (Figure 3-1) available for storing information relevant to the current task, has a specific number of slots in which to store information.” (31. oldal)
Idézet: „ultimately leading to frustration or even task abandonment” (31. oldal)
Idézet: „human short-term memory is limited, and chunking helps us retain information more effectively.” (32. oldal)
Idézet: „What chunking does not do is dictate a specific limit on the number of items that can be shown at a given time or within a group.” (36. oldal)
Mit ad az alkalomhoz: a szövegfal („wall of text”, 33. oldal) és a Nike.com termék- és szűrőcsoportjai (35. oldal) jól megmutatható példák a landing page-audithoz. A 36. oldal megvéd a „max. 7 menüpont” tévhittől.

### Hick-törvény, choice overload

**4. fejezet, 39–42. oldal, a választás ideje és a lekvárkísérlet.** A döntés ideje a lehetőségek számával és bonyolultságával nő. A szerző a felesleges lépéseket, a sok választást, a homályos cselekvésre hívást akadályként sorolja fel. A Paradox of Choice keretben (Schwartz, Iyengar és Lepper) a 24 fajta lekvár több figyelmet kapott, de a vásárlási arány a hatfajtás asztalnál volt tízszeres.
Idézet: „unnecessary steps, too many choices or too much information” (40. oldal)
Idézet: „more choice leads to choice overload.” (41. oldal)
Idézet: „individuals who saw the larger display were only one-tenth as likely to buy compared to those who saw the smaller display.” (42. oldal)
Mit ad az alkalomhoz: a 40. oldali felsorolás kész akadálylista az audithoz. A lekvárkísérlet a súrlódás témájához ad példát: több kínálat nem több vásárlás.

**4. fejezet, 39., 42., 44. és 48. oldal, lépésekre bontás, onboarding, túlegyszerűsítés.** A kulcsgondolatok között áll, hogy a bonyolult feladatot lépésekre kell bontani, és ki kell emelni az ajánlott lehetőséget. A Google csak a keresés után kínál szűrőt, a Notion ellenőrzőlistával vezeti be az új felhasználót. A túlegyszerűsített felület (például felirat nélküli ikonok) viszont növeli a terhelést.
Idézet: „Break complex tasks into smaller steps in order to decrease mental effort.” (39. oldal)
Idézet: „We can ensure better user experiences by providing the right choices at the right time rather than presenting all the possible choices all the time.” (44. oldal)
Idézet: „Onboarding is a crucial but risky process for new users” (44. oldal)
Idézet: „When an interface has been simplified to the point of abstraction, it’s no longer clear what actions are available, what the next steps are, or where to find specific information.” (48. oldal)
Mit ad az alkalomhoz: a regisztráció utáni első lépések (onboarding) és az üdvözlő e-mail-sor tervezéséhez: a megfelelő választás a megfelelő időben. Az e-mail-folyamatra vonatkoztatás saját következtetés, a könyv itt alkalmazásról beszél.

### Postel-törvény

**5. fejezet, 53–56. oldal, űrlapok.** Légy szigorú abban, amit adsz, és engedékeny abban, amit elfogadsz. Űrlapnál ez azt jelenti: csak azt kérd, ami tényleg kell, és ne kérd újra, amit már tudsz. Minél több a kötelező mező, annál kisebb az esély, hogy kitöltik; a „hibás név” üzenet is rontja az élményt.
Idézet: „we’re generally annoyed when asked to provide more information than is necessary.” (53. oldal)
Idézet: „Using Postel’s law as a guide in regard to forms, the first consideration is to be conservative in how much information you ask people to provide.” (55. oldal)
Idézet: „reduce the likelihood that they’ll complete the form.” (56. oldal)
Idézet: „By asking only for what’s absolutely necessary and not requesting information you already have, such as an email address or a password, you can minimize the effort required to fill out a form.” (56. oldal)
Idézet: „telling someone their name is “wrong” or “not accepted” can do a lot of damage to their experience and satisfaction with the product or service.” (56. oldal)
Mit ad az alkalomhoz: a regisztrációs és hírlevél-feliratkozó űrlap auditjának gerince (mezőszám, kötelező mezők, hibaüzenetek). Az adattakarékosság itt UX-érv, nem jogi; a GDPR adattakarékossági elvével való összevetés saját következtetés, a könyv a GDPR-t nem említi.

**5. fejezet, 55. és 63. oldal, a teher a rendszeren.** A szerző szerint a tervezés felelőssége áthidalni az ember és a gép közti különbséget, a terhet le kell venni a felhasználóról.
Idézet: „it’s the responsibility of design to bridge the communication gap.” (55. oldal)
Idézet: „we transfer this burden away from users and therefore ensure a more human user experience.” (63. oldal)
Mit ad az alkalomhoz: a Tesler-törvény mellett a második szöveghely ahhoz, hogy a terhet az oldalnak kell viselnie, nem a látogatónak.

### Peak–end szabály

**6. fejezet, 65. és 76. oldal, a csúcs és a vég.** Az élményt a legintenzívebb pillanat és a vége alapján ítéljük meg, nem az átlag alapján. A negatív élményre élénkebben emlékszünk. Az emlék dönti el, visszajön-e és ajánlja-e a felhasználó.
Idézet: „People judge an experience largely based on how they felt at its peak and at its end, rather than on the total sum or average of every moment of the experience.” (65. oldal)
Idézet: „Pay close attention to the most intense points and the final moments (the “end”) of the user journey.” (65. oldal)
Idézet: „Remember that people recall negative experiences more vividly than positive ones.” (65. oldal)
Idézet: „How users recall an experience will determine how likely they are to use a product or service again or recommend it to others.” (76. oldal)
Mit ad az alkalomhoz: az e-mail-folyamatban a vásárlás vagy feliratkozás utáni levél a „vég”, a visszaigazolás és a köszönőoldal az utolsó élmény (saját következtetés, a könyv e-mailt itt nem tárgyal). A recency effect a 68. oldalon: „items near the end of a sequence are the easiest to recall.”

**6. fejezet, 69. és 74–75. oldal, várakozás, regisztráció, hibaoldal.** Az Uber a várakozást három fogalommal kezelte, ezek egyike a goal gradient effect: a felhasználó lépésről lépésre látja, hogy halad a cél felé. A regisztrációnál a merev jelszószabály épp a lelkesedés pillanatában okoz negatív csúcsot; a Mailchimp valós idejű ellenőrzéssel oldja meg. A 404-es oldal is lehet márkaélmény.
Idézet: „It clearly explains each step of the process so customers feel that they are continuously making progress toward their goal of getting a ride (goal gradient effect).” (69. oldal)
Idézet: „By focusing on people’s perceptions of time and waiting, Uber was able to reduce its post-request cancellation rate” (69. oldal)
Idézet: „Rigid password rules can quickly lead to frustration just as people are excited enough about a product or service to create an account and give it a try.” (74. oldal)
Idézet: „Setbacks can also be opportunities, however, if the right fallbacks are in place.” (75. oldal)
Mit ad az alkalomhoz: a goal-gradient a könyvben csak itt, egy mondatban szerepel. A 74. oldal a regisztrációs logika auditjához ad kész szempontot. A 71–73. oldalon a journey map technika is van, ez visszaköt a 2. alkalom beadandójához.

### Aesthetic–usability hatás

**7. fejezet, 79–80. és 84. oldal, a szép felület használhatóbbnak tűnik.** A tetszetős felületet használhatóbbnak érzékeljük, és elnézőbbek vagyunk a kisebb hibáival. A szerző szerint ez hitelességet is ad, és az első benyomás számít: egy kutatás szerint 50 ezredmásodperc alatt véleményt alkotunk egy weboldalról, és ez ritkán változik.
Idézet: „Users often perceive aesthetically pleasing design as design that’s more usable.” (79. oldal)
Idézet: „it also enhances our cognitive abilities, increases the perception of usability, and extends credibility.” (79. oldal)
Idézet: „First impressions do matter.” (80. oldal)
Idézet: „The correlations between perceived attractiveness and other qualities (including trust and credibility) have also been explored” (82. oldal)
Idézet: „people form an opinion about a website within 50 milliseconds of seeing it, and that visual appeal is a primary determining factor.” (84. oldal)
Mit ad az alkalomhoz: ez az első benyomás legerősebb forrása ebben a könyvben, és párja a Chaffey-féle Fogg-adatnak (deckvázlat 12. dia). Az „öt másodperc” helyett az 50 ezredmásodperc itt forrással megvan (Lindgaard et al., 2006).

**7. fejezet, 79. és 91. oldal, a szépség elfedi a hibát.** A tetszetős design elfedheti a használhatósági problémákat, ezért a szerző szerint azt kell figyelni, mit csinál a felhasználó, nem csak azt, mit mond.
Idézet: „Visually pleasing design can mask usability problems and prevent issues from being discovered during usability testing.” (79. oldal)
Idézet: „listening to what users say when evaluating the usability of an experience and, more importantly, watching what they do.” (91. oldal)
Mit ad az alkalomhoz: módszertani figyelmeztetés a beadandóhoz: a csapat ne a szép oldalt dicsérje, hanem végigcsinálja a folyamatot és megfigyelje, hol akad el.

### Von Restorff-hatás

**8. fejezet, 93–94., 96., 98. és 101. oldal, kiemelés és mértéktartás.** A hasonlók közül a különböző marad meg. A fontos cselekvést vizuálisan ki kell emelni, de a túl sok kiemelés versenyez egymással, és ami hirdetésnek látszik, azt a látogató átugorja (banner blindness). Az árazási táblázatban (példa: Notion) egy csomagot szín, méret és pozíció emel ki.
Idézet: „When multiple similar objects are present, the one that differs from the rest is most likely to be remembered.” (93. oldal)
Idézet: „Make important information or key actions visually distinctive.” (93. oldal)
Idézet: „too many points of visual emphasis will compete with one another and make it harder for people to find the information they need.” (94. oldal)
Idézet: „Even legitimate content elements may be ignored if they remotely resemble ads or are placed in close proximity to them.” (96. oldal)
Idézet: „designers frequently differentiate the option they want to call out by adding visual cues.” (98. oldal)
Mit ad az alkalomhoz: audit-kérdés: van-e egyetlen egyértelmű fő gomb az oldalon. A banner blindness a felugró ablakok és akciós sávok vitapontjához ad érvet (saját következtetés).

### Tesler-törvény

**9. fejezet, 107–108. oldal, a komplexitás kié.** Minden folyamatnak van egy csökkenthetetlen komplexitása, amit vagy a rendszer, vagy a felhasználó visel. A szerző kérdése: ki viselje a terhet, a felhasználó vagy a tervezők és fejlesztők. Tesler idézett érve: ha egymillió felhasználó napi egy percet veszít, miközben egy mérnök egy hét alatt megoldhatta volna, akkor a felhasználót büntetjük.
Idézet: „All processes have a core of complexity that cannot be designed away and therefore must be assumed by either the system or the user.” (107. oldal)
Idézet: „Ensure as much as possible of the burden is lifted from users by dealing with inherent complexity during design and development.” (107. oldal)
Idézet: „Who should bear the burden of complexity within an application or a process” (107. oldal)
Idézet: „Inevitably, we reach a point at which complexity cannot be reduced any further but can only be transferred from one place to another.” (107. oldal)
Idézet: „you are penalizing the user to make the engineer’s job easier.” (108. oldal)
Mit ad az alkalomhoz: a legközelebbi szerzői megfogalmazása annak, hogy a látogató terhét az oldalnak kell átvennie. Részletesen lent.

**9. fejezet, 109–113. és 117. oldal, pénztár, Apple Pay, Amazon Go.** A szállítási cím átvétele a számlázási címből és az Apple Pay a vevő terhét a fejlesztőkre teszi át. Az Amazon Go-nál a vásárlás súrlódása szinte eltűnik, a komplexitást a fejlesztők nyelik le. A fejezet zárása kimondja a tervező felelősségét. Az e-mail itt levélírási példa (feladó előre kitöltve, címzett-javaslat), nem e-mail-marketing.
Idézet: „The complexity isn’t entirely gone; it’s just abstracted away to reduce the effort required of the user.” (110. oldal)
Idézet: „the complexity required to enable the feature has shifted to the designers and developers responsible for implementing it up front.” (111. oldal)
Idézet: „While the friction of shopping is drastically reduced for customers, the complexity that comes along with it must be absorbed by the designers and developers responsible for ensuring it all works.” (113. oldal)
Idézet: „As designers, we have a responsibility to remove inherent complexity from our interfaces, or else we ship that complexity to our users.” (117. oldal)
Idézet: „Where possible, designers and developers should handle complexity.” (117. oldal)
Mit ad az alkalomhoz: a 111. oldali címátvétel és az Apple Pay konkrét, auditálható pénztárelem. A 113. oldal egyszerre használja a súrlódás és a komplexitás szót, ez köti össze a súrlódás témáját a Tesler-törvénnyel.

**9. fejezet, 115. oldal, az aktív felhasználó paradoxona.** A felhasználó nem olvas kézikönyvet, azonnal használni kezdi a terméket, ezért a segítséget a folyamatba kell építeni.
Idézet: „users never read software manuals but instead start using the software immediately.” (115. oldal)
Idézet: „we can account for this paradox by making guidance accessible throughout the product experience.” (115. oldal)
Mit ad az alkalomhoz: a landing page nem várhatja, hogy a látogató utánaolvas; ami nincs ott, az nincs. Az AI-rész (Gmail Smart Compose 110. oldal, szándékalapú interakció 113–114. oldal) csak mellékszál: „Intent-based interaction via natural language lowers the barrier of knowledge required to interact with software” (114. oldal).

### Doherty-küszöb, flow

**10. fejezet, 119–120. és 126. oldal, betöltési idő.** 400 ezredmásodperc alatti válaszidőnél nő a termelékenység. A szerző szerint a sebesség design-kérdés, nem csak technikai. Minél hosszabb a várakozás, annál valószínűbb a feladás; egy másodperc fölött a figyelem elkalandozik, tíz másodperc a figyelem határa.
Idézet: „Productivity soars when a computer and its users interact at a pace (<400 ms) that ensures that neither has to wait on the other.” (119. oldal)
Idézet: „speed should be considered an essential design feature” (119. oldal)
Idézet: „the longer the wait times that people are subjected to, the more likely it is they will grow frustrated and even abandon the task altogether.” (120. oldal)
Idézet: „Once the delay extends past 1,000 ms (1 second), people begin thinking about other things” (120. oldal)
Idézet: „Ten seconds is the commonly recognized limit for keeping the user’s attention focused on the task at hand” (126. oldal)
Mit ad az alkalomhoz: a deckvázlat 15. diájához (súrlódás: idő és energia) a Chaffey mellé ad számokat. A 120. oldal HTTP Archive adata (2023-ban átlag 2 MB fölötti oldalsúly) háttérnek jó.

**10. fejezet, 119., 121–122., 125. és 127–128. oldal, észlelt sebesség, flow, szándékos súrlódás.** A progress bar és az animáció elviselhetőbbé teszi a várakozást. A flow-hoz a szerző szerint a felesleges súrlódás eltávolítása kell. A fejezet „Friction” alfejezete ellenpont: a szándékos késleltetés bizalmat építhet, a megerősítő ablak tudatos döntést kér (példa: Google Privacy Checkup).
Idézet: „Progress bars help make wait times tolerable, regardless of their accuracy.” (119. oldal)
Idézet: „Flow is the state that occurs when there is a balance between the difficulty of a task and the level of skill at the given task.” (121. oldal)
Idézet: „optimizing for efficiency and system responsiveness by removing any unnecessary friction” (122. oldal)
Idézet: „Purposefully adding a delay to a process can actually increase its perceived value and instill a sense of trust, even when the process itself actually takes much less time.” (119. oldal)
Idézet: „Friction can be carefully utilized when a more considered response is required from users.” (128. oldal)
Mit ad az alkalomhoz: vitapont a súrlódáshoz: nem minden súrlódás rossz, a bizalomépítő lépés lehet szándékos akadály. Ez a zárt klub vitapontjához (deckvázlat 18. dia) is ad szerzői hátteret (saját következtetés).

### Etika és dark pattern

**12. fejezet, 146–149. oldal, alapértékek, súrlódás hiánya, dark pattern.** Az alapbeállítások irányítják a döntést, mert a legtöbben nem változtatják meg; a Facebook alapértelmezett adatvédelmi beállításai a felhasználók elvárásainak csak 37%-ában egyeztek. A súrlódás eltávolítása viselkedést formál. A dark pattern olyan cselekvésre visz, amit a felhasználó nem akart, köztük marketingkommunikáció elfogadására; egy 2019-es vizsgálat kb. 11 ezer webshopon 1818 esetet talált. Példa a kényszerített cselekvésre: Instagram, adathozzáférés nélkül nem lehet továbblépni.
Idézet: „Default settings matter when it comes to choice architecture because most people never change them.” (146. oldal)
Idézet: „Facebook’s default privacy settings (Figure 12-6) matched users’ expectations only 37% of the time” (146. oldal)
Idézet: „the easier and more convenient you make an action, the more likely people will be to perform that action and form a habit around it.” (147. oldal)
Idézet: „Dark patterns are yet another way technology can be used to influence behavior, by making people perform actions that they didn’t intend to for the sake of increasing engagement or to convince users to complete a task that is not in their best interest” (148. oldal)
Idézet: „share unnecessary information, accept marketing communications, etc.” (148. oldal)
Idézet: „they identified 1,818 instances of dark patterns, with the more popular” (148. oldal)
Idézet: „Instagram, which makes use of the forced action pattern by providing no alternative option but to allow access to private data in order to proceed” (149. oldal)
Mit ad az alkalomhoz: a deckvázlat 21. diájához (adatkezelés mint felület): az előre bepipált doboz és a kényszerített hozzájárulás UX-oldali háttere. A jogi részhez (GDPR, NAIH) ez nem forrás.

**12. fejezet, 151–152. és 154. oldal, mérőszámok, felelősség, a súrlódás vállalása.** A szerző megkérdezi, mikor lett a napi aktív felhasználó és az oldalon töltött idő fontosabb annál, hogy a termék segít-e. Az üzleti cél és a felhasználó célja ritkán esik egybe, a tervező felelőssége a felhasználó céljait szolgálni. A zárás szerint a súrlódás hasznos eszköz is lehet, többek között hitelességet épít.
Idézet: „When did “daily active users” or “time on site” become a more meaningful metric than whether a product is actually helping people achieve their goals or facilitating meaningful connections?” (151. oldal)
Idézet: „In other words, the corporate goals of the business and the human goals of the end user are seldom aligned, and more often than not, designers are a conduit between them.” (152. oldal)
Idézet: „it’s our responsibility to create products and experiences that support and align with the goals and well-being of users.” (152. oldal)
Idézet: „We’ve been made to think that any friction within a user journey is negative and should be eliminated wherever possible” (154. oldal)
Idézet: „friction can also be a valuable tool when used appropriately, from preventing errors, enhancing security, and avoiding unintentional actions and consequences to building credibility” (154. oldal)
Mit ad az alkalomhoz: a 151. oldali kérdés a weboldal eseményeihez és mérőszámaihoz ad vitapontot: a látogatási mutató vagy az oldalon töltött idő nem azonos azzal, hogy a felület elvégzi a dolgát (saját következtetés, a szerző nem marketingforgalomról, hanem termékmutatókról beszél).


---

# A hármas és a keret témái a forrásokban

Az új hármas szó szerint egyik könyvben sincs meg, nem is várható, mert az oktató saját keretezése. Ez a szakasz témánként sorolja, mi támasztja alá, és hol nincs könyvi forrás. Az idézetek és az oldalszámok a fenti fejezetrészekben vannak, itt csak a hivatkozás áll.

**Kulcsgondolat: a megérkezés és az első benyomás.** Ehhez kapcsolódik:
Chaffey 7. fejezet: a landing page és a mélyen érkező látogató (386–387., Nielsen deep linking 397.), az alapkérdések, amire az oldalnak választ kell adnia: „who you are, what you do, where you operate and what makes you different” (387., kérdésformában 381.), a hitelesség (Fogg et al., 389.).
Yablonski: az első benyomás 50 ezredmásodperc alatt alakul ki (84., Lindgaard et al.), a tetszetős felületet használhatóbbnak érzékeljük (79.), Jakob-törvény: a látogató a máshol megszokottat várja.
Krug: a kezdőlap feladatai, köztük „Establish credibility and trust.” (Chapter 7), a goodwill-tartály, amivel a látogató érkezik (Chapter 11), és a mély oldalon a trunk test (Chapter 6).
Weinschenk: az oldalt előbb a kinézet alapján szűrik, utána a tartalom dönt (79. pont, 177–178.); a weboldal is társas helyzet, a túl korai adatkérés olyan, mint aki túl közel jön (66. pont, 151–153.).
Kotler: a hat észlelt kockázat a döntés előtti utolsó lépésben (6. fejezet, 171.), és a teljes vevői költség pénz, idő, energia és pszichés költség (125.).
Az „ő keres minket” fordulathoz könyvi forrás nincs; a 2. alkalom pull-logikája (Chaffey 1. fejezet, push kontra pull) a kurzusban már elhangzott háttér.

**Tanulság: minden lépés egy esemény.** Ez a legkevésbé könyvi rész. A könyvek a lépések élményét írják le, az eseményeket és a mérést szinte nem.
Ami van: Chaffey 10. fejezet, a webanalitika alapfogalmai és a vizsgakérdés, ami a mérést kulcsesemények rögzítéseként írja le (589); a micro-level és macro-level mérőszámok (555); a clickstream és az útvonalelemzés; az oldalon töltött idő mint torz mutató (561). Chaffey 7. fejezet, blocked arteries, vagyis a tölcsér lépései közötti legnagyobb lemorzsolódás keresése (361.); a betöltési idő (372.); Yablonski 151. oldal: mikor lett a „daily active users” és a „time on site” fontosabb annál, hogy a termék segít-e; Yablonski 79. és 91. oldal: azt kell nézni, mit csinál a felhasználó, nem csak azt, mit mond; Krug: csak megfigyelt probléma számít (Chapter 9); a goodwill-tartály lépésenként fogy és töltődik (Chapter 11).
Ami nincs a könyvekben (a 10. fejezetben sem), és a webkutatásban elsődleges forrással megvan: a Google Analytics 4 eseménymodellje (page_view, session_start, scroll, click, form_submit), a kulcsesemény (a korábbi „conversion”), az elköteleződési idő és az elköteleződött munkamenet, a mikro- és makrokonverzió (a régi Google-súgóban és a Nielsen Norman Groupnál), a hőtérkép és a munkamenet-felvétel (Microsoft Clarity, Hotjar), és hogy kívülről mi látszik egy idegen oldal méréséből.

**Hol érezte jól magát, és hol akadt el: akadályok az oldalon.** Ehhez a könyvek bőven adnak:
Krug goodwill-tartálya: mi fogyasztja (elrejtett szállítási díj és telefonszám, a feladathoz nem szükséges adat kérése, hosszú regisztrációs űrlap) és mi tölti (lépések spórolása, nyíltság a kellemetlen dolgokról) (Chapter 11); „take something (or some things) away […] rather than adding yet another distraction” (Chapter 9).
Yablonski: a súrlódás eltávolítása (2., 40., 147.), a Tesler-törvény: a komplexitás terhét vagy a felhasználó, vagy a tervező viseli (107., 117.), a Postel-fejezetben „we transfer this burden away from users” (63.), Doherty-küszöb (119–120.), Hick-törvény és a lekvár-kísérlet (42.).
Chaffey 7. fejezet: Hofacker öt akadálya (399.), „must be as simple as possible to avoid attrition” (375.), az oldalon lévő űrlap (387.). Chaffey 6. fejezet: kevés kérdés az űrlapon (316.), „Watch, don't ask” (319.).
Kotler: a TurboTax-eset, „sales jumped 6 percent” (129.), és a „kevesebb költség” út (126.).
Weinschenk: kognitív terhelés (28. pont), döntési túlterhelés (92. pont), űrlap stressz alatt (86. pont).

**Oldaltípusok, landing, tartalommodellek.** A könyvekből: Chaffey 7. fejezet (landing page, 386–387.), Krug (kezdőlap, mély oldal, navigáció, Chapter 6 és 7), Chaffey 4. fejezet (OVP, 222–223.). Chaffey 9. fejezet: a landing relevanciája és a dedikált landing a főoldal helyett (497–501), belső linkelés, a „meshed structure” a hierarchia helyett (494–495). A klasztermodell egyik könyvben sincs meg, a 9. fejezetben sem. Elsődleges forrása a HubSpot Research „Topic Clusters: The Next Evolution of SEO” cikke (2017, frissítve 2022), lásd `webkutatas-3-alkalom.md`. A landing típusai, a „message match” és az oldaltípusok listája szintén a webkutatásban van.

**Regisztráció, loyalty, automatizált e-mail.** Chaffey 6. fejezet: engedélyalapú marketing és Godin (313–314.), WIFM (316.), az üdvözlő sorozat (Table 6.1, 321.), életciklus-levelek (322.), right touching (319–320.), WHSmith (321.). Kotler: megtartás (140.), loyalty program és klub (142.), Godin (136–137.). Yablonski: a merev jelszószabály a regisztráció pillanatában (74.), peak–end szabály (65., 76.). Weinschenk: pecsétkártya, progress (50. és 55. pont). A webkutatásban: Baymard a kötelező regisztrációról mint kosárelhagyási okról, ESP-források az automatizált levelekről.

**Adatkezelés, cookie.** Chaffey 3. fejezet: a 2016-os állapot (hozzájárulás 150–151., opt-in 153–155., cookie 156–158., ellenőrzőlista 159.). Kotler 145–146.: viselkedési célzás és cookie-k. Krug: az előre bepipált hírlevél-doboz mint manipuláció (Chapter 13). Yablonski: alapértelmezett beállítások és dark pattern (146–149.). A jelenlegi jogi állapot a webkutatásban: ePrivacy-irányelv 5. cikk (3), GDPR hozzájárulás-definíció, Planet49-ítélet.

**Ellenpontok, vitának.** A pop-up akadály, mégis +40% leadet hozott (Chaffey 6. fejezet, 314.), Krug szerint tudatos üzleti döntésként vállalható (Chapter 11). A leiratkozás ne legyen túl könnyű (Chaffey 6. fejezet, 319.). A WHSmith-esetben a kedvezményes, határidős levél hozta a legtöbbet (Chaffey 6. fejezet, 321.). A szándékos súrlódás bizalmat építhet (Yablonski 119., 127–128., 154.). A zárt klub belépési feltétele szándékos akadály (Kotler 142.). Chaffey a marketingvezérelt tervezést „persuasion marketing”-nek nevezi (7. fejezet, 375.). Krug szerint a kinézet miatt szinte senki nem hagy el egy oldalt (Chapter 11), ez feszül a Fogg-adattal és Yablonski aesthetic–usability hatásával.


---

# A deckvázlat ellenőrzése (deck-vazlat-3-alkalom.md, v0.3)

A vázlat még a régi hármasra épült, a 4. fázisban az új keret szerint újraírandó. Az alábbi forráspontosítások az új deckben is érvényesek.

Diánként, csak ahol a forrás érinti. Ami eltér, kiemelve. A számozás a v0.3 vázlaté.

**8. dia (vázlat).** Megvan: Chaffey 7. fejezet, 361. oldal, Ben Jesson. Kiegészítés: Karl Blanks, 360.

**9. dia (vázlat), e-mail kontra platform.** Az e-mail kontra közösségi platform megvan: Chaffey 6. fejezet, 317. **Eltérés: a „bérelt figyelem” kifejezés egyik könyvben sincs; ha marad, „oktató” forrással.**

**10. Mit lát, amikor megérkezik.** Megvan: „who you are, what you do, where you operate and what makes you different” (Chaffey 7. fejezet, 387.), kérdésformában 381.; OVP: 4. fejezet, 222–223. **Az „öt másodperc” egyik könyvben sincs meg.** Forrással megvan helyette: Yablonski 84. oldal (50 ezredmásodperc, Lindgaard et al.), Krug 7. fejezet („first few seconds”). Az OVP-hez Chaffey 4. fejezetében nincs kérdéslista.

**11. Landing page, nem kezdőlap.** Megvan: Chaffey 7. fejezet, 386–387., 397. (Nielsen, deep linking). Krug 6. fejezet (trunk test, a mélyen érkező látogató). Hogy a See-ből és a Do-ból érkezőnek más oldal kell, az nincs meg egyik könyvben sem: saját következtetés marad.

**12. Percepció.** Fogg et al. megvan: Chaffey 7. fejezet, 389. („Design look 46.1%”). **Eltérés: a vizsgálatban a százalékok nem adnak ki 100-at, tehát nem „a legnagyobb részt viszi”, hanem a kinézet volt a leggyakrabban említett tényező; Chaffey maga is óvatosságra int (390.).** A figleaves-eset: 403–404. Vitapont: Krug szerint a kinézet miatt szinte senki nem hagy el egy oldalt (Chapter 11). Új forrás: Yablonski 79–84., Weinschenk 79. pont.

**13. Az érték két oldala.** Egyezik: Kotler 125–126. Pontosítás: a Caterpillar-eset három módot sorol fel (125.), a „két út” az ebből levont általános tanulság (126.).

**14. Hat kockázat, hat oldalelem.** A hat kockázat egyezik: Kotler 6. fejezet, 171. (a v9 25. diája is). **Pontosítás: a physical risk a könyvben „the user or others”, a v9 „árt nekem” szűkebb.** A „minden kockázathoz tartozik egy weboldalelem” gondolat nincs a könyvben, az oktatóé. A v9 jegyzetének eszközlistájából a könyvben csak a garancia szerepel.

**15. Súrlódás · idő és energia.** Megvan: betöltési idő Chaffey 7. fejezet, 372. (2011-es és 2014-es adat), Nielsen 377., az oldalon lévő űrlap 387. Frissebb forrás: Yablonski Doherty-küszöb (119–120., 126.).

**16. Súrlódás · egy akadály elvétele.** **Eltérés: a TurboTax-esetben a szám 6% („sales jumped 6 percent”, Kotler 129.), az elhagyott elem a visszatérítési eljárás vásárlásigazolási követelménye, nem egy rendelési lépés, és a „több eladást hozott, mint bármilyen új érv” összehasonlítás nincs a könyvben.** Ha a dián marad, az összehasonlítás „oktató” forrással. Kiegészítő példa forrással: Weinschenk 92. pont (lekvár), Krug 9. fejezet (elvétel hozzáadás helyett).

**17. Regisztráció és engedély.** Megvan: Godin Chaffey 6. fejezet 313–314. és Kotler 136–137.; WIFM Chaffey 316.; „Watch, don't ask” Chaffey 319. (Kotlernél a kettő nincs meg). Kiegészítés: Weinschenk 66. pont (túl korai adatkérés), Yablonski 74. (jelszószabály a regisztrációnál), Krug 11. fejezet (a hosszú regisztrációs űrlap kiüríti a tartályt).

**18. Loyalty logika.** Megvan: Kotler 140. („can cost five times more”, feltételes alakban), 142. (pontgyűjtés, klub, a zárt klub belépési feltétele szó szerint). Az új könyvekben loyalty program nincs; a legközelebb Weinschenk 50. pont (pecsétkártya) és 55. pont.

**19. Az e-mail-folyamat.** Megvan: életciklus-levelek Chaffey 6. fejezet, 322.; Table 6.1: 321. (a bevezető mondat 320.); right touching 319–320. **A Table 6.1 a könyv PDF-jén ellenőrizve: a 2. sorban „(i.e. <3 visits)” áll; az 1. sor médium-cellája és a 4. sor eredmény-cellája a könyvben is csonka, ezek nem idézhetők teljes mondatként.** Az új könyvek e-mail-automatizálást nem tárgyalnak. Yablonski peak–end szabálya (65., 76.) a folyamat utolsó élményéhez ad hátteret, az e-mailre alkalmazás saját következtetés.

**20. Egy levél, ami visszahoz.** **Eltérés: a WHSmith-esetben (Chaffey 6. fejezet, 321.) nem „a levél hozta vissza, nem a kedvezmény”. A felmérés azokra szól, akik a levélből vásároltak, de a kódot nem használták: őket a határidő hozta vissza. A teszt fő eredménye, hogy a kedvezményes, határidős levél hozta a legtöbbet (+100% és +200%, szemben a +10%-kal).**

**21. Adatkezelés mint felület.** A 2016-os állapot megvan Chaffey 3. fejezetében: hozzájárulás 150–151., opt-in 153–155., cookie 156–158., ellenőrzőlista 159. **Pontosítás: a 163. oldali előre bepipált doboz fogyasztóvédelmi összefüggésben áll (fizetős kiegészítők), nem hírlevél-hozzájárulásként.** Az előre bepipált hírlevél-doboz usability-oldalról Krugnál van (Chapter 13, manipulációként), a dark pattern és a kényszerített hozzájárulás Yablonskinál (146–149.). A GDPR egyik könyvben sincs: a jelenlegi szabályokhoz külső hivatalos forrás kell (EUR-Lex, NAIH), ez a 2. fázis.

**3. dia, Zing Burger és Wolt.** A vázlat ezt saját következtetésként jelöli. Könyvi háttér: Chaffey 6. fejezet, 304–305. (a vevő kiszolgálása a platformon) mint ellenpont.

---

# Mit ad a beadandóhoz (az 5. fázishoz, nem döntés)

A döntés (2026. október 5.): a saját márka oldala és egy külső márka oldala, ugyanazon szempontok szerint, javító javaslat nélkül. A feladat részleteit az 5. fázisban találjuk ki; itt csak az áll, mit adnak a források a megfigyeléshez.

Módszertani forrás magára a formára: a Nielsen Norman Group „Competitive Usability Evaluations” cikke (webkutatás). Krug a versenytárs-tesztet is javasolja („it's a good idea to do a test of competitive sites.”, Chapter 9), és szerinte csak megfigyelt probléma számít („they have to be observed problems; things that actually happened during one of the test sessions.”, Chapter 9). A kezdőlap-tour kérdései szó szerint megvannak („what strikes you about it, whose site you think it is, what you can do here, and what it's for.”, Chapter 9), a mély oldalhoz a trunk test (Chapter 6), a lépések rögzítéséhez a goodwill-tartály formája (Chapter 11). Yablonski figyelmeztet, hogy a szép felület elfedi a hibát, ezért azt kell nézni, mit csinál a felhasználó (79., 91.). Krug korlátja: a teszt nem méri, hogy valami kívánatos-e (Chapter 13), és nem bizonyít („actionable insights, not proof”, Chapter 9).

A mérési részhez a könyvek nem adnak módszert. A webkutatás szerint kívülről az látszik, milyen mérőeszközt és cookie-t használ egy oldal (böngésző fejlesztői eszközei, Wappalyzer, BuiltWith, Ghostery, a cookie-sáv), az adatai nem; a hallgatók tehát azt írhatják le, milyen eseményeket látnak az oldalon lehetségesnek és milyen eszközök futnak rajta.


---

# Nem találtam

Könyvenként, ahogy a feldolgozás találta.

**Chaffey, 7. fejezet.**

- „Öt másodperc” szabály (a 10. diához): a fejezetben nincs.
- „Friction” vagy „súrlódás” mint fogalom: a szó nem szerepel.
- Owned media vagy „saját felület” tulajdonlásként: csak a bevezetőben egy elválasztott mondatban, nem idézhetően.
- GDPR, cookie, hozzájárulás (consent): nincs. Az adatkezelésről csak az assurance rész (408) és a 7.5 táblázat opt-in sora (409) szól, a 3. fejezetre utalva.
- Loyalty program, pontgyűjtés, klub: nincs; a lojalitásról csak a 410. oldal egy bekezdése.
- Az üdvözlő e-mail-sorozat lépései, triggerek: nincsenek; az i-to-i esetben egy mondat szól róla, elválasztás miatt nem idézhetően (412).
- Kosárelhagyás (cart abandonment): nincs; az „abandoning web transactions” csak a SciVisum-adatnál (374).
- Pop-up, előre bepipált doboz: nincs.
- A See-Think-Do-Care szerinti eltérő érkezőoldal: nincs.
- Frissebb (2020 utáni) betöltési idő adat: nincs, a legfrissebb 2014-es.

**Chaffey, 6. fejezet.**

- A fejezet nyitóoldalát (vagy nyitóoldalait): a fájl a 301. oldallal kezdődik. Hiányzik a tanulási célok listája, a bevezető, és a Zappos-eset (Mini case study 6.1) eleje. Az első sor („Repeat customers spend more.”) a 301. oldali futófej előtt áll, ezért a `findq.py` nem ad rá oldalszámot, idézetként nem használható.
- A Table 6.1 két cellájának teljes szövegét (1. sor médium: „Email, post transaction pa”; 4. sor eredmény: „Use for range of services for guest members or full”): a nyomtatott könyvben (PDF, 321. oldal) is csonkán állnak. A „63 visits” valójában „<3 visits” (a PDF-en ellenőrizve).
- A „bérelt figyelem” (rented attention, rented land) kifejezést. A „Renting list” csak listabérlés értelemben szerepel (316. oldal).
- A „súrlódás” (friction) szót a konverzió értelmében. Egyszer fordul elő (307. oldal), de a szervezeti feszültségre vonatkozik, nem a vevő akadályaira.
- Landing page-ről szóló részt. A fejezet nem tárgyalja, a 7. fejezetre utal.
- A GDPR-t, a cookie-t és az előre bepipált dobozt. A fejezet csak általánosan említi, hogy az opt-in és az opt-out sok országban jogi kötelezettség (317., 319. oldal), és az adatvédelmet a 3. fejezetre utalja (313. oldal).
- Kosárelhagyási arányt vagy általános kosárelhagyási statisztikát. Csak a WHSmith-teszt számai vannak meg (321. oldal).
- A „megtartani olcsóbb, mint új vevőt szerezni” állítást. Ebben a fejezetben nincs meg (a vázlat ezt Kotlernél keresi).
- Az „öt másodperc” szabályt. Ebben a fejezetben sincs meg.

**Chaffey, 3. és 4. fejezet.**

- **GDPR.** A „GDPR” és a „General Data Protection Regulation” kifejezés (grep -i) egyik fejezetben sem szerepel, 0 találat a 3. és a 4. fejezetben. A „2016/679” sincs meg. A könyv jövőbeli rendeletként sem említi. A 3. fejezet 146. oldalán a „proposed EU directive” az adózásról szól, nem az adatvédelemről. A könyv jogi része teljes egészében a 95/46/EK irányelvre, a brit DPA-ra és a PECR-re épül. A GDPR-hoz és a jelenlegi szabályokhoz külső hivatalos forrás kell (2. fázis).
- **Jelenlegi fogalmak.** Nincs a fejezetekben: ePrivacy, jogos érdek (legitimate interest), elfeledtetéshez való jog, double opt-in, cookie banner (a cookie-sávot csak körülírja, 158. oldal), owned media definíció.
- **Az OVP kérdéslistája.** A 4. fejezetben az OVP-hez nincs kérdéssor, csak definíció, a Virgin Wines négy kérdése és az Activity 4.5 feladata. A 224–225. oldali tizenkét kérdés a közösségi média stratégiájához tartozik.
- **Magyar szabályozás.** A könyv brit és uniós példákat hoz, a magyar jogról és a NAIH-ról nem ír.
- **Öt másodperc.** A 10. dia javasolt „öt másodperc” szabálya a 3. és a 4. fejezetben nincs meg.

**Kotler, Keller, 5. és 6. fejezet.**

- Az 5. fejezet 125. oldal előtti részét: a fájl ott kezdődik. A fejezet kezdőoldalát nem tudom megállapítani.
- Kotlernél a WIFM-et és a „Watch, don't ask” elvet (az 5. fejezetben egyik sincs).
- A GDPR-t, a hozzájárulást, az opt-int, a cookie-sávot az 5. fejezetben. Adatvédelemről csak általánosan (145–146. oldal) és a cookie-alapú viselkedési célzásról (146. oldal) szól; az EU-törvényt nem nevezi meg.
- Landing page-et, űrlapot, kosárelhagyást, súrlódást (friction) mint fogalmat az 5. fejezetben.
- Azt az állítást, hogy a TurboTax-esetben az akadály elvétele több eladást hozott volna bármilyen új érvnél.
- Konkrét kockázatcsökkentő weboldalelemeket a 6. fejezet 171. oldalán; a könyv csak „information and support”-ot mond, a vevői rutinok között garanciát és ismert márkát.
- Az ingyenes visszaküldést, a méretsegédet és az „arc és név” elemet a 6. fejezet érintett részében.
- A 140. oldali „five times more” adat eredeti forrását: a 74. végjegyzetre hivatkozik, a végjegyzetek nincsenek a fájlban.

**Krug.**

- **E-mail-automatizálás, üdvözlő sorozat, életciklus-levelek:** nincs a könyvben. E-mail csak érkezési csatornaként (Chapter 7, Chapter 10), a visszaigazoló levél linkjeként (Chapter 11) és a túl sok hírlevél mint zaj példájaként (Chapter 3) szerepel.
- **Loyalty-program, pontgyűjtés, klub:** nincs. A legközelebbi: a látogató visszajön, ha okosnak érzi magát az oldalon (Chapter 2), és Krug azért vesz újra HP nyomtatót, mert a támogatási oldalon mindig megoldotta a problémáját (Chapter 11).
- **GDPR, hozzájárulás, cookie, adatkezelési jog:** nincs. Csak az előre bepipált hírlevél-doboz mint manipuláció (Chapter 13) és a szükségtelen személyes adat kérése mint goodwill-vesztés (Chapter 11). A „Privacy Policy” egy felsorolt link a segédlinkek között (Chapter 6), tartalmi tárgyalás nélkül.
- **A saját kontra bérelt felület gondolata:** nincs meg Krugnál.
- **Konverziós szám arra, hogy egy akadály elvétele mennyit hoz:** nincs. Egyetlen anekdota van (100 000 dollár megtakarítás, Chapter 9), és a pop-up „10 percent more revenue” feltételes mondatként (Chapter 11), nem mért adatként.
- **„Öt másodperc”:** nincs. Krug „first few seconds”-ot ír, és egy 50 ezredmásodperces kísérletre utal (Chapter 7).
- **A kezdőlap „négy kérdése” (Chapter 7) és a „fifth question” szövege:** a PDF-ben ezek képként szerepelnek, a szövegkivonatban nincsenek meg. A környező szövegből csak a „fifth question” válaszai olvashatók (hol kezdjem, ha keresni, böngészni vagy a legjobbat megnézni akarom; regisztrációnál hol regisztráljak). A négy kérdést nem írom le, mert nem tudom szó szerint ellenőrizni.
- **A kezdőlap négy mentségéről („The Top Four Plausible Excuses…”) és a teszt elleni öt kifogásról („The Top Five Plausible Reasons for not Testing…”) szóló táblázatok:** csak a címük van meg, a tartalmuk kép.
- **Oldalszámok:** a PDF-ben nincs nyomtatott oldalszám. A könyv tárgymutatója a szövegkivonatban oldalszámokat ad (például „goodwill reservoir, 166–71”), de ezeket nem tudom a szöveghez kötni, ezért nem használom őket.
- **Chapter 12 (Accessibility and you):** átolvastam; a beadandóhoz legfeljebb a „három másodperces” betűméret-teszt kapcsolódik, a tematikához nem tartozik, ezért külön alszakaszt nem kapott.

**Weinschenk.**

- E-mail-automatizálás, életciklus-levél, üdvözlő sorozat, kosárelhagyó levél: nincs a könyvben. Az e-mail csak felhasználói szokásként (53. pont), kutatási médiumként (67. pont) és a MailChimp példáiban (27., 34., 55. pont) szerepel.
- GDPR, adatvédelem, hozzájárulás, opt-in, cookie, hírlevél: egyik kulcsszó sem fordul elő (a fájlban kerestem: „privacy”, „consent”, „opt-in”, „cookie”, „newsletter”, „GDPR”).
- „Friction”, „conversion”, „landing page”, „checkout”, „shopping cart”: a szavak nem szerepelnek. A „landing” egyetlen előfordulása (82. pont) más értelmű.
- Regisztrációs folyamat mint téma: nincs külön pont. A legközelebbi a 66. pont (adatkérés túl korán) és a 60. pont (kis lépés).
- A „gyors ítélet” ezredmásodperces kutatása (például az 50 ezredmásodperces benyomás): nincs. A könyvben az egy-két másodperc a szerző példája (57. pont), a bizalomról a Sillence-kutatás szól (79. pont).
- Loyalty-program mint marketingeszköz: nincs külön pont; a pecsétkártya (50. pont), a jutalomütemezés (51. pont) és a 55. pont egy mondata érinti.
- Szűkösségről külön kutatás: nincs. A szűkösség a könyv egyik tanulságmondatában (56. pont, 131) és a szerző saját véleményeként (81. pont, 180) jelenik meg.

**Yablonski.**

- Zeigarnik-hatás: a könyvben nem szerepel.
- Goal-gradient hatás külön fejezetként: csak egy mondatban, az Uber-példánál (69. oldal); oldalszám az index szerint is csak ez.
- Serial position effect: nem szerepel; csak a recency effect egy mondata (68. oldal).
- GDPR, hozzájárulás, cookie, opt-in: nem szerepel. A legközelebbi az alapértelmezett adatvédelmi beállítás (146. oldal) és a dark pattern, benne a marketingkommunikáció elfogadása (148. oldal).
- E-mail-marketing, automatizált e-mail-folyamat, hírlevél: nem szerepel. Az e-mail csak levélírási felületként (Tesler, 109–110. oldal) és a Gmail betöltőképernyőjeként (125. oldal) jön elő.
- Landing page, konverziós arány mint mérőszám: a „landing” szó nem szerepel webes értelemben; „conversion rates” egyszer, a TikTok személyre szabásánál (145. oldal).
- Loyalty program, pontgyűjtés, klub: nem szerepel. A regisztrációhoz csak a jelszószabály (74. oldal) és a Notion onboarding (44. oldal) kapcsolódik.
- A látogatási mutató és a valódi eredmény különbsége, valamint a „saját felület” gondolata: szó szerint nincs.
- Choice overload, chunking, working memory, cognitive load, flow: van, de nem saját fejezetként (Hick 41. oldal, Miller 31–32. oldal, Doherty 121–122. oldal).


**Chaffey, 9. fejezet.**

- Klasztermodell, topic cluster, pillar page: a fejezetben nincs. A „hub” szó kétszer fordul elő: a PageRank kapcsán külső „hub sites” értelemben (494) és a 9.12 ábra feliratában a blogbejegyzés mint terjesztési középpont (509). A legközelebbi rokon a „Resource Centre” (494) és a hálós belső linkszerkezet (495).
- „Message match” kifejezés: nincs. A gondolat a quality score relevanciaelemeiben és az AdGroup-kérdésben van meg (497, 500).
- Mi nem landing oldal, landing típusai rendszerezve: nincs. Csak a főoldal és a dedikált oldal szembeállítása (499), a direkt válaszra épülő display céloldal (515) és az e-mail űrlapos landingje (526).
- Cookie-hozzájárulás, GDPR, adatvédelmi szabályozás a cookie-k kapcsán: nincs. A 516. oldalon egy utalás a 3. fejezet adatvédelmi aggályaira („However, it is unclear whether privacy concerns”), kifejtés nélkül.
- Hőtérkép: nincs.
- Oldalmegtekintés mint esemény: csak a display hirdetés megjelenésének szinonimájaként („impressions (page views).”, 519), nem mint az oldal mérőszáma.
- UX, UI, első benyomás, bizalmi elemek az oldalon: a fejezet nem tárgyalja; ezek a 7. fejezetben vannak.
- Loyalty program kifejtve: csak a Huggies-példában egy fél mondat (515).

**Chaffey, 10. fejezet.**

- Hőtérkép (heatmap), kattintási térkép (click overlay), görgetési térkép: nem szerepel a fejezetben.
- Munkamenet-felvétel (session recording, session replay): nem szerepel. A legközelebbi az Amazon „every last click and twitch of the mouse” mondata (584) és a fókuszcsoport megfigyelése (573).
- Szemkamerás vizsgálat (eye tracking): nem szerepel.
- „Mikrokonverzió” és „makrokonverzió” kifejezés: nem szerepel. Van „micro-level” és „macro-level metrics” (555), és egy margószócikkben „macro-conversion rates” (564), ez utóbbi findq-val nem ellenőrizhető egyben.
- Site-centric és customer-centric mérés szembeállítása: nem szerepel. A „customer-centric” csak az Amazon küldetésében és a Marcus-féle mérőszám-ötletelésben fordul elő (583–584), módszertani megkülönböztetésként nem.
- Az esemény (event) definíciója: nincs. Csak Kaushik „event logging” említése (553) és a 3. vizsgakérdés (589).
- Elköteleződési idő (engagement time): nincs, ez GA4-es fogalom. Az oldalon töltött idő („duration on a site”, „time on site”, „session time”) csak mellékesen szerepel (561, 579, 584), definíció nélkül.
- Az átkattintási arány (click-through rate) definíciója: nincs, csak az A/B teszt céljai között (564) és az Amazon e-mail-rendszerénél (585) említve.
- A cookie-k pontossági problémái (törlés, több eszköz, böngészőváltás, elutasítás): nem szerepelnek. A cookie csak azonosítóként (557, 561) és adatvédelmi szabályként (569) jelenik meg.
- Usability testing önálló módszertana: nincs. Csak említések: „Remote usability testing” (Kaushik, 552), a fókuszcsoport forgatókönyvekkel (572–573), a próbavásárló „site usability” pontja (573).
- A GA4 és a Universal Analytics megszűnése: természetesen nincs benne, a könyv 2016-os.
- A Google Website Optimiser sorsa (552): a könyvben nincs, a fenti megjegyzés ellenőrizendő.

---

# Döntések

1. **2026. október 5.:** a sorrend az átadó doksi szerint: előbb az 1–3. fázis, csak utána a deck és a feladat.
2. **2026. október 5.:** az e-mail-feliratkozás előre kiadásáról szóló kérdés törölve, nem kell.
3. **2026. október 5.:** a betűméret: az alapméret kb. 20%-kal nagyobb (1440 px szélességen kb. 23 px), semmi nem lesz 18 px alatt.
4. **2026. október 5.:** három új könyv a forrásokhoz: Krug (2014), Weinschenk (2011), Yablonski (2024).
5. **2026. október 5.:** a korábbi sessionből beemelt kulcsgondolat, tanulság és fázis-sor nem az oktatóé, elengedve. Az új hármas az A változat (fent).
6. **2026. október 5.:** a mérésből itt a weboldal kulcseseményei és a mérőeszközök (cookie, hőtérkép) kerülnek elő; a mérési terv és a hibakeresés a 6. alkalomé.
7. **2026. október 5.:** a beadandó a saját márka és egy külső márka oldalának elemzése, javító javaslat nélkül. A külső oldalt minden csapat egy előre összeállított listából választja.
8. **2026. október 5.:** a nap: másfél óra elmélet, másfél óra csoportmunka.
9. **2026. október 5.:** a csapatok márkáinak tisztázása (Kolorádó, Levendula, Katedra városa, Hotel Historia) elengedve.
10. **2026. október 5.:** a Table 6.1 a teljes könyv PDF-jén ellenőrizve (lásd a 6. fejezetnél).
11. **2026. október 5.:** a tematika jóváhagyva (`tematika-3-alkalom.md`), a lazítással. Chaffey 9. és 10. fejezete bekerült a teljes könyvből.

# Nyitott kérdések

Ezekről te döntesz.

1. **Krug oldalszámai.** A PDF-ben nincs nyomtatott oldalszám, ezért fejezettel hivatkozom (Chapter N). Elfogadod?
2. **Hiányzó fejezetkezdet.** Kotler 5. fejezetéből a 125. oldal előtti rész hiányzik. Kell? (Chaffey 6. fejezetének nyitóoldala a teljes könyvben megvan, ha kell, beemelem.)
3. **A régebbi könyvek súlya.** Javaslatom: a deckben Yablonski legyen az elsődleges UX-forrás, Krug a goodwill-tartály és a megfigyelési módszer miatt maradjon, Weinschenkből a lekvár-kísérlet és a 66. pont kerüljön a jegyzetbe. Így gondolod?
4. **Vitapontok.** A fenti ellenpontok a dián legyenek, vagy csak a jegyzetben?
