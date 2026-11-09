# -*- coding: utf-8 -*-
# AI a marketingben, 2026 ősz, gyakorlat: a deckek tartalma, magyarul és angolul.
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
CB_HU = json.load(open(os.path.join(HERE, 'codeblocks_hu.json')))
CB_EN = json.load(open(os.path.join(HERE, 'codeblocks_en.json')))

VER_HU = 'v1.3 · 2026. november 4.'
VER_EN = 'v1.3 · 4 November 2026'

# Eddig az alkalomig kattinthatók a linkek a kezdőlapon és a felső sávban.
# A többi alkalom szürke és nem nyitható. Hétről hétre ezt a számot emeljük.
NYITVA = 1

# Ha egy fájl frissebb a többinél, itt kap saját verziót: kulcs 1-6 a diasorokhoz, 'index' a kezdőlaphoz.
VER_KIVETEL = {1: ('v1.5 · 2026. november 6.', 'v1.5 · 6 November 2026')}


def VER(kulcs):
    '''A fájl verziószáma magyarul és angolul.'''
    return VER_KIVETEL.get(kulcs, (VER_HU, VER_EN))

def L(hu, en):
    return {'hu': hu, 'en': en}

SESS = [
  dict(n=1, short='11.&nbsp;05.', d=L('2026. november 5.', '5 November 2026'),
       t=L('Kiinduló márka és új kategória', 'Source brand and new category'),
       out=L('Ütemterv, márkaelemzés, versenytársak', 'Timeline, brand analysis, competitors')),
  dict(n=2, short='11.&nbsp;12.', d=L('2026. november 12.', '12 November 2026'),
       t=L('Márkaplatform, célcsoport és árazás', 'Brand platform, target audience and pricing'),
       out=L('Márkabrief: név, platform, personák', 'Brand brief: name, platform, personas')),
  dict(n=3, short='11.&nbsp;19.', d=L('2026. november 19.', '19 November 2026'),
       t=L('Arculat (ID), kulcsvizuálok és bannerek', 'Identity, key visuals and banners'),
       out=L('Logó, kézikönyv, kulcsvizuálok, bannerek', 'Logo, brand guide, key visuals, banners')),
  dict(n=4, short='11.&nbsp;26.', d=L('2026. november 26.', '26 November 2026'),
       t=L('Kampánybrief, koncepció, szövegek és posztok', 'Campaign brief, concept, copy and posts'),
       out=L('Kampánybrief, koncepció, szövegek, posztok', 'Campaign brief, concept, copy, posts')),
  dict(n=5, short='12.&nbsp;03.', d=L('2026. december 3.', '3 December 2026'),
       t=L('Weboldal, videóspot és a tenderdeck', 'Website, video spot and the pitch deck'),
       out=L('Weboldal, videóspot, a deck vázlata', 'Website, video spot, deck outline')),
  dict(n=6, short='12.&nbsp;10.', d=L('2026. december 10.', '10 December 2026'),
       t=L('Tenderprezentáció', 'Pitch presentation'),
       out=L('Bemutató és a készítés története', 'Presentation and the making-of story')),
]

# előző napi elméleti órák
THEORY = {
  1: (L('2026. november 4.', '4 November 2026'), [L('Kelly: AI engineering a marketingben', 'Kelly: AI engineering for marketing'), L('Kelly: AI a termékfejlesztésben, összefoglaló', 'Kelly: AI in product development, recap')]),
  2: (L('2026. november 11.', '11 November 2026'), [L('Nóra: Az AI alapfogalmai és története', 'Nóra: Basic concepts and history of AI'), L('Kelly: AI-alapú árazás', 'Kelly: AI-based pricing')]),
  3: (L('2026. november 18.', '18 November 2026'), [L('Kelly: Képszerkesztés AI-jal', 'Kelly: Image editing with AI'), L('Kelly: Hang- és videószerkesztés AI-jal', 'Kelly: Audio and video editing with AI')]),
  4: (L('2026. november 25.', '25 November 2026'), [L('Nóra: Promptolás és szövegírás', 'Nóra: Prompting and copywriting'), L('Kelly: Adatelemzés és prediktív marketing', 'Kelly: Data analysis and predictive marketing')]),
  5: (L('2026. december 2.', '2 December 2026'), [L('Nóra: AI és disztribúció', 'Nóra: AI and distribution'), L('Kelly: SEO és keresőmarketing AI-jal', 'Kelly: SEO and search engine marketing with AI')]),
  6: (L('2026. december 9.', '9 December 2026'), [L('Nóra: Prezentációkészítés', 'Nóra: Presentation creation')]),
}

# Cél, scope, leadandó, a feladatleírás szerint
GOAL = {
  1: L('Válassz márkát, és értsd meg, mitől működik a kiinduló márka.', 'Choose a brand and understand what makes the source brand work.'),
  2: L('Építsd fel az új márka alapjait.', 'Build the foundations of the new brand.'),
  3: L('Adj az új márkának saját arcot a kiinduló márka szellemében.', 'Give the new brand its own face in the spirit of the source brand.'),
  4: L('Tervezd meg a bevezető kampányt, írd meg minden elem szövegét, és készítsd el a posztokat és a hírlevelet.', 'Plan the launch campaign, write the copy for every element, and produce the posts and the newsletter.'),
  5: L('Készítsd el a kampány utolsó elemeit, és rakd össze a tenderdecket.', 'Produce the last campaign elements and assemble the pitch deck.'),
  6: L('Mutasd be a decket, és meséld el, hogyan készült.', 'Present the deck and tell how it was made.'),
}
SCOPE = {
  1: L('Az alkalom végére tudod, melyik márkával dolgozol, miért az működik, kik a versenytársak az új kategóriában, és van egy féléves terved.', 'By the end of the session you know which brand you work with, why it works, who the competitors are in the new category, and you have a plan for the semester.'),
  2: L('Az alkalom végére van neve a márkádnak, tudod, mit ígér, kinek és milyen hangon. Ez a deck 1-2. blokkjának alapja.', 'By the end of the session your brand has a name, and you know what it promises, to whom, and in what voice. This is the basis of blocks 1-2 of the deck.'),
  3: L('Az alkalom végére a márkádnak van arca: logó, színek, betűk, képi világ, és van néhány kész vizuál, amit a kampányban használni fogsz. Hogy ebből mennyi készül el órán és mennyi otthon, a te döntésed.', 'By the end of the session your brand has a face: logo, colours, type, imagery, and a few finished visuals you will use in the campaign. How much of this gets done in class and how much at home is your call.'),
  4: L('Az alkalom végére megvan a kampány nagy ötlete és szlogenje, és az összes szöveg, ami a kampányeszközökhöz kell. Ez a deck 3. és 5. blokkja.', "By the end of the session you have the campaign's big idea and slogan, and all the copy the campaign assets need. This is blocks 3 and 5 of the deck."),
  5: L('Az alkalom végére minden kampányeszköz megvan prototípusként, és áll a tenderdeck vázlata. Ez a deck 4. blokkja és maga a deck.', 'By the end of the session every campaign asset exists as a prototype, and the outline of the pitch deck stands. This is block 4 of the deck and the deck itself.'),
  6: L('Kész deck, megtartott bemutató.', 'Finished deck, presentation delivered.'),
}
DELIV = {
  1: L('Féléves ütemterv, márkaelemzés és versenytárstáblázat forrásokkal.', 'Semester timeline, brand analysis and competitor table with sources.'),
  2: L('Márkabrief (név, platform, personák).', 'Brand brief (name, platform, personas).'),
  3: L('Logó SVG, arculati kézikönyv PDF, 3 kulcsvizuál, 3 posztsablon, 2 banner, plakát-mockup, csomagolás- vagy terméklátvány.', 'Logo SVG, brand guide PDF, 3 key visuals, 3 post templates, 2 banners, billboard mock-up, packaging or product visual.'),
  4: L('Kampánybrief, kreatív koncepció, szövegcsomag, bevezetési és médiaterv, 5 poszt, HTML hírlevél.', 'Campaign brief, creative concept, copy deck, launch and media plan, 5 posts, HTML newsletter.'),
  5: L('Kulcsszólista, weboldal link, spot link, a tenderdeck vázlata.', 'Keyword list, website link, spot link, pitch deck outline.'),
  6: L('Végleges tenderdeck a készítés történetével, a bemutató és a teljes portfólió.', 'Final pitch deck with the making-of story, the presentation and the complete portfolio.'),
}

