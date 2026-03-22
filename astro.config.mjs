// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';
import { slugify } from './src/lib/slugify.js';

export default defineConfig({
  site: 'https://Olewol.github.io/driftsstotte-vg2',
  base: '/driftsstotte-vg2',
  integrations: [tailwind()],
  markdown: {
    remarkPlugins: [
      ['remark-wiki-link', {
        hrefTemplate: (permalink) => `/${permalink}`,
        pageResolver: (name) => [slugify(name)],
        aliasDivider: '|',
      }],
    ],
  },
});
