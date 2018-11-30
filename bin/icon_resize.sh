#!/bin/bash
#
# utility to resize the icons to 64x64
#

#set -o errexit
set -o pipefail
set -o nounset

ROOT=../www/logos

find ${ROOT} -name '*-icon.svg' -print0 |
    while IFS= read -r -d $'\0' SVG; do

        echo "INFO: processing ${SVG}"
        #xmlstarlet sel -t -m '/_:svg[not(@aria-label)]' -c . -n "${SVG}"
        #xmlstarlet sel -t -m '/_:svg[not(@aria-label)]' -c . -n "${SVG}"

        xmlstarlet ed --inplace \
            --update '/_:svg[@height]/@height' -v 64 \
            --update '/_:svg[@width]/@width' -v 64 \
            --insert '/_:svg[not(@height)]' -t attr -n height -v 64 \
            --insert '/_:svg[not(@width)]' -t attr -n width -v 64 \
            --insert '/_:svg[not(@viewBox)]' -t attr -n viewBox -v "0 0 32 32" \
            "${SVG}"
    done
