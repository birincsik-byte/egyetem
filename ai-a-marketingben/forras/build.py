# -*- coding: utf-8 -*-
import html, re, os, math, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from content import *

OUT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(OUT, exist_ok=True)
FN = lambda n: 'ai-marketing-2026-alkalom-%d.html' % n
LANGS = ('hu', 'en')

def e(s):
    return html.escape(s, quote=False)

def pmark(s):
    s = e(s)
    return re.sub(r'\[[^\]\n]+\]', lambda m: '<mark>' + m.group(0) + '</mark>', s)

def bi(hu, en, tag='span'):
    return '<%s class="hu">%s</%s><%s class="en">%s</%s>' % (tag, hu, tag, tag, en, tag)

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,300;9..144,500;9..144,700&family=Source+Sans+3:wght@400;600&display=swap" rel="stylesheet">'

CSS = r"""
:root{--paper:#F7F6F1;--ink:#1B1F3A;--ink-soft:#5A5E78;--line:#D9D7CE;--cobalt:#1E4BD8;--marker:#F2C94C;--cream:#FCEFC2;
--display:'Fraunces',Georgia,'Times New Roman',serif;--body:'Source Sans 3','Segoe UI',Helvetica,Arial,sans-serif;
--t-xl:3.6rem;--t-h2:2.2rem;--t-h3:1.3rem;--t-lead:1.25rem;--t-body:1rem;--t-sm:max(.8rem,18px);--sh:0 14px 30px -22px rgba(27,31,58,.45)}
*{box-sizing:border-box;margin:0;padding:0}
html,body{height:100%;background:var(--paper);color:var(--ink);font-family:var(--body);font-size:clamp(19px,min(1.55vw,2.55vh),28px);line-height:1.45;overflow:hidden}
button{font:inherit;color:inherit;background:none;border:0;cursor:pointer}
html[lang=en] .hu,html[lang=hu] .en{display:none!important}

/* évadsáv: vékony csík, ráállva lenyílik (a nappali deck mintájára) */
.strip{position:fixed;top:0;left:0;right:0;height:auto;max-height:10px;overflow:hidden;display:flex;align-items:stretch;border-bottom:1px solid var(--line);background:var(--paper);z-index:45;transition:max-height .2s,box-shadow .2s}
.strip:hover,.strip:focus-within{max-height:240px;box-shadow:0 10px 24px -14px rgba(27,31,58,.45)}
.strip a{flex:1;display:flex;flex-direction:column;justify-content:center;padding:0 14px;text-decoration:none;color:var(--ink-soft);border-right:1px solid var(--line);font-size:clamp(12px,.8vw,15px);line-height:1.2}
.strip a:last-child{border-right:0}
.strip a>*{opacity:0;transition:opacity .15s}
.strip:hover a>*,.strip:focus-within a>*{opacity:1}
.strip a b{font-family:var(--display);font-weight:500;font-size:1.25em;color:var(--ink)}
.strip a.on{background:var(--marker);color:var(--ink)}
.strip a.off{opacity:.45;cursor:default}
.strip a.off b{color:var(--ink-soft)}
.strip a:focus-visible{outline:3px solid var(--cobalt);outline-offset:-3px}

.deck{position:absolute;inset:0}
.slide{position:absolute;inset:0;padding:8vh 7vw 9vh;display:none;overflow-y:auto;flex-direction:column;justify-content:flex-start;max-width:1720px;margin:0 auto;font-size:var(--t-body)}
.slide.cur{display:flex}
/* a cím mindig ugyanott: a diák felülről indulnak, csak a címlap van középen */
.slide:has(> h1.cover)>:first-child{margin-top:auto}
.slide:has(> h1.cover)>:last-child{margin-bottom:auto}
.kicker{font-size:var(--t-sm);color:var(--ink-soft);margin-bottom:.9em}
.kicker .lt{display:inline-block;background:var(--cobalt);color:#fff;border-radius:99px;padding:.05em .75em;margin-right:.7em;font-weight:600}
h1{font-family:var(--display);font-weight:500;font-size:var(--t-xl);line-height:1.02;letter-spacing:-.01em;margin-bottom:.3em}
h2{font-family:var(--display);font-weight:500;font-size:var(--t-h2);line-height:1.12;margin-bottom:.6em;max-width:30ch}
h3{font-family:var(--display);font-weight:500;font-size:var(--t-h3);line-height:1.2;margin-bottom:.3em}
p{max-width:62ch}
p+p{margin-top:.6em}
.lead{font-size:var(--t-lead);max-width:52ch}
.hl{background:linear-gradient(transparent 55%,var(--marker) 55%);padding:0 .1em}
.muted{color:var(--ink-soft)}
.small{font-size:var(--t-sm)}
.note{color:var(--ink-soft);border-left:3px solid var(--marker);padding:.1em 0 .1em .8em;max-width:76ch;margin-top:1.1em;line-height:1.4}
.slide a{color:var(--cobalt)}
.rule{border:0;border-top:1px solid var(--line);margin:1.2em 0;max-width:60em}
.card{background:#fff;border-radius:12px;padding:.85em 1.2em;box-shadow:var(--sh);border-top:4px solid var(--marker)}
/* egy szín: minden kártya teteje sárga (oktatói kérés, 2026. november 11.) */
/* ahol több kártya áll egymás mellett, sorszámot kapnak a jobb felső sarokban */
.thg,.grid3,.cols{counter-reset:kc}
.thg>.card,.grid3>.card,.cols>.card{counter-increment:kc;position:relative}
.thg>.card::after,.grid3>.card::after,.cols>.card::after{content:counter(kc);position:absolute;right:.85em;top:.6em;font-family:var(--display);font-weight:500;color:var(--cobalt);font-size:1.3em;line-height:1}
.thg>.card h3,.grid3>.card h3,.cols>.card h3{padding-right:1.6em}
.card.alt{border-top-color:var(--marker)}
.card p{max-width:none}
.cols{display:grid;grid-template-columns:1fr 1fr;gap:2vw;align-items:start;max-width:72em}
.cols3{display:grid;grid-template-columns:repeat(3,1fr);gap:1.6vw;align-items:stretch;max-width:76em}

/* címlap: innen, ide */
.c1shift{display:grid;grid-template-columns:minmax(0,.85fr) auto minmax(0,1.5fr);gap:.2em 1.4em;align-items:center;margin-top:1.3rem;padding:1.1rem 1.5rem;background:#fff;border:1px solid var(--line);border-radius:14px;max-width:60rem}
.c1shift small,.c1tem small{display:block;font-size:max(.62rem,13px);letter-spacing:.12em;text-transform:uppercase;font-weight:600;color:var(--ink-soft);margin-bottom:.45em}
.c1shift .from p{color:var(--ink-soft);line-height:1.35}
.c1shift .arr{display:grid;place-items:center;width:2.2rem;height:2.2rem;border-radius:50%;background:var(--cobalt);color:#fff;font-size:1.1rem;line-height:1;margin-top:1.1em}
.c1shift .to p{font-size:var(--t-lead);line-height:1.3;font-weight:500}
.c1shift .add{grid-column:1/-1;margin-top:.9rem;padding:.8rem 0 0 1rem;border-top:1px dashed var(--line);position:relative}
.c1shift .add::before{content:"";position:absolute;left:0;top:.85rem;bottom:.1rem;width:4px;border-radius:2px;background:var(--marker)}
.c1tem{display:flex;flex-wrap:wrap;align-items:center;gap:.45rem .5rem;margin-top:1.3rem;max-width:60rem}
.c1tem small{flex-basis:100%;margin-bottom:.1em}
.c1tem span.chip{font-size:var(--t-sm);border:1px solid var(--line);border-radius:99px;padding:.2em .9em;background:#fff}

h1.cover{font-size:calc(var(--t-xl) * 1.25);max-width:18ch;margin-bottom:.4em}

/* nagy gondolat */
.big{font-family:var(--display);font-weight:500;font-size:2.35rem;line-height:1.18;max-width:30ch;margin-bottom:.8em}
.triad{display:grid;grid-template-columns:repeat(3,1fr);gap:1.4vw;max-width:56em;margin-bottom:1.2em}
.triad div{border-top:4px solid var(--cobalt);padding-top:.5em;font-family:var(--display);font-weight:500;font-size:var(--t-h3);color:var(--cobalt)}

/* folyamat */
.flow{display:grid;grid-template-columns:1fr auto 1fr auto 1fr;gap:1vw;align-items:stretch;max-width:74em;margin-top:.4em}
.flow .arr{align-self:center;color:var(--cobalt);font-size:1.6em}
.flow .card h3{color:var(--cobalt)}

/* karmester */
.orch{width:min(46rem,100%,calc(46vh * 2.33));margin-top:.4em}
.orch svg{width:100%;height:auto;display:block}
.orch text{font-family:var(--body)}

/* számok */
.stat .num{font-family:var(--display);font-weight:500;font-size:2.4rem;line-height:1;color:var(--cobalt);display:block;margin-bottom:.25em}

/* öt blokk */
.blocks5{display:grid;grid-template-columns:repeat(5,1fr);gap:1vw;max-width:80em}
.blk{background:#fff;border-radius:12px;padding:.8em 1em 1em;box-shadow:var(--sh);border-top:4px solid var(--cobalt)}
.blk .n{font-family:var(--display);font-weight:500;font-size:2.1em;line-height:1;color:var(--cobalt);display:block;margin-bottom:.15em}
.blk p{font-size:var(--t-sm);color:var(--ink-soft)}

/* hat alkalom */
.season{display:grid;grid-template-columns:repeat(6,1fr);gap:.9vw;max-width:84em}
.slide .ep{display:block;text-decoration:none;color:var(--ink);background:#fff;border-radius:12px;border-top:4px solid var(--line);padding:.7em .9em .9em;box-shadow:var(--sh);font-size:var(--t-sm);line-height:1.3;transition:transform .15s,border-color .15s}
.ep .n{font-family:var(--display);font-weight:500;font-size:2em;line-height:1;color:var(--cobalt);display:block}
.ep .d{color:var(--ink-soft);display:block;margin:.35em 0 .3em}
.ep b{display:block;font-family:var(--display);font-weight:500;font-size:1.12em;line-height:1.18;margin-bottom:.5em}
.ep .o{color:var(--ink-soft);display:block;border-top:1px solid var(--line);padding-top:.4em}
.slide .ep.now{border-top-color:var(--cobalt);background:#FFFDF4;outline:2px solid var(--marker);outline-offset:-2px}

/* táblázat */
table{border-collapse:collapse;width:100%;max-width:78em;font-size:var(--t-sm)}
th,td{text-align:left;vertical-align:top;padding:.42em .9em .42em 0;border-bottom:1px solid var(--line)}
th{font-weight:600;color:var(--ink-soft)}
td.dt{font-family:var(--display);font-weight:500;white-space:nowrap}
td b{font-weight:600}
tr.now td{background:var(--cream)}
td .who{color:var(--ink-soft)}

/* követelmények és tippek */
.grid3{display:grid;grid-template-columns:repeat(3,1fr);gap:1.2vw 1.4vw;max-width:80em}
.grid3 .card h3{font-size:1.15em}
.grid3 .card p{font-size:var(--t-sm)}
.tips{display:grid;grid-template-columns:1fr 1fr;gap:1.2vw 1.6vw;max-width:78em}
.tip{background:#fff;border-radius:12px;padding:.8em 1.15em .9em;box-shadow:var(--sh);border-top:4px solid var(--marker);position:relative}
.tip h3{padding-right:1.6em}
.tip .i{position:absolute;right:.9em;top:.7em;font-family:var(--display);font-weight:500;color:var(--cobalt);font-size:1.3em;line-height:1}

/* feladat: cél, scope, leadandó */
.goal{display:grid;grid-template-columns:auto 1fr;gap:.75em 1.4em;max-width:62em;background:#fff;border-radius:14px;padding:1.2em 1.6em;box-shadow:var(--sh);border-left:6px solid var(--marker)}
.goal dt{font-weight:600;color:var(--cobalt);font-size:var(--t-sm);text-transform:uppercase;letter-spacing:.08em;padding-top:.28em}
.goal dd{font-size:var(--t-lead);line-height:1.35}

/* lépések */
ol.steps{list-style:none;counter-reset:s;display:grid;gap:0 2.6vw;max-width:76em}
ol.steps.two{grid-template-columns:1fr 1fr}
ol.steps li{display:grid;grid-template-columns:1.7em 1fr;gap:.5em;align-items:baseline;padding:.5em 0;border-bottom:1px solid var(--line)}
ol.steps li::before{counter-increment:s;content:counter(s);font-family:var(--display);font-weight:500;color:var(--cobalt);font-size:1.35em;line-height:1}
.opt{display:inline-block;font-size:var(--t-sm);font-weight:600;color:var(--ink);background:var(--cream);border-radius:99px;padding:0 .6em;margin-right:.4em}

/* promptok */
.prompts{display:grid;grid-template-columns:1fr 1fr;gap:1.6vw;align-items:start;max-width:84em}
.prompts.one{grid-template-columns:1fr;max-width:60em}
.prompt{background:#fff;border:1px solid var(--line);border-radius:12px;overflow:hidden;box-shadow:var(--sh)}
.prompt .ph{display:flex;justify-content:space-between;align-items:center;gap:1em;padding:.4em .9em;background:var(--ink);color:#fff;font-size:var(--t-sm)}
.prompt .copy{border:1px solid rgba(255,255,255,.55);border-radius:4px;padding:.05em .7em;font-size:var(--t-sm);color:#fff;white-space:nowrap}
.prompt .copy:hover{background:rgba(255,255,255,.12)}
.prompt pre{white-space:pre-wrap;font-family:var(--body);font-size:var(--t-sm);line-height:1.45;padding:.75em 1em;max-height:50vh;overflow:auto;margin:0}
.prompt mark{background:var(--cream);color:inherit;border-radius:3px;padding:0 .12em}
.tools{font-size:var(--t-sm);color:var(--ink-soft);max-width:84em;margin:-.3em 0 1em}

/* márkapárok */
.pairs{display:grid;grid-template-columns:repeat(5,1fr);gap:.8vw;max-width:84em}
.pair{background:#fff;border-radius:10px;padding:.5em .8em .55em;box-shadow:var(--sh);border-left:4px solid var(--cobalt);font-size:var(--t-sm);line-height:1.25}
.pair i{font-style:normal;color:var(--ink-soft)}
.pair b{display:block;font-family:var(--display);font-weight:500;font-size:1.2em;margin:.1em 0}
.pair span{color:var(--cobalt)}

/* márkaválasztó: a játék */
h2.game{font-size:calc(var(--t-h2) * 1.25);margin-bottom:.15em}
.menu{display:grid;grid-template-columns:repeat(3,1fr);column-gap:3.2vw;max-width:86em;border-top:2px solid var(--ink);margin-top:.5em}
.menu .mi{display:grid;grid-template-columns:2.1em 1fr;align-items:baseline;text-align:left;padding:.45em .3em .5em;border-bottom:1px solid var(--line);position:relative;transition:background .15s}
.menu .mi i{font-style:normal;font-size:var(--t-sm);color:var(--ink-soft);grid-row:1/3;align-self:start;padding-top:.4em;font-variant-numeric:tabular-nums}
.menu .mi .l1,.menu .mi .l2{grid-column:2;white-space:nowrap;line-height:1.12}
.menu .mi b{font-family:var(--display);font-weight:500;font-size:1.32em;letter-spacing:-.01em}
.menu .mi .l2 b{color:var(--cobalt)}
.menu .mi em{font-style:normal;font-size:var(--t-sm);color:var(--ink-soft)}
.menu .mi small{position:absolute;right:.3em;top:.75em;font-size:max(.62rem,13px);letter-spacing:.1em;text-transform:uppercase;font-weight:600;color:#fff;background:var(--ink);border-radius:99px;padding:.15em .7em;visibility:hidden}
.menu .mi:hover{background:linear-gradient(90deg,rgba(242,201,76,.38),rgba(242,201,76,0))}
.menu .mi.taken b{text-decoration:line-through;text-decoration-thickness:2px;color:var(--ink-soft)}
.menu .mi.taken small{visibility:visible}
@media (max-width:900px){.menu{grid-template-columns:1fr}}

/* a mai feladat */
h2.wide{max-width:44ch}
table.task{max-width:88em;font-size:var(--t-body);margin-top:.2em}
table.task th{font-size:var(--t-sm);border-bottom:2px solid var(--ink);padding-bottom:.35em}
table.task td{padding:.6em 1.2em .6em 0;vertical-align:top}
table.task td.no{font-family:var(--display);font-weight:500;color:var(--cobalt);font-size:1.5em;line-height:1;width:1.6em;padding-top:.45em}
table.task td b{display:block;font-family:var(--display);font-weight:500;font-size:1.18em;line-height:1.2;margin-bottom:.15em}
table.task td span{display:block;color:var(--ink-soft);font-size:var(--t-sm);line-height:1.35;max-width:46ch}
table.task td.out{font-weight:600;width:24%}
table.task td.dk{width:24%;font-size:var(--t-sm);color:var(--cobalt)}
.deliv{margin-top:.9em;background:var(--ink);color:#fff;border-radius:10px;padding:.55em 1em;max-width:88em;font-size:var(--t-body)}
.deliv b{color:var(--marker);margin-right:.3em}

.kn{display:grid;grid-template-columns:1fr 1fr;gap:1.6vw;max-width:60em;margin-top:.4em}
.kn .card h3{font-size:1.3em}
.kn .qs li{font-size:var(--t-body)}
@media (max-width:900px){.kn{grid-template-columns:1fr}}

.need{margin-top:.9em;background:var(--cream);border-radius:10px;padding:.5em 1em;max-width:none;line-height:1.35}
.need b{margin-right:.3em}
.docwrap{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,1fr);gap:1.6vw;align-items:center;max-width:92em;margin-top:.4em}
.docpage{background:#fff;border-radius:6px;box-shadow:var(--sh);padding:.8em 1.3em 1em;border-top:6px solid var(--marker)}
.docpage .dt{display:block;font-size:var(--t-sm);color:var(--ink-soft);margin-bottom:.3em}
.dl{display:grid;grid-template-columns:1fr auto;gap:1em;align-items:baseline;padding:.32em 0;border-bottom:1px dashed var(--line)}
.dl b{font-weight:600;font-size:var(--t-sm)}
.dl small{font-size:var(--t-sm);color:var(--cobalt);white-space:nowrap}
.docside{display:grid;gap:.5em;justify-items:stretch}
.docside .arr{color:var(--cobalt);font-size:1.6em;justify-self:center}
.docside .card h3{font-size:1.15em}
.docside .card p{font-size:var(--t-sm)}
@media (max-width:900px){.docwrap{grid-template-columns:1fr}}

.tipbtn{display:inline-flex;align-items:center;gap:.35em;cursor:pointer;margin-left:.4em;padding:.12em .5em .12em .15em;border-radius:99px;background:#fff;border:2px solid var(--marker);font-size:var(--t-sm);font-weight:600;color:var(--ink);vertical-align:middle}
.tipbtn span{background:var(--marker);border-radius:99px;padding:.02em .6em;letter-spacing:.06em}
.tipbtn:hover{background:var(--marker)}
.tipbtn .clk{width:1.6em;height:1.6em;display:block;color:var(--ink)}
dialog.tipdlg{margin:auto;border:0;border-radius:14px;padding:1em 1.4em 1.3em;width:min(62rem,92vw);max-height:86vh;box-shadow:0 30px 80px rgba(0,0,0,.3);background:var(--paper);color:var(--ink);font-size:var(--t-body)}
dialog.tipdlg::backdrop{background:rgba(27,31,58,.5)}
.tdh{display:flex;align-items:center;gap:.7em;margin-bottom:.7em}
.tdh .tl{background:var(--marker);border-radius:99px;padding:.05em .7em;font-weight:600;font-size:var(--t-sm);letter-spacing:.06em}
.tdh h3{flex:1;font-size:var(--t-h3);margin:0}
.tdh .x{font-size:1.6em;line-height:1;color:var(--ink-soft);padding:0 .2em}
.tj{display:flex;justify-content:space-between;align-items:baseline;gap:1em;padding:.5em 0;border-bottom:1px solid var(--line);max-width:none}
.tj a{color:var(--cobalt);font-weight:600;white-space:nowrap;text-decoration:none}
.tp{margin:.6em 0 .8em}
.tp>p{margin-bottom:.5em;max-width:none}
.tp .prompt pre{max-height:44vh}

.need ul.needl{list-style:none;margin-top:.3em}
.need ul.needl li{display:flex;justify-content:space-between;align-items:center;gap:.8em;padding:.32em 0;border-top:1px dashed rgba(27,31,58,.18)}
.need ul.needl li .tipbtn{margin-left:0;flex:none}
.tdp{margin-bottom:.6em;max-width:none}
.tdh h3{font-size:var(--t-h3)}

/* 2. alkalom: a mai nap */
.build{display:flex;flex-wrap:wrap;align-items:stretch;gap:.55em;max-width:92em;margin-top:.6em}
.build .pc{flex:1 1 0;min-width:6.5em;background:#fff;border-radius:10px;box-shadow:var(--sh);border-top:4px solid var(--marker);padding:.6em .8em;font-family:var(--display);font-weight:500;font-size:1.02em;line-height:1.2;display:flex;align-items:center}
.build .pc.sum{flex:1.2 1 0;background:var(--cobalt);color:#fff;border-top-color:var(--cobalt);font-size:1.25em;justify-content:center}
.build .op{align-self:center;color:var(--ink-soft);font-size:1.4em;font-weight:600}
.slide h3.lbl2{font-family:var(--body)!important;font-weight:600!important;font-size:var(--t-sm);text-transform:uppercase;letter-spacing:.1em;color:var(--ink-soft);margin:1.3em 0 .5em}
.rhythm{display:grid;grid-template-columns:repeat(4,1fr);gap:1.2vw;max-width:92em}
.rhythm .n{font-family:var(--display);font-weight:500;color:var(--cobalt);font-size:1.6em;line-height:1;display:block;margin-bottom:.15em}
.rhythm .card h3{font-size:1.15em}
.rhythm .card p{font-size:var(--t-sm)}
@media (max-width:900px){.rhythm{grid-template-columns:1fr}.build .op{display:none}}

/* 2. alkalom: összefoglaló */
.recap{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1.5fr);gap:2.8vw;align-items:start;max-width:92em}
.slide .recap h3.lbl{font-family:var(--body)!important;font-weight:600;font-size:var(--t-sm);text-transform:uppercase;letter-spacing:.1em;color:var(--ink-soft);border-bottom:2px solid var(--ink);padding-bottom:.3em;margin-bottom:.2em}
ul.done{list-style:none}
ul.done li{padding:.45em 0 .45em 1.5em;border-bottom:1px solid var(--line);position:relative;line-height:1.35}
ul.done li::before{content:"✓";position:absolute;left:0;color:var(--cobalt);font-weight:600}
.today{margin-top:.9em;background:var(--ink);color:#fff;border-radius:10px;padding:.55em 1em;max-width:none}
.who{display:grid;grid-template-columns:1fr 1fr;column-gap:2.2vw}
.who>div{padding:.42em 0 .48em;border-bottom:1px solid var(--line)}
.who .nm{display:inline-block;background:var(--marker);color:var(--ink);font-weight:600;font-size:var(--t-sm);line-height:1.35;border-radius:4px;padding:.02em .45em;margin-bottom:.22em}
.nmh{background:var(--marker);color:var(--ink);font-weight:600;border-radius:4px;padding:0 .3em}
.who .gm{display:block;line-height:1.25}
.who .gm b{font-family:var(--display);font-weight:500;font-size:1.18em}
.who .gm b.c{color:var(--cobalt)}
.who .gm em{font-style:normal;font-size:var(--t-sm);color:var(--ink-soft)}
@media (max-width:900px){.recap,.who{grid-template-columns:1fr}}

/* 2. alkalom: kis feladatok */
.agenda{display:grid;grid-template-columns:1fr 1fr;gap:2.6vw;max-width:88em}
.slide .agenda h3{font-family:var(--body)!important;font-weight:600;font-size:var(--t-sm);text-transform:uppercase;letter-spacing:.1em;color:var(--ink-soft);border-bottom:2px solid var(--ink);padding-bottom:.3em;margin-bottom:.1em}
ol.ag{list-style:none}
ol.ag li{display:grid;grid-template-columns:1.6em 1fr auto;gap:.6em;align-items:baseline;padding:.4em 0;border-bottom:1px solid var(--line)}
ol.ag .no{font-family:var(--display);font-weight:500;color:var(--cobalt);font-size:1.25em;line-height:1}
ol.ag b{display:block;font-weight:600;line-height:1.25}
ol.ag em{display:block;font-style:normal;color:var(--ink-soft);font-size:var(--t-sm);line-height:1.3}
ol.ag .mm{font-size:var(--t-sm);color:var(--ink-soft);white-space:nowrap}
.thg{display:grid;grid-template-columns:repeat(auto-fit,minmax(13em,1fr));gap:1vw 1.4vw;max-width:88em;margin-top:.9em}
.tk .prompt pre{font-size:max(.86rem,18px)}
.thg .card h3{font-size:1.12em}
.thg .card p{font-size:var(--t-sm)}
.formula{font-family:var(--display);font-weight:500;font-size:1.32em;line-height:1.4;background:#fff;border-radius:12px;padding:.7em 1.1em;box-shadow:var(--sh);max-width:54em;margin:.1em 0 .9em}
.formula mark,.tk .what mark,.qs mark{background:var(--cream);color:inherit;border-radius:4px;padding:0 .15em}
.ex{margin-top:1em;background:var(--cream);border-radius:12px;padding:.6em 1.1em .7em;max-width:80em;border-left:5px solid var(--marker)}
.ex small,.qsw small{display:block;font-size:max(.62rem,13px);letter-spacing:.12em;text-transform:uppercase;font-weight:600;color:var(--ink-soft);margin-bottom:.25em}
.ex p{max-width:none}
.tk{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.25fr);gap:2.4vw;align-items:start;max-width:90em}
.tk .what{font-size:var(--t-lead);line-height:1.38;max-width:none}
.tk .ex{margin-top:.9em}
.res{margin-top:1em;background:var(--ink);color:#fff;border-radius:10px;padding:.55em 1em;max-width:none}
.res b{color:var(--marker);margin-right:.3em}
.qsw{margin-top:.9em}
.qs{list-style:none}
.qs li{padding:.28em 0 .28em 1.2em;border-bottom:1px solid var(--line);font-size:var(--t-sm);position:relative}
.qs li::before{content:"?";position:absolute;left:0;color:var(--cobalt);font-weight:600}
.qs.bl li::before{content:"·";font-size:1.4em;line-height:1;top:.18em}
@media (max-width:900px){.agenda,.tk{grid-template-columns:1fr}}

/* szabályok */
.rules{display:grid;grid-template-columns:repeat(3,1fr);gap:.9vw 1.4vw;max-width:80em}
.rule9{display:grid;grid-template-columns:1.6em 1fr;gap:.4em;padding:.55em 0;border-top:1px solid var(--line);font-size:var(--t-sm)}
.rule9 .k{font-family:var(--display);font-weight:500;color:var(--cobalt);font-size:1.35em;line-height:1.1}
.rule9 b{display:block;font-weight:600;color:var(--ink);font-size:1.08em}
.rule9 p{color:var(--ink-soft)}

/* lapozó, súgósor */
.hint{position:fixed;left:7vw;bottom:2.6vh;max-width:46vw;font-size:clamp(12px,.82vw,16px);color:var(--ink-soft);z-index:20}
.pager{position:fixed;right:7vw;bottom:2.2vh;font-size:clamp(13px,.88vw,17px);color:var(--ink-soft);display:flex;gap:.7em;align-items:center;z-index:20}
.pager button,.pager a.home{padding:.2em .6em;border:1px solid var(--line);border-radius:4px;background:var(--paper);color:var(--ink-soft);text-decoration:none}
.pager button:hover,.pager a.home:hover{color:var(--cobalt);border-color:var(--cobalt)}
.pager button:focus-visible,.pager a:focus-visible{outline:3px solid var(--cobalt)}
.lang{display:inline-flex}
.lang button{border-radius:0}
.lang button:first-child{border-radius:4px 0 0 4px}
.lang button:last-child{border-radius:0 4px 4px 0;border-left:0}
.pager .lang button.on{background:var(--ink);color:#fff;border-color:var(--ink)}
.jump{display:none;position:absolute;right:0;bottom:calc(100% + .6em);width:min(34em,80vw);max-height:70vh;overflow:auto;background:var(--paper);border:1px solid var(--line);border-radius:6px;box-shadow:0 10px 30px rgba(0,0,0,.12);padding:.4em 0;font-size:1.15em;z-index:50}
.jump.open{display:block}
.jump a{display:grid;grid-template-columns:2.2em 1fr;gap:.4em;padding:.35em 1em;color:var(--ink);text-decoration:none;line-height:1.3}
.jump a:hover{background:rgba(0,0,0,.05)}
.jump a.cur{font-weight:600;color:var(--cobalt)}
.jump a i{font-style:normal;color:var(--ink-soft)}

/* javító mód (J) */
body.rev .slide :is(h1,h2,h3,p,li,td,th,dd,.big){outline:1px dashed rgba(30,75,216,.35);outline-offset:2px;cursor:text}
body.rev .slide :is(h1,h2,h3,p,li,td,th,dd,.big):hover{background:rgba(242,201,76,.35)}
body.rev .rev-marked{border-left:4px solid var(--cobalt);padding-left:.5em}
.revbar{position:fixed;left:0;right:0;bottom:0;background:var(--ink);color:#F7F6F1;padding:.6em 7vw;font-size:clamp(13px,.9vw,17px);display:none;z-index:60;align-items:center;gap:1em}
body.rev .revbar{display:flex}
.revbar button{border:1px solid rgba(255,255,255,.4);color:#F7F6F1;padding:.2em .7em;border-radius:4px}
.revbox{position:fixed;z-index:61;background:#fff;color:var(--ink);border:1px solid var(--line);border-radius:6px;padding:.8em;width:min(30em,90vw);box-shadow:0 8px 30px rgba(0,0,0,.2);display:none;font-size:clamp(14px,1vw,18px)}
.revbox.open{display:block}
.revbox .orig{font-size:.85em;color:var(--ink-soft);max-height:6em;overflow:auto;margin-bottom:.5em;border-left:3px solid var(--marker);padding-left:.6em}
.revbox textarea{width:100%;min-height:5em;font:inherit;padding:.4em;border:1px solid var(--line);border-radius:4px}
.revbox .row{display:flex;gap:.5em;margin-top:.5em}
.revbox .row button{border:1px solid var(--cobalt);color:var(--cobalt);padding:.3em .8em;border-radius:4px}
.revout{position:fixed;inset:0;background:var(--paper);z-index:62;padding:4vh 7vw;display:none;overflow:auto}
.revout.open{display:block}
.revout textarea{width:100%;height:60vh;font:inherit;font-size:.85em;padding:.8em;border:1px solid var(--line);border-radius:6px;margin:1em 0}
.btn{display:inline-block;padding:.35em .9em;border:1px solid var(--cobalt);color:var(--cobalt);border-radius:4px;font-size:var(--t-sm);text-decoration:none}

@media (max-width:900px){
  html,body{overflow:auto}
  .slide{padding:5vh 6vw 14vh;justify-content:flex-start}
  .c1shift,.flow,.cols,.cols3,.triad,.tips,.prompts,.grid3,.rules,.blocks5{grid-template-columns:1fr}
  .flow .arr{transform:rotate(90deg);justify-self:center}
  .c1shift .arr{transform:rotate(90deg);margin:0}
  .season{grid-template-columns:1fr 1fr}
  .pairs{grid-template-columns:1fr 1fr 1fr}
  ol.steps.two{grid-template-columns:1fr}
  .hint{display:none}
  .pager{right:4vw;left:4vw;justify-content:flex-end;flex-wrap:wrap}
}
"""

