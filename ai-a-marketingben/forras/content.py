# -*- coding: utf-8 -*-
# AI a marketingben, 2026 ősz, gyakorlat: a deckek tartalma, magyarul és angolul.
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
CB_HU = json.load(open(os.path.join(HERE, 'codeblocks_hu.json')))
CB_EN = json.load(open(os.path.join(HERE, 'codeblocks_en.json')))

VER_HU = 'v1.4 · 2026. november 11.'
VER_EN = 'v1.4 · 11 November 2026'

# Eddig az alkalomig kattinthatók a linkek a kezdőlapon és a felső sávban.
# A többi alkalom szürke és nem nyitható. Hétről hétre ezt a számot emeljük.
NYITVA = 2

# Ha egy fájl frissebb a többinél, itt kap saját verziót: kulcs 1-6 a diasorokhoz, 'index' a kezdőlaphoz.
VER_KIVETEL = {1: ('v1.7 · 2026. november 11.', 'v1.7 · 11 November 2026'), 2: ('v2.2 · 2026. november 11.', 'v2.2 · 11 November 2026'), 'index': ('v1.5 · 2026. november 11.', 'v1.5 · 11 November 2026')}


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
       out=L('Márkabrief: platform, personák', 'Brand brief: platform, personas')),
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
  2: L('Építsd fel a márka alapjait az új iparágban.', 'Build the foundations of the brand in its new industry.'),
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
  2: L('Márkabrief (platform, personák).', 'Brand brief (platform, personas).'),
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
     L('Hogy mit viszel át a kiinduló márkából és mit nem, előbb írd meg magad, és csak utána kérj rá kritikát az AI-tól. Erre épül a márkaplatform, az arculat és a kampány.',
       'Write what you carry over from the source brand and what you do not yourself first, and only then ask the AI to critique it. The brand platform, the identity and the campaign build on it.')),
    (L('Reális ütemterv', 'A realistic timeline'),
     L('Az ütemtervhez add meg az AI-nak, mennyi időd van órán kívül, és kérd, hogy jelölje a szűk keresztmetszetet. Nézd meg külön az 5. alkalmat, ott sok minden összejön.',
       'For the timeline, tell the AI how much time you have outside class, and ask it to flag bottlenecks. Look at session 5 separately; a lot comes together there.')),
    (L('Ha elfogy a keret', 'If you run out of usage'),
     L('A szöveges munkát folytasd ChatGPT-ben, a Claude-ot tartsd meg a végleges kimenetre, vagy válts bármelyik másik eszközre. Hosszú chat helyett kezdj újat egy rövid összefoglalóval.',
       'Continue the text work in ChatGPT, keep Claude for the final output, or switch to any other tool. Instead of a long chat, start a new one with a short summary.')),
  ]),
 ],
 2: [
  (L('Mi marad, mi új', 'What stays, what is new'), [
    (L('Ami marad', 'What stays'),
     L('A név, a logó, a személyiség és az értékek. Ezekhez nem nyúlsz, ezekből dolgozol.',
       'The name, the logo, the personality and the values. You do not touch these; you work from them.')),
    (L('Ami új', 'What is new'),
     L('A termék vagy szolgáltatás, a célcsoport, az ár és a kampány. Itt van minden döntés.',
       'The product or service, the audience, the price and the campaign. Every decision is here.')),
    (L('Mit tenne a márka?', 'What would the brand do?'),
     L('Minden döntésnél kérdezd meg: ha az IKEA tényleg légitársaság lenne, ezt csinálná?',
       'For every decision, ask: if IKEA really were an airline, would it do this?')),
    (L('Nem a logón múlik', 'It does not depend on the logo'),
     L('A név és a logó adott. Az számít, hogy a márka viselkedése átjön-e az új iparágban.',
       "The name and logo are given. What matters is whether the brand's behaviour comes through in the new industry.")),
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
    (L('Vezesd vissza a márkára', 'Trace it back to the brand'),
     L('Minden érték mellé írd oda, hol látszik ma a valódi márkán. Így hihető, hogy az új iparágban is ugyanaz a márka.',
       'Next to every value, note where it shows in the real brand today. That makes it believable that it is the same brand in the new industry.')),
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


# ======================================================================
# 2. alkalom, 2026. november 11-i átdolgozás: kis feladatok, mindegyik előtt rövid elmélet és kitalált példa.
# Oktatói kérés: az 1. alkalmon nem nagyon értettek, ezért apróbb lépések kellenek, több promptjavaslattal.
# A diák sorrendje: S2_SLIDES. Elem típusa: ('agenda',) | ('th', kulcs) | ('task', szám)
# ======================================================================

EXAMPLE = L('Mi lenne, ha a Rubik-kocka cipőmárka lenne?', "What if the Rubik's Cube were a shoe brand?")

S2_TASKS = {1: {'t': {'hu': 'Bemelegítés: a márkád egy mondatban', 'en': 'Warm-up: your brand in one sentence'},
     'm': 10,
     'what': {'hu': 'Mondd ki a feladatodat egy mondatban: „Mi lenne, ha a [márka] [új kategória] lenne?” Írj mellé 5 jelzőt a márkáról az 1. alkalom elemzéséből, és jelöld, melyik három a '
                    'legfontosabb az új iparágban.',
              'en': 'Say your task in one sentence: "What if [brand] were a [new category]?" Add 5 adjectives describing the brand from your session 1 analysis, and mark the three that matter most '
                    'in the new industry.'},
     'out': {'hu': '1 mondat és 5 jelző, ebből 3 jelölve', 'en': '1 sentence and 5 adjectives, 3 of them marked'},
     'ex': {'hu': 'Mi lenne, ha a Rubik-kocka cipőmárka lenne? Okos, játékos, színes, makacs, ikonikus. A cipőnél a legfontosabb: játékos, színes, okos.',
            'en': "What if the Rubik's Cube were a shoe brand? Clever, playful, colourful, stubborn, iconic. For shoes the most important: playful, colourful, clever."},
     'p': {'hu': 'Az előző órán elemeztem a [márka] márkát, itt az elemzésem: [bemásolva vagy feltöltve]. Órai játékban azt találjuk ki, milyen lenne, ha a [márka] a nevével és a logójával együtt '
                 '[új kategória] lenne. Foglald össze 5 jelzőben, milyen ez a márka, ha ember lenne. Utána mondd meg, melyik 3 jelző a legfontosabb az új iparágban, és miért, egy-egy mondatban. Ha '
                 'az elemzésem hiányos, mondd meg, mi hiányzik belőle.',
           'en': 'Last class I analysed the [brand] brand; here is my analysis: [pasted or uploaded]. In a classroom game we work out what it would be like if [brand], name and logo included, were a '
                 '[new category]. Sum up in 5 adjectives what this brand would be like as a person. Then tell me which 3 adjectives matter most in the new industry, and why, in one sentence each. If '
                 'my analysis is incomplete, tell me what is missing.'}},
 2: {'t': {'hu': 'Pozicionálás', 'en': 'Positioning'},
     'm': 15,
     'what': {'hu': 'Töltsd ki a képletet a saját márkáddal. Kérj 3 változatot, és a versenytárstáblázatod alapján válaszd ki, melyik különbözik a legjobban.',
              'en': 'Fill in the formula with your own brand. Ask for 3 variants, and use your competitor table to choose the one that stands out most.'},
     'out': {'hu': '1 pozicionáló mondat', 'en': '1 positioning sentence'},
     'p': {'hu': 'Itt a versenytárstáblázatom az első óráról: [bemásolva]. A márkám: [márka] mint [új kategória]. Órai játék: a valódi márka egy elképzelt iparágban, a neve és a logója marad. Írj 3 '
                 'különböző pozicionáló mondatot ezzel a képlettel: [kinek], akik [mire vágynak], a [márka] az a [kategória], amely [miben más], mert [miért hihető]. Mindegyik mellé írd oda, melyik '
                 'versenytárstól különbözteti meg a legjobban, és ha valamelyik bármelyik versenytársra igaz lehetne, jelezd.',
           'en': 'Here is my competitor table from the first class: [pasted]. My brand: [brand] as a [new category]. A classroom game: the real brand in an imagined industry; its name and logo stay. '
                 'Write 3 different positioning sentences with this formula: for [whom], who [want what], [brand] is the [category] that [how it is different], because [why it is believable]. Next '
                 'to each, note which competitor it sets the brand apart from most, and flag any that could be true of any competitor.'}},
 3: {'t': {'hu': 'Ígéret és 3 érték', 'en': 'Promise and 3 values'},
     'm': 15,
     'what': {'hu': 'Írd meg az ígéretet egy mondatban, és a 3 értéket, mindegyiket egy mondattal arról, mit jelent a gyakorlatban.',
              'en': 'Write the promise in one sentence and the 3 values, each with one sentence on what it means in practice.'},
     'out': {'hu': '1 ígéret és 3 érték', 'en': '1 promise and 3 values'},
     'p': {'hu': 'A márkám: [márka] mint [új kategória], a pozicionálása: [mondat]. Javasolj 5 lehetséges ígéretet, mindegyik legyen egy rövid mondat, amit egy vevő a barátjának is elmondana. Utána '
                 'javasolj 6 értéket, és mindegyikhez írd oda, mit jelent a gyakorlatban, és hogyan illik a [márka] márkához. Húzd ki azokat, amelyek bármelyik márkára igazak lehetnének. A végső '
                 'hármat én választom ki.',
           'en': 'My brand: [brand] as a [new category], its positioning: [sentence]. Suggest 5 possible promises, each a short sentence a customer would tell a friend. Then suggest 6 values, and '
                 'for each note what it means in practice and how it fits [brand]. Cross out any that could be true of any brand. I will choose the final three.'}},
 4: {'t': {'hu': 'Személyiség és hangnem', 'en': 'Personality and tone of voice'},
     'm': 15,
     'what': {'hu': 'Írj 3 jelzőt a márka személyiségére, döntsd el, hol áll a négy skálán, és kérd ugyanazt az üzenetet háromféle hangon. Válaszd ki a tiédet.',
              'en': "Write 3 adjectives for the brand's personality, decide where it sits on the four scales, and ask for the same message in three voices. Choose yours."},
     'out': {'hu': '3 jelző, a hangnem és 1 példamondat', 'en': '3 adjectives, the tone and 1 example sentence'},
     'p': {'hu': 'A márkám: [márka] mint [új kategória], az ígérete: [ígéret], az értékei: [3 érték]. Írd meg ugyanazt a rövid üzenetet, például egy új termék bejelentését, háromféle hangon: egyszer '
                 'lazán és játékosan, egyszer magabiztosan és egyszerűen, egyszer visszafogottan és szakmaian. Mindegyik legfeljebb 2 mondat. Utána mondd meg, melyik illik leginkább a [márka] '
                 'személyiségéhez, de a döntés az enyém.',
           'en': 'My brand: [brand] as a [new category], its promise: [promise], its values: [3 values]. Write the same short message, for example a new product announcement, in three voices: once '
                 "relaxed and playful, once confident and simple, once restrained and expert. At most 2 sentences each. Then tell me which fits [brand]'s personality best, but the decision is "
                 'mine.'}},
 5: {'t': {'hu': 'Célcsoport és az első persona', 'en': 'Target audience and the first persona'},
     'm': 15,
     'what': {'hu': 'Írd le a célcsoportot egy mondatban, és készíts belőle egy personát a kártya mezőivel.',
              'en': 'Describe the target audience in one sentence, and create a persona from it with the card fields.'},
     'out': {'hu': '1 célcsoport-mondat és 1 persona-kártya', 'en': '1 target audience sentence and 1 persona card'},
     'p': {'hu': 'A márkám: [márka] mint [új kategória], a pozicionálása: [mondat]. Írd le egy mondatban a legfontosabb célcsoportját, aztán készíts belőle egy hihető personát: név, kor, '
                 'foglalkozás, lakóhely, egy átlagos napja, mit szeretne elérni, mitől tart, hogyan és hol vásárol [új kategória] terméket vagy szolgáltatást. Ne legyen tökéletes vásárló, legyenek '
                 'kétségei is.',
           'en': 'My brand: [brand] as a [new category], its positioning: [sentence]. Describe its most important target audience in one sentence, then create a believable persona from it: name, '
                 'age, occupation, where they live, an ordinary day, what they want to achieve, what they worry about, how and where they buy [new category] products or services. They should not be '
                 'a perfect customer; give them doubts too.'}},
 6: {'t': {'hu': 'Interjú a personával', 'en': 'Interview the persona'},
     'm': 20,
     'what': {'hu': 'Kérdezd ki a personát 5 kérdéssel, szerepjátékban. Jelöld meg a válaszokat, amelyek szerinted kitaláltak, vagy túl szépen illenek a márkádhoz.',
              'en': 'Interview the persona with 5 questions, in a role-play. Mark the answers you think are made up or fit your brand too neatly.'},
     'out': {'hu': '5 kérdés és válasz, jelölve', 'en': '5 questions and answers, marked'},
     'qs': {'hu': ['Mikor vettél utoljára [termék], és miért azt?',
                   'Mi zavar abban, amit most használsz?',
                   'Mi tartana vissza attól, hogy kipróbáld?',
                   'Mennyit adnál érte, és miért?',
                   'Kinek mesélnéd el, és mit mondanál?'],
            'en': ['When did you last buy [product], and why that one?',
                   'What bothers you about what you use now?',
                   'What would hold you back from trying it?',
                   'How much would you pay for it, and why?',
                   'Who would you tell about it, and what would you say?']},
     'p': {'hu': 'Szeretnék veled egy szerepjátékot játszani, hogy jobban megértsem a célcsoportomat. Egy órai játékban azt találom ki, milyen lenne, ha a [márka] a nevével és a logójával együtt [új '
                 'kategória] lenne. Röviden erről szól: [márkaplatform 3-4 mondatban].\n'
                 '\n'
                 'Kérlek, mostantól te legyél [persona neve], egy [kor] éves [foglalkozás], aki [2-3 mondat az életéről, szokásairól, arról, mi fontos neki]. Én egy piackutató vagyok, és kérdezni '
                 'foglak erről. Válaszolj úgy, ahogy ő válaszolna: a saját szavaival, őszintén, akár kritikusan is, és ne próbálj a kedvemben járni. Ha valamit ő nem tudna, mondd, hogy nem tudod. '
                 'Rövid, beszélt nyelvű válaszokat kérek, mintha egy interjún ülnénk.\n'
                 '\n'
                 'Ha készen állsz, mutatkozz be egy mondatban, és kezdem a kérdéseket.',
           'en': 'I would like to play a role-play with you to understand my target audience better. In a classroom game I am working out what it would be like if [brand], name and logo included, '
                 'were a [new category]. In short: [brand platform in 3-4 sentences].\n'
                 '\n'
                 'From now on, please be [persona name], a [age]-year-old [occupation] who [2-3 sentences about their life, habits and what matters to them]. I am a market researcher and I will ask '
                 'you about this. Answer the way they would: in their own words, honestly, even critically, and do not try to please me. If they would not know something, say you do not know. Short, '
                 'spoken answers please, as if we were in an interview.\n'
                 '\n'
                 'When you are ready, introduce yourself in one sentence and I will start asking.'}},
 7: {'t': {'hu': 'A második persona', 'en': 'The second persona'},
     'm': 20,
     'what': {'hu': 'Készíts egy második personát, aki más, mint az első: más élethelyzet, más kétség. Kérdezd ki 3-5 kérdéssel.',
              'en': 'Create a second persona who is different from the first: a different life situation, a different doubt. Interview them with 3-5 questions.'},
     'out': {'hu': '2. persona-kártya és interjú', 'en': 'Second persona card and interview'},
     'p': {'hu': 'Az első personám: [persona 1 röviden]. Készíts egy második personát ugyanabból vagy egy másodlagos célcsoportból, aki tényleg más: más élethelyzetben van, más okból vásárolna, és '
                 'más miatt hezitálna. Ugyanazokkal a mezőkkel kérem, mint az elsőt. Utána mondd meg egy mondatban, miben kell majd másképp szólni hozzá, mint az elsőhöz.',
           'en': 'My first persona: [persona 1 in brief]. Create a second persona from the same or a secondary target audience who is genuinely different: in a different life situation, buying for a '
                 'different reason, hesitating for a different reason. Use the same fields as for the first. Then tell me in one sentence how we will need to talk to them differently from the '
                 'first.'}},
 8: {'t': {'hu': 'Árazás · opcionális', 'en': 'Pricing · optional'},
     'm': 15,
     'what': {'hu': 'Gyűjts valódi árakat 3-5 versenytárstól, és döntsd el, hol áll a márkád: prémium, közép vagy belépő. Indokold egy mondatban.',
              'en': 'Collect real prices from 3-5 competitors and decide where your brand sits: premium, mid-range or entry level. Justify it in one sentence.'},
     'out': {'hu': 'Árszint és egymondatos indoklás', 'en': 'Price level and a one-sentence reason'},
     'p': {'hu': 'Webes kereséssel gyűjts valódi árakat 5 [új kategória] márkától a [ország vagy régió] piacon, forráslinkkel, táblázatban. Csak olyan árat írj, amit megtaláltál, a becslést jelöld. '
                 'Utána a pozicionálásom alapján ([mondat]) javasolj árszintet a [márka] márkának (prémium, közép vagy belépő), és indokold két mondatban.',
           'en': 'Use web search to collect real prices from 5 [new category] brands on the [country or region] market, with source links, in a table. Only list prices you actually found; mark '
                 'estimates. Then, based on my positioning ([sentence]), suggest a price level for [brand] (premium, mid-range or entry level) and justify it in two sentences.'}},
 9: {'t': {'hu': 'A márkabrief összerakása', 'en': 'Putting the brand brief together'},
     'm': 15,
     'what': {'hu': 'Rakd össze egy oldalba mindazt, ami ma elkészült. Az AI csak rendezzen, ne írjon hozzá újat.',
              'en': 'Put everything you made today on one page. The AI should only organise it, not add anything new.'},
     'out': {'hu': 'Márkabrief egy oldalon: ez készül el mára', 'en': 'A one-page brand brief: this is what is done by today'},
     'brief': {'hu': ['A „Mi lenne, ha…” mondat', 'Célcsoport', '2 persona röviden', 'Pozicionálás', 'Ígéret', '3 érték', 'Személyiség és hangnem, példamondattal', 'Árszint, ha van'],
               'en': ['The "What if…" sentence',
                      'Target audience',
                      '2 personas in brief',
                      'Positioning',
                      'Promise',
                      '3 values',
                      'Personality and tone, with an example sentence',
                      'Price level, if any']},
     'p': {'hu': 'Itt van minden, ami ma elkészült a márkámhoz: [bemásolva]. Rakd össze egy egyoldalas márkabriefbe ezekkel a fejezetekkel: a „Mi lenne, ha…” mondat, célcsoport, két persona röviden, '
                 'pozicionálás, ígéret, három érték, személyiség és hangnem egy példamondattal, árszint, ha van. Ne írj hozzá új tartalmat, csak rendezd és egységesítsd. Ha valami hiányzik, vagy két '
                 'rész ellentmond egymásnak, jelezd a végén.',
           'en': 'Here is everything I made for my brand today: [pasted]. Put it into a one-page brand brief with these sections: the "What if…" sentence, target audience, two personas in brief, '
                 'positioning, promise, three values, personality and tone with an example sentence, price level if any. Do not add new content, only organise and align it. If something is missing '
                 'or two parts contradict each other, flag it at the end.'}}}

# Rövid elmélet: (cím, bevezető mondat, [(címke, szöveg)], kitalált példa, opcionális képlet)
S2_THEORY = {
 'brief': dict(t=L('Mi az a márkabrief?', 'What is a brand brief?'),
    lead=L('Egy oldal, amire minden későbbi munka épül: a logótól a kampányig mindent ebből csinálsz.', 'One page that all later work builds on: from the logo to the campaign, you make everything from it.'),
    items=[(L('Kiindulás', 'Starting point'), L('Mi lenne, ha…: mi marad a márkából, és mi lesz új?', 'What if…: what stays of the brand, and what is new?')),
           (L('Pozicionálás', 'Positioning'), L('Miben vagy más, mint a többiek?', 'How are you different from the rest?')),
           (L('Ígéret és értékek', 'Promise and values'), L('Mit kap tőled a vevő, és mit képviselsz?', 'What does the customer get from you, and what do you stand for?')),
           (L('Személyiség és hangnem', 'Personality and tone'), L('Ha ember lennél, milyen lennél, és hogyan beszélnél?', 'If you were a person, what would you be like, and how would you talk?')),
           (L('Célcsoport és persona', 'Audience and persona'), L('Kinek szólsz, és ki az az egy ember, akire gondolsz?', 'Who do you speak to, and who is the one person you have in mind?')),
           (L('Árazás · opcionális', 'Pricing · optional'), L('Mennyibe kerülsz a többiekhez képest?', 'What do you cost compared with the rest?'))],
    ex=L('A mai diákon végig ezt a kitalált példát visszük: mi lenne, ha a Rubik-kocka cipőmárka lenne? A példa csak mutatja a formát, a te márkád tartalma a tiéd.',
         "Throughout today's slides we follow one made-up example: what if the Rubik's Cube were a shoe brand? The example only shows the form; the content of your brand is yours.")),
 'pos': dict(t=L('Pozicionálás: miben vagy más?', 'Positioning: how are you different?'),
    lead=L('Egy mondat arról, kinek szólsz, mi vagy, és miben különbözöl a versenytársaidtól.', 'One sentence on who you speak to, what you are, and how you differ from your competitors.'),
    formula=L('[Kinek], akik [mire vágynak], a [márka] az a [kategória], amely [miben más], mert [miért hihető].', 'For [whom], who [want what], [brand] is the [category] that [how it is different], because [why it is believable].'),
    items=[(L('Próba', 'Test'), L('Ha a mondatba egy versenytárs nevét írod, és ugyanúgy igaz, még nem pozicionálás.', "If you put a competitor's name into the sentence and it is still true, it is not positioning yet."))],
    ex=L('Városi fiataloknak, akik nem akarnak ugyanabban járni, mint mindenki, a Rubik az a sneakermárka, amelynek a színeit percek alatt átcsavarhatod, mert minden panelje cserélhető.',
         "For young city people who do not want to wear what everyone wears, Rubik is the sneaker brand whose colours you can twist around in minutes, because every panel is replaceable.")),
 'promise': dict(t=L('Ígéret és értékek', 'Promise and values'),
    lead=L('Az ígéret azt mondja meg, mit kap a vevő. Az értékek azt, mit képvisel a márka, és mi alapján dönt.', 'The promise says what the customer gets. The values say what the brand stands for and how it decides.'),
    items=[(L('Ígéret', 'Promise'), L('Egy mondat, amit a vevő a barátjának is elmondana.', 'One sentence a customer would tell a friend.')),
           (L('Értékek', 'Values'), L('Három elég. Mindegyikhez tartozzon egy mondat arról, mit jelent a gyakorlatban.', 'Three is enough. Each needs one sentence on what it means in practice.')),
           (L('Próba', 'Test'), L('Ha egy érték bármelyik márkára igaz lehetne (innovatív, minőségi, fenntartható), cseréld le.', 'If a value could be true of any brand (innovative, quality, sustainable), replace it.'))],
    ex=L('Ígéret: minden nap más cipő. Értékek: játék, alkotás, kitartás.', 'Promise: a different shoe every day. Values: play, creation, persistence.')),
 'voice': dict(t=L('Ha a márka ember lenne', 'If the brand were a person'),
    lead=L('A személyiség az, amilyen a márka. A hangnem az, ahogyan beszél.', 'Personality is what the brand is like. Tone of voice is how it talks.'),
    items=[(L('Személyiség', 'Personality'), L('3 jelző, amit egy emberre is mondanál.', '3 adjectives you would also use for a person.')),
           (L('Hangnem: négy skála', 'Tone: four scales'), L('hivatalos ↔ laza · komoly ↔ játékos · visszafogott ↔ harsány · egyszerű ↔ szakmai', 'formal ↔ relaxed · serious ↔ playful · restrained ↔ loud · simple ↔ expert')),
           (L('Próba', 'Test'), L('Írd meg ugyanazt az üzenetet három hangon. Amelyikre azt mondod, „ez ő”, az a tiéd.', 'Write the same message in three voices. The one you recognise as "that is them" is yours.'))],
    ex=L('Rubik: okos, játékos, magabiztos. Laza és játékos, rövid mondatokkal. „Hat oldal. Egy cipő. Te döntöd el.”', 'Rubik: clever, playful, confident. Relaxed and playful, in short sentences. "Six sides. One shoe. Your call."')),
 'persona': dict(t=L('Célcsoport és persona', 'Target audience and persona'),
    lead=L('A célcsoport egy csoport leírása. A persona egy kitalált, de hihető ember ebből a csoportból. Mellette könnyebb dönteni: tetszene ez neki?', 'The target audience describes a group. A persona is a made-up but believable person from that group. It makes decisions easier: would they like this?'),
    items=[(L('Célcsoport', 'Target audience'), L('Kik ők, és mi közös bennük?', 'Who are they, and what do they have in common?')),
           (L('Persona-kártya', 'Persona card'), L('Név, kor, foglalkozás, lakóhely, egy átlagos nap, mit akar elérni, mitől tart, hogyan vásárol.', 'Name, age, occupation, where they live, an ordinary day, what they want, what they worry about, how they buy.')),
           (L('Interjú', 'Interview'), L('Az AI eljátssza a personát. Gyors, de hajlamos mindent szeretni, ezért kérd, hogy legyen kritikus, és jelöld a kitalált válaszokat.', 'The AI plays the persona. It is quick, but tends to like everything, so ask it to be critical and mark the made-up answers.'))],
    ex=L('Célcsoport: 18-30 éves városi fiatalok, akik a ruhájukkal is kifejezik magukat. Persona: Dóri, 24 éves grafikushallgató Budapesten. Sokat gyalogol, szereti egyedivé alakítani a tárgyait, és tart attól, hogy egy feltűnő cipő fél év múlva ciki lesz.',
         'Target audience: young city people aged 18-30 who express themselves through what they wear. Persona: Dóri, 24, a graphic design student in Budapest. She walks a lot, likes to make her things her own, and worries that a striking shoe will look embarrassing in six months.')),
 'price': dict(t=L('Árazás · opcionális', 'Pricing · optional'),
    lead=L('Csak akkor foglalkozz vele, ha a márkádnál az ár a pozicionálás része.', 'Only work on it if price is part of your positioning.'),
    items=[(L('Prémium', 'Premium'), L('Drágább, mint a többség. Ezt meg kell tudni indokolni.', 'More expensive than most. You need to be able to justify it.')),
           (L('Közép', 'Mid-range'), L('A megszokott árszint. Más miatt választanak.', 'The usual price level. People choose it for other reasons.')),
           (L('Belépő', 'Entry level'), L('Olcsóbb a többségnél. Az ár maga az érv.', 'Cheaper than most. The price is the argument.')),
           (L('Mihez méred?', 'What do you measure against?'), L('A versenytársak áraihoz, ahhoz, amennyit a vevő szerint ér, vagy a költséghez és az árréshez.', 'Competitor prices, what it is worth to the customer, or cost plus margin.'))],
    ex=L('Rubik: prémium közép, mert a cserélhető panel többet ad egy sima sneakernél.', 'Rubik: upper mid-range, because the replaceable panels give more than a plain sneaker.')),
}

S2_SLIDES = [('agenda',), ('th', 'brief'), ('task', 1),
             ('th', 'pos'), ('task', 2),
             ('th', 'promise'), ('task', 3),
             ('th', 'voice'), ('task', 4),
             ('th', 'persona'), ('task', 5), ('task', 6), ('task', 7),
             ('th', 'price'), ('task', 8),
             ('task', 9)]
S2_BLOCKS = [(L('Első blokk', 'First block'), [1, 2, 3, 4]), (L('Második blokk', 'Second block'), [5, 6, 7, 8, 9])]

# A 2. alkalom összefoglaló diája: ki melyik márkát választotta 2026. november 5-én (oktatói lista).
# Oktatói döntés 2026. november 11.: teljes névvel kerülnek a fájlba. Neptun-kód nem kerül ide.
ROSTER = [('Alam Ratemul', 'Apple'), ('Awan Malik Danish Naveed', 'Tesla'), ('Ercetin Onur', 'Duolingo'),
          ('Fahim Md Fayaz Yasin', 'Nike'), ('Hasan Md Mehedi', 'Coca-Cola'), ('Hossain Md Mamun', 'IKEA'),
          ('Odikanuom Pascal Izunna', 'Ferrari'), ('Tran Hoai Truc Quynh', 'Spotify')]
NOBRAND = ['Akter Rokeya', 'Kishan Alif Nur', 'Vo Thi Diem Huong']

# ======================================================================
# 2026. november 11., este: minden prompt megmondja, mit kell bemásolni (Ehhez kell) és milyen formában
# kérje vissza az eredményt (fmt), hogy az a márkadokumentumba kerüljön, és onnan menjen tovább a következő promptba.
# ======================================================================
_FMT = {
 1: dict(need=L('Az 1. alkalom márkaelemzése.', 'Your brand analysis from session 1.'),
         doc=L('1. Mi lenne, ha… és a 3 jelző', '1. What if… and the 3 adjectives'),
         p=L('Az előző órán elemeztem a [márka] márkát, itt az elemzésem: [bemásolva vagy feltöltve]. Órai játékban azt találjuk ki, milyen lenne, ha a [márka] a nevével és a logójával együtt [új kategória] lenne. Foglald össze 5 jelzőben, milyen ez a márka, ha ember lenne, és mondd meg, melyik 3 jelző a legfontosabb az új iparágban.\n\nA válaszod legyen rövid. Csak ezt a blokkot add vissza, hogy be tudjam másolni a márkadokumentumomba:\nMI LENNE, HA: …\n5 JELZŐ: …\nA 3 LEGFONTOSABB AZ ÚJ IPARÁGBAN: … (mindegyik mellé egy rövid indoklás)\nAMI HIÁNYZIK AZ ELEMZÉSEMBŐL: …',
             'Last class I analysed the [brand] brand; here is my analysis: [pasted or uploaded]. In a classroom game we work out what it would be like if [brand], name and logo included, were a [new category]. Sum up in 5 adjectives what this brand would be like as a person, and tell me which 3 adjectives matter most in the new industry.\n\nKeep it short. Return only this block, so I can paste it into my brand document:\nWHAT IF: …\n5 ADJECTIVES: …\nTHE 3 THAT MATTER MOST IN THE NEW INDUSTRY: … (each with a short reason)\nWHAT IS MISSING FROM MY ANALYSIS: …')),
 2: dict(need=L('Az 1. feladat eredménye és az 1. alkalom versenytárstáblázata.', 'The output of task 1 and your competitor table from session 1.'),
         doc=L('2. Pozicionálás: a választott mondat', '2. Positioning: the sentence you chose'),
         p=L('A márkadokumentumom eddig: [1. feladat eredménye]. A versenytárstáblázatom az első óráról: [bemásolva]. A márkám: [márka] mint [új kategória], órai játékban, a neve és a logója marad. Írj 3 különböző pozicionáló mondatot ezzel a képlettel: „Kinek…, akik…, a márka az a…, amely…, mert…”. Ha valamelyik bármelyik versenytársra igaz lehetne, jelezd.\n\nA válaszod legyen rövid. Csak ezt a blokkot add vissza:\n1. MONDAT: …\n   LEGJOBBAN ETTŐL A VERSENYTÁRSTÓL KÜLÖNBÖZIK: …\n2. MONDAT: …\n   LEGJOBBAN ETTŐL A VERSENYTÁRSTÓL KÜLÖNBÖZIK: …\n3. MONDAT: …\n   LEGJOBBAN ETTŐL A VERSENYTÁRSTÓL KÜLÖNBÖZIK: …',
             'My brand document so far: [output of task 1]. My competitor table from the first class: [pasted]. My brand: [brand] as a [new category], in a classroom game; its name and logo stay. Write 3 different positioning sentences with this formula: "For…, who…, the brand is the… that…, because…". Flag any that could be true of any competitor.\n\nKeep it short. Return only this block:\n1. SENTENCE: …\n   DIFFERS MOST FROM THIS COMPETITOR: …\n2. SENTENCE: …\n   DIFFERS MOST FROM THIS COMPETITOR: …\n3. SENTENCE: …\n   DIFFERS MOST FROM THIS COMPETITOR: …')),
 3: dict(need=L('A 2. feladat eredménye: a pozicionáló mondatod.', 'The output of task 2: your positioning sentence.'),
         doc=L('3. Ígéret és 3 érték: amit kiválasztottál', '3. Promise and 3 values: the ones you chose'),
         p=L('A márkám: [márka] mint [új kategória], órai játékban. A pozicionálása: [2. feladat eredménye]. Javasolj 5 lehetséges ígéretet, mindegyik egy rövid mondat, amit egy vevő a barátjának is elmondana. Utána javasolj 6 értéket: mit jelent a gyakorlatban, és hol látszik ma a valódi [márka] márkán. Húzd ki azokat, amelyek bármelyik márkára igazak lehetnének. A végső ígéretet és a 3 értéket én választom ki.\n\nA válaszod legyen rövid. Csak ezt a blokkot add vissza:\nÍGÉRETEK:\n1. …\n2. …\n3. …\n4. …\n5. …\nÉRTÉKEK:\n1. … · a gyakorlatban: … · ma a márkán: …\n(és így tovább a 6. értékig)',
             'My brand: [brand] as a [new category], in a classroom game. Its positioning: [output of task 2]. Suggest 5 possible promises, each a short sentence a customer would tell a friend. Then suggest 6 values: what each means in practice and where it shows in the real [brand] today. Cross out any that could be true of any brand. I will choose the final promise and the 3 values.\n\nKeep it short. Return only this block:\nPROMISES:\n1. …\n2. …\n3. …\n4. …\n5. …\nVALUES:\n1. … · in practice: … · in the brand today: …\n(and so on up to value 6)')),
 4: dict(need=L('Az 1. feladat 3 jelzője és a 3. feladat eredménye: ígéret és 3 érték.', 'The 3 adjectives from task 1 and the output of task 3: promise and 3 values.'),
         doc=L('4. Személyiség (3 jelző), hangnem és egy példamondat', '4. Personality (3 adjectives), tone and one example sentence'),
         p=L('A márkám: [márka] mint [új kategória], órai játékban. A 3 legfontosabb jelzője: [1. feladat eredménye]. Az ígérete és az értékei: [3. feladat eredménye]. Írd meg ugyanazt a rövid üzenetet, például egy új termék bejelentését, háromféle hangon: lazán és játékosan; magabiztosan és egyszerűen; visszafogottan és szakmaian. Mindegyik legfeljebb 2 mondat. Utána mondd meg, melyik illik leginkább a [márka] személyiségéhez, de a döntés az enyém.\n\nCsak ezt a blokkot add vissza:\nA) LAZA ÉS JÁTÉKOS: …\nB) MAGABIZTOS ÉS EGYSZERŰ: …\nC) VISSZAFOGOTT ÉS SZAKMAI: …\nJAVASLAT: … (egy mondat, miért)',
             'My brand: [brand] as a [new category], in a classroom game. Its 3 key adjectives: [output of task 1]. Its promise and values: [output of task 3]. Write the same short message, for example a new product announcement, in three voices: relaxed and playful; confident and simple; restrained and expert. At most 2 sentences each. Then tell me which fits [brand]\'s personality best, but the decision is mine.\n\nReturn only this block:\nA) RELAXED AND PLAYFUL: …\nB) CONFIDENT AND SIMPLE: …\nC) RESTRAINED AND EXPERT: …\nSUGGESTION: … (one sentence on why)')),
 5: dict(need=L('A 2. feladat eredménye: a pozicionáló mondatod.', 'The output of task 2: your positioning sentence.'),
         doc=L('5. Célcsoport és az 1. persona', '5. Target audience and the first persona'),
         p=L('A márkám: [márka] mint [új kategória], órai játékban. A pozicionálása: [2. feladat eredménye]. Írd le egy mondatban a legfontosabb célcsoportját, aztán készíts belőle egy hihető personát. Ne legyen tökéletes vásárló, legyenek kétségei is.\n\nCsak ezt a blokkot add vissza:\nCÉLCSOPORT: … (egy mondat)\nNÉV: …\nKOR: …\nFOGLALKOZÁS: …\nLAKÓHELY: …\nEGY ÁTLAGOS NAPJA: … (2 mondat)\nMIT SZERETNE ELÉRNI: …\nMITŐL TART: …\nHOGYAN ÉS HOL VÁSÁROL: …',
             'My brand: [brand] as a [new category], in a classroom game. Its positioning: [output of task 2]. Describe its most important target audience in one sentence, then create a believable persona from it. They should not be a perfect customer; give them doubts too.\n\nReturn only this block:\nTARGET AUDIENCE: … (one sentence)\nNAME: …\nAGE: …\nOCCUPATION: …\nWHERE THEY LIVE: …\nAN ORDINARY DAY: … (2 sentences)\nWHAT THEY WANT: …\nWHAT THEY WORRY ABOUT: …\nHOW AND WHERE THEY BUY: …')),
 6: dict(need=L('Az 5. feladat personája, és a 2-4. feladat eredménye röviden.', 'The persona from task 5, and the outputs of tasks 2-4 in brief.'),
         doc=L('6. Az interjú: 5 kérdés és válasz, jelölve', '6. The interview: 5 questions and answers, marked'),
         p=L('Szeretnék veled egy szerepjátékot játszani, hogy jobban megértsem a célcsoportomat. Egy órai játékban azt találom ki, milyen lenne, ha a [márka] a nevével és a logójával együtt [új kategória] lenne. Röviden erről szól: [2-4. feladat eredménye röviden].\n\nKérlek, mostantól te legyél ez a persona: [5. feladat personája]. Én egy piackutató vagyok, és kérdezni foglak. Válaszolj úgy, ahogy ő válaszolna: a saját szavaival, őszintén, akár kritikusan is, és ne próbálj a kedvemben járni. Ha valamit ő nem tudna, mondd, hogy nem tudod. Rövid, beszélt nyelvű válaszokat kérek.\n\nHa azt írom, hogy VÉGE, lépj ki a szerepből, és csak ezt a blokkot add vissza:\nKÉRDÉS 1: … · VÁLASZ: … (egy mondatban)\n(és így tovább mind az 5 kérdésre)\nAMI MEGLEPŐ VOLT: …\n\nHa készen állsz, mutatkozz be egy mondatban, és kezdem a kérdéseket.',
             'I would like to play a role-play with you to understand my target audience better. In a classroom game I am working out what it would be like if [brand], name and logo included, were a [new category]. In short: [outputs of tasks 2-4 in brief].\n\nFrom now on, please be this persona: [persona from task 5]. I am a market researcher and I will ask you questions. Answer the way they would: in their own words, honestly, even critically, and do not try to please me. If they would not know something, say you do not know. Short, spoken answers please.\n\nWhen I write END, step out of the role and return only this block:\nQUESTION 1: … · ANSWER: … (in one sentence)\n(and so on for all 5 questions)\nWHAT WAS SURPRISING: …\n\nWhen you are ready, introduce yourself in one sentence and I will start asking.')),
 7: dict(need=L('Az 5. feladat personája. Az interjúhoz a 6. feladat promptja.', 'The persona from task 5. For the interview, the prompt from task 6.'),
         doc=L('7. A 2. persona és a rövid interjúja', '7. The second persona and its short interview'),
         p=L('Az első personám: [5. feladat personája]. Készíts egy második personát ugyanabból vagy egy másodlagos célcsoportból, aki tényleg más: más élethelyzetben van, más okból vásárolna, és más miatt hezitálna.\n\nCsak ezt a blokkot add vissza, ugyanazokkal a sorokkal, mint az első personánál:\nNÉV: …\nKOR: …\nFOGLALKOZÁS: …\nLAKÓHELY: …\nEGY ÁTLAGOS NAPJA: … (2 mondat)\nMIT SZERETNE ELÉRNI: …\nMITŐL TART: …\nHOGYAN ÉS HOL VÁSÁROL: …\nMIBEN MÁS, MINT AZ ELSŐ: …\nHOGYAN SZÓLJUNK HOZZÁ MÁSKÉPP: … (egy mondat)',
             'My first persona: [persona from task 5]. Create a second persona from the same or a secondary target audience who is genuinely different: in a different life situation, buying for a different reason, hesitating for a different reason.\n\nReturn only this block, with the same lines as the first persona:\nNAME: …\nAGE: …\nOCCUPATION: …\nWHERE THEY LIVE: …\nAN ORDINARY DAY: … (2 sentences)\nWHAT THEY WANT: …\nWHAT THEY WORRY ABOUT: …\nHOW AND WHERE THEY BUY: …\nHOW THEY DIFFER FROM THE FIRST: …\nHOW TO TALK TO THEM DIFFERENTLY: … (one sentence)')),
 8: dict(need=L('A 2. feladat eredménye és az 1. alkalom versenytárstáblázata.', 'The output of task 2 and your competitor table from session 1.'),
         doc=L('8. Árszint · opcionális', '8. Price level · optional'),
         p=L('A márkám: [márka] mint [új kategória], órai játékban. A pozicionálása: [2. feladat eredménye]. Webes kereséssel gyűjts valódi árakat 5 [új kategória] márkától a [ország vagy régió] piacon. Csak olyan árat írj, amit megtaláltál, a becslést jelöld. Utána javasolj árszintet: prémium, közép vagy belépő.\n\nCsak ezt a blokkot add vissza:\nÁRAK: márka · termék · ár · forráslink (soronként egy)\nJAVASOLT ÁRSZINT: …\nINDOKLÁS: … (2 mondat)',
             'My brand: [brand] as a [new category], in a classroom game. Its positioning: [output of task 2]. Use web search to collect real prices from 5 [new category] brands on the [country or region] market. Only list prices you actually found; mark estimates. Then suggest a price level: premium, mid-range or entry level.\n\nReturn only this block:\nPRICES: brand · product · price · source link (one per line)\nSUGGESTED PRICE LEVEL: …\nREASON: … (2 sentences)')),
 9: dict(need=L('Az egész márkadokumentumod: az 1-8. feladat eredménye.', 'Your whole brand document: the outputs of tasks 1-8.'),
         doc=L('A mai eredménytermék: a márkabrief. Ezzel jössz a 3. alkalomra.', "Today's output: the brand brief. You bring it to session 3."),
         p=L('Itt a márkadokumentumom: [az 1-8. feladat eredménye bemásolva]. Rakd össze belőle egy egyoldalas márkabriefet. Ne írj hozzá új tartalmat, csak rendezd és egységesítsd.\n\nPontosan ezekkel a címekkel add vissza:\nMI LENNE, HA: …\nCÉLCSOPORT: …\nPERSONÁK: … (kettő, 2-2 mondatban)\nPOZICIONÁLÁS: …\nÍGÉRET: …\nÉRTÉKEK: …\nSZEMÉLYISÉG ÉS HANGNEM: … (példamondattal)\nÁRSZINT: … (ha van)\nHIÁNYZIK VAGY ELLENTMOND: …',
             'Here is my brand document: [outputs of tasks 1-8 pasted]. Turn it into a one-page brand brief. Do not add new content, only organise and align it.\n\nReturn it with exactly these headings:\nWHAT IF: …\nTARGET AUDIENCE: …\nPERSONAS: … (two, 2 sentences each)\nPOSITIONING: …\nPROMISE: …\nVALUES: …\nPERSONALITY AND TONE: … (with an example sentence)\nPRICE LEVEL: … (if any)\nMISSING OR CONTRADICTORY: …')),
}
for _k, _v in _FMT.items():
    S2_TASKS[_k]['need'] = _v['need']
    S2_TASKS[_k]['doc'] = _v['doc']
    S2_TASKS[_k]['p'] = _v['p']
    S2_TASKS[_k].pop('pcb', None)
S2_TASKS[1]['what'] = L('Mondd ki a feladatodat egy mondatban: „Mi lenne, ha a [márka] [új kategória] lenne?” Írj mellé 5 jelzőt a márkáról, és jelöld, melyik három a legfontosabb az új iparágban. Nyiss egy üres dokumentumot: ez lesz a márkadokumentumod.',
                        'Say your task in one sentence: "What if [brand] were a [new category]?" Add 5 adjectives describing the brand, and mark the three that matter most in the new industry. Open an empty document: this will be your brand document.')
S2_TASKS[7]['what'] = L('Készíts egy második personát, aki más, mint az első: más élethelyzet, más kétség. Utána kérdezd ki 3-5 kérdéssel, a 6. feladat promptjával.',
                        'Create a second persona who is different from the first: a different life situation, a different doubt. Then interview them with 3-5 questions, using the prompt from task 6.')

# a márkadokumentum vázlata a 2. alkalomhoz
S2_DOC = [1, 2, 3, 4, 5, 6, 7, 8]
S2_SLIDES = [S2_SLIDES[0], ('doc',)] + S2_SLIDES[1:]
# melyik eredmény melyik későbbi feladathoz kell (a 9. feladat mindet használja)
S2_USED_BY = {1: [2, 4], 2: [3, 5, 6, 8], 3: [4, 6], 4: [6], 5: [6, 7], 6: [], 7: [], 8: []}

# 2026. november 11., este: az 5. dia (márkadokumentum) kikerült; helyette minden feladatnál TIPP gomb,
# ami felugró ablakban adja meg, mit tegyen, ha nincs meg a szükséges előzmény.
S2_SLIDES = [x for x in S2_SLIDES if x[0] != 'doc']
TIP_PROMPTS = {
 'analysis': L('Egy órai játékban a [márka] márkával dolgozom: azt találjuk ki, milyen lenne, ha a nevével és a logójával együtt [új kategória] lenne. Ehhez először értenem kell, mitől az a [márka], ami. Webes kereséssel elemezd a márkát: értékek, személyiség (ha ember lenne, milyen lenne), hangnem, vizuális kódok (színek, formák, betűk), 3 ikonikus kampány. Csak forrással alátámasztott dolgot írj, és ha valamiben nem vagy biztos, jelezd.\n\nA válaszod legyen rövid. Csak ezt a blokkot add vissza:\nÉRTÉKEK: …\nSZEMÉLYISÉG: … (5 jelző)\nHANGNEM: …\nVIZUÁLIS KÓDOK: …\nIKONIKUS KAMPÁNYOK: … (3, forráslinkkel)\nBIZONYTALAN: …',
               'In a classroom game I am working with the [brand] brand: we work out what it would be like if, name and logo included, it were a [new category]. First I need to understand what makes [brand] what it is. Use web search to analyse the brand: values, personality (what it would be like as a person), tone of voice, visual codes (colours, shapes, type), 3 iconic campaigns. Only write what you can back with a source, and flag anything you are not sure about.\n\nKeep it short. Return only this block:\nVALUES: …\nPERSONALITY: … (5 adjectives)\nTONE OF VOICE: …\nVISUAL CODES: …\nICONIC CAMPAIGNS: … (3, with source links)\nUNSURE: …'),
 'competitors': L('Egy órai játékban azt találjuk ki, milyen lenne, ha a [márka] [új kategória] lenne. Webes kereséssel keress 5 valódi [új kategória] márkát a [ország vagy régió] piacán. Csak létező cégeket írj, és ahol bizonytalan vagy, jelöld.\n\nCsak ezt a táblázatot add vissza:\nMÁRKA | AJÁNLAT | ÁRSZINT | HANGNEM | FŐ CSATORNÁK | FORRÁSLINK',
                  'In a classroom game we work out what it would be like if [brand] were a [new category]. Use web search to find 5 real [new category] brands on the [country or region] market. Only list existing companies, and mark where you are unsure.\n\nReturn only this table:\nBRAND | OFFER | PRICE LEVEL | TONE OF VOICE | MAIN CHANNELS | SOURCE LINK'),
}
S2_TIPS = {
 1: [('p', L('Az 1. alkalom márkaelemzése', 'Your brand analysis from session 1'), 'analysis')],
 2: [('j', L('Az 1. feladat eredménye', 'The output of task 1'), 1), ('p', L('Az 1. alkalom versenytárstáblázata', 'Your competitor table from session 1'), 'competitors')],
 3: [('j', L('A 2. feladat eredménye: a pozicionáló mondat', 'The output of task 2: the positioning sentence'), 2)],
 4: [('j', L('Az 1. feladat 3 jelzője', 'The 3 adjectives from task 1'), 1), ('j', L('A 3. feladat eredménye: ígéret és 3 érték', 'The output of task 3: promise and 3 values'), 3)],
 5: [('j', L('A 2. feladat eredménye: a pozicionáló mondat', 'The output of task 2: the positioning sentence'), 2)],
 6: [('j', L('Az 5. feladat personája', 'The persona from task 5'), 5), ('j', L('A 2-4. feladat eredménye', 'The outputs of tasks 2-4'), 2)],
 7: [('j', L('Az 5. feladat personája', 'The persona from task 5'), 5), ('j', L('Az interjúhoz a 6. feladat promptja', 'For the interview, the prompt from task 6'), 6)],
 8: [('j', L('A 2. feladat eredménye: a pozicionáló mondat', 'The output of task 2: the positioning sentence'), 2), ('p', L('Az 1. alkalom versenytárstáblázata', 'Your competitor table from session 1'), 'competitors')],
 9: [('j', L('%d. feladat eredménye' % k, 'The output of task %d' % k), k) for k in range(1, 9)],
}
VER_KIVETEL[2] = ('v2.3 · 2026. november 11.', 'v2.3 · 11 November 2026')
# 2026. november 11.: a feladatdiáról a kitalált példa kikerült (oktatói kérés: fölösleges, a prompt formátuma megmutatja az eredményt)
S2_TASKS[1].pop('ex', None)
VER_KIVETEL[2] = ('v2.4 · 2026. november 11.', 'v2.4 · 11 November 2026')

# 2026. november 11.: ha több előzmény kell, mindegyiknek saját TIPP gombja és ablaka van, visszautalás nélkül.
# Minden ablakban önálló prompt, ami a hiányzó előzményt most rögtön elkészíti.
_G = L('Egy órai játékban a [márka] márkával dolgozom: mi lenne, ha a nevével és a logójával együtt [új kategória] lenne. ',
       'In a classroom game I am working with the [brand] brand: what if, name and logo included, it were a [new category]. ')
TIP_PROMPTS.update({
 'adj3': L(_G['hu'] + 'Webes kereséssel nézd meg a márkát, és foglald össze 5 jelzőben, milyen lenne, ha ember lenne. Utána mondd meg, melyik 3 a legfontosabb az új iparágban.\n\nA válaszod legyen rövid. Csak ezt a blokkot add vissza:\nMI LENNE, HA: …\n5 JELZŐ: …\nA 3 LEGFONTOSABB AZ ÚJ IPARÁGBAN: … (mindegyik mellé egy rövid indoklás)',
           _G['en'] + 'Use web search to look at the brand and sum up in 5 adjectives what it would be like as a person. Then tell me which 3 matter most in the new industry.\n\nKeep it short. Return only this block:\nWHAT IF: …\n5 ADJECTIVES: …\nTHE 3 THAT MATTER MOST IN THE NEW INDUSTRY: … (each with a short reason)'),
 'positioning': L(_G['hu'] + 'Webes kereséssel nézz meg 3 valódi [új kategória] versenytársat, és írj egy pozicionáló mondatot ezzel a képlettel: „Kinek…, akik…, a márka az a…, amely…, mert…”. A mondat ne lehessen igaz egyik versenytársra sem.\n\nCsak ezt a blokkot add vissza:\nVERSENYTÁRSAK: … (3, forráslinkkel)\nPOZICIONÁLÁS: …',
                  _G['en'] + 'Use web search to look at 3 real [new category] competitors, and write one positioning sentence with this formula: "For…, who…, the brand is the… that…, because…". The sentence must not be true of any of the competitors.\n\nReturn only this block:\nCOMPETITORS: … (3, with source links)\nPOSITIONING: …'),
 'promise': L(_G['hu'] + 'Javasolj egy ígéretet (egy rövid mondat, amit egy vevő a barátjának is elmondana) és 3 értéket, amelyek a valódi [márka] márkán is látszanak. Ne írj olyat, ami bármelyik márkára igaz lehetne.\n\nCsak ezt a blokkot add vissza:\nÍGÉRET: …\nÉRTÉK 1: … · a gyakorlatban: …\nÉRTÉK 2: … · a gyakorlatban: …\nÉRTÉK 3: … · a gyakorlatban: …',
              _G['en'] + 'Suggest one promise (a short sentence a customer would tell a friend) and 3 values that also show in the real [brand]. Do not write anything that could be true of any brand.\n\nReturn only this block:\nPROMISE: …\nVALUE 1: … · in practice: …\nVALUE 2: … · in practice: …\nVALUE 3: … · in practice: …'),
 'persona': L(_G['hu'] + 'Írd le egy mondatban a legfontosabb célcsoportját, és készíts belőle egy hihető personát, kétségekkel együtt.\n\nCsak ezt a blokkot add vissza:\nCÉLCSOPORT: …\nNÉV: …\nKOR: …\nFOGLALKOZÁS: …\nLAKÓHELY: …\nEGY ÁTLAGOS NAPJA: … (2 mondat)\nMIT SZERETNE ELÉRNI: …\nMITŐL TART: …\nHOGYAN ÉS HOL VÁSÁROL: …',
              _G['en'] + 'Describe its most important target audience in one sentence, and create a believable persona from it, doubts included.\n\nReturn only this block:\nTARGET AUDIENCE: …\nNAME: …\nAGE: …\nOCCUPATION: …\nWHERE THEY LIVE: …\nAN ORDINARY DAY: … (2 sentences)\nWHAT THEY WANT: …\nWHAT THEY WORRY ABOUT: …\nHOW AND WHERE THEY BUY: …'),
 'platform': L(_G['hu'] + 'Foglald össze 3-4 mondatban, mi lenne ez a márka: kinek szól, miben más, mit ígér, és milyen hangon beszél.\n\nCsak ezt a blokkot add vissza:\nMÁRKAPLATFORM RÖVIDEN: …',
               _G['en'] + 'Sum up in 3-4 sentences what this brand would be: who it speaks to, how it is different, what it promises and in what voice it talks.\n\nReturn only this block:\nBRAND PLATFORM IN BRIEF: …'),
 'interview2': L(_FMT[6]['p']['hu'].replace('[5. feladat personája]', '[a második persona]'),
                 _FMT[6]['p']['en'].replace('[persona from task 5]', '[the second persona]')),
 'draftbrief': L(_G['hu'] + 'Ami eddig megvan: [amit eddig elkészítettél, ha van]. Készíts ebből egy egyoldalas márkabrief-vázlatot. Ahol nincs anyagom, ott tegyél javaslatot, és jelöld a JAVASLAT szóval, hogy lássam, mit kell még átnéznem.\n\nPontosan ezekkel a címekkel add vissza:\nMI LENNE, HA: …\nCÉLCSOPORT: …\nPERSONÁK: …\nPOZICIONÁLÁS: …\nÍGÉRET: …\nÉRTÉKEK: …\nSZEMÉLYISÉG ÉS HANGNEM: …\nÁRSZINT: …',
                 _G['en'] + 'What I have so far: [whatever you have made, if anything]. Turn it into a one-page draft brand brief. Where I have no material, make a suggestion and mark it with the word SUGGESTION, so I can see what I still need to check.\n\nReturn it with exactly these headings:\nWHAT IF: …\nTARGET AUDIENCE: …\nPERSONAS: …\nPOSITIONING: …\nPROMISE: …\nVALUES: …\nPERSONALITY AND TONE: …\nPRICE LEVEL: …'),
})
S2_NEED = {
 1: [(L('Az 1. alkalom márkaelemzése', 'Your brand analysis from session 1'), 'analysis')],
 2: [(L('Az 1. feladat eredménye: mi lenne, ha… és a 3 jelző', 'The output of task 1: what if… and the 3 adjectives'), 'adj3'),
     (L('Az 1. alkalom versenytárstáblázata', 'Your competitor table from session 1'), 'competitors')],
 3: [(L('A 2. feladat eredménye: a pozicionáló mondat', 'The output of task 2: the positioning sentence'), 'positioning')],
 4: [(L('Az 1. feladat 3 jelzője', 'The 3 adjectives from task 1'), 'adj3'),
     (L('A 3. feladat eredménye: ígéret és 3 érték', 'The output of task 3: promise and 3 values'), 'promise')],
 5: [(L('A 2. feladat eredménye: a pozicionáló mondat', 'The output of task 2: the positioning sentence'), 'positioning')],
 6: [(L('Az 5. feladat personája', 'The persona from task 5'), 'persona'),
     (L('A 2-4. feladat eredménye röviden', 'The outputs of tasks 2-4 in brief'), 'platform')],
 7: [(L('Az 5. feladat personája', 'The persona from task 5'), 'persona'),
     (L('Interjúprompt a második personához', 'Interview prompt for the second persona'), 'interview2')],
 8: [(L('A 2. feladat eredménye: a pozicionáló mondat', 'The output of task 2: the positioning sentence'), 'positioning'),
     (L('Az 1. alkalom versenytárstáblázata', 'Your competitor table from session 1'), 'competitors')],
 9: [(L('A márkadokumentumod: az 1-8. feladat eredménye', 'Your brand document: the outputs of tasks 1-8'), 'draftbrief')],
}
VER_KIVETEL[2] = ('v2.5 · 2026. november 11.', 'v2.5 · 11 November 2026')

VER_KIVETEL[2] = ('v2.6 · 2026. november 11.', 'v2.6 · 11 November 2026')

# ======================================================================
# Közös leírás a kis feladatos alkalmakhoz (a build.py sx_* függvényei ezt használják).
# ======================================================================
TIP_NOTE = {}
SPEC = {2: dict(tasks=S2_TASKS, theory=S2_THEORY, need=S2_NEED, ex=EXAMPLE)}

# ======================================================================
# 3. alkalom, 2026. november 17-i átdolgozás a 2. alkalom mintájára: kis feladatok, rövid elmélet példával,
# rögzített kimeneti formátumú promptok, „Ehhez kell” lista TIPP gombokkal.
# Oktatói döntések 2026. november 17.: logófeladat nincs (a logó megvan); a példa a LEGO Bank
# (az oktató LEGO_Bank anyaga alapján); minden eredménytermék kötelező; az összefoglalón nincs névsor.
# ======================================================================

NYITVA = 3
VER_HU = 'v1.5 · 2026. november 17.'
VER_EN = 'v1.5 · 17 November 2026'
VER_KIVETEL[1] = ('v1.8 · 2026. november 17.', 'v1.8 · 17 November 2026')
VER_KIVETEL[2] = ('v2.7 · 2026. november 17.', 'v2.7 · 17 November 2026')
VER_KIVETEL[3] = ('v3.0 · 2026. november 17.', 'v3.0 · 17 November 2026')
VER_KIVETEL['index'] = ('v1.6 · 2026. november 17.', 'v1.6 · 17 November 2026')

SESS[2]['out'] = L('Kézikönyv, kulcsvizuálok, posztok, bannerek', 'Brand guide, key visuals, posts, banners')
GOAL[3] = L('Add meg a márka arcát az új iparágban: színek, betűk, képi világ, és a kampány első vizuáljai.',
            "Give the brand its face in the new industry: colours, type, imagery, and the campaign's first visuals.")
SCOPE[3] = L('Az alkalom végére a márkádnak arca van az új iparágban: színek, betűk, képi világ, és néhány kész vizuál, amit a kampányban használni fogsz. A logó megvan, újat nem tervezel.',
             'By the end of the session your brand has a face in the new industry: colours, type, imagery, and a few finished visuals you will use in the campaign. The logo is already there; you do not design a new one.')
DELIV[3] = L('Arculati kézikönyv PDF, 3 kulcsvizuál, 3 posztsablon, 2 banner, plakát-mockup, csomagolás- vagy terméklátvány.',
             'Brand guide PDF, 3 key visuals, 3 post templates, 2 banners, billboard mock-up, packaging or product visual.')
FROMTO[3] = (FROMTO[3][0],
             L('A márkádnak arca van az új iparágban: színek, betűk, képi világ, és néhány kész vizuál a kampányhoz.', 'Your brand has a face in the new industry: colours, type, imagery, and a few finished visuals for the campaign.'),
             L('A logó megvan, újat nem tervezel.', 'The logo is already there; you do not design a new one.'))

TIPS[3][0] = (L('A logó és az új iparág', 'The logo and the new industry'), [
    (L('Hivatalos fájl', 'The official file'),
     L('A logót a márka hivatalos oldaláról vagy sajtóanyagából töltsd le. Ne generáltasd újra, mert az AI elrajzolja.',
       "Download the logo from the brand's official site or press materials. Do not have it regenerated, because the AI will draw it wrong.")),
    (L('Utólag kerül rá', 'It goes on afterwards'),
     L('A logót ne a képgenerálóval tetesd a képre, hanem utólag, a sablonban vagy a bannerben.',
       'Do not have the image generator put the logo on the image; add it afterwards, in the template or the banner.')),
    (L('Új környezet', 'A new setting'),
     L('A logó ugyanaz, de új helyeken jelenik meg: repülőn, bankkártyán, menükártyán. Ezt mutasd meg.',
       'The logo is the same, but it appears in new places: on a plane, a bank card, a menu. Show that.')),
    (L('Órai játék', 'A classroom game'),
     L('A kész anyagokat ne tedd közzé, és ne állítsd valódinak. A márka nem a tiéd, és ez a termék a valóságban nem létezik.',
       'Do not publish the finished materials or present them as real. The brand is not yours, and this product does not exist in reality.')),
])
TIPS[3][2][1][3] = (L('Fájlt ments, ne csak linket', 'Save files, not just links'),
                    L('A képeket, a sablonokat és a PDF-et töltsd le, és tedd a félév mappájába. A deckhez ezek kellenek.',
                      'Download the images, the templates and the PDF and put them in your semester folder. You need them for the deck.'))

EXAMPLE3 = L('Mi lenne, ha a LEGO bank lenne?', 'What if LEGO were a bank?')

# Rövid elmélet. A példák az oktató LEGO_Bank anyagából (brand book, stratégia) vannak; ahol a dia ezen túlmegy, az kitalált illusztráció.
S3_THEORY = {
 'id': dict(t=L('Mi az arculat?', 'What is a visual identity?'),
    lead=L('Minden, amiről ránézésre felismered a márkát. A logó megvan, ma a többit döntöd el az új iparágra.',
           'Everything that makes the brand recognisable at a glance. The logo is already there; today you decide the rest for the new industry.'),
    items=[(L('Logó', 'Logo'), L('Megvan, újat nem tervezel. Azt döntöd el, hol és hogyan jelenik meg.', 'You have it; you do not design a new one. You decide where and how it appears.')),
           (L('Színek', 'Colours'), L('Szerepük van: fő szín, kiemelő szín, háttér.', 'They have roles: main colour, accent colour, background.')),
           (L('Betűk', 'Type'), L('Egy a címekhez, egy a szöveghez.', 'One for headings, one for text.')),
           (L('Képi világ', 'Imagery'), L('Milyen a fény, kik szerepelnek, mi a hangulat.', 'What the light is like, who appears, what the mood is.')),
           (L('Formák és jelek', 'Shapes and signs'), L('A márka visszatérő elemei, amiket logó nélkül is felismersz.', 'The recurring elements of the brand that you recognise even without the logo.')),
           (L('Érintkezési pontok', 'Touchpoints'), L('Ahol a vevő találkozik a márkával: termék, hely, app, hirdetés.', 'Where the customer meets the brand: product, place, app, advertising.'))],
    ex=L('A mai diákon végig ezt a példát visszük: mi lenne, ha a LEGO bank lenne? A logó a piros négyzet, benne a LEGO, alatta a BANK szó. A példa csak mutatja a formát, a te márkád tartalma a tiéd.',
         "Throughout today's slides we follow one example: what if LEGO were a bank? The logo is the red square with LEGO and the word BANK underneath. The example only shows the form; the content of your brand is yours.")),
 'color': dict(t=L('Színek és betűk', 'Colours and type'),
    lead=L('A színeknek és a betűknek szerepük van. Egyszer döntöd el őket, és onnantól minden anyagon ugyanazok.',
           'Colours and type have roles. You decide them once, and from then on they are the same on every asset.'),
    items=[(L('Fő szín', 'Main colour'), L('Erről ismerik fel a márkát. A legtöbb felületen ez dominál.', 'This is what the brand is recognised by. It dominates most surfaces.')),
           (L('Kiemelő szín', 'Accent colour'), L('Gombok és fontos jelzések. Kevés, de feltűnő.', 'Buttons and important signals. Used sparingly, but it stands out.')),
           (L('Semleges színek', 'Neutral colours'), L('Háttér és szöveg, hogy minden olvasható maradjon.', 'Background and text, so everything stays readable.')),
           (L('HEX-kód', 'HEX code'), L('A szín pontos kódja, például #1E4BD8. Ezt másolod be minden promptba.', "The colour's exact code, for example #1E4BD8. You paste it into every prompt.")),
           (L('Két betűtípus', 'Two typefaces'), L('Egy karakteres a címekhez, egy jól olvasható a szöveghez és a számokhoz. Ingyenes forrás: Google Fonts.', 'A distinctive one for headings and a readable one for text and numbers. A free source: Google Fonts.'))],
    ex=L('LEGO Bank: a piros a fő szín, a bizalom jelzéseihez és a felület szerkezetéhez. A sárga a gombokhoz és az ATM-ekhez, a fehér és a fekete a rendhez és az olvashatósághoz. A címekhez buborékos betű, a számokhoz és a banki kifejezésekhez egyszerű geometrikus betű, hogy minden egyértelmű legyen.',
         'LEGO Bank: red is the main colour, for trust signals and the structure of the interface. Yellow is for buttons and the ATMs, white and black for order and readability. Bubble-style type for headings, a simple geometric typeface for numbers and banking terms, so everything is clear.')),
 'image': dict(t=L('Képi világ: egy világ, sok kép', 'Imagery: one world, many images'),
    lead=L('Ha egyszer leírod, milyenek a márka képei, minden kép ugyanabból a világból jön. Ezt a leírást minden képprompt elejére bemásolod: ez az alapprompt.',
           "Once you describe what the brand's images are like, every image comes from the same world. You paste this description at the start of every image prompt: this is the base prompt."),
    items=[(L('Fény és szín', 'Light and colour'), L('Világos vagy sötét, meleg vagy hideg, a márka színeivel.', "Bright or dark, warm or cool, in the brand's colours.")),
           (L('Kik és mit csinálnak', 'Who and what they do'), L('Kik vannak a képen, és mi történik velük.', 'Who is in the picture, and what is happening to them.')),
           (L('Kompozíció', 'Composition'), L('Közeli vagy tág, és hol marad hely a szövegnek.', 'Close-up or wide, and where the space for text is.')),
           (L('Alapprompt', 'Base prompt'), L('Ugyanaz a stílusleírás minden képprompt elején. Ettől lesz egységes a kampány.', 'The same style description at the start of every image prompt. This is what makes the campaign consistent.'))],
    ex=L('LEGO Bank: világos, egyenletes fény, erős kontraszt. Közeli képek kezekről, ahogy a digitális és a valódi felülettel játszanak, és családok, emberek, akik nyugodtak és urai a pénzüknek, a fiókban vagy az appban.',
         'LEGO Bank: bright, even lighting, high contrast. Close-ups of hands interacting with the digital and physical interface, and families and individuals who feel relaxed and in control of their money, in the branch or in the app.')),
 'kv': dict(t=L('Kulcsvizuál: a kampány fő képe', "Key visual: the campaign's main image"),
    lead=L('Ebből a képből lesz a poszt, a banner és a plakát. Egy gondolatot mutat az ígéretből, nem mindent.',
           'This image becomes the post, the banner and the billboard. It shows one idea from the promise, not everything.'),
    items=[(L('Egy gondolat', 'One idea'), L('Ha két mondatban kell elmagyarázni, túl sok van rajta.', 'If it takes two sentences to explain, there is too much in it.')),
           (L('Hely a szövegnek', 'Space for text'), L('Mondd meg a promptban, hová kerül a felirat, és azt a részt hagyja üresen.', 'Say in the prompt where the text will go, and have that area left empty.')),
           (L('Szöveg és logó utólag', 'Text and logo afterwards'), L('A képgenerálótól ne kérd. Utólag kerül rá a sablonban, így pontos lesz.', 'Do not ask the image generator for them. They go on afterwards in the template, so they come out right.')),
           (L('Három változat, egy fő', 'Three versions, one main'), L('Hármat készítesz, és egyet választasz a kampány fő képének.', "You make three and choose one as the campaign's main image."))],
    ex=L('LEGO Bank: közeli kép egy kézről, ahogy egy sárga kockát pattint egy alaplapra, amin a számla szolgáltatásai épülnek. A jobb felső harmad üres, oda kerül a felirat.',
         "LEGO Bank: a close-up of a hand snapping a yellow brick onto a baseplate on which the account's services are built. The top right third is empty; that is where the text goes.")),
 'formats': dict(t=L('Poszt, banner, plakát', 'Post, banner, billboard'),
    lead=L('Ugyanaz a kulcsvizuál és ugyanaz az arculat, csak más méretben és más helyzetben. Mindegyiknek megvan a maga szabálya.',
           'The same key visual and the same identity, just in a different size and situation. Each has its own rule.'),
    items=[(L('Négyzetes poszt', 'Square post'), L('1080×1080 pixel, a hírfolyamba. Egy kép, egy rövid cím.', '1080×1080 pixels, for the feed. One image, one short headline.')),
           (L('Story', 'Story'), L('1080×1920 pixel, 9:16. Felül és alul hagyj szabad sávot, mert ott vannak az app gombjai.', '1080×1920 pixels, 9:16. Leave a free strip at the top and bottom, because the app buttons are there.')),
           (L('Carousel nyitódia', 'Carousel opening slide'), L('Az első kép, ami miatt tovább lapoznak. 1080×1350 pixel (4:5) vagy négyzet.', 'The first image, the one that makes people swipe on. 1080×1350 pixels (4:5) or square.')),
           (L('Banner', 'Banner'), L('300×250 és 728×90 pixel. Márkanév, ígéret, egy gomb, más nem fér el.', '300×250 and 728×90 pixels. Brand name, promise, one button; nothing else fits.')),
           (L('Óriásplakát', 'Billboard'), L('Elhaladva, pár másodperc alatt kell megérteni. Nagy kép, néhány szó.', 'It has to be understood in a few seconds, in passing. A big image, a few words.'))],
    ex=L('LEGO Bank banner: a fő kulcsvizuál, a logó, egy sor szöveg: „Építsd fel a tökéletes bankodat. Kockáról kockára.”, és egy sárga gomb: Nyiss számlát.',
         'LEGO Bank banner: the main key visual, the logo, one line of text: "Build your perfect bank. Brick by brick.", and a yellow button: Open an account.')),
 'touch': dict(t=L('Hol találkozik a vevő a márkával?', 'Where does the customer meet the brand?'),
    lead=L('Az új iparágban a márka új helyeken jelenik meg. Ott is felismerhetőnek kell lennie, ahol eddig soha nem volt.',
           'In the new industry the brand appears in new places. It has to be recognisable even where it has never been before.'),
    items=[(L('Termék vagy csomagolás', 'Product or packaging'), L('Amit a vevő kézbe vesz.', 'What the customer holds in their hands.')),
           (L('Hely', 'Place'), L('Bolt, fiók, utastér, étterem.', 'Shop, branch, cabin, restaurant.')),
           (L('Ember', 'People'), L('Egyenruha, kiszolgálás.', 'Uniform, service.')),
           (L('Digitális felület', 'Digital surface'), L('App, weboldal, értesítés.', 'App, website, notification.'))],
    ex=L('LEGO Bank: a pénztárpult óriási 2×4-es kocka, az ATM-ek sárga, minifigurafej formájú gépek, a széfajtó egy hatalmas Technic-fogaskerék, az appban pedig szolgáltatás-kockákat pattintasz a saját alaplapodra.',
         'LEGO Bank: the teller desk is a giant 2×4 brick, the ATMs are yellow machines shaped like Minifigure heads, the vault door is a huge Technic gear, and in the app you snap service bricks onto your own baseplate.')),
 'guide': dict(t=L('Arculati kézikönyv: a márka szabálykönyve', "Brand guide: the brand's rulebook"),
    lead=L('Azért készül, hogy bárki, aki a márkával dolgozik, ugyanúgy használja. Arról szól, mit szabad és mit nem.',
           'It exists so that anyone who works with the brand uses it the same way. It is about what is allowed and what is not.'),
    items=[(L('Logó', 'Logo'), L('Védőtér, legkisebb méret, és mit nem szabad vele csinálni.', 'Clear space, minimum size, and what must not be done with it.')),
           (L('Színek és betűk', 'Colours and type'), L('HEX-kóddal, szereppel, mintával.', 'With HEX codes, roles and samples.')),
           (L('Képi stílus', 'Image style'), L('A szabályok és 3 példakép.', 'The rules and 3 example images.')),
           (L('Hangnem', 'Tone of voice'), L('A márkabriefből, egy példamondattal.', 'From the brand brief, with an example sentence.')),
           (L('Szabad és tilos', "Do and don't"), L('Példákkal, mert a szabályt a példán értik meg.', 'With examples, because people understand a rule through an example.')),
           (L('Alkalmazások', 'Applications'), L('A mai vizuálok: poszt, banner, plakát, csomagolás.', "Today's visuals: post, banner, billboard, packaging."))],
    ex=L('A LEGO Bank kézikönyve öt fejezet: logó, színek, betűk, hangnem, képi világ. Hangnempélda: a „Konfiguráld a prémium folyószámlahitel-beállításaidat” helyett „Pattintsd fel a folyószámlahitel-védelmet a nyugodt napokért”.',
         'The LEGO Bank guide has five chapters: logo, colours, type, tone of voice, imagery. Tone example: instead of "Configure your premium overdraft settings", "Snap on Overdraft Protection for extra peace of mind".')),
}

S3_SLIDES = [('agenda',), ('how',), ('th', 'id'), ('task', 1),
             ('th', 'color'), ('task', 2),
             ('th', 'image'), ('task', 3),
             ('th', 'kv'), ('task', 4),
             ('th', 'formats'), ('task', 5), ('task', 6), ('task', 7),
             ('th', 'touch'), ('task', 8),
             ('th', 'guide'), ('task', 9)]
S3_TILES = [L('Vizuális irány', 'Visual direction'), L('Színek és betűk', 'Colours and type'), L('Képi világ', 'Imagery'),
            L('Kulcsvizuálok', 'Key visuals'), L('Posztok és bannerek', 'Posts and banners'), L('Plakát és csomagolás', 'Billboard and packaging')]

# Oktatói kérés, 2026. november 17. este: minden prompt három részből áll: SZEREP (egy mondat, LLM-persona, kiemelve),
# BRIEF (az addig felépült brief, inputként), FELADAT. Minden kis feladat új chatben indul. Feladatonként piros TIPP:
# kérdezzék meg nyugodtan a modellt, mi a feladat szerkezete (ettől a háttértudásuk is nő).
def _p(role, brief, task):
    return L('SZEREP: %s\nBRIEF: %s\nFELADAT: %s' % (role['hu'], brief['hu'], task['hu']),
             'ROLE: %s\nBRIEF: %s\nTASK: %s' % (role['en'], brief['en'], task['en']))

_B_SOFAR = L('[az eddig felépült briefed]', '[your brief so far]')

def _t(t, m, what, doc, p, ask, files=False, **kw):
    d = dict(t=t, m=m, what=what, doc=doc, p=p, out=doc, ask=ask)
    if files:
        d['files'] = True
    d.update(kw)
    return d

S3_TASKS = {
 1: _t(L('Vizuális irány', 'Visual direction'), 15,
       L('Nyiss új chatet. Döntsd el, mit viszel át a márka vizuális kódjaiból az új iparágba, és mit nem, és írj mellé 3 vizuális kulcsszót. A briefed a múlt heti márkabrief: ma ennek az aljára gyűjtöd az eredményeket.',
         "Open a new chat. Decide which of the brand's visual codes you carry over into the new industry and which you do not, and add 3 visual keywords. Your brief is last week's brand brief: today you collect the outputs at the bottom of it."),
       L('1. Vizuális irány: amit átviszel, amit nem, és 3 kulcsszó', '1. Visual direction: what you carry over, what you do not, and 3 keywords'),
       _p(L('Te most art director vagy egy márkaépítő ügynökségnél.', 'You are now an art director at a branding agency.'),
          L('[a briefed: a márkabrief, alatta a márka vizuális kódjai az 1. alkalom elemzéséből]', "[your brief: the brand brief, with the brand's visual codes from your session 1 analysis underneath]"),
          L('Órai játékban azt találjuk ki, milyen lenne, ha a [márka] a nevével és a logójával együtt [új kategória] lenne. A brief alapján javasolj vizuális irányt az új iparágra: a márka vizuális kódjai közül (színek, formák, betűk, képi stílus) mit viszünk át, és mit nem, mert az új iparágban nem működne. Adj 3 vizuális kulcsszót, ami a márka személyiségéből jön.\n\nA válaszod legyen rövid. Csak ezt a blokkot add vissza, hogy be tudjam másolni a briefembe:\nÁTVISZEM: … (3-5 elem, mindegyik mellé, miért)\nNEM VISZEM ÁT: … (1-3 elem, mindegyik mellé, miért)\n3 VIZUÁLIS KULCSSZÓ: …',
            "In a classroom game we work out what it would be like if [brand], name and logo included, were a [new category]. Based on the brief, suggest a visual direction for the new industry: which of the brand's visual codes (colours, shapes, type, image style) we carry over, and which we do not because they would not work in the new industry. Give 3 visual keywords that come from the brand's personality.\n\nKeep it short. Return only this block, so I can paste it into my brief:\nCARRY OVER: … (3-5 items, each with a reason)\nLEAVE BEHIND: … (1-3 items, each with a reason)\n3 VISUAL KEYWORDS: …")),
       L('Milyen részekből áll egy márka vizuális iránya, és mire figyel ilyenkor egy art director?', "What parts make up a brand's visual direction, and what does an art director pay attention to?")),
 2: _t(L('Színek és betűk', 'Colours and type'), 15,
       L('Új chatben rögzítsd a színeket HEX-kóddal és szereppel, és válassz két ingyenes betűtípust: egyet a címekhez, egyet a szöveghez. Innentől ezek a briefedben vannak, így minden promptba bekerülnek.',
         'In a new chat, fix the colours with HEX codes and roles, and choose two free typefaces: one for headings, one for text. From now on they are in your brief, so they go into every prompt.'),
       L('2. Színek HEX-kóddal és szereppel, 2 betűtípus', '2. Colours with HEX codes and roles, 2 typefaces'),
       _p(L('Te most arculattervező grafikus vagy.', 'You are now a brand identity designer.'),
          L('[az eddig felépült briefed, benne az 1. feladat eredménye]', '[your brief so far, including the output of task 1]'),
          L('A [márka] órai játékban [új kategória] lett, a neve és a logója marad. A briefben lévő vizuális irány alapján, webes kereséssel nézd meg a [márka] színeit, és javasolj színpalettát az új iparágra: fő szín, kiemelő szín (gombok, fontos jelzések) és 2 semleges szín (háttér, szöveg). Ahol a márka hivatalos színét megtaláltad, add meg a forrást, ahol becsülsz, jelöld. Javasolj két ingyenes betűtípust a Google Fontsból: egyet a címekhez, egyet a szöveghez és a számokhoz.\n\nCsak ezt a blokkot add vissza:\nFŐ SZÍN: #… · mire: …\nKIEMELŐ SZÍN: #… · mire: …\nSEMLEGES 1: #… · mire: …\nSEMLEGES 2: #… · mire: …\nCÍMBETŰ: … · miért: …\nSZÖVEGBETŰ: … · miért: …\nFORRÁS VAGY BECSLÉS: …',
            "In a classroom game, [brand] has become a [new category]; its name and logo stay. Based on the visual direction in the brief, use web search to look at [brand]'s colours, and suggest a colour palette for the new industry: main colour, accent colour (buttons, important signals) and 2 neutral colours (background, text). Where you found the brand's official colour, give the source; where you estimate, mark it. Suggest two free typefaces from Google Fonts: one for headings, one for text and numbers.\n\nReturn only this block:\nMAIN COLOUR: #… · for: …\nACCENT COLOUR: #… · for: …\nNEUTRAL 1: #… · for: …\nNEUTRAL 2: #… · for: …\nHEADING TYPEFACE: … · why: …\nTEXT TYPEFACE: … · why: …\nSOURCE OR ESTIMATE: …")),
       L('Hogyan épül fel egy márka színpalettája és betűrendszere? Mi a fő szín, a kiemelő szín és a semleges színek dolga?', "How are a brand's colour palette and type system built? What do the main, accent and neutral colours do?")),
 3: _t(L('Képi világ és alapprompt', 'Imagery and base prompt'), 15,
       L('Új chatben írd le, milyenek a márka képei: fény, szín, kik és mit csinálnak rajtuk, hol marad hely a szövegnek. Ebből készül az alapprompt, amit minden képprompt elejére bemásolsz.',
         "In a new chat, describe what the brand's images are like: light, colour, who is in them and what they are doing, where the space for text is. This becomes the base prompt you paste at the start of every image prompt."),
       L('3. Képi stílus és az alapprompt', '3. Image style and the base prompt'),
       _p(L('Te most art director vagy, aki kampányfotózásokat irányít.', 'You are now an art director who runs campaign photo shoots.'),
          L('[az eddig felépült briefed, benne az 1-2. feladat eredménye]', '[your brief so far, including the outputs of tasks 1-2]'),
          L('A [márka] órai játékban [új kategória] lett. A briefben lévő vizuális irány, színek és célcsoport alapján írd le a márka képi stílusát: fény és szín, kompozíció, kik szerepelnek a képeken és mit csinálnak, mi nem szerepelhet. Utána írj belőle egy legfeljebb 60 szavas alappromptot képgeneráláshoz, amit minden későbbi képprompt elejére be tudok másolni. Ne kérj szöveget vagy logót a képre.\n\nCsak ezt a blokkot add vissza:\nFÉNY ÉS SZÍN: …\nKOMPOZÍCIÓ: …\nKIK ÉS MIT CSINÁLNAK: …\nAMI NEM SZEREPELHET: …\nALAPPROMPT: …',
            "In a classroom game, [brand] has become a [new category]. Based on the visual direction, colours and target audience in the brief, describe the brand's image style: light and colour, composition, who appears in the images and what they are doing, what must not appear. Then turn it into a base prompt for image generation of at most 60 words that I can paste at the start of every later image prompt. Do not ask for text or a logo in the image.\n\nReturn only this block:\nLIGHT AND COLOUR: …\nCOMPOSITION: …\nWHO AND WHAT THEY DO: …\nMUST NOT APPEAR: …\nBASE PROMPT: …")),
       L('Mit tartalmaz egy jó képi stílusleírás vagy fotós brief, és mire való a moodboard?', 'What goes into a good image style description or photo brief, and what is a moodboard for?')),
 4: _t(L('Három kulcsvizuál', 'Three key visuals'), 25,
       L('Nyiss új chatet egy képgenerálóban (például ChatGPT vagy Gemini), és készíts 3 kulcsvizuált az alappromptból. Jelöld meg, melyik a kampány fő képe. Előbb a promptot csiszold, csak utána generálj.',
         "Open a new chat in an image generator (for example ChatGPT or Gemini) and make 3 key visuals from the base prompt. Mark which one is the campaign's main image. Polish the prompt first; generate only after that."),
       L('3 kép a mappádba, ebből 1 a fő kulcsvizuál. A 3 ötlet és a képpromptok a briefedbe.', '3 images into your folder, 1 of them the main key visual. The 3 ideas and the image prompts into your brief.'),
       _p(L('Te most art director vagy egy reklámügynökségnél, és kampány-kulcsvizuálokat tervezel.', 'You are now an art director at an advertising agency, designing campaign key visuals.'),
          L('[az eddig felépült briefed, benne az alapprompt]', '[your brief so far, including the base prompt]'),
          L('A [márka] órai játékban [új kategória] lett. A briefben lévő ígéret és alapprompt alapján írj 3 különböző kulcsvizuál-ötletet a bevezető kampányhoz. Mindegyik egy gondolatot mutasson az ígéretből, szöveg és logó nélkül, és hagyjon helyet a feliratnak. Minden képprompt az alappromptommal kezdődjön. Még ne generálj: ha valami hiányzik, előbb kérdezz. Amikor kiválasztottam egyet, csak azt generáld le, utána a következőt.\n\nElőször csak ezt a blokkot add vissza:\n1. ÖTLET: … · KÉPPROMPT: …\n2. ÖTLET: … · KÉPPROMPT: …\n3. ÖTLET: … · KÉPPROMPT: …\nHOL MARAD HELY A SZÖVEGNEK: …',
            'In a classroom game, [brand] has become a [new category]. Based on the promise and the base prompt in the brief, write 3 different key visual ideas for the launch campaign. Each should show one idea from the promise, without text or logo, and leave space for the headline. Every image prompt should start with my base prompt. Do not generate yet: if anything is missing, ask first. When I have chosen one, generate only that one, then the next.\n\nFirst return only this block:\nIDEA 1: … · IMAGE PROMPT: …\nIDEA 2: … · IMAGE PROMPT: …\nIDEA 3: … · IMAGE PROMPT: …\nWHERE THE SPACE FOR TEXT IS: …')),
       L('Mitől jó egy kampány kulcsvizuálja, és milyen részekből áll?', 'What makes a good campaign key visual, and what parts does it have?'),
       files=True),
 5: _t(L('Három posztsablon', 'Three post templates'), 20,
       L('Új chatben készíts 3 posztsablont az arculattal: négyzetes poszt, 9:16-os story és carousel nyitódia. Claude Designban, Canvában, vagy Claude-ban artifactként.',
         'In a new chat, make 3 post templates with the identity: square post, 9:16 story and carousel opening slide. In Claude Design, in Canva, or in Claude as an artifact.'),
       L('3 posztsablon: link vagy képernyőkép a mappádba', '3 post templates: a link or a screenshot into your folder'),
       _p(L('Te most közösségimédia-designer vagy.', 'You are now a social media designer.'), _B_SOFAR,
          L('Csatoltam a logót és a fő kulcsvizuált. Készíts 3 közösségimédia-posztsablont a [márka] márkának, ami órai játékban [új kategória] lett. Egy oldalon, egymás mellett kérem: négyzetes poszt (1080×1080), 9:16-os story (1080×1920) és carousel nyitódia (1080×1350). A színeket és a betűket a briefből vedd, a betűket a Google Fontsból töltsd be. Mindegyiken legyen hely a címnek, egy rövid szövegnek és a logónak. A szöveg helyén egyelőre a brief ígérete álljon. Ne találj ki új színt vagy betűt. Ha a csatolt képet nem tudod beépíteni, tegyél a helyére jól látható képhelyet, és írd meg, hogyan cseréljem be.\n\nA sablonok után röviden add vissza:\nSABLONOK: … (mi hol van rajtuk)\nAMIT MÉG CSERÉLNI KELL: …',
            'I have attached the logo and the main key visual. Make 3 social media post templates for [brand], which in a classroom game has become a [new category]. On one page, side by side: square post (1080×1080), 9:16 story (1080×1920) and carousel opening slide (1080×1350). Take the colours and type from the brief, and load the typefaces from Google Fonts. Each should have room for a headline, a short text and the logo. For now, put the promise from the brief in place of the text. Do not invent new colours or typefaces. If you cannot build in the attached image, put a clearly visible image placeholder in its place and tell me how to swap it in.\n\nAfter the templates, briefly return:\nTEMPLATES: … (what is where on them)\nSTILL TO BE SWAPPED: …')),
       L('Milyen elemekből áll egy jó közösségimédia-posztsablon, és mit rögzít egy sablon?', 'What elements make up a good social media post template, and what does a template fix?'),
       files=True),
 6: _t(L('Két banner', 'Two banners'), 15,
       L('Új chatben készíts egy 300×250-es és egy 728×90-es HTML-bannert a fő kulcsvizuállal, Claude-ban artifactként. A szlogen még nincs meg: most a márkanév és az ígéret kerül rá, a szlogent az 5. alkalmon cseréled be.',
         'In a new chat, make a 300×250 and a 728×90 HTML banner with the main key visual, in Claude as an artifact. There is no slogan yet: for now the brand name and the promise go on it; you swap in the slogan in session 5.'),
       L('2 banner: link vagy képernyőkép a mappádba', '2 banners: a link or a screenshot into your folder'),
       _p(L('Te most digitális designer vagy, aki display bannereket készít.', 'You are now a digital designer who makes display banners.'), _B_SOFAR,
          L('Csatoltam a logót és a fő kulcsvizuált. Készíts két HTML-bannert a [márka] márkának, ami órai játékban [új kategória] lett: 300×250 és 728×90 pixel, egy oldalon, artifactként. A színeket és a betűket a briefből vedd. Szöveg: a márkanév, a brief ígérete, és egy gomb: [a gomb szövege, például Fedezd fel]. A 728×90-esen legfeljebb egy sor szöveg legyen. Ha a csatolt képet nem tudod beépíteni, tegyél a helyére jól látható képhelyet, és írd meg, hogyan cseréljem be.\n\nA bannerek után röviden add vissza:\nBANNEREK: … (mi van rajtuk)\nA SZLOGEN HELYE: … (hová kerül majd)',
            'I have attached the logo and the main key visual. Make two HTML banners for [brand], which in a classroom game has become a [new category]: 300×250 and 728×90 pixels, on one page, as an artifact. Take the colours and type from the brief. Text: the brand name, the promise from the brief, and a button: [button text, for example Discover]. The 728×90 should have at most one line of text. If you cannot build in the attached image, put a clearly visible image placeholder in its place and tell me how to swap it in.\n\nAfter the banners, briefly return:\nBANNERS: … (what is on them)\nWHERE THE SLOGAN GOES: … (where it will go later)')),
       L('Milyen részei vannak egy display bannernek, és mire kell figyelni a kis méreteknél?', 'What parts does a display banner have, and what matters at small sizes?'),
       files=True),
 7: _t(L('Óriásplakát-mockup', 'Billboard mock-up'), 15,
       L('Új chatben, egy képgenerálóval készíts óriásplakát-mockupot: a fő kulcsvizuál egy valódi utcai helyzetben, a márkanévvel és pár szóval. A feliratot betűről betűre ellenőrizd.',
         'In a new chat, with an image generator, make a billboard mock-up: the main key visual in a real street setting, with the brand name and a few words. Check the lettering letter by letter.'),
       L('Plakát-mockup a mappádba, a képprompt a briefedbe', 'Billboard mock-up into your folder, the image prompt into your brief'),
       _p(L('Te most art director vagy, aki óriásplakát-kampányokat tervez.', 'You are now an art director who designs billboard campaigns.'), _B_SOFAR,
          L('Csatoltam a kampány fő kulcsvizuálját. A [márka] órai játékban [új kategória] lett. Készíts belőle óriásplakát-mockupot: a kép egy utcai óriásplakáton, valósághű városi környezetben, [helyszín és napszak, például esti buszmegálló Budapesten]. A plakáton a képen kívül csak a márkanév és a brief ígérete legyen, legfeljebb 6 szóban. A stílust a brief alappromptjából vedd. Generálás előtt írd le egy mondatban, mit fogsz készíteni, és ha valami hiányzik, kérdezz.\n\nA kép után csak ezt add vissza:\nHELYSZÍN: …\nSZÖVEG A PLAKÁTON: …\nKÉPPROMPT: …',
            "I have attached the campaign's main key visual. In a classroom game, [brand] has become a [new category]. Turn it into a billboard mock-up: the image on a street billboard, in a realistic city setting, [place and time of day, for example a bus stop in Budapest in the evening]. Apart from the image, the billboard should only carry the brand name and the promise from the brief, in at most 6 words. Take the style from the base prompt in the brief. Before generating, describe in one sentence what you will make, and if anything is missing, ask.\n\nAfter the image, return only this:\nPLACE: …\nTEXT ON THE BILLBOARD: …\nIMAGE PROMPT: …")),
       L('Mitől működik egy óriásplakát, és milyen részekből áll?', 'What makes a billboard work, and what parts does it have?'),
       files=True),
 8: _t(L('Csomagolás vagy termék', 'Packaging or product'), 15,
       L('Új chatben gyűjtsd össze, hol találkozik a vevő a márkával az új iparágban. Válassz egyet, és készíts róla látványt egy képgenerálóval: csomagolás, termék vagy hely.',
         'In a new chat, collect where the customer meets the brand in the new industry. Choose one and make a visual of it with an image generator: packaging, product or place.'),
       L('Csomagolás- vagy terméklátvány a mappádba. Az 5 érintkezési pont és a képprompt a briefedbe.', 'Packaging or product visual into your folder. The 5 touchpoints and the image prompt into your brief.'),
       _p(L('Te most márkaélmény-tervező vagy, aki a márka érintkezési pontjait, csomagolását és termékeit tervezi.', "You are now a brand experience designer who designs the brand's touchpoints, packaging and products."), _B_SOFAR,
          L('A [márka] órai játékban [új kategória] lett, a neve és a logója marad. A brief alapján sorolj fel 5 helyet vagy tárgyat, ahol a vevő találkozik a márkával az új iparágban (termék, csomagolás, hely, egyenruha, digitális felület), és mindegyikhez írd le egy mondatban, hogyan látszana rajta a márka. Mondd meg, melyik mutatná meg a legjobban, de a választás az enyém. Ha választottam, írd meg hozzá a képpromptot a brief alappromptjával kezdve, és generáld le.\n\nElőször csak ezt a blokkot add vissza:\nÉRINTKEZÉSI PONTOK:\n1. …\n2. …\n3. …\n4. …\n5. …\nJAVASLAT: … (egy mondat, miért)',
            'In a classroom game, [brand] has become a [new category]; its name and logo stay. Based on the brief, list 5 places or objects where the customer meets the brand in the new industry (product, packaging, place, uniform, digital surface), and for each write one sentence on how the brand would show on it. Tell me which would show the brand best, but the choice is mine. Once I have chosen, write the image prompt for it, starting with the base prompt from the brief, and generate it.\n\nFirst return only this block:\nTOUCHPOINTS:\n1. …\n2. …\n3. …\n4. …\n5. …\nSUGGESTION: … (one sentence on why)')),
       L('Mi az az érintkezési pont (touchpoint), és mit tartalmaz egy csomagolásterv?', 'What is a touchpoint, and what goes into a packaging design?'),
       files=True),
 9: _t(L('Az arculati kézikönyv összerakása', 'Putting the brand guide together'), 20,
       L('Új chatben rakd össze a briefből az arculati kézikönyvet Claude Designban, vagy Claude-ban artifactként, és mentsd PDF-be (artifactnál a böngésző nyomtatás funkciójával). Az AI csak rendezzen, ne találjon ki új színt, betűt vagy szabályt.',
         "In a new chat, put the brand guide together from your brief in Claude Design, or in Claude as an artifact, and save it as a PDF (for an artifact, with the browser's print function). The AI should only organise it, not invent new colours, typefaces or rules."),
       L('Arculati kézikönyv PDF: ez készül el mára. Ezzel, a briefeddel, a képekkel és a sablonokkal jössz a 4. alkalomra.', 'Brand guide PDF: this is what is done by today. You bring it, your brief, the images and the templates to session 4.'),
       _p(L('Te most senior brand designer vagy, aki arculati kézikönyvet ír.', 'You are now a senior brand designer writing a brand guide.'),
          L('[az eddig felépült briefed: a márkabrief és a mai 1-8. feladat eredménye]', "[your brief so far: the brand brief and the outputs of today's tasks 1-8]"),
          L('Csatoltam a logót és a mai képeket. A briefből készíts arculati kézikönyvet a [márka] márkának, ami órai játékban [új kategória] lett. Csak rendezd, amit a brief tartalmaz: ne találj ki új színt, betűt vagy szabályt, és ha egy képet nem tudsz beépíteni, hagyj neki jól látható helyet.\n\nEzek a fejezetek legyenek benne, mindegyik külön oldalon:\nBORÍTÓ: a márkanév és a „Mi lenne, ha…” mondat\nLOGÓ ÉS HASZNÁLATA: védőtér, legkisebb méret, 3 tilos példa\nSZÍNEK: HEX-kóddal és szereppel\nBETŰK: cím és szöveg, mintával\nKÉPI STÍLUS: a szabályok, 3 példaképpel\nHANGNEM: a briefből, egy példamondattal\nSZABAD ÉS TILOS: 3-3 példa\nALKALMAZÁSOK: kulcsvizuál, poszt, banner, plakát, csomagolás\nHIÁNYZIK VAGY ELLENTMOND: … (a végén, külön)',
            'I have attached the logo and today\'s images. From the brief, make a brand guide for [brand], which in a classroom game has become a [new category]. Only organise what the brief contains: do not invent new colours, typefaces or rules, and if you cannot build in an image, leave clearly visible space for it.\n\nIt should have these chapters, each on its own page:\nCOVER: the brand name and the "What if…" sentence\nLOGO AND ITS USE: clear space, minimum size, 3 examples of misuse\nCOLOURS: with HEX codes and roles\nTYPE: headings and text, with samples\nIMAGE STYLE: the rules, with 3 example images\nTONE OF VOICE: from the brief, with an example sentence\nDO AND DON\'T: 3 examples each\nAPPLICATIONS: key visual, post, banner, billboard, packaging\nMISSING OR CONTRADICTORY: … (at the end, separately)')),
       L('Mit tartalmaz egy arculati kézikönyv, és milyen sorrendben szokták felépíteni?', 'What does a brand guide contain, and in what order is it usually built?'),
       files=True),
}

_B_IFANY = L('[az eddig felépült briefed, ha van]', '[your brief so far, if you have one]')
TIP_PROMPTS.update({
 'draftbrief3': _p(L('Te most márkastratéga vagy.', 'You are now a brand strategist.'), L('[amit eddig elkészítettél, ha van]', '[whatever you have made so far, if anything]'),
     L(_G['hu'] + 'Ebből készíts egyoldalas márkabrief-vázlatot. Ahol nincs anyagom, ott tegyél javaslatot, és jelöld a JAVASLAT szóval, hogy lássam, mit kell még átnéznem.\n\nPontosan ezekkel a címekkel add vissza:\nMI LENNE, HA: …\nCÉLCSOPORT: …\nPERSONÁK: …\nPOZICIONÁLÁS: …\nÍGÉRET: …\nÉRTÉKEK: …\nSZEMÉLYISÉG ÉS HANGNEM: …\nÁRSZINT: …',
       _G['en'] + "Turn it into a one-page draft brand brief. Where I have no material, make a suggestion and mark it with the word SUGGESTION, so I can see what I still need to check.\n\nReturn it with exactly these headings:\nWHAT IF: …\nTARGET AUDIENCE: …\nPERSONAS: …\nPOSITIONING: …\nPROMISE: …\nVALUES: …\nPERSONALITY AND TONE: …\nPRICE LEVEL: …")),
 'promise3': _p(L('Te most márkastratéga vagy.', 'You are now a brand strategist.'), _B_IFANY,
     L(_G['hu'] + 'Javasolj egy ígéretet (egy rövid mondat, amit egy vevő a barátjának is elmondana) és 3 értéket, amelyek a valódi [márka] márkán is látszanak. Ne írj olyat, ami bármelyik márkára igaz lehetne.\n\nCsak ezt a blokkot add vissza:\nÍGÉRET: …\nÉRTÉK 1: … · a gyakorlatban: …\nÉRTÉK 2: … · a gyakorlatban: …\nÉRTÉK 3: … · a gyakorlatban: …',
       _G['en'] + 'Suggest a promise (one short sentence a customer would also tell a friend) and 3 values that can also be seen in the real [brand]. Do not write anything that could be true of any brand.\n\nReturn only this block:\nPROMISE: …\nVALUE 1: … · in practice: …\nVALUE 2: … · in practice: …\nVALUE 3: … · in practice: …')),
 'visualcodes': _p(L('Te most márkakutató vagy, aki vizuális kódokat elemez.', 'You are now a brand researcher who analyses visual codes.'), _B_IFANY,
     L(_G['hu'] + 'Webes kereséssel nézd meg a [márka] vizuális kódjait: színek (hivatalos HEX-kóddal, ha találsz rá forrást), formák és visszatérő jelek, betűtípusok, képi stílus, a logó jellemzői. Csak forrással alátámasztott dolgot írj, és ha valamiben nem vagy biztos, jelezd.\n\nA válaszod legyen rövid. Csak ezt a blokkot add vissza:\nSZÍNEK: …\nFORMÁK ÉS JELEK: …\nBETŰK: …\nKÉPI STÍLUS: …\nLOGÓ: …\nFORRÁSOK: …\nBIZONYTALAN: …',
       _G['en'] + "Use web search to look at [brand]'s visual codes: colours (with official HEX codes if you find a source), shapes and recurring signs, typefaces, image style, the features of the logo. Only write what you can back with a source, and flag anything you are not sure about.\n\nKeep it short. Return only this block:\nCOLOURS: …\nSHAPES AND SIGNS: …\nTYPE: …\nIMAGE STYLE: …\nLOGO: …\nSOURCES: …\nUNSURE: …")),
 'visdir': _p(L('Te most art director vagy egy márkaépítő ügynökségnél.', 'You are now an art director at a branding agency.'), _B_IFANY,
     L(_G['hu'] + 'Webes kereséssel nézd meg a [márka] vizuális kódjait (színek, formák, betűk, képi stílus), és a brief alapján javasolj vizuális irányt az új iparágra: mit viszünk át, és mit nem, mert az új iparágban nem működne. Adj 3 vizuális kulcsszót.\n\nCsak ezt a blokkot add vissza:\nÁTVISZEM: … (3-5 elem, mindegyik mellé, miért)\nNEM VISZEM ÁT: … (1-3 elem, mindegyik mellé, miért)\n3 VIZUÁLIS KULCSSZÓ: …',
       _G['en'] + "Use web search to look at [brand]'s visual codes (colours, shapes, type, image style), and based on the brief suggest a visual direction for the new industry: what we carry over, and what we do not because it would not work in the new industry. Give 3 visual keywords.\n\nReturn only this block:\nCARRY OVER: … (3-5 items, each with a reason)\nLEAVE BEHIND: … (1-3 items, each with a reason)\n3 VISUAL KEYWORDS: …")),
 'colors': _p(L('Te most arculattervező grafikus vagy.', 'You are now a brand identity designer.'), _B_IFANY,
     L(_G['hu'] + 'Webes kereséssel nézd meg a [márka] színeit, és javasolj színpalettát az új iparágra: fő szín, kiemelő szín és 2 semleges szín, HEX-kóddal. Javasolj két ingyenes betűtípust a Google Fontsból: egyet a címekhez, egyet a szöveghez és a számokhoz. Ahol becsülsz, jelöld.\n\nCsak ezt a blokkot add vissza:\nFŐ SZÍN: #… · mire: …\nKIEMELŐ SZÍN: #… · mire: …\nSEMLEGES 1: #… · mire: …\nSEMLEGES 2: #… · mire: …\nCÍMBETŰ: …\nSZÖVEGBETŰ: …\nFORRÁS VAGY BECSLÉS: …',
       _G['en'] + "Use web search to look at [brand]'s colours, and suggest a colour palette for the new industry: main colour, accent colour and 2 neutral colours, with HEX codes. Suggest two free typefaces from Google Fonts: one for headings, one for text and numbers. Mark where you estimate.\n\nReturn only this block:\nMAIN COLOUR: #… · for: …\nACCENT COLOUR: #… · for: …\nNEUTRAL 1: #… · for: …\nNEUTRAL 2: #… · for: …\nHEADING TYPEFACE: …\nTEXT TYPEFACE: …\nSOURCE OR ESTIMATE: …")),
 'styleprompt': _p(L('Te most art director vagy, aki kampányfotózásokat irányít.', 'You are now an art director who runs campaign photo shoots.'), _B_IFANY,
     L(_G['hu'] + 'A brief alapján írd le a márka képi stílusát az új iparágban: fény és szín, kompozíció, kik szerepelnek a képeken és mit csinálnak, mi nem szerepelhet. Ha a briefben nincsenek színek, javasolj. Utána írj belőle egy legfeljebb 60 szavas alappromptot képgeneráláshoz, amit minden képprompt elejére be tudok másolni. Ne kérj szöveget vagy logót a képre.\n\nCsak ezt a blokkot add vissza:\nFÉNY ÉS SZÍN: …\nKOMPOZÍCIÓ: …\nKIK ÉS MIT CSINÁLNAK: …\nAMI NEM SZEREPELHET: …\nALAPPROMPT: …',
       _G['en'] + "Based on the brief, describe the brand's image style in the new industry: light and colour, composition, who appears in the images and what they are doing, what must not appear. If the brief has no colours, suggest some. Then turn it into a base prompt for image generation of at most 60 words that I can paste at the start of every image prompt. Do not ask for text or a logo in the image.\n\nReturn only this block:\nLIGHT AND COLOUR: …\nCOMPOSITION: …\nWHO AND WHAT THEY DO: …\nMUST NOT APPEAR: …\nBASE PROMPT: …")),
 'kvquick': _p(L('Te most art director vagy egy reklámügynökségnél.', 'You are now an art director at an advertising agency.'), _B_IFANY,
     L(_G['hu'] + 'A briefben lévő ígéret és alapprompt alapján (ha nincsenek benne, javasolj) írj egy kulcsvizuál-ötletet a bevezető kampányhoz: egy gondolatot mutasson az ígéretből, szöveg és logó nélkül, és hagyjon helyet a feliratnak. Írd meg hozzá a képpromptot, és generáld le a képet. Ha nem tudsz képet generálni, csak a blokkot add vissza, és a képpromptot beviszem egy képgenerálóba.\n\nA kép mellé csak ezt add vissza:\nÖTLET: …\nKÉPPROMPT: …\nHOL MARAD HELY A SZÖVEGNEK: …',
       _G['en'] + 'Based on the promise and the base prompt in the brief (if they are missing, suggest them), write one key visual idea for the launch campaign: it should show one idea from the promise, without text or logo, and leave space for the headline. Write the image prompt for it and generate the image. If you cannot generate images, return only the block, and I will take the image prompt to an image generator.\n\nWith the image, return only this:\nIDEA: …\nIMAGE PROMPT: …\nWHERE THE SPACE FOR TEXT IS: …')),
 'logo': L('SZEREP: Te most egy ügynökség asszisztense vagy, aki márkaanyagokat gyűjt.\nFELADAT: Egy órai játékban a [márka] márkával dolgozom, és szükségem van a hivatalos logójára. Webes kereséssel keresd meg, honnan tölthető le jó minőségben: a márka hivatalos oldala vagy sajtóanyaga, vagy a Wikimedia Commons. Csak létező linket adj meg, és ha nem találsz, mondd meg.\n\nCsak ezt a blokkot add vissza:\nLINK: …\nFORMÁTUM: … (SVG vagy PNG)\nSZÍNVÁLTOZATOK: … (színes, fehér, fekete, ha van)',
           "ROLE: You are now an agency assistant who collects brand materials.\nTASK: In a classroom game I am working with the [brand] brand, and I need its official logo. Use web search to find where it can be downloaded in good quality: the brand's official site or press materials, or Wikimedia Commons. Only give links that exist, and if you cannot find one, say so.\n\nReturn only this block:\nLINK: …\nFORMAT: … (SVG or PNG)\nCOLOUR VERSIONS: … (colour, white, black, if any)"),
 'draftguide': _p(L('Te most senior brand designer vagy.', 'You are now a senior brand designer.'), L('[az eddig felépült briefed, amennyi megvan]', '[your brief so far, as much as you have]'),
     L(_G['hu'] + 'Csatoltam a logót és a képeket, ha vannak. A briefből készíts arculati kézikönyv-vázlatot. Ahol nincs anyagom, ott tegyél javaslatot, és jelöld a JAVASLAT szóval, hogy lássam, mit kell még átnéznem.\n\nPontosan ezekkel a fejezetekkel add vissza:\nLOGÓ ÉS HASZNÁLATA: …\nSZÍNEK: … (HEX-kóddal és szereppel)\nBETŰK: …\nKÉPI STÍLUS: …\nHANGNEM: …\nSZABAD ÉS TILOS: …\nALKALMAZÁSOK: …',
       _G['en'] + "I have attached the logo and the images, if any. From the brief, make a draft brand guide. Where I have no material, make a suggestion and mark it with the word SUGGESTION, so I can see what I still need to check.\n\nReturn it with exactly these chapters:\nLOGO AND ITS USE: …\nCOLOURS: … (with HEX codes and roles)\nTYPE: …\nIMAGE STYLE: …\nTONE OF VOICE: …\nDO AND DON'T: …\nAPPLICATIONS: …")),
})
TIP_NOTE.update({
 'kvquick': L('Készítsd el most új chatben, egy képgenerálóban (például ChatGPT), és mentsd a képet a mappádba.', 'Make it now in a new chat in an image generator (for example ChatGPT), and save the image into your folder.'),
 'logo': L('Keresd meg most ezzel a prompttal, töltsd le a logót, és mentsd a mappádba.', 'Find it now with this prompt, download the logo, and save it into your folder.'),
})

_N_BRIEF = (L('A briefed: a múlt heti márkabrief', 'Your brief: last week\'s brand brief'), 'draftbrief3')
_N_PROMISE = (L('A briefben: az ígéret', 'In your brief: the promise'), 'promise3')
_N_VISDIR = (L('A briefben: az 1. feladat vizuális iránya', 'In your brief: the visual direction from task 1'), 'visdir')
_N_COLORS = (L('A briefben: a 2. feladat színei és betűi', 'In your brief: the colours and type from task 2'), 'colors')
_N_STYLE = (L('A briefben: a 3. feladat alappromptja', 'In your brief: the base prompt from task 3'), 'styleprompt')
_N_KV = (L('A 4. feladat fő kulcsvizuálja, képfájlként', 'The main key visual from task 4, as an image file'), 'kvquick')
_N_LOGO = (L('A logód fájlja', 'Your logo file'), 'logo')
S3_NEED = {
 1: [_N_BRIEF, (L('A márka vizuális kódjai az 1. alkalom elemzéséből', "The brand's visual codes from your session 1 analysis"), 'visualcodes')],
 2: [_N_VISDIR],
 3: [_N_VISDIR, _N_COLORS, (L('A briefben: a célcsoport és a két persona', 'In your brief: the target audience and the two personas'), 'draftbrief3')],
 4: [_N_STYLE, _N_PROMISE],
 5: [_N_COLORS, _N_KV, _N_LOGO, _N_PROMISE],
 6: [_N_COLORS, _N_KV, _N_LOGO, _N_PROMISE],
 7: [_N_KV, _N_STYLE, _N_PROMISE],
 8: [(L('A briefben: a 2. feladat színei', 'In your brief: the colours from task 2'), 'colors'), _N_STYLE],
 9: [(L('A briefed: a márkabrief és az 1-8. feladat eredménye', 'Your brief: the brand brief and the outputs of tasks 1-8'), 'draftguide'),
     (L('A logód és a mai képek', "Your logo and today's images"), 'logo'),
     (L('A briefben: a hangnem', 'In your brief: the tone of voice'), 'draftbrief3')],
}
SPEC[3] = dict(tasks=S3_TASKS, theory=S3_THEORY, need=S3_NEED, ex=EXAMPLE3,
               reslab=L('Eredmény, a briefedbe:', 'Output, into your brief:'),
               tipnote=L('Készítsd el most új chatben ezzel a prompttal, és másold be a briefedbe.', 'Make it now in a new chat with this prompt, and paste it into your brief.'))