# Lépések. Egy lista egy diára kerül; ha több lista van, több dia.
# (cím, [lépések]); a lépés elé 'OPT:' = opcionális
STEPS = {
  1: [(L('Lépések', 'Steps'), [
      L('Lépj be az AI-fiókodba, ha még nincs, regisztrálj. Lehet ChatGPT, Claude vagy bármi más, amit ismersz, de a Claude vagy a ChatGPT az ajánlott. Ismerkedj a felülettel, próbáld ki, mit tud: webes keresés, fájlfeltöltés, dokumentum és prezentáció készítése. Itt vagyok, segítek.',
        'Log in to your AI account; if you do not have one, register. It can be ChatGPT, Claude or anything else you know, but Claude or ChatGPT is recommended. Get to know the interface and try what it can do: web search, file upload, creating documents and presentations. I am here to help.'),
      L('Válassz egy márkát a listából. Mindenkinek más jut.', 'Choose a brand from the list. Everyone gets a different one.'),
      L('Rakd össze az AI-jal a saját féléves tervedet: nézd át vele az órarendet, a deck öt blokkját és a hat alkalom leadandóit, és kérd meg, hogy készítsen neked egy ütemtervet, mikor mivel készülsz el. Ez lesz a térképed a félévre.',
        'Build your own semester plan with the AI: go through the schedule, the five blocks of the deck and the outputs of the six sessions with it, and ask it to make you a timeline of when you finish what. This will be your map for the semester.'),
      L('Kezdj el gondolkodni a márkán: elemezd a kiinduló márkát az AI-jal, bekapcsolt webes kereséssel: értékek, személyiség, hangnem, vizuális kódok (színek, formák, betűk), ikonikus kampányok. Nyisd meg a forrásokat, tanulmányozd.',
        'Start thinking about the brand: analyse the source brand with the AI, with web search switched on: values, personality, tone of voice, visual codes (colours, shapes, type), iconic campaigns. Open the sources and study them.'),
      L('Térképezz fel 5 valódi versenytársat az új kategóriában: ajánlat, árszint, hangnem, fő csatornák. Tedd táblázatba, forráslinkekkel.',
        'Map 5 real competitors in the new category: offer, price level, tone of voice, main channels. Put it in a table with source links.'),
      L('Írd le egy bekezdésben, mit viszel át a kiinduló márkából, és mit nem.', 'Write one paragraph on what you carry over from the source brand and what you do not.'),
  ])],
  2: [(L('Lépések', 'Steps'), [
      L('Generálj AI-jal 20 névötletet, válassz egyet, és webes kereséssel nézd meg, használja-e már valaki a kategóriában.', 'Generate 20 name ideas with AI, choose one, and check with web search whether anyone already uses it in the category.'),
      L('Írd meg a márkaplatformot: pozicionálás, ígéret, 3 érték, személyiség, hangnem.', 'Write the brand platform: positioning, promise, 3 values, personality, tone of voice.'),
      L('Készíts legalább 2 personát AI-jal. Kérdezd ki mindkettőt 5 kérdéssel szerepjátékos chatben, és jelöld meg a válaszokat, amelyekről úgy gondolod, hogy kitaláltak.', 'Create at least 2 personas with AI. Interview each with 5 questions in a role-play chat, and mark the answers you think are made up.'),
      L('OPT:Ha a márkádhoz fontos az ár (például prémium vagy olcsó pozicionálás), vázolj egy árazási irányt, és vesd össze a versenytársakkal. Ha nem, hagyd ki.', 'OPT:If price matters for your brand (for example premium or budget positioning), sketch a pricing direction and compare it with the competitors. If not, skip it.'),
  ])],
  3: [(L('Lépések 1/2', 'Steps 1/2'), [
      L('Írd le a vizuális irányt: mit veszel át a kiinduló márka vizuális kódjaiból, mit nem, és 3 vizuális kulcsszó.', "Describe the visual direction: what you take from the source brand's visual codes, what you do not, and 3 visual keywords."),
      L('Logó: készíttess Claude-dal 3 logóirányt SVG-ben, artifactként. Válassz egyet, és finomítsd. A kiinduló márka logóját ne másold.', "Logo: have Claude make 3 logo directions in SVG, as artifacts. Pick one and refine it. Do not copy the source brand's logo."),
      L('Készíts arculati kézikönyvet Claude Designban: logó és használata, színek HEX-kóddal, betűtípusok, képi stílus, egy mintaposzt. Exportáld PDF-be. Ha nálad nem érhető el a Claude Design, kérd meg Claude-ot, hogy artifactként készítse el, és mentsd PDF-be a böngésző nyomtatás funkciójával.', "Make a brand guide in Claude Design: logo and its use, colours with HEX codes, typefaces, image style, one sample post. Export it as PDF. If Claude Design is not available to you, ask Claude to make it as an artifact and save it as PDF with the browser's print function."),
      L('Készíts 3 kulcsvizuált a ChatGPT képgenerálásával, ebből egy legyen a kampány fő kulcsvizuálja. Az ingyenes csomagban a képgenerálás korlátozott, ezért generálás előtt csiszold a promptot.', "Make 3 key visuals with ChatGPT image generation; one of them should be the campaign's main key visual. Image generation is limited on the free plan, so polish the prompt before you generate."),
    ]),
    (L('Lépések 2/2', 'Steps 2/2'), [
      L('Készíts 3 posztsablont az arculattal Claude Designban vagy artifactként: négyzetes poszt, 9:16-os story, carousel nyitódia.', 'Make 3 post templates with the identity in Claude Design or as an artifact: square post, 9:16 story, carousel opening slide.'),
      L('Bannerek és plakát: 300×250 és 728×90 pixeles HTML-banner a fő kulcsvizuállal, artifactként, plusz egy óriásplakát-mockup a ChatGPT képgenerálásával. A kampányszlogen még nincs meg, ezért egyelőre a márkanévvel és az ígérettel készüljenek, a szlogent az 5. alkalmon cseréled be.', 'Banners and billboard: 300×250 and 728×90 pixel HTML banners with the main key visual, as artifacts, plus a billboard mock-up with ChatGPT image generation. The campaign slogan does not exist yet, so for now make them with the brand name and the promise; you swap in the slogan in session 5.'),
      L('Csomagolás vagy termékdizájn: készíts látványt a ChatGPT képgenerálásával, a kategóriád szerint (például az autó, a kozmetikum doboza vagy a kávéspohár).', 'Packaging or product design: make a visual with ChatGPT image generation, according to your category (for example the car, the cosmetics box or the coffee cup).'),
    ])],
  4: [(L('Lépések 1/2', 'Steps 1/2'), [
      L('Írd meg a kampánybriefet: cél, célcsoport, fő üzenet, csatornák, időtáv, sikermérők.', 'Write the campaign brief: objective, target audience, key message, channels, timeframe, success metrics.'),
      L('Építs márkaasszisztenst: hozz létre egy Claude-projektet, töltsd fel bele a márkabriefet és a personákat, a hangnemet pedig írd be a projekt utasításaiba. A további szövegeket ebben a projektben írasd, és figyeld, mennyiben tartja a márka hangját.', "Build a brand assistant: create a Claude project, upload the brand brief and the personas into it, and write the tone of voice into the project instructions. Write all further copy in this project, and watch how well it keeps the brand's voice."),
      L('Promptlánc: generálj 10 kampányötletet (big idea), válassz egyet, generálj hozzá 20 szlogent, válassz ki 3-at, és teszteld őket a personákon.', 'Prompt chain: generate 10 campaign ideas (big ideas), choose one, generate 20 slogans for it, shortlist 3, and test them on the personas.'),
      L('Írd meg a kreatív koncepciót egy oldalban.', 'Write the creative concept on one page.'),
    ]),
    (L('Lépések 2/2', 'Steps 2/2'), [
      L('Írd meg a szövegeket: a weboldal szövegei oldalanként, 5 közösségi poszt, 1 hírlevél, egy 15 másodperces videóspot forgatókönyve (6 képkocka, kép és szöveg). Szerkeszd át magad, jelölj meg minden állítást, amit nem tudtál ellenőrizni, aztán javítsd vagy töröld.', 'Write the copy: website copy page by page, 5 social posts, 1 newsletter, a script for a 15-second video spot (6 frames, image and text). Edit everything yourself, mark every claim you could not verify, then fix or delete it.'),
      L('Bevezetési és médiaterv: teaser, launch és sustain fázis; paid, earned és owned csatornák; idővonal Gantt-diagramként; a büdzsé százalékos felosztása; KPI-ok számszerű céllal.', 'Launch and media plan: teaser, launch and sustain phases; paid, earned and owned channels; timeline as a Gantt chart; budget split in percentages; KPIs with numeric targets.'),
      L('5 kész közösségi poszt: a 3. alkalom sablonjai és kulcsvizuáljai a mai szövegekkel, a platform és a formátum megnevezésével.', "5 finished social posts: session 3's templates and key visuals with today's copy, naming the platform and the format."),
      L('HTML hírlevél: a hírlevélszövegből készíttess Claude-dal arculatos e-mail sablont.', 'HTML newsletter: have Claude turn the newsletter copy into an on-brand email template.'),
      L('OPT:Kérd meg Claude-ot, hogy készítsen 12 havi minta értékesítési adatsort az új márkához, elemezze, és jelezze előre a következő 3 hónapot. Írj 3 okot, amiért az előrejelzés tévedhet.', 'OPT:Ask Claude to create a 12-month sample sales dataset for the new brand, analyse it, and forecast the next 3 months. Write 3 reasons why the forecast may be wrong.'),
    ])],
  5: [(L('Első blokk: megvalósítás', 'First block: production'), [
      L('Kulcsszavak: gyűjts 40-et AI-jal, keresési szándék szerint csoportosítva. Claude webes keresésével nézd meg 3 versenytárs oldalát, milyen kifejezések vannak a címekben és alcímekben. Az AI által írt keresési számokban ne bízz, valódi keresési adatot az ingyenes eszközök nem adnak. Minden weboldalhoz rendelj egy fő kulcsszót.', "Keywords: collect 40 with AI, grouped by search intent. With Claude's web search, look at 3 competitors' sites to see which phrases appear in their titles and subheadings. Do not trust search volumes written by AI; free tools do not give real search data. Assign one main keyword to every page."),
      L('Weboldal HTML-prototípusként: építtesd meg Claude-dal artifactként vagy Claude Designban, legalább 4 oldallal vagy szekcióval (főoldal, termék, árak, rólunk és kapcsolat). Legyen benne az arculat, a szövegeid és a képeid, oldalanként meta cím és meta leírás, és működjön mobilon is. Oszd meg a linkjét.', 'Website as an HTML prototype: have Claude build it as an artifact or in Claude Design, with at least 4 pages or sections (home, product, prices, about and contact). It should carry the identity, your copy and your images, a meta title and meta description per page, and work on mobile. Share its link.'),
      L('Animált videóspot: a forgatókönyvből készíttess Claude-dal egy 15 másodperces animált HTML-spotot artifactként, ami a böngészőben lejátszható.', 'Animated video spot: from the script, have Claude make a 15-second animated HTML spot as an artifact that plays in the browser.'),
      L('A bannereken cseréld be a kampányszlogent.', 'Swap the campaign slogan into the banners.'),
    ]),
    (L('Második blokk: tenderdeck', 'Second block: pitch deck'), [
      L('Építsd meg a tenderdecket Claude Slidesban a 15-20 diás szerkezet szerint. Ha nálad nem érhető el a Claude Slides, kérd meg Claude-ot, hogy PPTX fájlként készítse el.', 'Build the pitch deck in Claude Slides along the 15-20 slide structure. If Claude Slides is not available to you, ask Claude to make it as a PPTX file.'),
      L('Próba AI-jal: add az AI-nak az ügyfél marketingigazgatójának szerepét, kérj tőle 5 kemény kérdést, és válaszolj rájuk. Mérd le, belefér-e a bemutatód 15-20 percbe a készítés történetével együtt.', "Rehearse with AI: give the AI the role of the client's marketing director, ask it for 5 tough questions, and answer them. Time whether your presentation fits into 15-20 minutes together with the making-of story."),
    ])],
  6: [(L('Lépések', 'Steps'), [
      L('Utolsó simítások, 30 perc: javítsd a decket az előző napi prezentációs óra alapján, és exportáld PPTX-be vagy PDF-be.', "Final touches, 30 minutes: improve the deck based on the previous day's presentation class, and export it as PPTX or PDF."),
      L('Egészítsd ki a decket a készítés történetével, 3-5 diában: milyen eszközöket használtál és mire; mi ment jól; hol hibázott vagy akadt el az AI, és hogyan oldottad meg; mi idegesített; mit csinálnál máshogy.', 'Add the making-of story to the deck in 3-5 slides: which tools you used and for what; what went well; where the AI failed or got stuck, and how you solved it; what annoyed you; what you would do differently.'),
      L('Bemutató mindenki előtt, 15-20 perc: a tenderdeck és a készítés története, utána kérdések.', 'Presentation in front of everyone, 15-20 minutes: the pitch deck and the making-of story, then questions.'),
      L('Közös visszajelzés a végén.', 'Joint feedback at the end.'),
  ])],
}

