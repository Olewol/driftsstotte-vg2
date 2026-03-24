// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import { slugify } from './src/lib/slugify.js';

const BASE = '/driftsstotte-vg2';

export default defineConfig({
  site: 'https://Olewol.github.io/driftsstotte-vg2',
  base: BASE,
  integrations: [tailwind()],
  markdown: {
    remarkPlugins: [
      ['remark-wiki-link', {
        hrefTemplate: (permalink) => `${BASE}/${permalink}`,
        pageResolver: (name) => [slugify(name)],
        aliasDivider: '|',
      }],
    ],
  },
});