JS = r"""
(function(){
  var KEY='aim2026-lang', D=document, root=D.documentElement, DECK=root.getAttribute('data-deck');
  function qp(n){var m=location.search.match(new RegExp('[?&]'+n+'=([a-z]+)'));return m?m[1]:null}
  var lang=qp('lang'); if(lang!=='hu'&&lang!=='en'){lang=null;try{lang=localStorage.getItem(KEY)}catch(e){} if(lang!=='hu'&&lang!=='en')lang='hu'}
  var all=[].slice.call(D.querySelectorAll('section.slide')), slides=[], i=0, pos=D.getElementById('pos'), jump=D.getElementById('jump');
  function build(){
    slides=all.filter(function(s){return s.getAttribute('data-l')===lang});
    jump.innerHTML='';
    slides.forEach(function(sl,k){var h=sl.querySelector('h1,h2,.big');var t=(h?h.textContent:(sl.querySelector('.kicker')||{}).textContent||'').replace(/\s+/g,' ').trim();if(t.length>72)t=t.slice(0,70)+'…';var a=D.createElement('a');a.href='#d'+(k+1);a.innerHTML='<i>'+(k+1)+'.</i><span></span>';a.lastChild.textContent=t;a.addEventListener('click',function(ev){ev.preventDefault();jump.classList.remove('open');show(k)});jump.appendChild(a)});
  }
  function url(){return location.pathname+'?lang='+lang+'#d'+(i+1)}
  function show(n){
    n=Math.max(0,Math.min(slides.length-1,n));
    all.forEach(function(s){s.classList.remove('cur')});
    i=n; slides[i].classList.add('cur');
    pos.textContent=(i+1)+' / '+slides.length;
    try{history.replaceState(null,'',url())}catch(e){location.hash='d'+(i+1)}
    fit(slides[i]);
  }
  function applyLang(){
    root.lang=lang;
    var t=D.querySelector('title'); if(t&&t.getAttribute('data-'+lang))t.textContent=t.getAttribute('data-'+lang);
    [].forEach.call(D.querySelectorAll('[data-setlang]'),function(b){b.classList.toggle('on',b.getAttribute('data-setlang')===lang)});
    [].forEach.call(D.querySelectorAll('a[data-href]'),function(a){a.href=a.getAttribute('data-href')+'?lang='+lang+(a.getAttribute('data-hash')||'')});
  }
  function setLang(l){if(l===lang)return;lang=l;try{localStorage.setItem(KEY,l)}catch(e){}applyLang();build();show(i)}
  /* ha egy dia nem fér ki, csak azt az egy diát kicsinyíti, legfeljebb 76%-ig */
  function fit(s){ if(!s||window.innerWidth<=900)return; var ch=[].slice.call(s.children).filter(function(c){return !c.matches('.kicker,h1,h2,.big')}); ch.forEach(function(c){c.style.zoom=''}); var f=1;
    while(s.scrollHeight>s.clientHeight+2&&f>0.77){f-=0.03;ch.forEach(function(c){c.style.zoom=f.toFixed(2)})} }
  function next(){show(i+1)} function prev(){show(i-1)}
  applyLang(); build();
  var m=location.hash.match(/^#d(\d+)$/); show(m?+m[1]-1:0);
  window.addEventListener('resize',function(){fit(slides[i])});
  window.addEventListener('load',function(){fit(slides[i])});
  if(D.fonts&&D.fonts.ready)D.fonts.ready.then(function(){fit(slides[i])});
  window.addEventListener('hashchange',function(){var m=location.hash.match(/^#d(\d+)$/);if(m)show(+m[1]-1)});

  D.addEventListener('keydown',function(ev){
    if(ev.target&&/^(INPUT|TEXTAREA|SELECT)$/.test(ev.target.tagName))return;
    if(D.querySelector('dialog[open]'))return;
    if(ev.key==='ArrowRight'||ev.key==='PageDown'||ev.key===' '){next();ev.preventDefault()}
    else if(ev.key==='ArrowLeft'||ev.key==='PageUp'){prev();ev.preventDefault()}
    else if(ev.key==='Home'){show(0)} else if(ev.key==='End'){show(slides.length-1)}
    else if(ev.key==='l'||ev.key==='L'){setLang(lang==='hu'?'en':'hu')}
    else if(ev.key==='j'||ev.key==='J'){D.body.classList.toggle('rev')}
    else if(ev.key==='f'||ev.key==='F'){D.fullscreenElement?D.exitFullscreen():D.documentElement.requestFullscreen&&D.documentElement.requestFullscreen()}
    else if(ev.key==='Escape'){jump.classList.remove('open');D.getElementById('revbox').classList.remove('open');D.getElementById('revout').classList.remove('open')}
  });
  [].forEach.call(D.querySelectorAll('[data-nav]'),function(b){b.addEventListener('click',function(ev){ev.stopPropagation();b.getAttribute('data-nav')==='1'?next():prev()})});
  [].forEach.call(D.querySelectorAll('[data-setlang]'),function(b){b.addEventListener('click',function(ev){ev.stopPropagation();setLang(b.getAttribute('data-setlang'))})});
  pos.addEventListener('click',function(ev){ev.stopPropagation();[].forEach.call(jump.children,function(a,k){a.classList.toggle('cur',k===i)});jump.classList.toggle('open');var c=jump.children[i];if(c)jump.scrollTop=c.offsetTop-jump.clientHeight/2});
  D.addEventListener('click',function(ev){if(!jump.contains(ev.target))jump.classList.remove('open')});
  D.querySelector('.deck').addEventListener('click',function(ev){
    if(ev.target.closest('a,button,input,textarea,pre,.prompt,dialog'))return;
    if(D.body.classList.contains('rev'))return;
    var sel=window.getSelection&&String(window.getSelection());if(sel)return;
    next();
  });

  /* márkaválasztó: kattintásra foglalt, a böngészőben marad */
  (function(){var K='aim2026-taken',t={};try{t=JSON.parse(localStorage.getItem(K)||'{}')}catch(e){}
    function paint(){[].forEach.call(D.querySelectorAll('[data-pick] .mi'),function(b){var k=b.getAttribute('data-k');b.classList.toggle('taken',!!t[k]);b.setAttribute('aria-pressed',t[k]?'true':'false')})}
    [].forEach.call(D.querySelectorAll('[data-pick] .mi'),function(b){b.addEventListener('click',function(ev){ev.stopPropagation();var k=b.getAttribute('data-k');if(t[k])delete t[k];else t[k]=1;try{localStorage.setItem(K,JSON.stringify(t))}catch(e){}paint()})});
    paint();})();

  /* TIPP: felugró ablak, ha nincs meg az előzmény */
  [].forEach.call(D.querySelectorAll('[data-tip]'),function(b){b.addEventListener('click',function(ev){ev.stopPropagation();var d=D.getElementById(b.getAttribute('data-tip'));if(d&&d.showModal)d.showModal()})});
  [].forEach.call(D.querySelectorAll('dialog.tipdlg'),function(d){d.addEventListener('click',function(ev){if(ev.target===d)d.close()})});
  [].forEach.call(D.querySelectorAll('dialog [data-close]'),function(b){b.addEventListener('click',function(ev){ev.stopPropagation();b.closest('dialog').close()})});
  [].forEach.call(D.querySelectorAll('[data-jump]'),function(a){a.addEventListener('click',function(ev){ev.preventDefault();ev.stopPropagation();var d=a.closest('dialog');if(d)d.close();show(+a.getAttribute('data-jump')-1)})});

  /* promptok másolása */
  [].forEach.call(D.querySelectorAll('.copy'),function(b){b.addEventListener('click',function(ev){ev.stopPropagation();
    var t=b.closest('.prompt').querySelector('pre').innerText, lab=b.textContent;
    function done(){b.textContent=lang==='en'?'Copied ✓':'Kimásolva ✓';setTimeout(function(){b.textContent=lab},1600)}
    function fb(){var ta=D.createElement('textarea');ta.value=t;ta.style.position='fixed';ta.style.opacity='0';D.body.appendChild(ta);ta.select();try{D.execCommand('copy');done()}catch(e){}D.body.removeChild(ta)}
    if(navigator.clipboard&&window.isSecureContext){navigator.clipboard.writeText(t).then(done,fb)}else fb();
  })});

  /* javító mód: J billentyű; a megjegyzések a böngészőben maradnak, a Lista kimentése adja ki őket */
  var REVQ='h1,h2,h3,p,li,td,th,dd,.big', REVKEY='aim2026-rev-'+DECK, rev={}, revTarget=null;
  try{rev=JSON.parse(localStorage.getItem(REVKEY)||'{}')}catch(e){rev={}}
  function slideOf(el){return el.closest('section.slide')}
  function revId(el){var sl=slideOf(el);var k=all.indexOf(sl);var list=[].slice.call(sl.querySelectorAll(REVQ));return 's'+k+'-'+list.indexOf(el)}
  function slideNo(el){var sl=slideOf(el);return slides.indexOf(sl)+1||(all.indexOf(sl)+1)}
  function revText(el){return el.textContent.replace(/\s+/g,' ').trim()}
  function revMark(){[].forEach.call(D.querySelectorAll('.rev-marked'),function(x){x.classList.remove('rev-marked')});Object.keys(rev).forEach(function(k){var p=k.match(/^s(\d+)-(\d+)$/);if(!p)return;var sl=all[+p[1]];if(!sl)return;var el=sl.querySelectorAll(REVQ)[+p[2]];if(el)el.classList.add('rev-marked')})}
  function revSave(){try{localStorage.setItem(REVKEY,JSON.stringify(rev))}catch(e){}D.getElementById('revcount').textContent=Object.keys(rev).length;revMark()}
  D.addEventListener('click',function(ev){if(!D.body.classList.contains('rev'))return;if(ev.target.closest('#revbox,#revbar,#revout,button,input,textarea,a'))return;var el=ev.target.closest('.slide '+REVQ.split(',').join(',.slide '));if(!el)return;ev.preventDefault();ev.stopPropagation();
    revTarget=el;var box=D.getElementById('revbox');D.getElementById('revorig').textContent=revText(el);var id=revId(el);D.getElementById('revtext').value=rev[id]?rev[id].note:'';box.style.left=Math.min(ev.clientX,window.innerWidth-520)+'px';box.style.top=Math.min(ev.clientY,window.innerHeight-260)+'px';box.classList.add('open');D.getElementById('revtext').focus()},true);
  D.getElementById('revsave').addEventListener('click',function(){var t=D.getElementById('revtext').value.trim();var id=revId(revTarget);if(t){rev[id]={slide:slideNo(revTarget),lang:slideOf(revTarget).getAttribute('data-l'),orig:revText(revTarget),note:t}}else{delete rev[id]}revSave();D.getElementById('revbox').classList.remove('open')});
  D.getElementById('revdel').addEventListener('click',function(){delete rev[revId(revTarget)];revSave();D.getElementById('revbox').classList.remove('open')});
  D.getElementById('revcancel').addEventListener('click',function(){D.getElementById('revbox').classList.remove('open')});
  D.getElementById('revexport').addEventListener('click',function(){var ks=Object.keys(rev).sort(function(a,b){return rev[a].slide-rev[b].slide});var out=ks.map(function(k){var r=rev[k];return DECK+'. alkalom, '+r.slide+'. dia ('+r.lang+')\nEredeti: '+r.orig+'\nJavítás: '+r.note}).join('\n\n')||'Nincs megjegyzés.';D.getElementById('revouttext').value=out;D.getElementById('revout').classList.add('open');try{navigator.clipboard.writeText(out)}catch(e){}});
  D.getElementById('revoutclose').addEventListener('click',function(){D.getElementById('revout').classList.remove('open')});
  D.getElementById('revclear').addEventListener('click',function(){if(confirm('Minden megjegyzés törlése?')){rev={};revSave()}});
  D.getElementById('revoff').addEventListener('click',function(){D.body.classList.remove('rev')});
  revSave();
})();
"""

