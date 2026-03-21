// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwind from '@astrojs/tailwind';

export default defineConfig({
  integrations: [tailwind()],
  markdown: {
    remarkPlugins: [
      ['remark-wiki-link', {
        hrefTemplate: (permalink) => `/${permalink}`,
        pageResolver: (name) => [name],
        aliasDivider: '|',
      }]
    ],
  },
});