TOOLS = {
  1: L('Kutatásra és elemzésre Claude vagy ChatGPT bekapcsolt webes kereséssel, Perplexity, Gemini; a féléves tervhez bármelyik asszisztens, a források rendezésére NotebookLM.', 'For research and analysis Claude or ChatGPT with web search on, Perplexity, Gemini; for the semester plan any assistant; for organising sources NotebookLM.'),
  2: L('Névötletekhez és márkaplatformhoz ChatGPT vagy Claude (sok kör, ide a ChatGPT korlátlan szöveges chatje jól jön), a név ellenőrzésére webes keresés bármelyikben; persona-szerepjátékhoz bármelyik asszisztens, Grok, Gemini, Le Chat is.', "For name ideas and the brand platform ChatGPT or Claude (many rounds; ChatGPT's unlimited text chat comes in handy here), for checking the name web search in either; for persona role-play any assistant, Grok, Gemini or Le Chat too."),
  3: L('Bármi más is jó, amit ismersz: logóhoz Claude (SVG artifact), Figma AI, Recraft, Ideogram, Adobe Illustrator; arculati kézikönyvhöz és posztsablonhoz Claude Design, Figma, Canva, Adobe Express; kulcsvizuálhoz, plakáthoz és csomagoláshoz ChatGPT képgenerálás, Gemini, Midjourney, Adobe Firefly, Leonardo AI, Microsoft Designer; bannerhez Claude artifact, Figma vagy Canva.', 'Anything else you know is fine: for the logo Claude (SVG artifact), Figma AI, Recraft, Ideogram, Adobe Illustrator; for the brand guide and post templates Claude Design, Figma, Canva, Adobe Express; for key visuals, billboard and packaging ChatGPT image generation, Gemini, Midjourney, Adobe Firefly, Leonardo AI, Microsoft Designer; for banners Claude artifact, Figma or Canva.'),
  4: L('Ötletelésre és szlogenekre ChatGPT, Claude, Gemini, Grok; a márkaasszisztenshez Claude-projekt (vagy ChatGPT-ben egy projekt, ha a fiókodban van); szövegírásra a márkaasszisztens; posztokhoz Canva vagy Claude Design; HTML hírlevélhez Claude artifact; médiatervhez bármelyik asszisztens táblázatban.', 'For ideation and slogans ChatGPT, Claude, Gemini, Grok; for the brand assistant a Claude project (or a project in ChatGPT, if your account has it); for copywriting the brand assistant; for posts Canva or Claude Design; for the HTML newsletter Claude artifact; for the media plan any assistant, in a table.'),
  5: L('Bármi más is jó: kulcsszavakhoz Claude vagy ChatGPT webes kereséssel, Perplexity; weboldal-prototípushoz Claude artifact vagy Claude Design, Figma, Lovable, v0, Bolt.new, Framer AI; animált spothoz Claude artifact (HTML), vagy ha videót akarsz, Runway, Kling, Pika, Luma, CapCut; a deckhez Claude Slides, Gamma, Canva.', 'Anything else is fine: for keywords Claude or ChatGPT with web search, Perplexity; for the website prototype Claude artifact or Claude Design, Figma, Lovable, v0, Bolt.new, Framer AI; for the animated spot Claude artifact (HTML), or if you want video, Runway, Kling, Pika, Luma, CapCut; for the deck Claude Slides, Gamma, Canva.'),
  6: L('A próbához bármelyik asszisztens, hangos gyakorláshoz a ChatGPT vagy a Claude hangmódja; a deck véglegesítéséhez Claude Slides, Gamma, Canva, PowerPoint.', 'For the rehearsal any assistant, for practising out loud the voice mode of ChatGPT or Claude; for finalising the deck Claude Slides, Gamma, Canva, PowerPoint.'),
}

# Promptdiák: (cím, strukturált index, szabad szöveges index) a kódblokk-listában
PROMPTS = {
  1: [(L('Márkaelemzés', 'Brand analysis'), 0, 1)],
  2: [(L('Persona-interjú', 'Persona interview'), 2, 3)],
  3: [(L('Logóirányok', 'Logo directions'), 4, 6), (L('Kulcsvizuál', 'Key visual'), 5, 7)],
  4: [(L('Promptlánc a kreatív koncepcióhoz', 'Prompt chain for the creative concept'), 8, 10),
      (L('Márkaasszisztens, a Claude-projekt utasításaiba', 'Brand assistant, in the Claude project instructions'), 9, 11)],
  5: [(L('Weboldal-prototípus', 'Website prototype'), 12, 13)],
  6: [(L('Pitchpróba', 'Pitch rehearsal'), 14, 15)],
}
# rövid, folyó szövegű promptjavaslatok a feladatleírásból
INLINE = {
  1: [(L('Féléves ütemterv', 'Semester timeline'),
       L('Itt a félév feladatleírása [bemásolva vagy feltöltve]. Egy [új kategória] márkát építek a [kiinduló márka] szellemében. Készíts nekem egy ütemtervet a hat alkalomra: mi készül órán, mi marad otthonra, és melyik anyag a deck melyik blokkjába kerül. Táblázatban kérem, és jelezd, hol látsz szűk keresztmetszetet.',
         'Here is the assignment description for the semester [pasted or uploaded]. I am building a [new category] brand in the spirit of [source brand]. Make me a timeline for the six sessions: what gets done in class, what is left for home, and which material goes into which block of the deck. In a table, and flag where you see a bottleneck.')),
      (L('Versenytársak', 'Competitors'),
       L('Keress 5 valódi [új kategória] márkát [ország vagy régió] piacán. Táblázatban: ajánlat, árszint, hangnem, fő csatornák, forráslink. Csak létező cégeket írj, és ahol bizonytalan vagy, jelöld.',
         'Find 5 real [new category] brands on the [country or region] market. In a table: offer, price level, tone of voice, main channels, source link. Only list existing companies, and mark where you are unsure.'))],
  5: [(L('Animált spot', 'Animated spot'),
       L('A forgatókönyv alapján készíts egy 15 másodperces animált HTML-spotot artifactként, 6 jelenettel, a márka színeivel és betűivel. Automatikusan induljon, és legyen újrajátszás gomb.',
         "Based on the script, create a 15-second animated HTML spot as an artifact, with 6 scenes, in the brand's colours and type. It should start automatically and have a replay button."))],
}

