import { c as createComponent, m as maybeRenderHead, r as renderScript, a as renderTemplate, b as createAstro, d as addAttribute, e as renderComponent, f as renderSlot, j as renderHead } from './astro/server_B0BmM5RJ.mjs';
import 'piccolore';
import 'clsx';
/* empty css                          */

const $$ThemeToggle = createComponent(($$result, $$props, $$slots) => {
  return renderTemplate`${maybeRenderHead()}<button id="themeToggle" class="icon-btn" aria-label="Bytt til lys modus" style="width:38px;height:38px;background:var(--surface2);border:1px solid var(--border);border-radius:9px;cursor:pointer;font-size:17px;display:flex;align-items:center;justify-content:center;transition:background .15s;">🌙</button> ${renderScript($$result, "/home/ole/workspace/driftsstotte-vg2/src/components/ThemeToggle.astro?astro&type=script&index=0&lang.ts")}`;
}, "/home/ole/workspace/driftsstotte-vg2/src/components/ThemeToggle.astro", void 0);

const $$Astro$2 = createAstro("https://Olewol.github.io/driftsstotte-vg2");
const $$MobileNav = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro$2, $$props, $$slots);
  Astro2.self = $$MobileNav;
  const base = "/driftsstotte-vg2";
  const links = [
    { href: `${base}/`, label: "Årsplan" },
    { href: `${base}/nettverk`, label: "Nettverk" },
    { href: `${base}/sikkerhet`, label: "Sikkerhet" },
    { href: `${base}/operativsystem`, label: "Operativsystem" },
    { href: `${base}/skripting`, label: "Skripting" },
    { href: `${base}/databaser`, label: "Databaser" },
    { href: `${base}/it-drift`, label: "IT-drift" },
    { href: `${base}/kompetansemaal`, label: "Kompetansemål" },
    { href: `${base}/repetisjon`, label: "Eksamensrepetisjon" }
  ];
  const currentPath = Astro2.url.pathname;
  const isEnglish = currentPath.endsWith("-en/");
  let otherLangPath;
  let showLangToggle = true;
  if (currentPath === `${base}/`) {
    showLangToggle = false;
  } else if (currentPath === `${base}/en/`) {
    showLangToggle = false;
  } else {
    otherLangPath = isEnglish ? currentPath.replace(/-en\/$/, "/") : currentPath.replace(/\/$/, "-en/");
  }
  const otherLangLabel = isEnglish ? "Norsk" : "English";
  const otherLangIcon = isEnglish ? "🇳🇴" : "🇬🇧";
  const searchLabel = isEnglish ? "Search" : "Søk";
  return renderTemplate`${maybeRenderHead()}<button id="hamburger"${addAttribute(isEnglish ? "Open menu" : "Åpne meny", "aria-label")} aria-expanded="false" aria-controls="mobileMenu" style="display:none;width:38px;height:38px;background:var(--bg3);border:1px solid var(--border2);border-radius:9px;cursor:pointer;font-size:18px;align-items:center;justify-content:center;color:var(--text);" data-astro-cid-37bvxqo4>☰</button> <div id="mobileMenu" role="dialog" aria-modal="true" aria-label="Navigasjonsmeny" style="display:none;position:fixed;inset:0;background:var(--bg3);z-index:200;padding:24px;flex-direction:column;gap:8px;box-shadow:0 0 0 9999px rgba(0,0,0,0.5);" data-astro-cid-37bvxqo4> <div style="display:flex;align-items:center;justify-content:space-between;margin-bottom:8px;" data-astro-cid-37bvxqo4> <a${addAttribute(`${base}/sok`, "href")} style="flex:1;display:flex;align-items:center;gap:8px;background:var(--surface2);border:1px solid var(--border);border-radius:9px;padding:12px 16px;font-size:15px;color:var(--text2);text-decoration:none;margin-right:8px;" data-astro-cid-37bvxqo4> <span data-astro-cid-37bvxqo4>🔍</span><span data-astro-cid-37bvxqo4>${searchLabel}</span><span style="margin-left:auto;font-size:11px;color:var(--text3);" data-astro-cid-37bvxqo4>↵</span> </a> ${showLangToggle && renderTemplate`<a${addAttribute(otherLangPath, "href")} style="display:flex;align-items:center;gap:4px;background:var(--surface2);border:1px solid var(--border);border-radius:9px;padding:12px;font-size:14px;color:var(--text);text-decoration:none;white-space:nowrap;"${addAttribute(`Bytt språk til ${otherLangLabel}`, "aria-label")} data-astro-cid-37bvxqo4> <span data-astro-cid-37bvxqo4>${otherLangIcon}</span><span style="font-size:13px;" data-astro-cid-37bvxqo4>${otherLangLabel}</span> </a>`} </div> ${links.map((l) => renderTemplate`<a${addAttribute(l.href, "href")} style="font-size:18px;color:var(--text);padding:12px 0;border-bottom:1px solid var(--border);text-decoration:none;" data-astro-cid-37bvxqo4>${l.label}</a>`)} <!-- Close button ved bunnen for lett tilgang --> <button id="closeMenu" aria-label="Lukk menyen" style="margin-top:auto;width:100%;background:var(--surface2);border:1px solid var(--border);border-radius:9px;padding:14px;font-size:16px;color:var(--text);cursor:pointer;" data-astro-cid-37bvxqo4>✕ Lukk</button> </div>  ${renderScript($$result, "/home/ole/workspace/driftsstotte-vg2/src/components/MobileNav.astro?astro&type=script&index=0&lang.ts")}`;
}, "/home/ole/workspace/driftsstotte-vg2/src/components/MobileNav.astro", void 0);

