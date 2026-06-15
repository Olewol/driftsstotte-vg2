/* empty css                                  */
import { b as createAstro, c as createComponent, m as maybeRenderHead, d as addAttribute, a as renderTemplate, e as renderComponent } from '../chunks/astro/server_B0BmM5RJ.mjs';
import 'piccolore';
import { $ as $$BaseLayout } from '../chunks/BaseLayout_CSal1cln.mjs';
import 'clsx';
import { g as getEmneColor, E as EMNE_LIST } from '../chunks/emneColors_CfhC5xyU.mjs';
import { k as kompetansemaalData, a as getEntry } from '../chunks/kompetansemaal_w0e1UOzb.mjs';
export { renderers } from '../renderers.mjs';

const $$Astro = createAstro("https://Olewol.github.io/driftsstotte-vg2");
const $$WeekCard = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$WeekCard;
  const { veke } = Astro2.props;
  const { color, bg } = getEmneColor(veke.emne ?? "");
  const isFerie = veke.type === "ferie";
  const ukeLabel = veke.uke.length > 1 ? `Veke ${veke.uke[0]}–${veke.uke[veke.uke.length - 1]}` : `Veke ${veke.uke[0]}`;
  const kmArray = Array.isArray(veke.kompetansemaal) ? veke.kompetansemaal : veke.kompetansemaal ? [veke.kompetansemaal] : [];
  const kmTexts = kmArray.map((km) => kompetansemaalData[km] || km).join(" • ");
  const base = "/driftsstotte-vg2";
  const href = isFerie ? void 0 : veke.notat[0] ? `${base}/${veke.emne}/${veke.notat[0]}` : `${base}/${veke.emne}`;
  return renderTemplate`${isFerie ? renderTemplate`${maybeRenderHead()}<div aria-hidden="true"${addAttribute(`background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:20px;opacity:0.4;position:relative;overflow:hidden;`, "style")}><div style="position:absolute;top:0;left:0;right:0;height:3px;background:var(--text3);border-radius:14px 14px 0 0;"></div><div style="font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--text3);margin-bottom:7px;">${ukeLabel}</div><div style="font-size:15px;font-weight:600;color:var(--text);">${veke.tema}</div></div>` : renderTemplate`<a${addAttribute(href, "href")}${addAttribute(`background:linear-gradient(145deg, ${bg} 0%, var(--surface) 60%);border:1px solid var(--border);border-radius:14px;padding:20px;cursor:pointer;position:relative;overflow:hidden;text-decoration:none;display:block;color:var(--text);transition:transform .18s,border-color .2s,box-shadow .2s;`, "style")} onmouseover="this.style.transform='translateY(-4px)';this.style.borderColor='var(--border2)'" onmouseout="this.style.transform='';this.style.borderColor='var(--border)'"><div${addAttribute(`position:absolute;top:0;left:0;right:0;height:3px;background:${color};border-radius:14px 14px 0 0;`, "style")}></div><div style="font-size:11px;font-weight:700;letter-spacing:.06em;text-transform:uppercase;color:var(--text3);margin-bottom:7px;">${ukeLabel}</div><div style="font-size:15px;font-weight:600;color:var(--text);margin-bottom:7px;line-height:1.3;">${veke.tema}</div><div style="font-size:13px;color:var(--text2);line-height:1.55;margin-bottom:14px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;">${kmTexts}</div><div style="display:flex;align-items:center;justify-content:space-between;gap:6px;">${veke.emne && renderTemplate`<span${addAttribute(`font-size:10px;font-weight:700;padding:3px 9px;border-radius:20px;border:1px solid ${color};color:${color};`, "style")}>${veke.emne.charAt(0).toUpperCase() + veke.emne.slice(1)}</span>`}${(veke.ressurstal > 0 || veke.oppgavetar > 0) && renderTemplate`<span style="font-size:11px;color:var(--text3);white-space:nowrap;">${[veke.ressurstal > 0 && `${veke.ressurstal} res.`, veke.oppgavetar > 0 && `${veke.oppgavetar} oppg.`].filter(Boolean).join(" · ")}</span>`}</div></a>`}`;
}, "/home/ole/workspace/driftsstotte-vg2/src/components/WeekCard.astro", void 0);

