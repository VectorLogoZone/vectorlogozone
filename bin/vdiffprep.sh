#!/bin/bash
#
# prepare raster images for visual diff-ing
#

set -o errexit
set -o pipefail
set -o nounset

if ! [ -x "$(command -v rsvg-convert)" ]; then
  echo "ERROR: rsvg-convert is not installed.  Try 'brew install librsvg' or 'apt-get install librsvg2-bin'"
  exit 1
fi


SCRIPT_HOME="$( cd "$( dirname "$0" )" && pwd )"
WWW_HOME=$(realpath "${SCRIPT_HOME}/../www")

OUTPUT_DIR="${SCRIPT_HOME}/../tmp/$(date -u +%Y-%m-%dT%H-%M)"
mkdir -p "${OUTPUT_DIR}"
OUTPUT_DIR=$(realpath "${OUTPUT_DIR}")

echo "INFO: output directory is ${OUTPUT_DIR}"
exit 1

find "${WWW_HOME}" -name '*-ar21.svg' -print0 |
    sort -z |
    while IFS= read -r -d $'\0' SVG; do

        CARD=${SVG%.svg}.png
        #echo "DEBUG: processing ${SVG} to ${CARD}"
        URLPATH=${SVG#"${WWW_HOME}"}

        if [ -e "${CARD}" ] ; then
            echo "DEBUG: existing card found (${CARD})"
        else
            echo "INFO: creating new card ${CARD}"
            #NO: (crops images): convert -density 1200 -resize 480x240 ${SVG} ${CARD}
            rsvg-convert \
                --background-color=white \
                --dpi-x=1200 \
                --dpi-y=1200 \
                --width=1200 \
                --height=600 \
                --format=png \
                "${SVG}" \
                >"${CARD}"
            mogrify -comment "This image is from [VectorLogoZone](https://www.vectorlogo.zone${URLPATH}).  Enjoy!" "${CARD}"
        fi
    done