const $$Astro$1 = createAstro("https://Olewol.github.io/driftsstotte-vg2");
const $$Nav = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro$1, $$props, $$slots);
  Astro2.self = $$Nav;
  const { currentPath = "/" } = Astro2.props;
  const base = "/driftsstotte-vg2";
  const links = [
    { href: `${base}/`, label: "Årsplan" },
    { href: `${base}/nettverk`, label: "Nettverk" },
    { href: `${base}/sikkerhet`, label: "Sikkerhet" },
    { href: `${base}/operativsystem`, label: "Operativsystem" },
    { href: `${base}/skripting`, label: "Skripting" },
    { href: `${base}/databaser`, label: "Databaser" },
    { href: `${base}/it-drift`, label: "IT-drift" },
    { href: `${base}/kompetansemaal`, label: "Kompetansemål" },
    { href: `${base}/repetisjon`, label: "Eksamensrepetisjon" }
  ];
  const isEnglish = currentPath.endsWith("-en/");
  const isHomePage = currentPath === `${base}/` || currentPath === `${base}/en/`;
  let otherLangPath = "";
  if (!isHomePage) {
    otherLangPath = isEnglish ? currentPath.replace(/-en\/$/, "/") : currentPath.replace(/\/$/, "-en/");
  }
  const otherLangLabel = isEnglish ? "Norsk" : "English";
  const otherLangIcon = isEnglish ? "🇳🇴" : "🇬🇧";
  const searchLabel = isEnglish ? "Search" : "Søk";
  return renderTemplate`${maybeRenderHead()}<nav role="navigation" aria-label="Hovednavigasjon" style="position:sticky;top:0;z-index:100;background:color-mix(in srgb, var(--bg) 88%, transparent);backdrop-filter:blur(20px);border-bottom:1px solid var(--border);padding:0 32px;height:62px;display:flex;align-items:center;transition:background .3s;" data-astro-cid-dmqpwcec> <a${addAttribute(`${base}/`, "href")} aria-label="Driftsstøtte VG2 – forside" style="display:flex;align-items:center;gap:12px;margin-right:36px;text-decoration:none;" data-astro-cid-dmqpwcec> <div style="width:36px;height:36px;border-radius:9px;background:var(--grad);display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:900;color:#fff;flex-shrink:0;" data-astro-cid-dmqpwcec>DS</div> <div data-astro-cid-dmqpwcec> <div style="font-size:15px;font-weight:700;color:var(--text);letter-spacing:-.01em;" data-astro-cid-dmqpwcec>Driftsstøtte</div> <div style="font-size:11px;color:var(--text2);" data-astro-cid-dmqpwcec>VG2 Informasjonsteknologi</div> </div> </a> <div class="desktop-links" style="display:flex;gap:2px;flex:1;" data-astro-cid-dmqpwcec> ${links.map((l) => renderTemplate`<a${addAttribute(l.href, "href")}${addAttribute(currentPath === l.href ? "page" : void 0, "aria-current")}${addAttribute(`padding:7px 14px;font-size:14px;color:${currentPath === l.href ? "var(--text)" : "var(--text2)"};text-decoration:none;border-radius:7px;background:${currentPath === l.href ? "var(--surface2)" : "transparent"};transition:color .15s,background .15s;`, "style")} data-astro-cid-dmqpwcec>${l.label}</a>`)} </div> <div style="display:flex;align-items:center;gap:10px;margin-left:auto;" data-astro-cid-dmqpwcec> <a${addAttribute(`${base}/sok`, "href")} class="desktop-links" style="background:var(--surface2);border:1px solid var(--border);border-radius:9px;padding:7px 14px;font-size:14px;color:var(--text2);display:flex;align-items:center;gap:7px;width:190px;text-decoration:none;"${addAttribute(searchLabel, "aria-label")} data-astro-cid-dmqpwcec> <span data-astro-cid-dmqpwcec>🔍</span><span data-astro-cid-dmqpwcec>${searchLabel}…</span> <kbd style="margin-left:auto;background:var(--bg3);border:1px solid var(--border2);border-radius:4px;padding:1px 6px;font-size:11px;color:var(--text3);" data-astro-cid-dmqpwcec>⌘K</kbd> </a> ${!isHomePage && renderTemplate`<a${addAttribute(otherLangPath, "href")} class="desktop-links" style="display:inline-flex;align-items:center;gap:5px;background:var(--surface2);border:1px solid var(--border);border-radius:8px;padding:7px 12px;font-size:13px;color:var(--text2);text-decoration:none;transition:color .15s,background .15s,border-color .15s;white-space:nowrap;"${addAttribute(`Bytt språk til ${otherLangLabel}`, "aria-label")} data-astro-cid-dmqpwcec> <span data-astro-cid-dmqpwcec>${otherLangIcon}</span> <span style="font-weight:600;" data-astro-cid-dmqpwcec>${otherLangLabel}</span> </a>`} ${renderComponent($$result, "ThemeToggle", $$ThemeToggle, { "data-astro-cid-dmqpwcec": true })} ${renderComponent($$result, "MobileNav", $$MobileNav, { "data-astro-cid-dmqpwcec": true })} </div> </nav> `;
}, "/home/ole/workspace/driftsstotte-vg2/src/components/Nav.astro", void 0);