# ---------- diaelemek ----------

def kicker(hu, en, lt=None):
    return {'hu': '<p class="kicker">%s%s</p>' % ('<span class="lt">%s</span>' % lt['hu'] if lt else '', hu),
            'en': '<p class="kicker">%s%s</p>' % ('<span class="lt">%s</span>' % lt['en'] if lt else '', en)}

def j(*parts):
    """részek összefűzése nyelvenként; egy rész lehet str (közös) vagy dict"""
    out = {}
    for l in LANGS:
        out[l] = ''.join(p[l] if isinstance(p, dict) else p for p in parts)
    return out

def tag(t, d, cls=None):
    c = ' class="%s"' % cls if cls else ''
    return {l: '<%s%s>%s</%s>' % (t, c, d[l], t) for l in LANGS}

def sess_lt(n):
    return L('%d. alkalom' % n, 'Session %d' % n)

def title_slide(n):
    s = SESS[n-1]
    return j(kicker('AI a marketingben · gyakorlat', 'AI in Marketing · practice'),
             {l: '<h1 class="cover">%s</h1>' % s['t'][l] for l in LANGS},
             {l: '<p class="lead">%s</p>' % (('%d. alkalom · %s' % (n, s['d']['hu'])) if l == 'hu' else ('Session %d · %s' % (n, s['d']['en']))) for l in LANGS})

