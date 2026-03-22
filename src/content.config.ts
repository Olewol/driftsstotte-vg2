import { defineCollection, z } from 'astro:content';

const ressursSchema = z.object({
  type: z.enum(['lenke', 'video', 'notat', 'oppgave']),
  tittel: z.string(),
  url: z.string().optional(),
  lengde: z.string().optional(),
});

const aarsplan = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    skoleaar: z.string(),
    veker: z.array(z.object({
      uke: z.array(z.number()),
      tema: z.string(),
      emne: z.string().nullable().optional(),
      kompetansemaal: z.string().optional().default(''),
      notat: z.array(z.string()).optional().default([]),
      ressurstal: z.number().optional().default(0),
      oppgavetar: z.number().optional().default(0),
      type: z.enum(['undervisning', 'ferie', 'eksamen', 'prosjekt']),
    })),
  }),
});

const emner = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    public: z.boolean().optional().default(true),
    emne: z.string(),
    uke: z.array(z.number()),
    kompetansemaal: z.string(),
    tags: z.array(z.string()).optional().default([]),
    relatert: z.array(z.string()).optional().default([]),
    ressursar: z.array(ressursSchema).optional().default([]),
    oppgaaver: z.array(z.string()).optional().default([]),
  }),
});

const oppgaver = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    public: z.boolean().optional().default(true),
    emne: z.string().optional(),
    uke: z.array(z.number()).optional().default([]),
  }),
});

const ressursar = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    public: z.boolean().optional().default(true),
    type: z.enum(['lenke', 'video', 'notat', 'oppgave']).optional(),
    url: z.string().optional(),
  }),
});

export const collections = { aarsplan, emner, oppgaver, ressursar };
