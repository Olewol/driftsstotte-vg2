// astro.config.mjs
import fs from 'node:fs';
import path from 'node:path';
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import { slugify } from './src/lib/slugify.js';
import rehypeExternalLinks from 'rehype-external-links';

const BASE = '/driftsstotte-vg2';
const emnerDir = path.resolve('./src/content/emner');
const slugToEmne = {};

if (fs.existsSync(emnerDir)) {
  const emnerFolders = fs.readdirSync(emnerDir);
  for (const emne of emnerFolders) {
    const emnePath = path.join(emnerDir, emne);
    if (fs.statSync(emnePath).isDirectory()) {
      const files = fs.readdirSync(emnePath);
      for (const file of files) {
        if (file.endsWith('.md') || file.endsWith('.mdx')) {
          const slug = slugify(file.replace(/\.mdx?$/, ''));
          slugToEmne[slug] = emne;
        }
      }
    }
  }
}

export default defineConfig({
  site: 'https://Olewol.github.io/driftsstotte-vg2',
  base: BASE,
  integrations: [tailwind()],
  markdown: {
    remarkPlugins: [
      ['remark-wiki-link', {
        hrefTemplate: (permalink) => {
          const slug = slugify(permalink);
          const emne = slugToEmne[slug];
          return emne ? `${BASE}/${emne}/${slug}` : `${BASE}/${slug}`;
        },
        pageResolver: (name) => [slugify(name)],
        aliasDivider: '|',
      }],
    ],
    rehypePlugins: [
      [rehypeExternalLinks, { target: '_blank', rel: ['noopener', 'noreferrer'] }]
    ],
  },
});