# Tippek és tanácsok: alkalmanként 2-3 dia, diánként (cím, [(tippcím, szöveg)])
TIPS = {
 1: [
  (L('Fiók és felület', 'Account and interface'), [
    (L('Egy feladat, egy chat', 'One task, one chat'),
     L('Minden részfeladatnak nyiss külön beszélgetést, és nevezd el, például „Márkaelemzés”. A félév végén így megtalálod, és a készítés történetéhez is kell.',
       'Open a separate conversation for every sub-task and name it, for example "Brand analysis". You will find it again at the end of the semester, and you will need it for the making-of story.')),
    (L('Webes keresés bekapcsolva', 'Web search on'),
     L('Kutatás előtt kapcsold be. Nélküle az AI a saját tudásából válaszol, ami lehet elavult vagy pontatlan.',
       'Switch it on before you research. Without it the AI answers from its own knowledge, which can be outdated or inaccurate.')),
    (L('Ma derüljön ki, mit tud a fiókod', 'Find out today what your account can do'),
     L('Próbáld ki a fájlfeltöltést, a dokumentum- és a prezentációkészítést, és nézd meg, elérhető-e nálad a Claude Design és a Claude Slides. Ha valami hiányzik, szólj még ma.',
       'Try file upload, creating documents and presentations, and check whether Claude Design and Claude Slides are available to you. If something is missing, say so today.')),
    (L('Egy mappa a félévre', 'One folder for the semester'),
     L('Hozz létre egy mappát a gépeden vagy a felhőben, és ments bele mindent, ami elkészül. A chat nem archívum.',
       'Create a folder on your computer or in the cloud and save everything you produce. A chat is not an archive.')),
  ]),
  (L('Kutatás AI-jal', 'Research with AI'), [
    (L('Nyisd meg a forrásokat', 'Open the sources'),
     L('Minden linket nyiss meg. Ha nem létezik, vagy mást mond, mint amit az AI állít, töröld az állítást.',
       'Open every link. If it does not exist or says something other than what the AI claims, delete the claim.')),
    (L('Két eszköz, egy kérdés', 'Two tools, one question'),
     L('Tedd fel ugyanazt a kérdést két AI-nak is, például Claude-nak és ChatGPT-nek. Ahol eltér a válasz, ott kell utánanézned.',
       'Ask the same question to two AIs, for example Claude and ChatGPT. Where the answers differ, that is where you need to check.')),
    (L('A versenytárs saját oldala', "The competitor's own site"),
     L('Az ajánlatot, az árszintet és a hangnemet a versenytárs saját oldalán és csatornáin ellenőrizd. Az árszintet valódi árakból írd, ne becslésből.',
       "Check the offer, price level and tone of voice on the competitor's own site and channels. Base the price level on real prices, not estimates.")),
    (L('Nézd meg a saját szemeddel', 'See it with your own eyes'),
     L('A vizuális kódokról ne csak olvass: nézd meg a márka oldalát, hirdetéseit, csomagolását, és vesd össze azzal, amit az AI írt.',
       "Do not just read about the visual codes: look at the brand's site, ads and packaging, and compare them with what the AI wrote.")),
  ]),
  (L('Gondolj előre', 'Think ahead'), [
    (L('Készítési napló már ma', 'A making-of log from today'),
     L('Jegyezd fel, melyik eszközt és promptot használtad, mi lett jó, és hol tévedett az AI. A 6. alkalmon ebből meséled el, hogyan készült a deck.',
       'Note which tool and prompt you used, what worked and where the AI was wrong. In session 6 you tell the story of the deck from this.')),
    (L('A bekezdés a tiéd', 'The paragraph is yours'),
     L('Hogy mit viszel át a kiinduló márkából és mit nem, előbb írd meg magad, és csak utána kérj rá kritikát az AI-tól. Erre épül a név, az arculat és a kampány.',
       'Write what you carry over from the source brand and what you do not yourself first, and only then ask the AI to critique it. The name, the identity and the campaign build on it.')),
    (L('Reális ütemterv', 'A realistic timeline'),
     L('Az ütemtervhez add meg az AI-nak, mennyi időd van órán kívül, és kérd, hogy jelölje a szűk keresztmetszetet. Nézd meg külön az 5. alkalmat, ott sok minden összejön.',
       'For the timeline, tell the AI how much time you have outside class, and ask it to flag bottlenecks. Look at session 5 separately; a lot comes together there.')),
    (L('Ha elfogy a keret', 'If you run out of usage'),
     L('A szöveges munkát folytasd ChatGPT-ben, a Claude-ot tartsd meg a végleges kimenetre, vagy válts bármelyik másik eszközre. Hosszú chat helyett kezdj újat egy rövid összefoglalóval.',
       'Continue the text work in ChatGPT, keep Claude for the final output, or switch to any other tool. Instead of a long chat, start a new one with a short summary.')),
  ]),
 ],
 2: [
  (L('A név', 'The name'), [
    (L('Adj kritériumot', 'Give criteria'),
     L('Mondd meg, milyen legyen a név: hossz, hangzás, hangulat, és működjön-e magyarul és angolul is. Kritérium nélkül átlagos neveket kapsz.',
       'Say what the name should be like: length, sound, mood, and whether it should work in Hungarian and in English. Without criteria you get average names.')),
    (L('Kérj többet, tarts meg kevesebbet', 'Ask for more, keep fewer'),
     L('A 20 névből húzz ki 15-öt, és a maradék ötre kérj új változatokat. A második kör sokszor jobb, mint az első.',
       'Cross out 15 of the 20 names and ask for new variants of the remaining five. The second round is often better than the first.')),
    (L('Mondd ki hangosan', 'Say it out loud'),
     L('Ami leírva jó, kimondva lehet nehéz vagy félreérthető. Mondd ki, írd le, képzeld el egy plakáton.',
       'What looks good written down can be hard to say or easy to mishear. Say it, write it, picture it on a billboard.')),
    (L('Szabad-e még', 'Is it still free'),
     L('Webes kereséssel nézd meg, használja-e már valaki a kategóriában. Érdemes megnézni a domaint és a közösségi fióknevet is.',
       'Use web search to see whether anyone in the category already uses it. It is worth checking the domain and the social handle too.')),
  ]),
  (L('A márkaplatform', 'The brand platform'), [
    (L('Az ígéret egy mondat', 'The promise is one sentence'),
     L('Olyan mondat, amit a vevő elmondana a barátjának. Ha nem fér egy mondatba, még nincs kész.',
       'A sentence a customer would tell a friend. If it does not fit into one sentence, it is not finished.')),
    (L('Töröld az üres szavakat', 'Delete the empty words'),
     L('Az AI szívesen ír olyat, hogy innovatív, fenntartható, prémium. Ha egy érték bármelyik márkára igaz lehetne, cseréld le.',
       'AI likes words like innovative, sustainable, premium. If a value could be true of any brand, replace it.')),
    (L('A hangnemhez kérj példát', 'Ask for examples of the voice'),
     L('Kérd ugyanazt az üzenetet három különböző hangon, és válaszd ki, melyik a tiéd. A választott példa a briefbe is menjen bele.',
       'Ask for the same message in three different voices and choose which one is yours. Put the chosen example in the brief too.')),
    (L('Vezesd vissza a kiinduló márkára', 'Trace it back to the source brand'),
     L('Minden érték mellé írd oda, mi jön belőle a kiinduló márkából. Így látszik, hogy az új márka tényleg a kiinduló márkából nő ki.',
       'Next to every value, note what in it comes from the source brand. That shows the new brand really grows out of the source brand.')),
  ]),
  (L('Persona és árazás', 'Personas and pricing'), [
    (L('Adj életet a personának', 'Give the persona a life'),
     L('Munka, napirend, pénz, kétségek, szokások. Minél konkrétabb a leírás, annál kevésbé általános a válasza.',
       'Job, daily routine, money, doubts, habits. The more specific the description, the less generic its answers.')),
    (L('Ne a kedvedben járjon', 'It should not try to please you'),
     L('Az AI-persona hajlamos mindent jónak találni. Kérd meg, hogy legyen kritikus, és kérdezz rá arra is, mi tartaná vissza a vásárlástól.',
       'An AI persona tends to like everything. Ask it to be critical, and ask what would hold it back from buying.')),
    (L('Jelöld a kitalált választ', 'Mark the made-up answers'),
     L('Gyanús, ami túl szépen illik a márkádhoz, vagy amit egy valódi ember nem tudhatna. Ezeket jelöld meg a briefben.',
       'Be suspicious of anything that fits your brand too neatly, or that a real person could not know. Mark these in the brief.')),
    (L('Az árazás opcionális', 'Pricing is optional'),
     L('Ha fontos a márkádnál, valódi versenytársárakból indulj, és az ár legyen összhangban a pozicionálással. Ha nem fontos, hagyd ki.',
       'If it matters for your brand, start from real competitor prices and keep the price consistent with the positioning. If it does not matter, skip it.')),
  ]),
 ],
 3: [
  (L('Logó', 'Logo'), [
    (L('Előbb a gondolat', 'The idea first'),
     L('Írd le egy mondatban, mit mond a logó, és ezt add meg a promptban. Gondolat nélkül díszt kapsz, nem jelet.',
       'Write in one sentence what the logo says, and put it in the prompt. Without an idea you get decoration, not a mark.')),
    (L('Egyszerű SVG', 'Simple SVG'),
     L('Kevés forma, legfeljebb két szín. Nézd meg kicsiben, alkalmazásikon méretben, és fekete-fehérben is.',
       'Few shapes, two colours at most. Look at it small, at app icon size, and in black and white too.')),
    (L('Konkrét javítás', 'Specific corrections'),
     L('A „legyen szebb” nem utasítás. Ilyet kérj: vastagabb betű, kisebb kör, a szín #1E4BD8.',
       '"Make it nicer" is not an instruction. Ask for something like: heavier type, smaller circle, colour #1E4BD8.')),
    (L('Ne másold', 'Do not copy'),
     L('A kiinduló márka logóját és betűtípusát ne vedd át. A vizuális kódokat átviheted, de saját formában.',
       "Do not take over the source brand's logo or typeface. You can carry over visual codes, but in your own form.")),
  ]),
  (L('Képgenerálás', 'Image generation'), [
    (L('Előbb a prompt', 'Prompt first'),
     L('Az ingyenes csomagban kevés kép jut. Írd meg a promptot, kérd meg az AI-t, hogy kérdezzen rá a hiányzó részletekre, és csak utána generálj.',
       'On the free plan you get few images. Write the prompt, ask the AI to ask about the missing details, and only then generate.')),
    (L('Egy kampány, nem három kép', 'One campaign, not three images'),
     L('Ugyanaz a fény, a színvilág és a stílus minden képen. Mentsd el a jól működő promptot, és abból készüljön a következő.',
       'Same light, colours and style in every image. Save the prompt that works and build the next one from it.')),
    (L('A szöveg utólag kerül rá', 'Text goes on afterwards'),
     L('A feliratot ne a képre generáld. Utólag tedd rá a bannerben vagy a posztsablonban, így cserélhető, és nem lesz benne elírás.',
       'Do not generate the text into the image. Add it afterwards in the banner or the post template, so it can be changed and has no typos.')),
    (L('Hagyj helyet', 'Leave space'),
     L('Mondd meg a promptban, hová kerül majd a szöveg, például a jobb felső harmadba. Különben a kép tele lesz, és nem fér rá semmi.',
       'Say in the prompt where the text will go, for example the top right third. Otherwise the image is full and nothing fits.')),
  ]),
  (L('Kézikönyv, posztok, bannerek', 'Brand guide, posts, banners'), [
    (L('Egyszer rögzített színek', 'Colours fixed once'),
     L('A HEX-kódokat egyszer döntsd el, és minden promptba ugyanazokat másold be. Különben minden anyag kicsit más színű lesz.',
       'Decide the HEX codes once and paste the same ones into every prompt. Otherwise every asset ends up a slightly different colour.')),
    (L('A kézikönyv szabálykönyv', 'The guide is a rulebook'),
     L('Arról szól, hogyan kell használni a márkát. Legyen benne, mit szabad és mit nem, példákkal.',
       'It is about how the brand is used. Include what is allowed and what is not, with examples.')),
    (L('A banner kicsi', 'A banner is small'),
     L('Márkanév, ígéret, egy gomb. A 728×90-es csíkban egy sor szöveg is sok lehet, nézd meg valódi méretben.',
       'Brand name, promise, one button. In the 728×90 strip even one line of text can be too much; check it at real size.')),
    (L('Fájlt ments, ne csak linket', 'Save files, not just links'),
     L('A végleges logót, a képeket és a PDF-et töltsd le, és tedd a félév mappájába. A deckhez ezek kellenek.',
       'Download the final logo, the images and the PDF and put them in your semester folder. You need them for the deck.')),
  ]),
 ],
 4: [
  (L('Big idea és szlogen', 'Big idea and slogan'), [
    (L('Az első tíz a kézenfekvő', 'The first ten are the obvious ones'),
     L('Az első kör ötletei sokszor a legbiztonságosabbak. Kérj még tízet, merészebbet, és csak utána válassz.',
       'The first round of ideas is often the safest. Ask for ten more, bolder ones, and only then choose.')),
    (L('A big idea nem szlogen', 'The big idea is not a slogan'),
     L('Egy gondolat, amiből sok anyag születhet. Próba: el tudod-e képzelni belőle a posztot, a plakátot és a spotot is?',
       'It is a thought many assets can grow from. Test: can you picture the post, the billboard and the spot from it?')),
    (L('Ellenőrizd a szlogent', 'Check the slogan'),
     L('Mondd ki hangosan, és webes kereséssel nézd meg, nem használja-e már valaki.',
       'Say it out loud, and use web search to see whether someone already uses it.')),
    (L('Az indoklást nézd', 'Look at the reasoning'),
     L('A personás tesztnél nem a pontszám a lényeg, hanem az indoklás: abból derül ki, mit értett félre a célcsoport.',
       'In the persona test the score matters less than the reasoning: that shows what the audience misunderstood.')),
  ]),
  (L('Márkaasszisztens és szövegek', 'Brand assistant and copy'), [
    (L('Tiltás és példa is kell', 'It needs bans and examples'),
     L('A projekt utasításaiba ne csak jelzőket írj. Írd le, mit kerül a márka, és adj két-három példamondatot a hangjára.',
       'Do not write only adjectives into the project instructions. Write what the brand avoids, and give two or three example sentences in its voice.')),
    (L('Minden szöveget írj át', 'Rewrite every text'),
     L('Legalább egyszer, magad. Ha egy mondatot te nem mondanál ki, vedd ki.',
       'At least once, yourself. If you would not say a sentence, take it out.')),
    (L('Jelöld, amit nem tudsz ellenőrizni', 'Mark what you cannot verify'),
     L('Minden állítást, amit nem tudtál ellenőrizni, jelölj meg, aztán javítsd vagy töröld.',
       'Mark every claim you could not verify, then fix or delete it.')),
    (L('A spot rövid', 'The spot is short'),
     L('15 másodpercbe kevés szó fér. Képkockánként legfeljebb egy rövid mondat, a többit a kép mondja el.',
       'Few words fit into 15 seconds. At most one short sentence per frame; let the image say the rest.')),
  ]),
  (L('Médiaterv', 'Media plan'), [
    (L('A KPI szám és határidő', 'A KPI is a number and a deadline'),
     L('Nem „nagy ismertség”, hanem számszerű cél egy időponttal. Írd oda azt is, miből mérnéd.',
       'Not "high awareness" but a numeric target with a date. Also write down what you would measure it from.')),
    (L('Minden százalék mögött egy mondat', 'A sentence behind every percentage'),
     L('A büdzsé felosztásánál írd oda, miért annyi. A tenderen ezt fogják kérdezni.',
       'For the budget split, write why each share is what it is. That is what they will ask at the pitch.')),
    (L('Benchmark csak forrással', 'Benchmarks only with a source'),
     L('Az AI által írt átkattintási és konverziós arányokat ne vedd át forrás nélkül. Ha nincs forrás, írd oda, hogy becslés.',
       'Do not adopt click-through and conversion rates written by the AI without a source. If there is none, label it as an estimate.')),
    (L('Kreatív és csatorna párban', 'Creative and channel in pairs'),
     L('Minden kreatívhoz írd oda, melyik csatornán fut, és hogy paid, earned vagy owned. Ebből lesz a deck 5. blokkja.',
       'For every creative, note which channel it runs on and whether it is paid, earned or owned. This becomes block 5 of the deck.')),
  ]),
 ],
 5: [
  (L('Weboldal', 'Website'), [
    (L('Előbb terv, aztán építés', 'Plan first, then build'),
     L('Kérd meg, hogy oldalanként írja le a szekciókat, és csak a jóváhagyásod után építsen. Így kevesebb kör kell.',
       'Ask it to describe the sections per page and only build after you approve. That takes fewer rounds.')),
    (L('A tartalom tőled jön', 'The content comes from you'),
     L('A szövegeket, a színeket és a képeket te add meg a 3. és a 4. alkalom anyagaiból. Ne az AI találja ki őket újra.',
       'Give it the copy, colours and images from sessions 3 and 4. Do not let the AI reinvent them.')),
    (L('Egyszerre egy javítás', 'One fix at a time'),
     L('Mondd meg, mit változtasson, és azt is, mi maradjon változatlan. Ha sok javítást kérsz egyszerre, gyakran mást is elront.',
       'Say what to change and also what must stay the same. If you ask for many fixes at once, it often breaks something else.')),
    (L('Nézd meg mobilon', 'Check it on mobile'),
     L('Nyisd meg a telefonodon is, vagy szűkítsd a böngészőablakot. A menü, a gombok és a betűméret ott derül ki.',
       'Open it on your phone too, or narrow the browser window. That is where the menu, the buttons and the type size show.')),
  ]),
  (L('Spot és kulcsszavak', 'Spot and keywords'), [
    (L('Jelenetenként add meg', 'Give it scene by scene'),
     L('A forgatókönyvet jelenetenként írd le: mit látunk, mit olvasunk, és meddig. Az időzítést másodpercben kérd.',
       'Describe the script scene by scene: what we see, what we read, and for how long. Ask for the timing in seconds.')),
    (L('Nézd végig háromszor', 'Watch it three times'),
     L('Egyszer egészben, egyszer csak a szöveget, egyszer csak az időzítést figyelve. Ehhez kell az újrajátszás gomb.',
       'Once as a whole, once just for the text, once just for the timing. That is what the replay button is for.')),
    (L('Keresési számokban ne bízz', 'Do not trust search volumes'),
     L('Az AI által írt keresési számok nem valódi adatok. Írd be a kulcsszót a keresőbe, és nézd meg, milyen oldalakat hoz fel.',
       'Search volumes written by AI are not real data. Type the keyword into the search engine and see which pages come up.')),
    (L('Egy oldal, egy fő kulcsszó', 'One page, one main keyword'),
     L('A fő kulcsszó szerepeljen az oldal címében és a meta leírásában, természetes mondatban.',
       'The main keyword should appear in the page title and the meta description, in a natural sentence.')),
  ]),
  (L('A tenderdeck', 'The pitch deck'), [
    (L('Egy dia, egy gondolat', 'One slide, one thought'),
     L('A dia címe maga az állítás, ne egyetlen szó. Ha a címekből összeáll a történet, jó a deck.',
       'The slide title is the claim itself, not a single word. If the titles alone tell the story, the deck works.')),
    (L('Válogass', 'Curate'),
     L('Nem kell minden eredménytermék a deckbe. Ami nem segít megnyerni a tendert, maradjon a háttéranyagban.',
       'Not every output needs to be in the deck. What does not help win the pitch stays in the background materials.')),
    (L('A próba a decket javítja', 'The rehearsal fixes the deck'),
     L('Ha az AI-marketingigazgató kérdésére nincs jó válaszod, valami hiányzik a deckből. Ott javíts.',
       "If you have no good answer to the AI marketing director's question, something is missing from the deck. Fix it there.")),
    (L('Mérd le az időt', 'Time it'),
     L('Hangosan, órával, a készítés történetével együtt: 15-20 perc.',
       'Out loud, with a clock, including the making-of story: 15-20 minutes.')),
  ]),
 ],
 6: [
  (L('A készítés története', 'The making-of story'), [
    (L('Történet, nem eszközlista', 'A story, not a tool list'),
     L('Mi volt a cél, mit próbáltál, mi nem működött, és mit csináltál helyette. Az eszközök diája ezt csak alátámasztja.',
       'What the goal was, what you tried, what did not work and what you did instead. The tools slide only supports this.')),
    (L('Mutass egy példát', 'Show an example'),
     L('Tegyél egymás mellé egy rossz AI-választ és a javított változatot. Ez többet mond, mint bármilyen összefoglaló.',
       'Put a bad AI answer next to the corrected version. It says more than any summary.')),
    (L('Mondd el, mi idegesített', 'Say what annoyed you'),
     L('Az elakadásokból tanul a legtöbbet mindenki. Mondd el azt is, hogyan jutottál túl rajtuk.',
       'Everyone learns most from the dead ends. Also tell how you got past them.')),
    (L('A naplóból dolgozz', 'Work from your log'),
     L('A készítési naplód a forrásod. Ne emlékezetből rakd össze a történetet.',
       'Your making-of log is your source. Do not reconstruct the story from memory.')),
  ]),
  (L('A bemutató', 'The presentation'), [
    (L('Ügyfélnek beszélsz', 'You are talking to a client'),
     L('Az elején a tender: mi a probléma, mi a megoldás, miért nyer ez a kampány. A készítés története utána jön.',
       'The pitch comes first: what the problem is, what the solution is, why this campaign wins. The making-of story comes after.')),
    (L('Ne olvasd fel a diát', 'Do not read the slide'),
     L('Ami a dián van, azt nem kell elmondani. Azt mondd el, ami mögötte van.',
       'What is on the slide does not need saying. Say what is behind it.')),
    (L('Legyen B terved', 'Have a plan B'),
     L('A decket vidd PDF-ben is, és a prototípusok linkjeit tartsd egy helyen. Ha a gép vagy a net elakad, onnan folytatod.',
       'Bring the deck as a PDF too, and keep the prototype links in one place. If the computer or the network fails, you carry on from there.')),
    (L('Tartsd az időt', 'Keep to time'),
     L('15-20 perc. Gyakorold le egyszer hangosan, órával, és tudd előre, melyik diát hagyod ki, ha kifutsz az időből.',
       '15-20 minutes. Practise once out loud with a clock, and know in advance which slide you skip if you run out of time.')),
  ]),
 ],
}

