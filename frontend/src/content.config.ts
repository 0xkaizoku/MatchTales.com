import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const source = z.object({ name: z.string(), url: z.string() });
const leaderboardRow = z.object({
  pos: z.string(),
  name: z.string(),
  score: z.string(),
  note: z.string().optional().default(''),
});
const tennisSet = z.object({ p1: z.string(), p2: z.string() });

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
    matchday: z.number().optional().default(0),
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
    sport: z.string().optional().default('soccer'),
    competition: z.string().optional().default('world-cup-2026'),
    format: z.enum(['team-match', 'singles', 'race', 'leaderboard']).optional().default('team-match'),
    season: z.string().optional().default(''),
    roundLabel: z.string().optional().default(''),
    resultSummary: z.string().optional().default(''),
    leaderboard: z.array(leaderboardRow).optional().default([]),
    tennisSets: z.array(tennisSet).optional().default([]),
    sources: z.array(source).optional().default([]),
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
    sport: z.string().optional().default('soccer'),
    competition: z.string().optional().default(''),
    relatedSlug: z.string().optional().default(''),
    sources: z.array(source).optional().default([]),
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