def goal_slide(n):
    s = SESS[n-1]
    return j(kicker('A feladat', 'The task', sess_lt(n)),
             tag('h2', L('Cél, scope, leadandó', 'Goal, scope, deliverable')),
             {l: '<dl class="goal"><dt>%s</dt><dd>%s</dd><dt>Scope</dt><dd>%s</dd><dt>%s</dt><dd>%s</dd></dl>' % (
                 'Cél' if l == 'hu' else 'Goal', GOAL[n][l], SCOPE[n][l], 'Leadandó' if l == 'hu' else 'Deliverable', DELIV[n][l]) for l in LANGS},
             tag('p', L('A lépések egy javasolt utat mutatnak, nem kötelező sorrendet. Az eszközlisták csak példák: ha más AI-eszközt ismersz vagy szeretsz, használd azt.',
                        'The steps show a suggested path, not a mandatory order. The tool lists are only examples: if you know or like another AI tool, use it.'), 'note'))

def task_slides(n):
    """A mai feladat: részfeladatonként mit csinálsz, mi az eredménytermék, hová kerül a deckben."""
    out = []
    groups = SUB[n]
    start = 0
    for gi, (sub, rows) in enumerate(groups):
        body = {}
        for l in LANGS:
            hd = ('Részfeladat', 'Eredménytermék', 'Hová kerül a deckben') if l == 'hu' else ('Sub-task', 'Output', 'Where it goes in the deck')
            trs = ['<tr><th></th><th>%s</th><th>%s</th><th>%s</th></tr>' % hd]
            for q, (t, d, o, k) in enumerate(rows):
                trs.append('<tr><td class="no">%d</td><td><b>%s</b><span>%s</span></td><td class="out">%s</td><td class="dk">%s</td></tr>' % (start + q + 1, t[l], d[l], o[l], k[l]))
            body[l] = '<table class="task">%s</table>' % ''.join(trs)
        last = gi == len(groups) - 1
        pg = (' %d/%d' % (gi + 1, len(groups))) if len(groups) > 1 else ''
        h2 = {l: GOAL[n][l] if sub is None else sub[l] for l in LANGS}
        foot = {l: '' for l in LANGS}
        if last:
            foot = {l: '<p class="deliv"><b>%s</b> %s</p>' % ('Mára elkészül:' if l == 'hu' else 'Done by today:', DELIV[n][l]) for l in LANGS}
        note = tag('p', L('Ami a dián van, javaslat arra az esetre, ha nincs ötleted, hogyan indulj el. A lényeg az eredménytermék.',
                          'What is on the slide is a suggestion in case you do not know how to start. What counts is the output.'), 'note')
        out.append(j(kicker('A mai feladat' + pg, "Today's task" + pg, sess_lt(n)), tag('h2', h2, 'wide'), body, foot, note))
        start += len(rows)
    return out

def prompt_box(label, text):
    return '<div class="prompt"><div class="ph"><span>%s</span><button type="button" class="copy">%s</button></div><pre>%s</pre></div>' % (label, '{COPY}', pmark(text))

def copyfix(s, l):
    return s.replace('{COPY}', 'Másolás' if l == 'hu' else 'Copy')

def prompt_slides(n):
    out = []
    for k, (ttl, si, fi) in enumerate(PROMPTS[n]):
        body = {}
        for l in LANGS:
            cb = CB_HU if l == 'hu' else CB_EN
            a = prompt_box('Strukturált' if l == 'hu' else 'Structured', cb[si])
            b = prompt_box('Szabad szöveggel, ahogy egy kollégának mondanád' if l == 'hu' else 'In free text, the way you would say it to a colleague', cb[fi])
            body[l] = copyfix('<div class="prompts">%s%s</div>' % (a, b), l)
        tools = tag('p', j(L('<b>Eszközök ehhez:</b> ', '<b>Tools for this:</b> '), TOOLS[n]), 'tools') if k == 0 else {'hu': '', 'en': ''}
        out.append(j(kicker('Ha nincs ötleted, hogyan indulj el', 'If you do not know how to start', sess_lt(n)), tag('h2', j(L('Promptjavaslat: ', 'Prompt suggestion: '), ttl)), tools, body))
    if n in INLINE:
        body = {}
        for l in LANGS:
            boxes = ''.join(prompt_box(ttl[l], txt[l]) for ttl, txt in INLINE[n])
            body[l] = copyfix('<div class="prompts%s">%s</div>' % ('' if len(INLINE[n]) > 1 else ' one', boxes), l)
        h = L('Féléves ütemterv és versenytársak', 'Semester timeline and competitors') if n == 1 else L('Animált spot', 'Animated spot')
        note = tag('p', L('A szögletes zárójeles részeket a saját projekted adataival töltsd ki.', 'Fill in the parts in square brackets with your own project details.'), 'note') if n == 1 else ''
        out.append(j(kicker('Ha nincs ötleted, hogyan indulj el', 'If you do not know how to start', sess_lt(n)), tag('h2', j(L('Promptjavaslat: ', 'Prompt suggestion: '), h)), body, note))
    return out