# Innen → Ide a címlapon (2-6.)
FROMTO = {
  2: (L('Ismered a kiinduló márkát és a versenytársakat.', 'You know the source brand and the competitors.'),
      L('Van neve a márkádnak, tudod, mit ígér, kinek és milyen hangon.', 'Your brand has a name, and you know what it promises, to whom, and in what voice.'),
      L('Ez a deck 1-2. blokkjának alapja.', 'This is the basis of blocks 1-2 of the deck.')),
  3: (L('Van neve, ígérete és hangja a márkádnak.', 'Your brand has a name, a promise and a voice.'),
      L('A márkádnak arca van: logó, színek, betűk, képi világ, és néhány kész vizuál a kampányhoz.', 'Your brand has a face: logo, colours, type, imagery, and a few finished visuals for the campaign.'),
      L('Hogy ebből mennyi készül el órán és mennyi otthon, a te döntésed.', 'How much of this gets done in class and how much at home is your call.')),
  4: (L('A márkádnak van arca és vannak kész vizuáljai.', 'Your brand has a face and finished visuals.'),
      L('Megvan a kampány nagy ötlete és szlogenje, és az összes szöveg, ami a kampányeszközökhöz kell.', "You have the campaign's big idea and slogan, and all the copy the campaign assets need."),
      L('Ez a deck 3. és 5. blokkja.', 'This is blocks 3 and 5 of the deck.')),
  5: (L('Megvan a kampány ötlete, szlogenje és minden szövege.', "You have the campaign's idea, slogan and all its copy."),
      L('Minden kampányeszköz megvan prototípusként, és áll a tenderdeck vázlata.', 'Every campaign asset exists as a prototype, and the outline of the pitch deck stands.'),
      L('Ez a deck 4. blokkja és maga a deck.', 'This is block 4 of the deck and the deck itself.')),
  6: (L('Áll a tenderdeck vázlata és minden prototípus.', 'The pitch deck outline and every prototype are in place.'),
      L('Kész deck, megtartott bemutató.', 'Finished deck, presentation delivered.'),
      L('Bemutató mindenki előtt, 15-20 perc: a tenderdeck és a készítés története.', 'Presentation in front of everyone, 15-20 minutes: the pitch deck and the making-of story.')),
}

