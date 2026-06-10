import { defineCollection, z } from "astro:content";
import { glob } from "astro/loaders";

const logos = defineCollection({
  loader: glob({ pattern: "**/index.md", base: "./src/content/logos" }),
  schema: z.object({
    logohandle: z.string().optional(),
    title: z.string().optional(),
    sort: z.string().optional(),
    subtitle: z.string().optional(),
    h1: z.string().optional(),
    noindex: z.boolean().optional(),
    no_h1: z.boolean().optional(),
    images: z.array(z.string()).optional(),
    colors: z.array(z.string()).optional(),
    tags: z.array(z.string()).optional(),
    notes: z.string().optional(),
    guide: z.string().optional(),
    website: z.string().optional(),
    redirect_from: z.union([z.string(), z.array(z.string())]).optional(),
    font: z.any().optional()
  }).passthrough()
});

export const collections = {
  logos
};
