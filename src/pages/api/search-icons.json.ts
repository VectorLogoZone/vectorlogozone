import type { APIRoute } from "astro";
import { buildSearchImageData } from "../../lib/search-data";

export const GET: APIRoute = async () => {
  const payload = await buildSearchImageData({
    targetSuffix: "-icon",
    targetName: "(icons)",
    width: 64,
    height: 64
  });

  return new Response(JSON.stringify(payload, null, 2), {
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "public, max-age=300"
    }
  });
};
