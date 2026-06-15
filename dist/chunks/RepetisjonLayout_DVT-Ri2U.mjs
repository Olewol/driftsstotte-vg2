import { b as createAstro, c as createComponent, e as renderComponent, r as renderScript, a as renderTemplate, m as maybeRenderHead, d as addAttribute, f as renderSlot } from './astro/server_B0BmM5RJ.mjs';
import 'piccolore';
import { $ as $$BaseLayout } from './BaseLayout_CSal1cln.mjs';
/* empty css                                         */

const $$Astro = createAstro("https://Olewol.github.io/driftsstotte-vg2");
const $$RepetisjonLayout = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$RepetisjonLayout;
  const { title, description, prev, next, prevLabel, nextLabel } = Astro2.props;
  const base = "/driftsstotte-vg2";
  const path = Astro2.url.pathname;
  const topics = [
    "brukeradministrasjon",
    "infrastruktur-maskinvare",
    "nettverk-segmentering",
    "nettverkssikkerhet",
    "servermodeller-virtualisering",
    "backup-gjenoppretting",
    "dokumentasjon-planlegging",
    "nettverksprotokoller",
    "sikkerhet-driftsprinsipper"
  ];
  const topicIndex = topics.findIndex((t) => path.includes(t)) + 1;
  const totalTopics = topics.length;
  const topicSlug = topics[topicIndex - 1] || "";
  return renderTemplate`${renderComponent($$result, "BaseLayout", $$BaseLayout, { "title": title, "description": description, "lang": "no", "data-astro-cid-2g6q35qg": true }, { "default": ($$result2) => renderTemplate` ${maybeRenderHead()}<article class="repetisjon-article" data-astro-cid-2g6q35qg> <!-- Breadcrumb + progress --> <div class="rep-header" data-astro-cid-2g6q35qg> <div class="rep-breadcrumb" data-astro-cid-2g6q35qg> <a${addAttribute(`${base}/repetisjon`, "href")} data-astro-cid-2g6q35qg>Forberedelse</a> <span data-astro-cid-2g6q35qg>/</span> <span data-astro-cid-2g6q35qg>${title}</span> </div> <div class="rep-dots" aria-label="Tema {topicIndex} av {totalTopics}" data-astro-cid-2g6q35qg> <div class="rep-dot-row" data-astro-cid-2g6q35qg> ${Array.from({ length: totalTopics }, (_, i) => renderTemplate`<div${addAttribute(`rep-dot ${i < topicIndex ? "rep-dot--done" : ""} ${i === topicIndex - 1 ? "rep-dot--active" : ""}`, "class")} data-astro-cid-2g6q35qg></div>`)} </div> <span class="rep-dots-label" data-astro-cid-2g6q35qg>${topicIndex}/${totalTopics}</span> </div> </div> <!-- Progress bar --> <div class="rep-progress-bar" data-astro-cid-2g6q35qg> <div class="rep-progress-fill" style="width:\${(topicIndex / totalTopics) * 100}%" data-astro-cid-2g6q35qg></div> </div> <!-- Header --> <div class="rep-hero" data-astro-cid-2g6q35qg> <div class="rep-hero-badge" data-astro-cid-2g6q35qg> <span class="rep-hero-check" id="theme-check"${addAttribute(topicSlug, "data-slug")} onclick="toggleCompletion(this)" data-astro-cid-2g6q35qg>○</span>
Tema ${topicIndex} av ${totalTopics} </div> <h1 class="rep-hero-title" data-astro-cid-2g6q35qg>${title}</h1> ${description && renderTemplate`<p class="rep-hero-desc" data-astro-cid-2g6q35qg>${description}</p>`} </div> <!-- Desktop: sidebar + content grid --> <div class="rep-layout" data-astro-cid-2g6q35qg> <!-- TOC Sidebar --> <nav class="rep-toc" aria-label="På denne siden" data-astro-cid-2g6q35qg> <div class="rep-toc-title" data-astro-cid-2g6q35qg>På denne siden</div> <ul id="toc-list" class="rep-toc-list" data-astro-cid-2g6q35qg></ul> </nav> <!-- Content --> <div class="rep-prose" data-astro-cid-2g6q35qg> ${renderSlot($$result2, $$slots["default"])} </div> </div> <!-- Bottom nav --> <div class="rep-bottom-nav" data-astro-cid-2g6q35qg> ${prev ? renderTemplate`<a${addAttribute(`${base}/repetisjon/${prev}`, "href")} class="rep-nav-link rep-nav-link--prev" data-astro-cid-2g6q35qg> <div class="rep-nav-label" data-astro-cid-2g6q35qg>← Forrige tema</div> <div class="rep-nav-title" data-astro-cid-2g6q35qg>${prevLabel || prev}</div> </a>` : renderTemplate`<div style="flex:1;" data-astro-cid-2g6q35qg></div>`} ${next ? renderTemplate`<a${addAttribute(`${base}/repetisjon/${next}`, "href")} class="rep-nav-link rep-nav-link--next" data-astro-cid-2g6q35qg> <div class="rep-nav-label" data-astro-cid-2g6q35qg>Neste tema →</div> <div class="rep-nav-title" data-astro-cid-2g6q35qg>${nextLabel || next}</div> </a>` : renderTemplate`<div style="flex:1;" data-astro-cid-2g6q35qg></div>`} </div> <div class="rep-back-link" data-astro-cid-2g6q35qg> <a${addAttribute(`${base}/repetisjon`, "href")} data-astro-cid-2g6q35qg>← Tilbake til oversikten</a> </div> </article>  <button id="scroll-top" class="rep-scroll-top" onclick="window.scrollTo({top:0,behavior:'smooth'})" aria-label="Til toppen" data-astro-cid-2g6q35qg>↑</button> ` })}  ${renderScript($$result, "/home/ole/workspace/driftsstotte-vg2/src/layouts/RepetisjonLayout.astro?astro&type=script&index=0&lang.ts")}`;
}, "/home/ole/workspace/driftsstotte-vg2/src/layouts/RepetisjonLayout.astro", void 0);

export { $$RepetisjonLayout as $ };
