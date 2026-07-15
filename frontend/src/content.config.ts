import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const matches = defineCollection({
  loader: glob({ pattern: '*.json', base: './src/content/matches' }),
  schema: z.object({
    slug: z.string(),
    headline: z.string(),
    whyCareScore: z.number(),
    whyCareReason: z.string(),
    teaser: z.string(),
    story: z.string(),
    stakes: z.string(),
    rivalryAngle: z.string(),
    funFacts: z.array(z.string()),
    keyPlayers: z.array(z.object({ name: z.string(), team: z.string(), hook: z.string() })),
    headToHead: z.string().optional().default(''),
    tags: z.array(z.string()).default([]),
    home: z.string(),
    away: z.string(),
    homeCode: z.string().optional().nullable(),
    awayCode: z.string().optional().nullable(),
    homeFlag: z.string().optional().nullable(),
    awayFlag: z.string().optional().nullable(),
    group: z.string(),
    matchday: z.number(),
    date: z.string(),
    time: z.string(),
    venue: z.string(),
    city: z.string(),
    status: z.string(),
    homeScore: z.union([z.number(), z.string()]).nullable().optional(),
    awayScore: z.union([z.number(), z.string()]).nullable().optional(),
    marquee: z.boolean().default(false),
    liveMinute: z.union([z.number(), z.string()]).nullable().optional(),
    image: z.string().optional().nullable(),
    decidedBy: z.string().optional().nullable(),
    homePen: z.union([z.number(), z.string()]).nullable().optional(),
    awayPen: z.union([z.number(), z.string()]).nullable().optional(),
  }),
});

const stories = defineCollection({
  loader: glob({ pattern: '*.md', base: './src/content/stories' }),
  schema: z.object({
    title: z.string(),
    subtitle: z.string().optional().default(''),
    category: z.string(),
    excerpt: z.string(),
    image: z.string(),
    readingTime: z.number().default(5),
    pubDate: z.coerce.date(),
  }),
});

const teams = defineCollection({
  loader: glob({ pattern: '*.json', base: './src/content/teams' }),
  schema: z.object({
    slug: z.string(),
    name: z.string(),
    dossier: z.string(),
    whatToWatch: z.string(),
    xFactor: z.string(),
    verdict: z.string(),
    funFacts: z.array(z.string()).default([]),
  }),
});

export const collections = { matches, stories, teams };
