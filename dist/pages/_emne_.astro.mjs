/* empty css                                  */
import { b as createAstro, c as createComponent, e as renderComponent, a as renderTemplate, m as maybeRenderHead, d as addAttribute } from '../chunks/astro/server_B0BmM5RJ.mjs';
import 'piccolore';
import { g as getCollection, k as kompetansemaalData } from '../chunks/kompetansemaal_w0e1UOzb.mjs';
import { $ as $$BaseLayout } from '../chunks/BaseLayout_CSal1cln.mjs';
import { g as getEmneColor, E as EMNE_LIST } from '../chunks/emneColors_CfhC5xyU.mjs';
import { s as slugify } from '../chunks/slugify_hFVwgOAe.mjs';
export { renderers } from '../renderers.mjs';

const $$Astro = createAstro("https://Olewol.github.io/driftsstotte-vg2");
async function getStaticPaths() {
  const paths = [];
  for (const emne of EMNE_LIST) {
    paths.push({ params: { emne } });
    paths.push({ params: { emne: emne + "-en" } });
  }
  return paths;
}
const $$Index = createComponent(async ($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$Index;
  const { emne } = Astro2.params;
  const base = "/driftsstotte-vg2";
  const isEnglish = emne.endsWith("-en");
  const baseEmne = isEnglish ? emne.slice(0, -3) : emne;
  const notes = await getCollection(
    "emner",
    (e) => e.data.public !== false && e.id.startsWith(baseEmne + "/")
  );
  const filteredNotes = notes.filter((n) => {
    const filename = n.id.split("/").pop() || "";
    const isEnFile = filename.endsWith("-en.md") || filename.endsWith("-en.mdx");
    return isEnglish ? isEnFile : !isEnFile;
  });
  const { color, bg } = getEmneColor(baseEmne);
  const emneLabel = baseEmne.charAt(0).toUpperCase() + baseEmne.slice(1) + (isEnglish ? " — English" : "");
  const pageLang = isEnglish ? "en" : "no";
  return renderTemplate`${renderComponent($$result, "BaseLayout", $$BaseLayout, { "title": emneLabel, "lang": pageLang }, { "default": async ($$result2) => renderTemplate` ${maybeRenderHead()}<div style="max-width:1140px;margin:0 auto;padding:48px 32px 80px;"> <div${addAttribute(`font-size:12px;font-weight:700;letter-spacing:.1em;text-transform:uppercase;color:${color};margin-bottom:10px;`, "style")}>${emneLabel}</div> <h1 style="font-size:36px;font-weight:800;letter-spacing:-.025em;margin-bottom:32px;"> ${isEnglish ? `All articles in ${baseEmne}` : `Alle notater i ${baseEmne}`} </h1> ${filteredNotes.length === 0 ? renderTemplate`<p style="color:var(--text2);">${isEnglish ? "No published content yet." : "Ingen publisert innhold ennå."}</p>` : renderTemplate`<div style="display:grid;grid-template-columns:repeat(auto-fill,minmax(280px,1fr));gap:14px;"> ${filteredNotes.map((note) => {
    const slug = slugify(note.id.split("/").pop().replace(/\.md$/, ""));
    const kmArray = Array.isArray(note.data.kompetansemaal) ? note.data.kompetansemaal : note.data.kompetansemaal ? [note.data.kompetansemaal] : [];
    const kmTexts = kmArray.map((km) => kompetansemaalData[km] || km).join(" • ");
    return renderTemplate`<a${addAttribute(`${base}/${baseEmne}/${slug}`, "href")}${addAttribute(`background:linear-gradient(145deg,${bg} 0%,var(--surface) 60%);border:1px solid var(--border);border-radius:14px;padding:20px;text-decoration:none;display:block;color:var(--text);transition:transform .18s,border-color .2s;`, "style")} onmouseover="this.style.transform='translateY(-3px)'" onmouseout="this.style.transform=''"> <div style="font-size:15px;font-weight:600;margin-bottom:6px;">${note.data.title}</div> <div style="font-size:13px;color:var(--text2);line-height:1.5;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden;">${kmTexts}</div> </a>`;
  })} </div>`} </div> ` })}`;
}, "/home/ole/workspace/driftsstotte-vg2/src/pages/[emne]/index.astro", void 0);
const $$file = "/home/ole/workspace/driftsstotte-vg2/src/pages/[emne]/index.astro";
const $$url = "/driftsstotte-vg2/[emne]";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Index,
  file: $$file,
  getStaticPaths,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
