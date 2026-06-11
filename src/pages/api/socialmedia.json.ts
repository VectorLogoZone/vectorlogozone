import type { APIRoute } from "astro";
import { getSocialMedia } from "../../lib/logos";

export const GET: APIRoute = async () => {
  const payload = {
    success: true,
    data: {
      sites: getSocialMedia()
    }
  };

  return new Response(JSON.stringify(payload, null, 2), {
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "public, max-age=300"
    }
  });
};
