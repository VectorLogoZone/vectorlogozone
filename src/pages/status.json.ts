import type { APIRoute } from "astro";
import { getAllLogoRecords } from "../lib/logos";
import { execSync } from "node:child_process";

const getCommit = () => {
	let retVal = "null";
  try {
    retVal = execSync('git rev-parse --short HEAD').toString().trim();
  } catch {
    return retVal;
  }

  try {
	const isDirty = execSync('git diff --quiet || echo "dirty"').toString().trim();
	if (isDirty === "dirty") {
		retVal = `${retVal}-dirty`;
	}
  } catch {
	return `${retVal}-error`;
  }
  return retVal;
};


export const GET: APIRoute = async () => {
  const records = await getAllLogoRecords();

  let images = 0;
  let pages = 0;
  let pending = 0;

  for (const record of records) {
    const imageCount = Array.isArray(record.data.images) ? record.data.images.length : 0;
    images += imageCount;

    if (imageCount > 0) {
      pages += 1;
    } else {
      pending += 1;
    }
  }

  const payload = {
    success: true,
    message: "OK",
    commit: process.env.GITHUB_SHA?.slice(0, 7) ?? process.env.WORKERS_CI_COMMIT_SHA?.slice(0, 7) ?? getCommit(),
    tech: "astro",
    images,
    lastmod: new Date().toISOString(),
    pages,
    pending
  };

  return new Response(JSON.stringify(payload), {
    headers: {
      "content-type": "application/json; charset=utf-8",
      "cache-control": "public, max-age=300"
    }
  });
};
