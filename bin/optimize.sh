#!/bin/bash
#
# utility to resize the icons to 64x64
#

set -o errexit
set -o pipefail
set -o nounset

ROOT=../www/logos

find ${ROOT} -name '*-tile.svg' -print0 |
    while IFS= read -r -d $'\0' SVG; do

        echo "INFO: processing ${SVG}"
        svgo --pretty --indent=4 "${SVG}"
    done
