import { defineCollection, z } from 'astro:content';

const ressursSchema = z.object({
  type: z.enum(['lenke', 'video', 'notat', 'oppgave']),
  tittel: z.string(),
  url: z.string().url().optional(),
  lengde: z.string().optional(),
});

const vekeSchema = z.object({
  uke: z.array(z.number()),
  tema: z.string(),
  emne: z.string().nullable(),
  kompetansemaal: z.string().default(''),
  notat: z.array(z.string()).default([]),
  ressurstal: z.number().default(0),
  oppgavetar: z.number().default(0),
  type: z.enum(['undervisning', 'ferie', 'eksamen', 'prosjekt']).default('undervisning'),
});

export const collections = {
  aarsplan: defineCollection({
    type: 'data',
    schema: z.object({
      title: z.string(),
      skoleaar: z.string(),
      veker: z.array(vekeSchema),
    }),
  }),
  emner: defineCollection({
    type: 'content',
    schema: z.object({
      title: z.string(),
      public: z.boolean().default(true),
      emne: z.string(),
      uke: z.array(z.number()).default([]),
      kompetansemaal: z.string().default(''),
      tags: z.array(z.string()).default([]),
      relatert: z.array(z.string()).default([]),
      ressursar: z.array(ressursSchema).default([]),
      oppgaaver: z.array(z.string()).default([]),
    }),
  }),
};
