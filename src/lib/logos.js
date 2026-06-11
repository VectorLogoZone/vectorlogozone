import { readFileSync } from "node:fs";
import { parse as parseYaml } from "yaml";
import { getCollection } from "astro:content";

const repoRoot = process.cwd();
const dataRoot = `${repoRoot}/src/data`;

let logoRecordsPromise;
let imageTypesCache;
let socialMediaCache;
let tagsCache;
let svgpornCache;
let simpleIconsCache;
let faviconsCache;
let supertinyIconsCache;
let rasterSizesCache;

const readYaml = (filename) => {
  const source = readFileSync(`${dataRoot}/${filename}`, "utf8");
  return parseYaml(source);
};

const readJson = (filename) => {
  const source = readFileSync(`${dataRoot}/${filename}`, "utf8");
  return JSON.parse(source);
};

const loadLogoRecords = async () => {
  if (logoRecordsPromise) {
    return logoRecordsPromise;
  }

  logoRecordsPromise = (async () => {
    const entries = await getCollection("logos");

    const records = entries.map((entry) => {
      const defaultHandle = entry.id.split("/")[0];
      const data = entry.data || {};
      const handle = data.logohandle || defaultHandle;

      return {
        handle,
        data: {
          ...data,
          logohandle: handle,
          title: data.title || handle,
          sort: (data.sort || data.title || handle).toString().toLowerCase(),
          images: Array.isArray(data.images) ? data.images : []
        },
        content: entry.body || ""
      };
    });

    records.sort((a, b) => a.data.sort.localeCompare(b.data.sort));
    return records;
  })();

  return logoRecordsPromise;
};

export const getLogoHandles = async () => (await loadLogoRecords()).map((record) => record.handle);

export const getLogoRecord = async (handle) => (await loadLogoRecords()).find((record) => record.handle === handle);

export const getAllLogoRecords = async () => loadLogoRecords();

export const getVisibleLogoRecords = async () => (await loadLogoRecords()).filter((record) => !record.data.noindex);

export const getLogoNeighbors = async (handle) => {
  const visible = await getVisibleLogoRecords();
  const index = visible.findIndex((record) => record.handle === handle);
  if (index < 0) {
    return { prev: null, next: null };
  }

  return {
    prev: index > 0 ? visible[index - 1].data : null,
    next: index < visible.length - 1 ? visible[index + 1].data : null
  };
};

const toArray = (value) => {
  if (!value) {
    return [];
  }
  return Array.isArray(value) ? value : [value];
};

const parseLogoAlias = (value) => {
  if (typeof value !== "string") {
    return null;
  }

  const candidate = value.trim().replace(/\/$/, "");
  const match = candidate.match(/^\/logos\/([^/]+)(?:\/index\.html)?$/);
  return match ? match[1] : null;
};

export const getLogoRedirectAliases = async () => {
  const records = await loadLogoRecords();
  const canonicalHandles = new Set(records.map((record) => record.handle));
  const seenAliases = new Set();
  const aliases = [];

  for (const record of records) {
    for (const redirectValue of toArray(record.data.redirect_from)) {
      const aliasHandle = parseLogoAlias(redirectValue);
      if (!aliasHandle || aliasHandle === record.handle || canonicalHandles.has(aliasHandle) || seenAliases.has(aliasHandle)) {
        continue;
      }

      seenAliases.add(aliasHandle);
      aliases.push({
        aliasHandle,
        canonicalHandle: record.handle
      });
    }
  }

  return aliases;
};

export const getImageTypes = () => {
  if (!imageTypesCache) {
    imageTypesCache = readYaml("imagetype.yaml") || [];
  }
  return imageTypesCache;
};

export const getSocialMedia = () => {
  if (!socialMediaCache) {
    socialMediaCache = readYaml("socialmedia.yaml") || [];
  }
  return socialMediaCache;
};

export const getTags = () => {
  if (!tagsCache) {
    tagsCache = readYaml("tags.yaml") || {};
  }
  return tagsCache;
};

export const getSvgporn = () => {
  if (!svgpornCache) {
    svgpornCache = readJson("svgporn.json") || {};
  }
  return svgpornCache;
};

export const getSimpleIcons = () => {
  if (!simpleIconsCache) {
    simpleIconsCache = readJson("simple-icons.json") || {};
  }
  return simpleIconsCache;
};

export const getFavicons = () => {
  if (!faviconsCache) {
    faviconsCache = readJson("favicons.json") || {};
  }
  return faviconsCache;
};

export const getSupertinyIcons = () => {
  if (!supertinyIconsCache) {
    supertinyIconsCache = readJson("supertinyicons.json") || {};
  }
  return supertinyIconsCache;
};

export const getRasterSizes = () => {
  if (!rasterSizesCache) {
    rasterSizesCache = readYaml("rastersize.yaml") || [];
  }
  return rasterSizesCache;
};
