import { c as createComponent, e as renderComponent, r as renderScript, a as renderTemplate, b as createAstro, m as maybeRenderHead, d as addAttribute, l as createVNode, J as Fragment, _ as __astro_tag_component__ } from './astro/server_B0BmM5RJ.mjs';
import 'piccolore';
/* empty css                                 */
/* empty css                                                               */
import 'clsx';
/* empty css                                                                 */

const urlPattern = /(?=(\s*))\1(?:<a [^>]*?>)??(?=(\s*))\2(?:https?:\/\/)??(?:w{3}\.)??(?:youtube\.com|youtu\.be)\/(?:watch\?v=|embed\/|shorts\/)??([A-Za-z0-9-_]{11})(?:[^\s<>]*)(?=(\s*))\4(?:<\/a>)??(?=(\s*))\5/;
function matcher(url) {
  const match = url.match(urlPattern);
  return match?.[3];
}

const $$Astro$1 = createAstro("https://Olewol.github.io/driftsstotte-vg2");
const $$YouTube = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro$1, $$props, $$slots);
  Astro2.self = $$YouTube;
  const {
    id,
    poster,
    posterQuality = "default",
    title,
    style,
    ...attrs
  } = Astro2.props;
  const idRegExp = /^[A-Za-z0-9-_]+$/;
  function extractID(idOrUrl) {
    if (idRegExp.test(idOrUrl)) return idOrUrl;
    return matcher(idOrUrl);
  }
  const videoid = extractID(id);
  const posterFile = {
    max: "maxresdefault",
    high: "sddefault",
    default: "hqdefault",
    low: "default"
  }[posterQuality] || "hqdefault";
  const posterURL = poster || `https://i.ytimg.com/vi/${videoid}/${posterFile}.jpg`;
  const href = `https://youtube.com/watch?v=${videoid}`;
  const styles = [];
  if (style) styles.push(style);
  if (posterURL) styles.push(`background-image: url('${posterURL}')`);
  return renderTemplate`${renderComponent($$result, "lite-youtube", "lite-youtube", { "videoid": videoid, "title": title, "data-title": title, ...attrs, "style": styles.join(";") }, { "default": () => renderTemplate` ${maybeRenderHead()}<a${addAttribute(href, "href")} class="lyt-playbtn"> <span class="lyt-visually-hidden">${attrs.playlabel || "Play"}</span> </a> ` })} ${renderScript($$result, "/home/ole/workspace/driftsstotte-vg2/node_modules/.pnpm/@astro-community+astro-embed-youtube@0.5.10/node_modules/@astro-community/astro-embed-youtube/YouTube.astro?astro&type=script&index=0&lang.ts")} `;
}, "/home/ole/workspace/driftsstotte-vg2/node_modules/.pnpm/@astro-community+astro-embed-youtube@0.5.10/node_modules/@astro-community/astro-embed-youtube/YouTube.astro", void 0);

const $$Astro = createAstro("https://Olewol.github.io/driftsstotte-vg2");
const $$FlashCard = createComponent(($$result, $$props, $$slots) => {
  const Astro2 = $$result.createAstro($$Astro, $$props, $$slots);
  Astro2.self = $$FlashCard;
  const { question, answer, emoji = "\u{1F4C7}" } = Astro2.props;
  const uid = Math.random().toString(36).slice(2, 8);
  return renderTemplate`${maybeRenderHead()}<div class="flashcard"${addAttribute(uid, "data-fcid")} role="button" tabindex="0"${addAttribute(`Sp\xF8rsm\xE5l: ${question}`, "aria-label")} data-astro-cid-hwx6ohlm> <div class="fc-front" data-astro-cid-hwx6ohlm> <span class="fc-icon" data-astro-cid-hwx6ohlm>${emoji}</span> <span class="fc-q" data-astro-cid-hwx6ohlm>${question}</span> <span class="fc-hint" data-astro-cid-hwx6ohlm>Klikk for svar</span> </div> <div class="fc-back" aria-hidden="true" data-astro-cid-hwx6ohlm> <span class="fc-a" data-astro-cid-hwx6ohlm>${answer}</span> </div> </div>  ${renderScript($$result, "/home/ole/workspace/driftsstotte-vg2/src/components/FlashCard.astro?astro&type=script&index=0&lang.ts")}`;
}, "/home/ole/workspace/driftsstotte-vg2/src/components/FlashCard.astro", void 0);