PAIRS = [('Coca-Cola', L('autó', 'car')), ('IKEA', L('légitársaság', 'airline')), ('LEGO', L('bank', 'bank')),
         ('Apple', L('szállodalánc', 'hotel chain')), ('Nike', L('kávézólánc', 'café chain')), ('Red Bull', L('biztosító', 'insurance company')),
         ('Netflix', L('fitneszterem-lánc', 'gym chain')), ('Patagonia', L('mobilszolgáltató', 'mobile carrier')), ('Spotify', L('étteremhálózat', 'restaurant chain')),
         ('Tesla', L('divatruha-márka', 'fashion brand')), ('Duolingo', L('utazási iroda', 'travel agency')), ('Harley-Davidson', L('kozmetikai márka', 'cosmetics brand')),
         ('Disney', L('háztartási elektronika', 'home electronics')), ("McDonald's", L('wellness- és spa-lánc', 'wellness and spa chain')), ('Ferrari', L('payment', 'payment'))]

BLOCKS = [
  (L('Bevezetés', 'Introduction'), L('Címlap névvel, logóval és szlogennel. A probléma, amit a márka megold. A megoldás és az egyedi értékajánlat.', 'Title slide with name, logo and tagline. The problem the brand solves. The solution and the unique value proposition.')),
  (L('Stratégia', 'Strategy'), L('Célcsoport és 2 persona. Hol áll a márka a versenytársakhoz képest. Márkaszemélyiség, hangnem, arculat.', 'Target audience and 2 personas. Where the brand stands against competitors. Brand personality, tone of voice, identity.')),
  (L('Kampánykoncepció', 'Campaign concept'), L('A nagy ötlet és a kampányszlogen. A bevezetés három fázisa: teaser, launch, sustain.', 'The big idea and the campaign slogan. The three launch phases: teaser, launch, sustain.')),
  (L('Kreatív bemutató', 'Creative showcase'), L('Kulcsvizuálok, posztok, bannerek, plakát, csomagolás, weboldal-prototípus, videóspot, hírlevél.', 'Key visuals, posts, banners, billboard, packaging, website prototype, video spot, newsletter.')),
  (L('Csatornák', 'Channels'), L('Melyik kreatív melyik csatornán fut: paid, earned, owned.', 'Which creative runs on which channel: paid, earned, owned.')),
]

