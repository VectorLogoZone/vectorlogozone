import type { APIRoute } from "astro";
import { getAllLogoRecords } from "../../lib/logos";

export const GET: APIRoute = async () => {
  const records = await getAllLogoRecords();
  const data = records.map((record) => record.data);

  return new Response(
    JSON.stringify({
      success: true,
      message: "OK",
      data
    }),
    {
      headers: {
        "content-type": "application/json; charset=utf-8",
        "cache-control": "public, max-age=300"
      }
    }
  );
};
