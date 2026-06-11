import type { APIRoute } from "astro";
import { getAllLogoRecords } from "../lib/logos";
import { siteConfig } from "../lib/site";

const xmlEscape = (value: string) =>
  value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&apos;");

const staticPaths = [
  "/",
  "/about.html",
  "/logos/index.html",
  "/logos/tags.html",
  "/support/index.html",
  "/report/index.html",
  "/report/all-ar21.html",
  "/report/all-horizontal.html",
  "/report/all-icon.html",
  "/report/all-official.html",
  "/report/all-tile.html",
  "/report/all-wordmark.html",
  "/report/colors.html",
  "/report/first-letter.html",
  "/report/fonts.html",
  "/report/icon-vs-favicon.html",
  "/report/icon-vs-svgporn.html",
  "/report/icon-vs-tile.html",
  "/report/inventory.html",
  "/report/least-social.html",
  "/report/metadata.html",
  "/report/missing.html",
  "/report/most-social.html",
  "/report/notes.html",
  "/report/official-vs-all.html",
  "/report/tags.html",
  "/report/takedown.html",
  "/report/tile-vs-supertiny.html",
  "/report/unknown-meta.html",
  "/report/visual.html"
];

export const GET: APIRoute = async () => {
  const records = await getAllLogoRecords();
  const sorted = [...records].sort((a, b) => a.data.sort.localeCompare(b.data.sort));

  let logoCount = 0;
  let pageCount = 0;

  const urls: string[] = [];

  for (const relPath of staticPaths) {
    pageCount += 1;
    urls.push(`  <url>\n    <loc>${xmlEscape(`${siteConfig.productionUrl}${relPath}`)}</loc>\n  </url>`);
  }

  for (const record of sorted) {
    const data = record.data;
    if (data.noindex || !data.logohandle || !Array.isArray(data.images) || data.images.length === 0) {
      continue;
    }

    logoCount += 1;
    pageCount += 1;

    const base = `${siteConfig.productionUrl}/logos/${data.logohandle}/`;
    const imageNodes = data.images
      .filter((img) => img.toLowerCase().endsWith(".svg"))
      .map(
        (img) =>
          `    <image:image>\n      <image:loc>${xmlEscape(`${base}${img}`)}</image:loc>\n    </image:image>`
      )
      .join("\n");

    urls.push(
      [
        "  <url>",
        `    <loc>${xmlEscape(`${base}${siteConfig.indexPage}`)}</loc>`,
        imageNodes,
        "  </url>"
      ]
        .filter(Boolean)
        .join("\n")
    );
  }

  const body = [
    '<?xml version="1.0" encoding="UTF-8"?>',
    '<?xml-stylesheet type="text/xsl" href="sitemap.xslt"?>',
    '<urlset',
    '    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"',
    '    xsi:schemaLocation="http://www.sitemaps.org/schemas/sitemap/0.9"',
    '    xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
    '    xmlns:image="http://www.google.com/schemas/sitemap-image/1.1">',
    urls.join("\n"),
    '</urlset>',
    `<!-- logos: ${logoCount} pages: ${pageCount} -->`
  ].join("\n");

  return new Response(body, {
    headers: {
      "content-type": "application/xml; charset=utf-8"
    }
  });
};