def tips_slides(n):
    out = []
    tot = len(TIPS[n])
    for k, (ttl, tips) in enumerate(TIPS[n]):
        cards = {l: '<div class="tips">%s</div>' % ''.join('<div class="tip"><span class="i" aria-hidden="true">%d</span><h3>%s</h3><p>%s</p></div>' % (q+1, a[l], b[l]) for q, (a, b) in enumerate(tips)) for l in LANGS}
        out.append(j(kicker('Tippek és tanácsok · %d/%d' % (k+1, tot), 'Tips and advice · %d/%d' % (k+1, tot), sess_lt(n)), tag('h2', ttl), cards))
    return out

RAG = {'2026. november 12.': '2026. november 12-én', '2026. november 19.': '2026. november 19-én', '2026. november 26.': '2026. november 26-án',
       '2026. december 3.': '2026. december 3-án', '2026. december 10.': '2026. december 10-én', '2026. november 11.': '2026. november 11-én',
       '2026. november 18.': '2026. november 18-án', '2026. november 25.': '2026. november 25-én', '2026. december 2.': '2026. december 2-án',
       '2026. december 9.': '2026. december 9-én'}

def close_slide(n):
    s = SESS[n-1]
    if n < 6:
        nx = SESS[n]
        th_d, th = THEORY[n+1]
        nxt = {l: ('<p class="lead">%s</p><p class="muted">%s</p>' % (
            ('Jövő csütörtökön, %s: %s.' % (RAG[nx['d']['hu']], nx['t']['hu'])) if l == 'hu' else ('Next Thursday, %s: %s.' % (nx['d']['en'], nx['t']['en'])),
            (('Előtte szerdán, %s: ' % RAG[th_d['hu']]) if l == 'hu' else ('The day before, %s: ' % th_d['en'])) + ' · '.join(x[l] for x in th))) for l in LANGS}
    else:
        nxt = tag('p', L('2026. december 16-án még két elméleti óra lesz: Nóra: Fogyasztói viselkedés · Jogi szabályozás és etika.',
                         'On 16 December 2026 there are two more lectures: Nóra: Consumer behaviour · Legal regulation and ethics.'), 'lead')
    return j(kicker('Zárás', 'Wrap-up', sess_lt(n)),
             {l: '<h2>%s</h2>' % (('Mára elkészül: ' if l == 'hu' else 'Done by today: ') + DELIV[n][l][0].lower() + DELIV[n][l][1:]) for l in LANGS},
             '<hr class="rule">', nxt,
             (tag('p', L('A leadás helyét és határidejét az oktató adja meg.', 'The instructor will tell you where and when to upload.'), 'note') if n == 6 else ''))

# ---------- az 1. alkalom bevezető diái ----------

def orch_svg(roles, center):
    W, H = 1000, 430
    cx, cy = 500, 360
    rx, ry = 390, 290
    angs = [165, 135, 105, 75, 45, 15]
    parts = ['<svg viewBox="0 0 %d %d" role="img" aria-label="%s">' % (W, H, e(', '.join(roles)) + ' · ' + e(center))]
    pos = []
    for a, r in zip(angs, roles):
        x = cx + rx * math.cos(math.radians(a)); y = cy - ry * math.sin(math.radians(a))
        pos.append((x, y, r))
    for x, y, r in pos:
        parts.append('<line x1="%d" y1="%d" x2="%.0f" y2="%.0f" stroke="#C9C7BE" stroke-width="2" stroke-dasharray="4 6"/>' % (cx, cy - 20, x, y))
    for x, y, r in pos:
        w = len(r) * 12.5 + 44
        parts.append('<rect x="%.0f" y="%.0f" width="%.0f" height="50" rx="25" fill="#fff" stroke="#D9D7CE" stroke-width="1.5"/>' % (x - w/2, y - 25, w))
        parts.append('<text x="%.0f" y="%.0f" text-anchor="middle" font-size="23" fill="#1B1F3A">%s</text>' % (x, y + 8, e(r)))
    parts.append('<circle cx="%d" cy="%d" r="70" fill="#1E4BD8"/>' % (cx, cy - 10))
    parts.append('<circle cx="%d" cy="%d" r="82" fill="none" stroke="#F2C94C" stroke-width="5"/>' % (cx, cy - 10))
    parts.append('<text x="%d" y="%d" text-anchor="middle" font-size="30" font-weight="600" fill="#fff">%s</text>' % (cx, cy, e(center)))
    parts.append('</svg>')
    return ''.join(parts)

def intro_slides():
    S = []
    # 1. címlap
    S.append(j(kicker('Pannon Egyetem · Marketing MSc · 2026 ősz', 'University of Pannonia · Marketing MSc · autumn 2026'),
               {'hu': '<h1 class="cover">AI a marketingben</h1>', 'en': '<h1 class="cover">AI in Marketing</h1>'},
               tag('p', L('Gyakorlat · 1. alkalom · 2026. november 5.', 'Practice · Session 1 · 5 November 2026'), 'lead'),
               tag('p', L('Birincsik Albert', 'Albert Birincsik'), 'muted')))
    # 2. miért
    S.append(j(kicker('A tárgy', 'The course'), tag('h2', L('Miért vagyunk itt?', 'Why are we here?')),
               tag('p', L('Hogy megtanuld, hogyan dolgozik egy marketinges AI-jal.', 'To learn how a marketer works with AI.'), 'lead'),
               {l: '<div class="cols" style="margin-top:1.1em"><div class="card"><h3>%s</h3><p>%s</p></div><div class="card alt"><h3>%s</h3><p>%s</p></div></div>' % (
                   ('Nem helyetted gondolkodik', 'Gyorsabban és többet tudsz vele kipróbálni.', 'A félév végére', 'egy teljes márkabevezetést viszel végig, az ötlettől a kész kampányanyagokig.') if l == 'hu' else
                   ('It does not think for you', 'It lets you try more things, faster.', 'By the end of the semester', 'you will have taken a complete brand launch from idea to finished campaign materials.')) for l in LANGS}))
    # 3. ami a legfontosabb
    S.append(j(kicker('Ami a legfontosabb', 'What matters most'),
               tag('p', L('Az AI nagy segítség, de mindent, amit ad, értelmezni kell, felülbírálni és kritikusan szemlélni.', 'AI is a great help, but everything it gives you has to be interpreted, overruled where needed and looked at critically.'), 'big'),
               {l: '<div class="triad"><div>%s</div><div>%s</div><div>%s</div></div>' % (('Értelmezed', 'Javítod', 'Kritikával nézed') if l == 'hu' else ('Interpret', 'Correct', 'Question')) for l in LANGS},
               tag('p', L('Nem attól leszel jó szakember, hogy egy az egyben elfogadod, amit kapsz. Nem arra vagyok kíváncsi, milyen gyorsan tudsz dolgozni. Itt a hatékonyság <span class="hl">a minőséget és a mélységet</span> jelenti.',
                          'You do not become a good professional by accepting what you get as it is. I am not interested in how fast you can work. Here, efficiency means <span class="hl">quality and depth</span>.'), 'lead')))
    # 4. mit csinálunk
    S.append(j(kicker('Mit csinálunk', 'What we do'), tag('h2', L('Marketing tender: valós márka egy elképzelt iparágban', 'Marketing pitch: a real brand in an imagined industry')),
               tag('p', L('Például: mi lenne, ha a Coca-Cola autómárka lenne?', 'For example: what if Coca-Cola were a car brand?'), 'lead'),
               {l: '<div class="flow" style="margin-top:1em"><div class="card"><h3>%s</h3><p>%s</p></div><div class="arr" aria-hidden="true">→</div><div class="card"><h3>%s</h3><p>%s</p></div><div class="arr" aria-hidden="true">→</div><div class="card alt"><h3>%s</h3><p>%s</p></div></div>' % (
                   ('Megtartod', 'A márka nevét, logóját, személyiségét, értékeit és vizuális kódjait.', 'Áthelyezed', 'Egy elképzelt új iparágba. Kitalálod, mit kínálna ott, kinek és hogyan.', 'Elindítod', 'Megtervezed és elkészíted a bevezető kampányát.') if l == 'hu' else
                   ('You keep', "The brand's name, logo, personality, values and visual codes.", 'You move it', 'Into an imagined new industry. You work out what it would offer there, to whom and how.', 'You launch', 'You plan and produce its launch campaign.')) for l in LANGS},
               tag('p', L('Órai játék: a valódi márka nevével és logójával dolgozunk, de csak itt, az órán. A kész anyagokat ne tedd közzé, mert a márka nem a tiéd. Egyéni munka, mindenki a választott márkával dolgozik.', "A classroom game: we work with the real brand's name and logo, but only here, in class. Do not publish the finished materials, because the brand is not yours. Individual work, everyone works with the brand they chose."), 'note')))
    # 5. szimuláció, karmester
    S.append(j(kicker('Min fogsz dolgozni', 'What you will work on'), tag('h2', L('Egy ügynökség egy tenderen. A karmester te vagy.', 'An agency on a pitch. You are the conductor.')),
               tag('p', L('Ez egy szimuláció, ami a valós életet modellezi: így dolgozik egy ügynökség, amikor meg akar nyerni egy ügyfelet. Egy tenderen ezek a szakemberek dolgoznak együtt. Te ezt egymagad csinálod meg, a kompetenciákat az AI segítségével oldod meg.',
                          'This is a simulation that models real life: this is how an agency works when it wants to win a client. On a pitch, these specialists work together. You do all of it on your own, covering these competencies with the help of AI.')),
               {l: '<div class="orch">%s</div>' % orch_svg(ROLES[l], 'Te + AI' if l == 'hu' else 'You + AI') for l in LANGS}))
    # 6. elvárt kimenet
    S.append(j(kicker('Az elvárt kimenet', 'What is expected'), tag('h2', L('Egy tenderdeck, amit óráról órára építesz fel', 'A pitch deck you build session by session')),
               {l: '<div class="cols3 stat">%s</div>' % ''.join('<div class="card%s"><span class="num">%s</span><p>%s</p></div>' % x for x in (
                   (('', '15-20 dia', 'Tenderdeck az új márkáról és a bevezető kampányáról, rögzített szerkezet szerint.'), ('', 'Prototípusok', 'A deck mögött: arculat, weboldal, posztok, videóspot és a többi.'), (' alt', '15-20 perc', '2026. december 10-én bemutatod a decket, és elmeséled, hogyan készült.')) if l == 'hu' else
                   (('', '15-20 slides', 'A pitch deck of the new brand and its launch campaign, along a fixed structure.'), ('', 'Prototypes', 'Behind the deck: identity, website, posts, video spot and the rest.'), (' alt', '15-20 minutes', 'On 10 December 2026 you present the deck and tell the story of how it was made.')))) for l in LANGS},
               tag('p', L('Mintha ügynökségként az ügyfélnek vinnéd, és meg akarnád nyerni a tendert. A bemutatón azt is elmondod, mit csináltál, mivel, mire jöttél rá, és hol voltak az AI korlátai.',
                          'As if you were an agency bringing it to the client to win the pitch. In the presentation you also tell what you did, with what, what you learned, and where the limits of AI were.'), 'note')))
    # 7. öt blokk
    S.append(j(kicker('A tenderdeck szerkezete', 'The structure of the pitch deck'), tag('h2', L('Öt blokk', 'Five blocks')),
               {l: '<div class="blocks5">%s</div>' % ''.join('<div class="blk"><span class="n">%d</span><h3>%s</h3><p>%s</p></div>' % (k+1, a[l], b[l]) for k, (a, b) in enumerate(BLOCKS)) for l in LANGS},
               tag('p', L('Minden, amit a hat alkalmon készítesz, ebbe a deckbe kerül. A blokkok aránya rajtad múlik. A kreatív anyagok prototípusok: valódi gyártás, éles kampány és védjegybejegyzés nem része a feladatnak.',
                          'Everything you make in the six sessions goes into this deck. How you balance the blocks is up to you. The creative materials are prototypes: real production, a live campaign and trademark registration are not part of the assignment.'), 'note')))
    # 8. hat alkalom
    eps = {}
    for l in LANGS:
        cards = []
        for s in SESS:
            cards.append('<div class="ep%s"><span class="n">%d</span><span class="d">%s</span><b>%s</b><span class="o">%s</span></div>' % (
                ' now' if s['n'] == 1 else '', s['n'], s['d'][l], s['t'][l], s['out'][l]))
        eps[l] = '<div class="season">%s</div>' % ''.join(cards)
    S.append(j(kicker('Hogyan', 'How'), tag('h2', L('Hat csütörtök, 8:00 és 12:00 között', 'Six Thursdays, from 8:00 to 12:00')), eps,
               tag('p', L('Minden alkalom két másfél órás blokk, és mindegyiken a tenderdeck egy-egy részét készíted el. Az ingyenes Claude és ChatGPT elég hozzá.',
                          'Each session is two blocks of an hour and a half, and in each you produce one part of the pitch deck. The free Claude and ChatGPT are enough.'), 'note')))
    # 10. követelmények
    req = L([('Részvétel', 'Kötelező, a hiányzás nem haladhatja meg a HKR szerinti mértéket.'),
             ('Munka és bemutató', 'A félév alatt órán dolgozol, részleadás nincs. Az aláírás feltétele a december 10-i tenderprezentáció és a végleges deck.'),
             ('Értékelés', 'Folyamatos számonkérés, ötfokozatú jegy, a tantárgy tematikája szerinti ponthatárokkal.'),
             ('AI-használat', 'Megengedett, sőt ez a feladat lényege. Az ingyenes változat elég, de ha van előfizetésed, használhatod.'),
             ('Tények', 'Minden tényt forrással igazolj. Az AI által írt, nem ellenőrizhető állítást javítsd vagy töröld.'),
             ('Órai játék', 'A márka nevét és logóját csak az órán használjuk. Amit készítesz, ne tedd közzé, és ne állítsd valódinak.')],
            [('Attendance', 'Mandatory; absences may not exceed the limit set by the university regulations (HKR).'),
             ('Work and presentation', 'You work in class through the semester; there are no interim submissions. The condition for the course signature is the pitch presentation on 10 December and the final deck.'),
             ('Assessment', 'Continuous assessment, five-grade scale, with the thresholds set in the course syllabus.'),
             ('Use of AI', 'Allowed, in fact it is the point of the assignment. The free version is enough, but if you have a subscription you may use it.'),
             ('Facts', 'Back every fact with a source. Fix or delete any AI-written claim you cannot verify.'),
             ('A classroom game', "We use the brand's name and logo only in class. Do not publish what you make or present it as real.")])
    S.append(j(kicker('Követelmények', 'Requirements'), tag('h2', L('Amit a félév kér', 'What the semester asks of you')),
               {l: '<div class="grid3">%s</div>' % ''.join('<div class="card%s"><h3>%s</h3><p>%s</p></div>' % (' alt' if k % 2 else '', a, b) for k, (a, b) in enumerate(req[l])) for l in LANGS},
               tag('p', L('Záróbemutató 2026. december 10-én, hallgatónként 15-20 perc. A deckben legyen egy dia a használt eszközökről.',
                          'Final presentation on 10 December 2026, 15-20 minutes per student. Include one slide in the deck about the tools you used.'), 'note')))
    # 11. eszközök
    tt = {l: '<table style="max-width:72em"><tr><th>%s</th><th>%s</th><th>%s</th></tr>%s</table>' % ((('Mire', 'Ajánlott eszköz', 'Más eszközzel is') if l == 'hu' else ('For what', 'Recommended tool', 'Also works with')) +
          (''.join('<tr><td>%s</td><td><b>%s</b></td><td>%s</td></tr>' % (a[l], b[l], c[l]) for a, b, c in TOOLTABLE),)) for l in LANGS}
    S.append(j(kicker('AI-eszközök', 'AI tools'), tag('h2', L('Bármit használhatsz. A Claude és a ChatGPT az ajánlott.', 'You can use anything. Claude and ChatGPT are recommended.')), tt,
               tag('p', L('A harmadik oszlop példa, nem teljes lista: szinte minden sor megcsinálható ChatGPT-vel is, és bármilyen más eszközt használhatsz. A kész anyagban írd oda, melyik részhez melyik eszközt használtad. Ma nézd meg, elérhető-e a saját ingyenes Claude-fiókodban a Claude Design és a Claude Slides.',
                          'The third column is an example, not a full list: almost every row can be done with ChatGPT as well, and you may use any other tool. In the finished material, note which tool you used for which part. Today, check whether Claude Design and Claude Slides are available in your own free Claude account.'), 'note')))
    # 12. promptolás
    S.append(j(kicker('Promptolás', 'Prompting'), tag('h2', L('A jó prompt olyan, mint egy jó brief', 'A good prompt is like a good brief')),
               tag('p', L('Aki kapja, kérdés nélkül el tudja végezni a munkát.', 'Whoever receives it can do the job without asking questions.'), 'lead'),
               {l: '<div class="rules" style="margin-top:.9em">%s</div>' % ''.join('<div class="rule9"><span class="k">%d</span><div><b>%s</b><p>%s</p></div></div>' % (k+1, a[l], b[l]) for k, (a, b) in enumerate(RULES)) for l in LANGS}))
    # 13. promptsablon
    S.append(j(kicker('Promptolás', 'Prompting'), tag('h2', L('Promptsablon, amit minden feladathoz kitölthetsz', 'A prompt template you can fill in for every task')),
               {l: copyfix('<div class="prompts one">%s</div>' % prompt_box('Sablon' if l == 'hu' else 'Template', (CB_HU if l == 'hu' else CB_EN)[16]), l) for l in LANGS},
               tag('p', L('Tippek: bontsd lépésekre a nagy feladatot, kérj több változatot, adj konkrét visszajelzést, és kérd meg, hogy értékelje a saját válaszát a kritériumaid szerint. Személyes vagy bizalmas adatot ne írj bele.',
                          'Tips: break the big task into steps, ask for several variants, give specific feedback, and ask it to rate its own answer against your criteria. Do not put personal or confidential data in it.'), 'note')))
    # 14. márkák: a játék, kattintható választólista
    EN_ART = {'car': 'a', 'airline': 'an', 'bank': 'a', 'hotel chain': 'a', 'café chain': 'a', 'insurance company': 'an', 'gym chain': 'a',
              'mobile carrier': 'a', 'restaurant chain': 'a', 'fashion brand': 'a', 'travel agency': 'a', 'cosmetics brand': 'a',
              'home electronics': '', 'wellness and spa chain': 'a', 'payment': ''}
    def item(k, brand, cat, l):
        if l == 'hu':
            l1 = '<em>%s</em> <b>%s</b>' % ('az' if brand in ('IKEA', 'Apple') else 'a', e(brand))
            l2 = '<b>%s</b> <em>lenne?</em>' % cat['hu']
            tg = 'foglalt'
        else:
            art = EN_ART[cat['en']]
            l1 = '<b>%s</b>' % e(brand)
            l2 = '<em>were%s</em> <b>%s</b><em>?</em>' % ((' ' + art) if art else '', cat['en'])
            tg = 'taken'
        return '<button type="button" class="mi" data-k="%s"><i>%02d</i><span class="l1">%s</span><span class="l2">%s</span><small>%s</small></button>' % (e(brand), k+1, l1, l2, tg)
    S.append(j(kicker('A játék', 'The game', sess_lt(1)), {'hu': '<h2 class="game">Mi lenne, ha…</h2>', 'en': '<h2 class="game">What if…</h2>'},
               tag('p', L('Válassz egy márkát. Mindenkinek más jut.', 'Choose a brand. Everyone gets a different one.'), 'lead'),
               {l: '<div class="menu" data-pick>%s</div>' % ''.join(item(k, a_, b_, l) for k, (a_, b_) in enumerate(PAIRS)) for l in LANGS},
               tag('p', L('A márkát másképp használjuk, mint a valóságban: a neve és a logója marad, csak az iparág új. Azt kérdezzük, milyen lenne, ha a személyiségével, az értékeivel és a stílusával egy egészen más iparágban működne. Ez órai játék, a valóságban nem létezik.',
                          'We use the brand differently from reality: its name and logo stay, only the industry is new. The question is what it would be like if, with its personality, values and style, it worked in a completely different industry. It is a classroom game; it does not exist in reality.'), 'note')))
    return S

