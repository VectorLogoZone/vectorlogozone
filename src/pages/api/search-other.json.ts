import type { APIRoute } from "astro";
import { buildSearchOtherData } from "../../lib/search-data";

export const GET: APIRoute = async () => {
  const payload = await buildSearchOtherData({
    targetSuffix: "-other",
    targetName: "(other)"
  });

  return new Response(JSON.stringify(payload, null, 2), {
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "public, max-age=300"
    }
  });
};