const frontmatter = {
  "title": "OSI-modellen (interaktiv)",
  "emne": "nettverk",
  "kompetansemaal": ["km-05"],
  "public": true,
  "language": "nb"
};
function getHeadings() {
  return [{
    "depth": 2,
    "slug": "introduksjon",
    "text": "Introduksjon"
  }, {
    "depth": 2,
    "slug": "interaktive-flashcards--osi-modellen",
    "text": "Interaktive Flashcards — OSI-modellen"
  }, {
    "depth": 2,
    "slug": "fordeler-med-osi-modellen",
    "text": "Fordeler med OSI-modellen"
  }];
}
function _createMdxContent(props) {
  const _components = {
    h2: "h2",
    li: "li",
    p: "p",
    ul: "ul",
    ...props.components
  };
  return createVNode(Fragment, {
    children: [createVNode(_components.h2, {
      id: "introduksjon",
      children: "Introduksjon"
    }), "\n", createVNode(_components.p, {
      children: "OSI-modellen (Open Systems Interconnection) er en 7-lags referansemodell utviklet av ISO. Den er standarden for å beskrive og forstå nettverkskommunikasjon."
    }), "\n", createVNode($$YouTube, {
      id: "vv4y_uOneC0"
    }), "\n", createVNode(_components.h2, {
      id: "interaktive-flashcards--osi-modellen",
      children: "Interaktive Flashcards — OSI-modellen"
    }), "\n", createVNode($$FlashCard, {
      question: "Hva er lag 1 i OSI-modellen?",
      answer: "Fysisk lag (Physical Layer) — overfører rå bits over kabel eller trådløst",
      emoji: "🔌"
    }), "\n", createVNode($$FlashCard, {
      question: "Hva gjør Datalink-laget (lag 2)?",
      answer: "Håndterer MAC-adresser og overfører rammer mellom enheter på samme nettverk",
      emoji: "🔗"
    }), "\n", createVNode($$FlashCard, {
      question: "Hva er Nettverkslagets (lag 3) viktigste oppgave?",
      answer: "Ruting — finne beste vei gjennom nettverket ved hjelp av IP-adresser",
      emoji: "🌐"
    }), "\n", createVNode($$FlashCard, {
      question: "Hva gjør Transportlaget (lag 4)?",
      answer: "Sikrer pålitelig eller rask datalevering via TCP (pålitelig) eller UDP (rask)",
      emoji: "📦"
    }), "\n", createVNode($$FlashCard, {
      question: "Nevn lag 5, 6 og 7 i OSI-modellen",
      answer: "5: Sesjonslag — styrer samtaler, 6: Presentasjonslag — kryptering/koding, 7: Applikasjonslag — protokoller som HTTP",
      emoji: "📚"
    }), "\n", createVNode(_components.h2, {
      id: "fordeler-med-osi-modellen",
      children: "Fordeler med OSI-modellen"
    }), "\n", createVNode(_components.ul, {
      children: ["\n", createVNode(_components.li, {
        children: "Standardisert feilsøking: “På hvilket lag oppstår problemet?”"
      }), "\n", createVNode(_components.li, {
        children: "Felles vokabular for nettverksteknikere"
      }), "\n", createVNode(_components.li, {
        children: "Separerer ansvar — hvert lag har sin jobb"
      }), "\n", createVNode(_components.li, {
        children: "Lettere å forstå kompleks kommunikasjon"
      }), "\n"]
    })]
  });
}
function MDXContent(props = {}) {
  const {wrapper: MDXLayout} = props.components || ({});
  return MDXLayout ? createVNode(MDXLayout, {
    ...props,
    children: createVNode(_createMdxContent, {
      ...props
    })
  }) : _createMdxContent(props);
}

const url = "src/content/emner/nettverk/osi-modellen-interaktiv.mdx";
const file = "/home/ole/workspace/driftsstotte-vg2/src/content/emner/nettverk/osi-modellen-interaktiv.mdx";
const Content = (props = {}) => MDXContent({
  ...props,
  components: { Fragment: Fragment, ...props.components, },
});
Content[Symbol.for('mdx-component')] = true;
Content[Symbol.for('astro.needsHeadRendering')] = !Boolean(frontmatter.layout);
Content.moduleId = "/home/ole/workspace/driftsstotte-vg2/src/content/emner/nettverk/osi-modellen-interaktiv.mdx";
__astro_tag_component__(Content, 'astro:jsx');

export { Content, Content as default, file, frontmatter, getHeadings, url };
