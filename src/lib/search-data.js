import { getVisibleLogoRecords } from "./logos";
import { siteConfig } from "./site";

const COMMON_FIELDS = {
  logo: "https://www.vectorlogo.zone/logos/vectorlogozone/vectorlogozone-icon.svg",
  provider: "remote",
  provider_icon: "https://logosear.ch/images/remote.svg",
  url: "https://github.com/VectorLogoZone/vectorlogozone",
  website: "https://www.vectorlogo.zone/"
};

const buildImageEntry = ({ logohandle, title, suffix, width, height }) => {
  const file = `${logohandle}${suffix}.svg`;
  const entry = {
    img: `${siteConfig.productionUrl}/logos/${logohandle}/${file}`,
    name: title,
    src: `${siteConfig.productionUrl}/logos/${logohandle}/index.html`
  };

  if (typeof width === "number") {
    entry.width = width;
  }

  if (typeof height === "number") {
    entry.height = height;
  }

  return { file, entry };
};

export const buildSearchImageData = async ({ targetSuffix, targetName, width, height }) => {
  const records = await getVisibleLogoRecords();
  const images = [];

  for (const record of records) {
    const data = record.data;
    const logohandle = data.logohandle;

    if (!logohandle || !Array.isArray(data.images)) {
      continue;
    }

    const { file, entry } = buildImageEntry({
      logohandle,
      title: data.title || logohandle,
      suffix: targetSuffix,
      width,
      height
    });

    if (!data.images.includes(file)) {
      continue;
    }

    images.push(entry);
  }

  return {
    handle: `vlz${targetSuffix}`,
    images,
    lastmodified: new Date().toISOString(),
    logo: COMMON_FIELDS.logo,
    name: `VectorLogoZone ${targetName}`,
    provider: COMMON_FIELDS.provider,
    provider_icon: COMMON_FIELDS.provider_icon,
    url: COMMON_FIELDS.url,
    website: COMMON_FIELDS.website
  };
};

export const buildSearchOtherData = async ({ targetSuffix, targetName }) => {
  const records = await getVisibleLogoRecords();
  const images = [];

  for (const record of records) {
    const data = record.data;
    const logohandle = data.logohandle;

    if (!logohandle || !Array.isArray(data.images)) {
      continue;
    }

    for (const imageName of data.images) {
      if (imageName.includes("-ar21") || imageName.includes("-icon")) {
        continue;
      }

      images.push({
        img: `${siteConfig.productionUrl}/logos/${logohandle}/${imageName}`,
        name: data.title || logohandle,
        src: `${siteConfig.productionUrl}/logos/${logohandle}/index.html`
      });
    }
  }

  return {
    handle: `vlz${targetSuffix}`,
    images,
    lastmodified: new Date().toISOString(),
    logo: "https://www.vectorlogo.zone/logos/vectorlogozone/vectorlogozone-icon.svg",
    name: `VectorLogoZone ${targetName}`,
    provider: "remote",
    provider_icon: "https://logosear.ch/images/remote.svg",
    url: "https://github.com/VectorLogoZone/vectorlogozone",
    website: "https://www.vectorlogo.zone/"
  };
};