# ---------- összeállítás ----------

def strip(n):
    a = ['<a href="index.html" data-href="index.html"><b>AI</b>%s</a>' % bi('a marketingben · kezdőlap', 'in Marketing · home')]
    for s in SESS:
        m = s['n']
        lbl = bi('%s&nbsp;·&nbsp;%s' % (s['t']['hu'], s['short']), '%s&nbsp;·&nbsp;%s' % (s['t']['en'], s['short']))
        if m == n:
            # a saját fül akkor is látszik, ha ez az alkalom még nincs megnyitva
            a.append('<a href="%s" data-href="%s" class="on" aria-current="page"><b>%d</b>%s</a>' % (FN(m), FN(m), m, lbl))
        elif m <= NYITVA:
            a.append('<a href="%s" data-href="%s"><b>%d</b>%s</a>' % (FN(m), FN(m), m, lbl))
        else:
            a.append('<a class="off" aria-disabled="true" data-off="%s"><b>%d</b>%s</a>' % (FN(m), m, lbl))
    return '<nav class="strip" aria-label="Alkalmak">%s</nav>' % ''.join(a)

# ---------- a 2. alkalom: kis feladatok elmélettel ----------

def s2_agenda():
    """A mai nap: nem feladatlista, hanem az, hogy a témát kis feladatokra szedjük, és ezekből áll össze a márkabrief."""
    parts = S2_THEORY['brief']['items']
    body = {}
    for l in LANGS:
        tiles = []
        for q, (a, _) in enumerate(parts):
            if q:
                tiles.append('<span class="op" aria-hidden="true">+</span>')
            tiles.append('<span class="pc">%s</span>' % a[l])
        tiles.append('<span class="op" aria-hidden="true">=</span>')
        tiles.append('<span class="pc sum">%s</span>' % ('Márkabrief' if l == 'hu' else 'Brand brief'))
        rh = L([('Rövid elmélet', 'Mi ez, és mire jó, egy kitalált példával.'), ('Kis feladat', '10-20 perc, másolható prompttal. A prompt megmondja, mit másolj be, és milyen formában kérd vissza.'), ('Márkadokumentum', 'Az eredményt bemásolod a márkadokumentumodba.'), ('Továbbviszed', 'A következő prompt ebből indul. A végén ebből lesz a márkabrief.')],
               [('Short theory', 'What it is and what it is for, with a made-up example.'), ('Small task', '10-20 minutes, with a prompt you can copy. The prompt says what to paste in and in what form to ask for the result.'), ('Brand document', 'You paste the output into your brand document.'), ('Carry it on', 'The next prompt starts from it. At the end it becomes the brand brief.')])[l]
        rhythm = '<div class="rhythm">%s</div>' % ''.join('<div class="card%s"><span class="n">%d</span><h3>%s</h3><p>%s</p></div>' % ('', q + 1, t, d) for q, (t, d) in enumerate(rh))
        body[l] = '<div class="build">%s</div><h3 class="lbl2">%s</h3>%s' % (''.join(tiles), 'Minden témánál ugyanaz a menet' if l == 'hu' else 'Same rhythm for every topic', rhythm)
    foot = {l: '<p class="deliv"><b>%s</b> %s</p>' % ('Mára elkészül:' if l == 'hu' else 'Done by today:', DELIV[2][l]) for l in LANGS}
    return j(kicker('A mai nap', "Today's plan", sess_lt(2)),
             tag('h2', L('Ma kis lépésekben haladunk', 'Today we go in small steps'), 'wide'),
             tag('p', L('A mai témát, a márkaplatformot, a célcsoportot és az árazást kis feladatokra szedjük szét. Mindegyik az előzőre épül, és a végén ezekből áll össze a márkabrief.',
                        'We break today\'s topic, the brand platform, the target audience and pricing, into small tasks. Each builds on the one before, and at the end they add up to the brand brief.'), 'lead'),
             body, foot,
             tag('p', L('A promptok csak javaslatok, ha nincs ötleted, hogyan indulj el.', 'The prompts are only suggestions in case you do not know how to start.'), 'note'))

def s2_theory(key):
    t = S2_THEORY[key]
    body = {}
    for l in LANGS:
        h = ''
        if t.get('formula'):
            h += '<div class="formula">%s</div>' % pmark(t['formula'][l])
        h += '<div class="thg">%s</div>' % ''.join('<div class="card%s"><h3>%s</h3><p>%s</p></div>' % (' alt' if q % 2 else '', a[l], b[l]) for q, (a, b) in enumerate(t['items']))
        h += '<div class="ex"><small>%s</small><p>%s</p></div>' % (('Kitalált példa · ' + EXAMPLE['hu']) if l == 'hu' else ('Made-up example · ' + EXAMPLE['en']), t['ex'][l])
        body[l] = h
    return j(kicker('Elmélet', 'Theory', sess_lt(2)), tag('h2', t['t'], 'wide'), tag('p', t['lead'], 'lead'), body)