RULES = [
  (L('Szerepkör', 'Role'), L('Kinek a fejével gondolkodjon. „Te egy tapasztalt márkastratéga vagy egy ügynökségnél.”', 'Whose head it should think with. "You are an experienced brand strategist at an agency."')),
  (L('Kontextus', 'Context'), L('Amit tudnia kell. Másold be vagy töltsd fel az eddigi anyagaidat.', 'What it needs to know. Paste in or upload your materials so far.')),
  (L('Feladat', 'Task'), L('Egy mondatban, mit kell csinálnia. Egy prompt, egy feladat.', 'In one sentence, what it has to do. One prompt, one task.')),
  (L('Scope', 'Scope'), L('Mi tartozik bele és mi nem.', 'What is in and what is out.')),
  (L('Elvárt kimenet', 'Expected output'), L('Táblázat, lista, egy oldal, HTML, SVG.', 'Table, list, one page, HTML, SVG.')),
  (L('Paraméterek', 'Parameters'), L('Darabszám, hossz, hangnem, nyelv, célközönség, stílus. Képnél képarány, fény, színek HEX-kóddal.', 'Quantity, length, tone, language, audience, style. For images aspect ratio, light, colours with HEX codes.')),
  (L('Kritériumok', 'Criteria'), L('Mi alapján jó az eredmény, mit kerüljön.', 'What makes the result good, what it should avoid.')),
  (L('Példa', 'Example'), L('Ha van mintád, add meg.', 'If you have a sample, give it.')),
  (L('Kérdezzen', 'Let it ask'), L('A végére: „Ha valami hiányzik, előbb kérdezz.”', 'At the end: "If anything is missing, ask first."')),
]

ROLES = L(['Kampánystratéga', 'Médiatervező', 'Szövegíró', 'Art director', 'Grafikus', 'Programozó'],
          ['Campaign strategist', 'Media planner', 'Copywriter', 'Art director', 'Graphic designer', 'Developer'])

# (mire, ajánlott eszköz, más eszközzel is)
TOOLTABLE = [
  (L('Kutatás forrásokkal', 'Research with sources'), L('Claude, bekapcsolt webes kereséssel', 'Claude, with web search switched on'),
   L('ChatGPT vagy Gemini, szintén webes kereséssel; Perplexity', 'ChatGPT or Gemini, also with web search; Perplexity')),
  (L('Ötletelés, sok szöveges kör', 'Ideation, many text rounds'), L('ChatGPT', 'ChatGPT'),
   L('Claude, Gemini', 'Claude, Gemini')),
  (L('Képek, plakát, csomagolás', 'Images, billboard, packaging'), L('ChatGPT képgenerálás (az ingyenes csomagban korlátozott)', 'ChatGPT image generation (limited on the free plan)'),
   L('Gemini, Midjourney, Canva', 'Gemini, Midjourney, Canva')),
  (L('Arculati kézikönyv, posztsablonok', 'Brand guide, post templates'), L('Claude Design', 'Claude Design'),
   L('Canva, Figma', 'Canva, Figma')),
  (L('Weboldal, bannerek, videóspot, hírlevél', 'Website, banners, video spot, newsletter'), L('Claude artifact', 'Claude artifact'),
   L('ChatGPT canvas, Gemini; a kész HTML bárhol megnyitható', 'ChatGPT canvas, Gemini; the finished HTML opens anywhere')),
  (L('Márkaasszisztens', 'Brand assistant'), L('Claude-projekt', 'Claude project'),
   L('ChatGPT-projekt vagy egyéni GPT, Gemini Gem', 'ChatGPT project or a custom GPT, Gemini Gem')),
  (L('Tenderdeck', 'Pitch deck'), L('Claude Slides', 'Claude Slides'),
   L('Canva, Google Slides, PowerPoint', 'Canva, Google Slides, PowerPoint')),
]

# A mai feladat részfeladatokra bontva: (részfeladat, leírás, eredménytermék, hová kerül a deckben)
# diánként csoportosítva: {alkalom: [(diacím-kiegészítés vagy None, [sorok])]}
def R(t, d, o, k):
    return (t, d, o, k)
