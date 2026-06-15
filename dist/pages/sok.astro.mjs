/* empty css                                  */
import { c as createComponent, a as renderTemplate, d as addAttribute, e as renderComponent, m as maybeRenderHead } from '../chunks/astro/server_B0BmM5RJ.mjs';
import 'piccolore';
import { $ as $$BaseLayout } from '../chunks/BaseLayout_CSal1cln.mjs';
export { renderers } from '../renderers.mjs';

var __freeze = Object.freeze;
var __defProp = Object.defineProperty;
var __template = (cooked, raw) => __freeze(__defProp(cooked, "raw", { value: __freeze(cooked.slice()) }));
var _a;
const $$Sok = createComponent(($$result, $$props, $$slots) => {
  const base = "/driftsstotte-vg2";
  return renderTemplate(_a || (_a = __template(["", ' <link rel="stylesheet"', "> <script", "></script> <script>\n  window.addEventListener('DOMContentLoaded', () => {\n    if (typeof PagefindUI !== 'undefined') {\n      new PagefindUI({\n        element: '#search',\n        showSubResults: true,\n        resetStyles: false,\n        baseUrl: '/driftsstotte-vg2/',\n      });\n    }\n  });\n</script>"])), renderComponent($$result, "BaseLayout", $$BaseLayout, { "title": "Søk" }, { "default": ($$result2) => renderTemplate` ${maybeRenderHead()}<div style="max-width:860px;margin:0 auto;padding:48px 32px 80px;"> <h1 style="font-size:36px;font-weight:800;margin-bottom:10px;">Søk</h1> <p style="font-size:16px;color:var(--text2);margin-bottom:32px;">Søk i alt innhold på siden.</p> <div id="search" style="--pagefind-ui-scale:1;--pagefind-ui-primary:var(--accent);--pagefind-ui-text:var(--text);--pagefind-ui-background:var(--bg2);--pagefind-ui-border:var(--border2);--pagefind-ui-tag:var(--bg3);"></div> </div> ` }), addAttribute(`${base}pagefind/pagefind-ui.css`, "href"), addAttribute(`${base}pagefind/pagefind-ui.js`, "src"));
}, "/home/ole/workspace/driftsstotte-vg2/src/pages/sok.astro", void 0);
const $$file = "/home/ole/workspace/driftsstotte-vg2/src/pages/sok.astro";
const $$url = "/driftsstotte-vg2/sok";

const _page = /*#__PURE__*/Object.freeze(/*#__PURE__*/Object.defineProperty({
  __proto__: null,
  default: $$Sok,
  file: $$file,
  url: $$url
}, Symbol.toStringTag, { value: 'Module' }));

const page = () => _page;

export { page };