S2_TASK_SLIDE = {it[1]: 4 + q for q, it in enumerate(S2_SLIDES) if it[0] == 'task'}

def s2_task(k):
    t = S2_TASKS[k]
    body = {}
    for l in LANGS:
        left = '<p class="what">%s</p>' % pmark(t['what'][l])
        if k in S2_NEED:
            ICON = '<svg class="clk" viewBox="0 0 24 24" aria-hidden="true"><path d="M10 8.5v12.2l3.1-3 2.4 5.2 2.2-1-2.4-5.1h4.4z" fill="currentColor" stroke="currentColor" stroke-width=".8" stroke-linejoin="round"/><path d="M10 2.4v3M3.6 8.5h3M5.2 3.7l2.1 2.1M14.8 3.7l-2.1 2.1M5.2 13.3l2.1-2.1" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round"/></svg>'
            lis = ''.join('<li><span>%s</span><button type="button" class="tipbtn" data-tip="tip-%s-%d-%d" aria-label="%s" title="%s"><span>%s</span>%s%s</button></li>' % (
                lab[l], l, k, i, ('Kattints ide, ha nincs meg' if l == 'hu' else 'Click here if missing'), ('Kattints ide, ha nincs meg' if l == 'hu' else 'Click here if missing'),
                'TIPP' if l == 'hu' else 'TIP', ('Ha nincs meg' if l == 'hu' else 'If missing'), ICON) for i, (lab, _) in enumerate(S2_NEED[k]))
            left += '<div class="need"><b>%s</b><ul class="needl">%s</ul></div>' % ('Ehhez kell:' if l == 'hu' else 'You need:', lis)
        if t.get('qs'):
            left += '<div class="qsw"><small>%s</small><ul class="qs">%s</ul></div>' % ('Jó kérdések' if l == 'hu' else 'Good questions', ''.join('<li>%s</li>' % pmark(q) for q in t['qs'][l]))
        if t.get('brief'):
            left += '<div class="qsw"><small>%s</small><ul class="qs bl">%s</ul></div>' % ('A márkabrief részei' if l == 'hu' else 'Parts of the brand brief', ''.join('<li>%s</li>' % e(q) for q in t['brief'][l]))
        if t.get('ex'):
            left += '<div class="ex"><small>%s</small><p>%s</p></div>' % ('Kitalált példa' if l == 'hu' else 'Made-up example', t['ex'][l])
        if t.get('doc'):
            lab = ('Eredmény, a márkadokumentumodba:' if l == 'hu' else 'Output, into your brand document:') if k < len(S2_TASKS) else ('Eredmény:' if l == 'hu' else 'Output:')
            left += '<p class="res"><b>%s</b> %s</p>' % (lab, t['doc'][l])
        else:
            left += '<p class="res"><b>%s</b> %s</p>' % ('Eredmény:' if l == 'hu' else 'Output:', t['out'][l])
        ptxt = (CB_HU if l == 'hu' else CB_EN)[t['pcb']] if 'pcb' in t else t['p'][l]
        right = prompt_box('Promptjavaslat, ha nincs ötleted' if l == 'hu' else 'Prompt suggestion, if you are stuck', ptxt)
        dlg = ''
        for i, (lab, key) in enumerate(S2_NEED.get(k, [])):
            dlg += '<dialog class="tipdlg" id="tip-%s-%d-%d"><div class="tdh"><span class="tl">%s</span><h3>%s %s</h3><button type="button" class="x" data-close aria-label="%s">×</button></div><p class="tdp">%s</p>%s</dialog>' % (
                l, k, i, 'TIPP' if l == 'hu' else 'TIP', 'Ha nincs meg:' if l == 'hu' else 'If you do not have it:', lab[l], 'Bezár' if l == 'hu' else 'Close',
                'Készítsd el most ezzel a prompttal, és másold be a márkadokumentumodba.' if l == 'hu' else 'Make it now with this prompt, and paste it into your brand document.',
                prompt_box('Prompt', TIP_PROMPTS[key][l]))
        body[l] = copyfix('<div class="tk"><div>%s</div><div>%s</div></div>%s' % (left, right, dlg), l)
    kk = {l: ('%d/%d kis feladat · kb. %d perc' % (k, len(S2_TASKS), t['m'])) if l == 'hu' else ('Small task %d/%d · approx. %d min' % (k, len(S2_TASKS), t['m'])) for l in LANGS}
    return j(kicker(kk['hu'], kk['en'], sess_lt(2)), tag('h2', t['t'], 'wide'), body)

def s2_recap():
    cats = dict(PAIRS)
    taken = set(b for _, b in ROSTER)
    free = [b for b, _ in PAIRS if b not in taken]
    EN_ART = {'car': 'a', 'airline': 'an', 'hotel chain': 'a', 'café chain': 'a', 'fashion brand': 'a', 'travel agency': 'a',
              'restaurant chain': 'a', 'payment': '', 'bank': 'a', 'insurance company': 'an', 'gym chain': 'a', 'mobile carrier': 'a',
              'cosmetics brand': 'a', 'home electronics': '', 'wellness and spa chain': 'a'}
    body = {}
    for l in LANGS:
        done = L(['Választottál egy márkát és hozzá egy új iparágat. A neve és a logója marad.',
                  'Megismerted a kiinduló márkát: értékek, személyiség, hangnem, vizuális kódok, kampányok.',
                  'Megnézted az 5 legfontosabb versenytársat az új kategóriában.',
                  'Leírtad, mit viszel át a kiinduló márkából, és mit nem.'],
                 ['You chose a brand and a new industry for it. Its name and logo stay.',
                  'You got to know the source brand: values, personality, tone of voice, visual codes, campaigns.',
                  'You looked at the 5 most important competitors in the new category.',
                  'You wrote down what you carry over from the source brand and what you do not.'])[l]
        left = '<div><h3 class="lbl">%s</h3><ul class="done">%s</ul><p class="today">%s</p></div>' % (
            'Múlt héten, 2026. november 5.' if l == 'hu' else 'Last week, 5 November 2026',
            ''.join('<li>%s</li>' % x for x in done),
            'Ma erre építünk: a márkád ígéretet, hangot és célcsoportot kap az új iparágban.' if l == 'hu' else 'Today we build on this: your brand gets a promise, a voice and an audience in its new industry.')
        rows = []
        for name, brand in ROSTER:
            c = cats[brand]
            if l == 'hu':
                g = '<em>%s</em> <b>%s</b> <b class="c">%s</b> <em>lenne?</em>' % ('az' if brand in ('IKEA', 'Apple') else 'a', e(brand), c['hu'])
            else:
                art = EN_ART[c['en']]
                g = '<b>%s</b> <em>were%s</em> <b class="c">%s</b><em>?</em>' % (e(brand), (' ' + art) if art else '', c['en'])
            rows.append('<div><span class="nm">%s</span><span class="gm">%s</span></div>' % (e(name), g))
        right = '<div><h3 class="lbl">%s</h3><div class="who">%s</div></div>' % ('Ki mit választott' if l == 'hu' else 'Who chose what', ''.join(rows))
        body[l] = '<div class="recap">%s%s</div>' % (left, right)
    note = {'hu': '<p class="note">Még nem választott márkát: %s. Ma az elején válasszatok a szabad márkák közül: %s.</p>' % (', '.join('<span class="nmh">%s</span>' % e(x) for x in NOBRAND), ', '.join(e(x) for x in free)),
            'en': '<p class="note">No brand chosen yet: %s. Choose at the start of today from the free brands: %s.</p>' % (', '.join('<span class="nmh">%s</span>' % e(x) for x in NOBRAND), ', '.join(e(x) for x in free))}
    return j(kicker('Összefoglaló', 'Recap', sess_lt(2)), tag('h2', L('Hol tartunk?', 'Where are we?'), 'wide'), body, note)

def s2_task_def():
    """Mi a feladat: a márka neve és logója marad, csak az iparág új (oktatói döntés, 2026. november 11.)."""
    keep = L(['A név', 'A logó', 'A személyiség', 'Az értékek', 'A vizuális kódok'], ['The name', 'The logo', 'The personality', 'The values', 'The visual codes'])
    new = L(['Az iparág', 'A termék vagy szolgáltatás', 'A célcsoport', 'Az ár', 'A kampány'], ['The industry', 'The product or service', 'The target audience', 'The price', 'The campaign'])
    body = {}
    for l in LANGS:
        body[l] = '<div class="kn"><div class="card"><h3>%s</h3><ul class="qs bl">%s</ul></div><div class="card"><h3>%s</h3><ul class="qs bl">%s</ul></div></div>' % (
            'Marad' if l == 'hu' else 'Stays', ''.join('<li>%s</li>' % x for x in keep[l]),
            'Új' if l == 'hu' else 'New', ''.join('<li>%s</li>' % x for x in new[l]))
    return j(kicker('Mi a feladat?', 'What is the task?', sess_lt(2)),
             tag('h2', L('Az IKEA marad IKEA. Csak légitársaság lesz.', 'IKEA stays IKEA. It just becomes an airline.'), 'wide'),
             tag('p', L('A valódi márkával dolgozunk, a nevével és a logójával együtt. Azt találjuk ki, milyen lenne egy elképzelt új iparágban.', "We work with the real brand, name and logo included. We work out what it would be like in an imagined new industry."), 'lead'),
             body,
             tag('p', L('A kérdés minden döntésnél: ha a márkád tényleg ebben az iparágban lenne, ezt csinálná? Órai játék: amit készítesz, ne tedd közzé, és ne állítsd valódinak.',
                        'The question for every decision: if your brand really were in this industry, would it do this? A classroom game: do not publish what you make or present it as real.'), 'note'))

def s2_doc():
    """A márkadokumentum: minden kis feladat eredménye ide kerül, és innen megy tovább a következő promptba."""
    body = {}
    for l in LANGS:
        rows = []
        for k in S2_DOC:
            t = S2_TASKS[k]
            nxt = S2_USED_BY.get(k, [])
            if nxt:
                ns = ', '.join('%d.' % x for x in nxt)
                to = ('→ kell hozzá: %s feladat' % ns) if l == 'hu' else ('→ needed for: task %s' % ', '.join(str(x) for x in nxt))
            else:
                to = '→ a márkabriefbe' if l == 'hu' else '→ into the brand brief'
            rows.append('<div class="dl"><b>%s</b><small>%s</small></div>' % (t['doc'][l], to))
        page = '<div class="docpage"><small class="dt">%s</small>%s</div>' % ('Márkadokumentum · [márka] mint [új kategória]' if l == 'hu' else 'Brand document · [brand] as a [new category]', ''.join(rows))
        side = ('<div class="docside"><div class="arr" aria-hidden="true">→</div><div class="card"><h3>%s</h3><p>%s</p></div><div class="arr" aria-hidden="true">→</div><div class="card"><h3>%s</h3><p>%s</p></div></div>' % (
            ('9. feladat: márkabrief', 'Az egész dokumentumból egy oldal, rögzített címekkel.', '3. alkalom', 'A márkabrieffel jössz: erre épül az arculat.') if l == 'hu' else
            ('Task 9: brand brief', 'One page from the whole document, with fixed headings.', 'Session 3', 'You bring the brand brief: the identity builds on it.')))
        body[l] = '<div class="docwrap">%s%s</div>' % (page, side)
    return j(kicker('A márkadokumentum', 'The brand document', sess_lt(2)),
             tag('h2', L('Minden eredmény egy dokumentumba kerül', 'Every output goes into one document'), 'wide'),
             tag('p', L('Nyiss egy üres dokumentumot (Google Docs, Word vagy bármi). Minden kis feladat eredményét másold bele. A következő promptba innen másolod be, amire szükség van.',
                        'Open an empty document (Google Docs, Word or anything). Paste the output of every small task into it. You copy what the next prompt needs from here.'), 'lead'),
             body,
             tag('p', L('Minden prompt megmondja, mit másolj be („Ehhez kell”), és pontosan milyen formában kérd vissza az eredményt. Így az AI nem ír össze-vissza, és mindig tovább tudod vinni.',
                        'Every prompt says what to paste in ("You need") and exactly in what form to ask for the result. That way the AI does not ramble, and you can always carry it on.'), 'note'))

def session2_slides():
    out = [s2_recap(), s2_task_def()]
    for it in S2_SLIDES:
        if it[0] == 'agenda':
            out.append(s2_agenda())
        elif it[0] == 'doc':
            out.append(s2_doc())
        elif it[0] == 'th':
            out.append(s2_theory(it[1]))
        else:
            out.append(s2_task(it[1]))
    return out

