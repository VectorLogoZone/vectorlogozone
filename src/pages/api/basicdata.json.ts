import type { APIRoute } from "astro";
import { getAllLogoRecords } from "../../lib/logos";

type BasicDataItem = {
    ar21: boolean;
    icon: boolean;
    logohandle: string;
    name: string;
    tile: boolean;
    website: string;
};

function hasImage(row: any, suffix: string): boolean {
    if (!row.images || row.images.length == 0) {
        return false;
    }

    for (const img of row.images) {
        if (img === `${row.logohandle}-${suffix}.svg`) {
            return true;
        }
    }
    return false;
}

export const GET: APIRoute = async () => {
    const records = await getAllLogoRecords();

    const data: BasicDataItem[] = [];

    for (const record of records) {

        const row = record.data;

        if (row.noindex) {
            continue;
        }
        const item = {
            ar21: hasImage(row, "ar21"),
            icon: hasImage(row, "icon"),
            logohandle: row.logohandle,
            name: row.title,
            tile: hasImage(row, "tile"),
            website: row.website,
        };
        data.push(item);
    }

    return new Response(JSON.stringify(data), {
        headers: {
            "content-type": "application/json; charset=utf-8",
            "cache-control": "public, max-age=300",
        },
    });
};
