import { readFileSync, readdirSync, statSync } from "node:fs";
import path from "node:path";
import matter from "gray-matter";
import { parse as parseYaml } from "yaml";

const repoRoot = process.cwd();
const logosRoot = path.join(repoRoot, "www", "logos");
const dataRoot = path.join(repoRoot, "www", "_data");

let logoRecordsCache;
let imageTypesCache;
let socialMediaCache;
let tagsCache;
let svgpornCache;
let simpleIconsCache;
let faviconsCache;
let supertinyIconsCache;
let rasterSizesCache;

const readYaml = (filename) => {
  const source = readFileSync(path.join(dataRoot, filename), "utf8");
  return parseYaml(source);
};

const readJson = (filename) => {
  const source = readFileSync(path.join(dataRoot, filename), "utf8");
  return JSON.parse(source);
};

const loadLogoRecords = () => {
  if (logoRecordsCache) {
    return logoRecordsCache;
  }

  const handles = readdirSync(logosRoot)
    .filter((entry) => statSync(path.join(logosRoot, entry)).isDirectory())
    .sort();

  const records = [];

  for (const handle of handles) {
    const indexFile = path.join(logosRoot, handle, "index.md");
    try {
      const parsed = matter(readFileSync(indexFile, "utf8"));
      const data = parsed.data || {};
      records.push({
        handle,
        data: {
          ...data,
          logohandle: data.logohandle || handle,
          title: data.title || handle,
          sort: (data.sort || data.title || handle).toString().toLowerCase(),
          images: Array.isArray(data.images) ? data.images : []
        },
        content: parsed.content || ""
      });
    } catch {
      records.push({
        handle,
        data: {
          logohandle: handle,
          title: handle,
          sort: handle.toLowerCase(),
          images: []
        },
        content: ""
      });
    }
  }

  records.sort((a, b) => a.data.sort.localeCompare(b.data.sort));

  logoRecordsCache = records;
  return records;
};

export const getLogoHandles = () => loadLogoRecords().map((record) => record.handle);

export const getLogoRecord = (handle) => loadLogoRecords().find((record) => record.handle === handle);

export const getAllLogoRecords = () => loadLogoRecords();

export const getVisibleLogoRecords = () => loadLogoRecords().filter((record) => !record.data.noindex);

export const getLogoNeighbors = (handle) => {
  const visible = getVisibleLogoRecords();
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

export const getLogoRedirectAliases = () => {
  const canonicalHandles = new Set(loadLogoRecords().map((record) => record.handle));
  const seenAliases = new Set();
  const aliases = [];

  for (const record of loadLogoRecords()) {
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