const $$Index = createComponent(async ($$result, $$props, $$slots) => {
  const aarsplan = await getEntry("aarsplan", "aarsplan");
  const { veker } = aarsplan.data;
  const haust = veker.filter((v) => Math.min(...v.uke) >= 34 && Math.min(...v.uke) <= 51);
  const vaar = veker.filter((v) => Math.min(...v.uke) < 34 || Math.min(...v.uke) > 51);
  const emneLabels = {
    nettverk: "Nettverk",
    sikkerhet: "Sikkerhet",
    operativsystem: "Operativsystem",
    skripting: "Skripting",
    databaser: "Databaser",
    "it-drift": "IT-drift"
  };
  const progression = [
    { emne: "nettverk", uker: "Uke 34\u201339", timer: "~30t", desc: "Grunnmuren \u2014 nettverk er fundamentet all IT-drift bygger p\xE5. Elevene m\xE5 forst\xE5 hvordan data flyter f\xF8r de kan administrere, sikre eller scripte." },
    { emne: "operativsystem", uker: "Uke 41\u201345", timer: "~25t", desc: "OS-administrasjon \u2014 brukere, filsystemer og Linux. N\xF8dvendig f\xF8r sikkerhet (hva skal beskyttes?) og skripting (hva skal automatiseres?)." },
    { emne: "sikkerhet", uker: "Uke 46\u201348", timer: "~15t", desc: "Sikkerhet bygger direkte p\xE5 nettverk og OS \u2014 elevene m\xE5 kjenne infrastrukturen f\xF8r de kan vurdere risiko og tiltak." },
    { emne: "skripting", uker: "Uke 49\u201351", timer: "~15t", desc: "Automatisering forutsetter OS-forst\xE5else. PowerShell (Windows) og Bash (Linux) gj\xF8r driften effektiv og reproduserbar." },
    { emne: "databaser", uker: "Uke 2\u20135", timer: "~20t", desc: "Databaser er delvis uavhengig, men skripting-kunnskap gj\xF8r SQL-automatisering mulig. Naturlig start p\xE5 v\xE5rsemesteret." },
    { emne: "it-drift", uker: "Uke 6\u201311", timer: "~30t", desc: "Kapstone \u2014 integrerer alle emner i praktisk drift: sky, backup, dokumentasjon. Forutsetter kunnskap fra alle foreg\xE5ende emner." },
    { emne: "repetisjon", uker: "Uke 14\u201324", timer: "~35t", desc: "Eksamensforberedelse med tverrfaglige oppgaver, muntlig trening og dybde-repetisjon av alle kompetansem\xE5l." }
  ];
  return renderTemplate`${renderComponent($$result, "BaseLayout", $$BaseLayout, { "title": "\xC5rsplan \u2014 Driftsst\xF8tte 2026\u20132027" }, { "default": async ($$result2) => renderTemplate` ${maybeRenderHead()}<div style="max-width:1140px;margin:0 auto;padding:48px 32px 80px;"> <div style="font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;background:var(--grad);-webkit-background-clip:text;-webkit-text-fill-color:transparent;background-clip:text;margin-bottom:10px;">
Østfold fylkeskommune — Skoleåret 2026–2027
</div> <h1 style="font-size:36px;font-weight:800;letter-spacing:-.025em;margin-bottom:8px;">Årsplan — Driftsstøtte VG2</h1> <p style="font-size:16px;color:var(--text2);max-width:620px;line-height:1.65;margin-bottom:10px;">
Første skoledag 17. august — siste skoledag 17. juni. 190 skoledager fordelt på 6 emner + eksamensforberedelse.
</p> <!-- Pedagogisk progresjon --> <div style="background:var(--surface);border:1px solid var(--border);border-radius:14px;padding:24px 28px;margin-bottom:36px;"> <div style="font-size:11px;font-weight:700;text-transform:uppercase;letter-spacing:.08em;color:var(--text3);margin-bottom:16px;">📈 Pedagogisk progresjon — bygger stegvis</div> <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:12px;"> ${progression.map((p, i) => {
    const { color, bg } = getEmneColor(p.emne);
    return renderTemplate`<div style="display:flex;gap:12px;align-items:flex-start;"> <div${addAttribute(`width:36px;height:36px;border-radius:10px;background:${bg};border:1px solid color-mix(in srgb, ${color} 30%, transparent);display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;color:${color};flex-shrink:0;`, "style")}>${i + 1}</div> <div style="flex:1;min-width:0;"> <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;"> <span style="font-size:14px;font-weight:600;color:var(--text);">${emneLabels[p.emne] || p.emne}</span> <span style="font-size:11px;color:var(--text3);background:var(--bg3);padding:2px 8px;border-radius:4px;">${p.uker}</span> <span style="font-size:11px;color:var(--text3);">${p.timer}</span> </div> <div style="font-size:13px;color:var(--text2);line-height:1.5;margin-top:4px;">${p.desc}</div> </div> </div>`;
  })} </div> </div> <!-- Legend --> <div style="display:flex;gap:18px;flex-wrap:wrap;margin-bottom:28px;" role="list" aria-label="Emneforklaring"> ${EMNE_LIST.map((emne) => {
    const { color } = getEmneColor(emne);
    return renderTemplate`<div style="display:flex;align-items:center;gap:7px;font-size:13px;color:var(--text2);" role="listitem"> <div${addAttribute(`width:9px;height:9px;border-radius:50%;background:${color};flex-shrink:0;`, "style")}></div> ${emneLabels[emne] ?? emne} </div>`;
  })} </div> <!-- Ferie-oversikt --> <details style="margin-bottom:28px;background:var(--surface);border:1px solid var(--border);border-radius:10px;padding:12px 18px;"> <summary style="font-size:13px;font-weight:600;color:var(--text2);cursor:pointer;">📅 Skolerute Østfold 2026–2027 — ${veker.filter((v) => v.type === "ferie").length} ferieperioder</summary> <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:8px;margin-top:10px;font-size:13px;color:var(--text2);"> <div>🏁 <strong>Første skoledag:</strong> 17. august (uke 34)</div> <div>🍂 <strong>Høstferie:</strong> uke 40</div> <div>🎄 <strong>Juleferie:</strong> uke 52–1</div> <div>❄️ <strong>Vinterferie:</strong> uke 8</div> <div>🐣 <strong>Påskeferie:</strong> uke 12–13</div> <div>🏁 <strong>Siste skoledag:</strong> 17. juni (uke 24)</div> </div> </details> <!-- Haust --> <div style="margin-bottom:48px;"> <div style="font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--text3);padding-bottom:14px;margin-bottom:18px;border-bottom:1px solid var(--border);">
Høst 2026 — Uke 34–51
</div> <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px;"> ${haust.map((v) => renderTemplate`${renderComponent($$result2, "WeekCard", $$WeekCard, { "veke": v })}`)} </div> </div> <!-- Vår --> ${vaar.length > 0 && renderTemplate`<div> <div style="font-size:12px;font-weight:700;letter-spacing:.08em;text-transform:uppercase;color:var(--text3);padding-bottom:14px;margin-bottom:18px;border-bottom:1px solid var(--border);">
Vår 2027 — Uke 1–24
</div> <div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px;"> ${vaar.map((v) => renderTemplate`${renderComponent($$result2, "WeekCard", $$WeekCard, { "veke": v })}`)} </div> </div>`} </div> ` })}`;
}, "/home/ole/workspace/driftsstotte-vg2/src/pages/index.astro", void 0);

const $$file = "/home/ole/workspace/driftsstotte-vg2/src/pages/index.astro";
const $$url = "/driftsstotte-vg2";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Index,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
