/* empty css                                  */
import { c as createComponent, e as renderComponent, a as renderTemplate, m as maybeRenderHead, d as addAttribute } from '../chunks/astro/server_B0BmM5RJ.mjs';
import 'piccolore';
import { g as getCollection, k as kompetansemaalData } from '../chunks/kompetansemaal_w0e1UOzb.mjs';
import { $ as $$BaseLayout } from '../chunks/BaseLayout_CSal1cln.mjs';
import { s as slugify } from '../chunks/slugify_hFVwgOAe.mjs';
export { renderers } from '../renderers.mjs';

const $$Kompetansemaal = createComponent(async ($$result, $$props, $$slots) => {
  const notes = await getCollection("emner", (e) => e.data.public !== false);
  const grouped = notes.reduce((acc, note) => {
    let kmTags = note.data.kompetansemaal;
    if (!kmTags) return acc;
    if (!Array.isArray(kmTags)) kmTags = [kmTags];
    for (const km of kmTags) {
      if (!km) continue;
      if (!acc[km]) acc[km] = [];
      acc[km].push(note);
    }
    return acc;
  }, {});
  return renderTemplate`${renderComponent($$result, "BaseLayout", $$BaseLayout, { "title": "Kompetansem\xE5l" }, { "default": async ($$result2) => renderTemplate` ${maybeRenderHead()}<div style="max-width:1140px;margin:0 auto;padding:48px 32px 80px;"> <h1 style="font-size:36px;font-weight:800;letter-spacing:-.025em;margin-bottom:10px;">Kompetansemål</h1> <p style="font-size:16px;color:var(--text2);margin-bottom:40px;">Alle kompetansemål i faget, med lenket innhold.</p> ${Object.entries(grouped).map(([kmId, kmNotes]) => {
    const kmText = kompetansemaalData[kmId] || kmId;
    return renderTemplate`<div style="margin-bottom:28px;padding:20px;background:var(--surface2);border:1px solid var(--border);border-radius:12px;"> <div style="font-size:15px;font-weight:600;color:var(--text);margin-bottom:12px;">🎯 ${kmText}</div> <div style="display:flex;gap:8px;flex-wrap:wrap;"> ${kmNotes.map((note) => {
      const slug = slugify(note.id.split("/").pop().replace(/\.md$/, ""));
      return renderTemplate`<a${addAttribute(`/driftsstotte-vg2/${note.data.emne}/${slug}`, "href")} style="font-size:13px;color:var(--accent);background:var(--surface);border:1px solid var(--border);padding:4px 12px;border-radius:6px;text-decoration:none;transition:border-color .15s;" onmouseover="this.style.borderColor='var(--accent)'" onmouseout="this.style.borderColor='var(--border)'"> ${note.data.title} </a>`;
    })} </div> </div>`;
  })} </div> ` })}`;
}, "/home/ole/workspace/driftsstotte-vg2/src/pages/kompetansemaal.astro", void 0);

const $$file = "/home/ole/workspace/driftsstotte-vg2/src/pages/kompetansemaal.astro";
const $$url = "/driftsstotte-vg2/kompetansemaal";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Kompetansemaal,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