B1 = L('1. blokk · Bevezetés', 'Block 1 · Introduction')
B2 = L('2. blokk · Stratégia', 'Block 2 · Strategy')
B3 = L('3. blokk · Kampánykoncepció', 'Block 3 · Campaign concept')
B4 = L('4. blokk · Kreatív bemutató', 'Block 4 · Creative showcase')
B5 = L('5. blokk · Csatornák', 'Block 5 · Channels')
NODECK = L('Nem kerül a deckbe', 'Not in the deck')
SUB = {
 1: [(None, [
   R(L('Fiók és felület', 'Account and interface'), L('Lépj be vagy regisztrálj (Claude, ChatGPT vagy bármi más), és próbáld ki, mit tud: webes keresés, fájlfeltöltés, dokumentum, prezentáció.', 'Log in or register (Claude, ChatGPT or anything else) and try what it can do: web search, file upload, documents, presentations.'),
     L('Működő fiók', 'A working account'), L('A készítés történetéhez', 'For the making-of story')),
   R(L('Márkaválasztás', 'Choosing a brand'), L('Válassz egy márkát a listából. Mindenkinek más jut.', 'Choose a brand from the list. Everyone gets a different one.'),
     L('A márkád és az új kategória', 'Your brand and the new category'), L('Az egész deck kiindulópontja', 'The starting point of the whole deck')),
   R(L('Féléves terv', 'Semester plan'), L('Az AI-jal nézd át az órarendet, a deck öt blokkját és az eredménytermékeket, és kérj tőle ütemtervet.', 'Go through the schedule, the five blocks of the deck and the outputs with the AI, and ask it for a timeline.'),
     L('Féléves ütemterv', 'Semester timeline'), L('Nem kerül a deckbe, ez a térképed', 'Not in the deck; it is your map')),
  ]), (None, [
   R(L('Márkaelemzés', 'Brand analysis'), L('Webes kereséssel: értékek, személyiség, hangnem, vizuális kódok, ikonikus kampányok. Nyisd meg a forrásokat.', 'With web search: values, personality, tone of voice, visual codes, iconic campaigns. Open the sources.'),
     L('Márkaelemzés forrásokkal', 'Brand analysis with sources'), B2),
   R(L('Versenytársak', 'Competitors'), L('5 valódi versenytárs az új kategóriában: ajánlat, árszint, hangnem, fő csatornák.', '5 real competitors in the new category: offer, price level, tone of voice, main channels.'),
     L('Versenytárstáblázat forráslinkekkel', 'Competitor table with source links'), B2),
   R(L('Mit viszel át', 'What you carry over'), L('Egy bekezdés arról, mit viszel át a kiinduló márkából, és mit nem.', 'One paragraph on what you carry over from the source brand and what you do not.'),
     L('Egy bekezdés', 'One paragraph'), L('Az 1. és 2. blokk alapja', 'The basis of blocks 1 and 2')),
  ])],
 2: [(None, [
   R(L('Név', 'Name'), L('20 névötlet AI-jal, egyet választasz, és webes kereséssel megnézed, használja-e már valaki a kategóriában.', '20 name ideas with AI; you choose one and check with web search whether anyone in the category already uses it.'),
     L('A márka neve, ellenőrizve', 'The brand name, checked'), L('1. blokk · Bevezetés (címlap)', 'Block 1 · Introduction (title slide)')),
   R(L('Márkaplatform', 'Brand platform'), L('Pozicionálás, ígéret, 3 érték, személyiség, hangnem.', 'Positioning, promise, 3 values, personality, tone of voice.'),
     L('Márkaplatform', 'Brand platform'), L('1. blokk (megoldás, értékajánlat) · 2. blokk (személyiség, hangnem)', 'Block 1 (solution, value proposition) · Block 2 (personality, tone)')),
   R(L('Personák', 'Personas'), L('Legalább 2 persona AI-jal. Mindkettőt kérdezd ki 5 kérdéssel, és jelöld, mit gondolsz kitaláltnak.', 'At least 2 personas with AI. Interview each with 5 questions and mark what you think is made up.'),
     L('2 persona, interjúval', '2 personas, with interviews'), L('2. blokk · Stratégia (célcsoport)', 'Block 2 · Strategy (target audience)')),
   R(L('Árazás · opcionális', 'Pricing · optional'), L('Ha fontos a márkádnál, vázolj árazási irányt, és vesd össze a versenytársakkal. Ha nem, hagyd ki.', 'If it matters for your brand, sketch a pricing direction and compare it with the competitors. If not, skip it.'),
     L('Árazási irány', 'Pricing direction'), B2),
  ])],
 3: [(None, [
   R(L('Vizuális irány', 'Visual direction'), L('Mit veszel át a kiinduló márka vizuális kódjaiból, mit nem, és 3 vizuális kulcsszó.', "What you take from the source brand's visual codes, what you do not, and 3 visual keywords."),
     L('Vizuális irány', 'Visual direction'), L('2. blokk · Stratégia (arculat)', 'Block 2 · Strategy (identity)')),
   R(L('Logó', 'Logo'), L('3 logóirány SVG-ben, egyet választasz és finomítasz. A kiinduló márka logóját ne másold.', "3 logo directions in SVG; you pick one and refine it. Do not copy the source brand's logo."),
     L('Logó SVG', 'Logo SVG'), L('1. blokk (címlap) · 2. blokk (arculat)', 'Block 1 (title slide) · Block 2 (identity)')),
   R(L('Arculati kézikönyv', 'Brand guide'), L('Logó és használata, színek HEX-kóddal, betűk, képi stílus, egy mintaposzt. Claude Designban, vagy artifactként és PDF-be mentve.', 'Logo and its use, colours with HEX codes, type, image style, one sample post. In Claude Design, or as an artifact saved as PDF.'),
     L('Kézikönyv PDF', 'Brand guide PDF'), L('2. blokk · Stratégia (arculat)', 'Block 2 · Strategy (identity)')),
   R(L('Kulcsvizuálok', 'Key visuals'), L('3 kulcsvizuál, egy közülük a kampány fő képe. Generálás előtt csiszold a promptot.', "3 key visuals, one of them the campaign's main image. Polish the prompt before you generate."),
     L('3 kulcsvizuál', '3 key visuals'), B4),
  ]), (None, [
   R(L('Posztsablonok', 'Post templates'), L('Négyzetes poszt, 9:16-os story és carousel nyitódia az arculattal.', 'Square post, 9:16 story and carousel opening slide with the identity.'),
     L('3 posztsablon', '3 post templates'), B4),
   R(L('Bannerek és plakát', 'Banners and billboard'), L('300×250 és 728×90 pixeles HTML-banner a fő kulcsvizuállal, plusz óriásplakát-mockup. A szlogent az 5. alkalomon cseréled be.', '300×250 and 728×90 pixel HTML banners with the main key visual, plus a billboard mock-up. You swap in the slogan in session 5.'),
     L('2 banner, plakát-mockup', '2 banners, billboard mock-up'), B4),
   R(L('Csomagolás vagy termék', 'Packaging or product'), L('Látvány a kategóriád szerint, például az autó, a kozmetikum doboza vagy a kávéspohár.', 'A visual according to your category, for example the car, the cosmetics box or the coffee cup.'),
     L('Csomagolás- vagy terméklátvány', 'Packaging or product visual'), B4),
  ])],
 4: [(None, [
   R(L('Kampánybrief', 'Campaign brief'), L('Cél, célcsoport, fő üzenet, csatornák, időtáv, sikermérők.', 'Objective, target audience, key message, channels, timeframe, success metrics.'),
     L('Kampánybrief', 'Campaign brief'), L('A 3. blokk alapja', 'The basis of block 3')),
   R(L('Márkaasszisztens', 'Brand assistant'), L('Claude-projekt a márkabrieffel és a personákkal, a hangnem a projekt utasításaiban. A további szövegeket ebben írod.', 'A Claude project with the brand brief and the personas, the tone of voice in the project instructions. You write all further copy in it.'),
     L('Márkaasszisztens', 'Brand assistant'), L('A készítés történetéhez', 'For the making-of story')),
   R(L('Big idea és szlogen', 'Big idea and slogan'), L('10 kampányötlet, egy kiválasztva, hozzá 20 szlogen, 3 kiválasztva és tesztelve a personákon.', '10 campaign ideas, one chosen, 20 slogans for it, 3 shortlisted and tested on the personas.'),
     L('Nagy ötlet és szlogen', 'Big idea and slogan'), B3),
   R(L('Kreatív koncepció', 'Creative concept'), L('A koncepció egy oldalban.', 'The concept on one page.'),
     L('Egyoldalas koncepció', 'One-page concept'), B3),
   R(L('Szövegek', 'Copy'), L('Weboldal oldalanként, 5 poszt, 1 hírlevél, 15 másodperces spot forgatókönyve. Szerkeszd át, és ami nem ellenőrizhető, javítsd vagy töröld.', 'Website page by page, 5 posts, 1 newsletter, a 15-second spot script. Edit it, and fix or delete what cannot be verified.'),
     L('Szövegcsomag', 'Copy deck'), B4),
  ]), (None, [
   R(L('Bevezetési és médiaterv', 'Launch and media plan'), L('Teaser, launch, sustain; paid, earned, owned; Gantt-diagram; a büdzsé százalékban; KPI-ok számszerű céllal.', 'Teaser, launch, sustain; paid, earned, owned; Gantt chart; budget in percentages; KPIs with numeric targets.'),
     L('Bevezetési és médiaterv', 'Launch and media plan'), L('3. blokk (fázisok) · 5. blokk (csatornák)', 'Block 3 (phases) · Block 5 (channels)')),
   R(L('5 poszt', '5 posts'), L('A 3. alkalom sablonjai és kulcsvizuáljai a mai szövegekkel, platformmal és formátummal.', "Session 3's templates and key visuals with today's copy, with platform and format."),
     L('5 kész poszt', '5 finished posts'), B4),
   R(L('HTML hírlevél', 'HTML newsletter'), L('A hírlevélszövegből arculatos e-mail sablon, Claude-dal.', 'An on-brand email template from the newsletter copy, with Claude.'),
     L('HTML hírlevél', 'HTML newsletter'), B4),
   R(L('Előrejelzés · opcionális', 'Forecast · optional'), L('12 havi minta adatsor, elemzés, előrejelzés 3 hónapra, és 3 ok, amiért tévedhet.', 'A 12-month sample dataset, analysis, a 3-month forecast, and 3 reasons why it may be wrong.'),
     L('Előrejelzés', 'Forecast'), L('Háttéranyag', 'Background material')),
  ])],
 5: [(L('Első blokk: megvalósítás', 'First block: production'), [
   R(L('Kulcsszavak', 'Keywords'), L('40 kulcsszó keresési szándék szerint, 3 versenytárs oldalának vizsgálata, oldalanként egy fő kulcsszó. Az AI keresési számaiban ne bízz.', '40 keywords by search intent, a look at 3 competitor sites, one main keyword per page. Do not trust search volumes written by AI.'),
     L('Kulcsszólista', 'Keyword list'), L('A weboldalba épül', 'Goes into the website')),
   R(L('Weboldal', 'Website'), L('HTML-prototípus legalább 4 oldallal: főoldal, termék, árak, rólunk és kapcsolat. Arculat, szövegek, képek, meta adatok, mobilon is.', 'HTML prototype with at least 4 pages: home, product, prices, about and contact. Identity, copy, images, meta data, works on mobile.'),
     L('Weboldal link', 'Website link'), B4),
   R(L('Animált spot', 'Animated spot'), L('A forgatókönyvből 15 másodperces animált HTML-spot, ami a böngészőben lejátszható.', 'A 15-second animated HTML spot from the script that plays in the browser.'),
     L('Spot link', 'Spot link'), B4),
   R(L('Szlogen a bannereken', 'Slogan on the banners'), L('A bannereken cseréld be a kampányszlogent.', 'Swap the campaign slogan into the banners.'),
     L('Végleges bannerek', 'Final banners'), B4),
  ]), (L('Második blokk: tenderdeck', 'Second block: pitch deck'), [
   R(L('Tenderdeck', 'Pitch deck'), L('A deck Claude Slidesban a 15-20 diás szerkezet szerint. Ha nem érhető el, PPTX fájlként.', 'The deck in Claude Slides along the 15-20 slide structure. If it is not available, as a PPTX file.'),
     L('A tenderdeck vázlata', 'Pitch deck outline'), L('Maga a deck', 'The deck itself')),
   R(L('Próba AI-jal', 'Rehearsal with AI'), L('Az AI az ügyfél marketingigazgatója: 5 kemény kérdés, a válaszaid, és időmérés a készítés történetével együtt.', "The AI is the client's marketing director: 5 tough questions, your answers, and timing including the making-of story."),
     L('Javított deck, lemért idő', 'Improved deck, timed'), L('Maga a deck', 'The deck itself')),
  ])],
 6: [(None, [
   R(L('Utolsó simítások', 'Final touches'), L('30 perc: javítás az előző napi prezentációs óra alapján, export PPTX-be vagy PDF-be.', "30 minutes: improvements based on the previous day's presentation class, export to PPTX or PDF."),
     L('Végleges deck', 'Final deck'), L('Maga a deck', 'The deck itself')),
   R(L('A készítés története', 'The making-of story'), L('Eszközök és mire, mi ment jól, hol akadt el az AI és hogyan oldottad meg, mi idegesített, mit csinálnál máshogy.', 'Tools and what for, what went well, where the AI got stuck and how you solved it, what annoyed you, what you would do differently.'),
     L('3-5 dia', '3-5 slides'), L('A deck végén', 'At the end of the deck')),
   R(L('Bemutató', 'Presentation'), L('Mindenki előtt, 15-20 perc: a tenderdeck és a készítés története, utána kérdések.', 'In front of everyone, 15-20 minutes: the pitch deck and the making-of story, then questions.'),
     L('Megtartott bemutató', 'Presentation delivered'), L('Az egész deck', 'The whole deck')),
   R(L('Visszajelzés', 'Feedback'), L('Közös visszajelzés a végén.', 'Joint feedback at the end.'),
     L('Visszajelzés', 'Feedback'), L('-', '-')),
  ])],
}

# a 4. alkalom kilenc részfeladata három diára
_r4 = SUB[4][0][1] + SUB[4][1][1]
SUB[4] = [(None, _r4[0:3]), (None, _r4[3:6]), (None, _r4[6:9])]
