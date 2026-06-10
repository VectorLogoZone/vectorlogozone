import type { APIRoute } from "astro";
import { getVisibleLogoRecords } from "../../lib/logos";

export const GET: APIRoute = async () => {
  const records = await getVisibleLogoRecords();
  const payload: Record<string, { title: string; haslogo: boolean; website?: string; keywords?: unknown }> = {};

  for (const record of records) {
    const data = record.data;
    const logohandle = data.logohandle;

    if (!logohandle) {
      continue;
    }

    const ar21 = `${logohandle}-ar21.svg`;
    const item: { title: string; haslogo: boolean; website?: string; keywords?: unknown } = {
      title: data.title || logohandle,
      haslogo: Array.isArray(data.images) && data.images.includes(ar21),
      website: data.website
    };

    if (data.keywords !== undefined) {
      item.keywords = data.keywords;
    }

    payload[logohandle] = item;
  }

  return new Response(JSON.stringify(payload), {
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "public, max-age=300"
    }
  });
};
