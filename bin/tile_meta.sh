#!/bin/bash
#
# utility to resize the icons to 64x64
#

#set -o errexit
set -o pipefail
set -o nounset

ROOT=../www/logos

find ${ROOT} -name '*-tile.svg' -print0 |
    while IFS= read -r -d $'\0' SVG; do

        echo "INFO: processing ${SVG}"
        #xmlstarlet sel -t -m '/_:svg[not(@aria-label)]' -c . -n "${SVG}"
        #xmlstarlet sel -t -m '/_:svg[not(@aria-label)]' -c . -n "${SVG}"

        xmlstarlet ed --inplace \
            --update '/_:svg[@height]/@height' -v 512 \
            --update '/_:svg[@width]/@width' -v 512 \
            --insert '/_:svg[not(@height)]' -t attr -n height -v 512 \
            --insert '/_:svg[not(@width)]' -t attr -n width -v 512 \
            --insert '/_:svg[not(@viewBox)]' -t attr -n viewBox -v "0 0 512 512" \
            "${SVG}"
    done