var __freeze = Object.freeze;
var __defProp = Object.defineProperty;
var __template = (cooked, raw) => __freeze(__defProp(cooked, "raw", { value: __freeze(cooked.slice()) }));
var _a;
const $$Astro = createAstro("https://Olewol.github.io/driftsstotte-vg2");
const $$BaseLayout = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$BaseLayout;
  const { title, description = "Driftsst\xF8tte VG2 Informasjonsteknologi", lang = "no" } = Astro2.props;
  const currentPath = Astro2.url.pathname;
  return renderTemplate(_a || (_a = __template(["<html", '> <head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><meta name="description"', "><title>", ` \u2014 Driftsst\xF8tte VG2</title><link rel="icon" type="image/svg+xml" href="/driftsstotte-vg2/favicon.svg"><script>
    // Prevent flash of wrong theme
    const t = localStorage.getItem('theme') ?? (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    document.documentElement.dataset.theme = t;
  <\/script>`, '</head> <body> <a class="skip-link" href="#main">Hopp til innhold</a> ', ' <main id="main" style="position:relative;z-index:1;"> ', " </main> </body></html>"])), addAttribute(lang, "lang"), addAttribute(description, "content"), title, renderHead(), renderComponent($$result, "Nav", $$Nav, { "currentPath": currentPath }), renderSlot($$result, $$slots["default"]));
}, "/home/ole/workspace/driftsstotte-vg2/src/layouts/BaseLayout.astro", void 0);

export { $$BaseLayout as $ };