def deck_slides(n):
    if n == 2:
        S = [title_slide(2)] + session2_slides() + tips_slides(2)
        S.append(close_slide(2))
        return S
    if n == 1:
        S = intro_slides()
    else:
        S = [title_slide(n)]
    S += task_slides(n)
    S += prompt_slides(n)
    S += tips_slides(n)
    S.append(close_slide(n))
    return S

def task_index(n):
    # a „Cél, scope, leadandó” dia sorszáma (1-től)
    return 14 if n == 1 else (4 if n == 2 else 2)

def render_deck(n):
    s = SESS[n-1]
    S = deck_slides(n)
    secs = []
    for l in LANGS:
        for k, sl in enumerate(S):
            cls = 'slide'
            secs.append('<section class="%s" data-l="%s">\n%s\n</section>' % (cls, l, sl[l]))
    t_hu = 'AI a marketingben · %d. alkalom · %s' % (n, s['t']['hu'])
    t_en = 'AI in Marketing · Session %d · %s' % (n, s['t']['en'])
    v_hu, v_en = VER(n)
    hint = bi('← → lapozás · szóköz: következő · F: teljes képernyő · L: nyelv · J: javító mód · ' + v_hu,
              '← → navigate · space: next · F: full screen · L: language · J: review mode · ' + v_en)
    doc = '''<!DOCTYPE html>
<html lang="hu" data-deck="%d">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
<title data-hu="%s" data-en="%s">%s</title>
%s
<style>%s</style>
</head>
<body>
%s
<main class="deck">
%s
</main>
<div class="hint">%s</div>
<div class="pager"><a class="home" href="index.html" data-href="index.html" title="Kezdőlap">⌂ %s</a><span class="lang" role="group" aria-label="Nyelv / Language"><button type="button" data-setlang="hu">HU</button><button type="button" data-setlang="en">EN</button></span><button id="pos" type="button" aria-label="Ugrás diára">1 / %d</button><div class="jump" id="jump"></div><button type="button" data-nav="-1" aria-label="Előző">‹</button><button type="button" data-nav="1" aria-label="Következő">›</button></div>
<div class="revbar" id="revbar"><b>Javító mód</b><span>Kattints bármelyik szövegre, és írd oda, mi legyen helyette vagy mi a bajod vele. <span id="revcount">0</span> megjegyzés.</span><button type="button" id="revexport">Lista kimentése</button><button type="button" id="revclear">Összes törlése</button><button type="button" id="revoff">Kilép (J)</button></div>
<div class="revbox" id="revbox"><div class="orig" id="revorig"></div><textarea id="revtext" placeholder="Mi legyen helyette, vagy mi a bajod vele?"></textarea><div class="row"><button type="button" id="revsave">Ment</button><button type="button" id="revdel">Töröl</button><button type="button" id="revcancel">Mégse</button></div></div>
<div class="revout" id="revout"><h2>Megjegyzések</h2><p class="muted">Ez a szöveg a vágólapra is került. Másold be a chatbe, és a diaszámok alapján átvezetem.</p><textarea id="revouttext" readonly></textarea><p><button class="btn" type="button" id="revoutclose">Bezár</button></p></div>
<script>%s</script>
</body>
</html>
''' % (n, e(t_hu), e(t_en), e(t_hu), FONTS, CSS, strip(n), '\n'.join(secs), hint, bi('Kezdőlap', 'Home'), len(S), JS)
    open(os.path.join(OUT, FN(n)), 'w').write(doc)
    return len(S)

# ---------- kezdőlap ----------

INDEX_CSS = r"""
:root{--paper:#F7F6F1;--ink:#1B1F3A;--soft:#5A5E78;--line:#D9D7CE;--cobalt:#1E4BD8;--marker:#F2C94C}
*{box-sizing:border-box;margin:0;padding:0}
html[lang=en] .hu,html[lang=hu] .en{display:none!important}
body{background:var(--paper);color:var(--ink);font-family:'Source Sans 3','Segoe UI',Helvetica,Arial,sans-serif;font-size:18px;line-height:1.45;padding:1.5em 16px 3em}
.wrap{max-width:52em;margin:0 auto}
.top{display:flex;justify-content:space-between;align-items:center;gap:1em;flex-wrap:wrap}
.d{color:var(--soft);font-size:.9em}
h1{font-family:'Fraunces',Georgia,'Times New Roman',serif;font-weight:500;font-size:2.1em;line-height:1.05;margin:.3em 0 .3em}
.lead{color:var(--soft);max-width:40em;margin-bottom:1.4em}
.lang{display:inline-flex}
.lang button{font:inherit;font-size:.85em;padding:.2em .7em;border:1px solid var(--line);background:none;color:var(--soft);cursor:pointer}
.lang button:first-child{border-radius:4px 0 0 4px}.lang button:last-child{border-radius:0 4px 4px 0;border-left:0}
.lang button.on{background:var(--ink);border-color:var(--ink);color:#fff}
.alk{display:grid;grid-template-columns:3em 1fr;gap:.8em;padding:1em 0;border-top:1px solid var(--line);align-items:start}
.alk:last-of-type{border-bottom:1px solid var(--line)}
.alk .n{font-family:'Fraunces',Georgia,'Times New Roman',serif;font-size:1.6em;line-height:1;color:var(--cobalt)}
.alk b{font-family:'Fraunces',Georgia,'Times New Roman',serif;font-weight:500;font-size:1.15em;display:block}
.alk .q{margin:.2em 0 .5em}
.links a{display:inline-block;padding:.25em .7em;border:1px solid var(--cobalt);color:var(--cobalt);border-radius:4px;text-decoration:none;font-size:.88em;margin:.15em .3em .15em 0}
.links a.main{background:var(--marker);border-color:var(--marker);color:var(--ink)}
.links a.off,.links a.main.off{background:transparent;border-color:var(--line);color:var(--soft);cursor:default}
.foot{margin-top:2em;color:var(--soft);font-size:.85em}
input,button{font:inherit}
"""

def render_index():
    rows = []
    for s in SESS:
        n = s['n']
        th_d, th = THEORY[n]
        ti = task_index(n)
        if n <= NYITVA:
            links = '<a class="main" href="%s" data-href="%s">%s</a> <a href="%s#d%d" data-href="%s" data-hash="#d%d">%s</a>' % (
                FN(n), FN(n), bi('Prezentáció', 'Slides'), FN(n), ti, FN(n), ti, bi('A feladat', 'The task'))
        else:
            links = '<a class="main off" aria-disabled="true" data-off="%s">%s</a> <a class="off" aria-disabled="true" data-off="%s" data-off-hash="#d%d">%s</a>' % (
                FN(n), bi('Prezentáció', 'Slides'), FN(n), ti, bi('A feladat', 'The task'))
        rows.append('<div class="alk"><div class="n">%d</div><div><b>%s</b><span class="d">%s · 8:00-12:00</span><p class="q">%s</p><p class="links">%s</p></div></div>' % (
            n, bi(s['t']['hu'], s['t']['en']), bi(s['d']['hu'], s['d']['en']),
            bi('Mára elkészül: ' + DELIV[n]['hu'][0].lower() + DELIV[n]['hu'][1:], 'Done by today: ' + DELIV[n]['en'][0].lower() + DELIV[n]['en'][1:]),
            links))
    doc = '''<!DOCTYPE html>
<html lang="hu">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="robots" content="noindex, nofollow">
%s
<title>AI a marketingben · 2026 ősz · gyakorlat</title>
<style>%s</style>
</head>
<body>
<div class="wrap" id="gate">
  <div class="top"><p class="d">%s</p><span class="lang"><button type="button" data-setlang="hu">HU</button><button type="button" data-setlang="en">EN</button></span></div>
  <h1>%s</h1>
  <p class="lead">%s</p>
  <p><input id="g_code" type="password" autocomplete="one-time-code" placeholder="Neptun" style="padding:.5em .8em;border:1px solid var(--line);border-radius:4px;width:14em"> <button id="g_send" type="button" style="padding:.5em 1em;border:1px solid var(--cobalt);color:var(--cobalt);background:none;border-radius:4px;cursor:pointer">%s</button></p>
  <p class="d" id="g_status"></p>
</div>
<div class="wrap" id="site" style="display:none">
  <div class="top"><p class="d">%s <span id="who"></span></p><span class="lang"><button type="button" data-setlang="hu">HU</button><button type="button" data-setlang="en">EN</button></span></div>
  <h1>%s</h1>
  <p class="lead">%s</p>
  <p class="lead">%s</p>
  %s
  <p class="foot">%s · <a href="#" id="logout" style="color:var(--soft)">%s</a> · %s</p>
</div>
<script>
(function(){
  var KEY='aim2026-lang',D=document,root=D.documentElement;
  var m=location.search.match(/[?&]lang=(hu|en)/),lang=m?m[1]:null;
  if(!lang){try{lang=localStorage.getItem(KEY)}catch(e){}} if(lang!=='hu'&&lang!=='en')lang='hu';
  function applyLang(){root.lang=lang;D.title=lang==='en'?'AI in Marketing · autumn 2026 · practice':'AI a marketingben · 2026 ősz · gyakorlat';
    [].forEach.call(D.querySelectorAll('[data-setlang]'),function(b){b.classList.toggle('on',b.getAttribute('data-setlang')===lang)});
    [].forEach.call(D.querySelectorAll('a[data-href]'),function(a){a.href=a.getAttribute('data-href')+'?lang='+lang+(a.getAttribute('data-hash')||'')});}
  [].forEach.call(D.querySelectorAll('[data-setlang]'),function(b){b.addEventListener('click',function(){lang=b.getAttribute('data-setlang');try{localStorage.setItem(KEY,lang)}catch(e){}applyLang()})});
  applyLang();
  var gate=D.getElementById('gate'),site=D.getElementById('site');
  function api(a,body){return fetch('api.php?a='+a,body?{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(body),credentials:'same-origin'}:{credentials:'same-origin'}).then(function(r){return r.json()})}
  function show(role,code){gate.style.display='none';site.style.display='';D.getElementById('who').textContent=role==='oktato'?'· oktató':(code?'· '+code:'')}
  if(location.protocol==='file:'){show('oktato');D.getElementById('who').textContent='· helyi előnézet, belépés nélkül';}
  else api('me').then(function(d){if(d.role)show(d.role,d.code)}).catch(function(){});
  function st(hu,en){D.getElementById('g_status').textContent=lang==='en'?en:hu}
  function go(){var c=D.getElementById('g_code').value.trim();if(!c){st('Írd be a kódot.','Enter your code.');return}
    api('auth',{code:c}).then(function(d){if(d.ok)show(d.role,c.toUpperCase());else st('Nincs ilyen kód.','Unknown code.')}).catch(function(){st('A szerver nem elérhető.','The server is not reachable.')})}
  D.getElementById('g_send').addEventListener('click',go);
  D.getElementById('g_code').addEventListener('keydown',function(e){if(e.key==='Enter')go()});
  D.getElementById('logout').addEventListener('click',function(e){e.preventDefault();api('logout').then(function(){location.reload()})});
})();
</script>
</body>
</html>
''' % (FONTS, INDEX_CSS,
       bi('Pannon Egyetem · AI a marketingben · 2026 ősz · gyakorlat', 'University of Pannonia · AI in Marketing · autumn 2026 · practice'),
       bi('Belépés', 'Log in'),
       bi('Add meg a Neptun-kódodat. A kód csak arra kell, hogy a kurzus hallgatói lássák az anyagot; a félév végén a lista törlődik.', 'Enter your Neptun code. It is only needed so that the students of the course can see the material; the list is deleted at the end of the semester.'),
       bi('Belépek', 'Log in'),
       bi('Pannon Egyetem · AI a marketingben · 2026 ősz · gyakorlat', 'University of Pannonia · AI in Marketing · autumn 2026 · practice'),
       bi('Marketing tender: valós márka egy elképzelt iparágban', 'Marketing pitch: a real brand in an imagined industry'),
       bi('Mi lenne, ha a Coca-Cola autómárka lenne.', 'What if Coca-Cola were a car brand?'),
       bi('Hat csütörtökön át egy új márkát indítasz el ügynökségként, AI-jal. Minden alkalomhoz itt a diasor: a feladat, a promptjavaslatok és a tippek.', 'Over six Thursdays you launch a new brand as an agency, with AI. Here are the slides for every session: the task, the prompt suggestions and the tips.'),
       '\n  '.join(rows),
       bi('Oktató: Birincsik Albert', 'Instructor: Albert Birincsik'), bi('Kilépés', 'Log out'), bi(*VER('index')))
    open(os.path.join(OUT, 'index.html'), 'w').write(doc)

if __name__ == '__main__':
    for n in range(1, 7):
        c = render_deck(n)
        print(FN(n), c, 'dia')
    render_index()
    print('index.html')
