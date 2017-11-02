#!/bin/bash
#
# utility to make images for OpenGraph & Twitter cards
#
# http://superuser.com/questions/516095/bake-an-svg-image-into-a-png-at-a-given-resolution

set -o errexit
set -o pipefail
set -o nounset

ROOT=../www/logos

find ${ROOT} -name '*-ar21.svg' -print0 |
    while IFS= read -r -d $'\0' SVG; do

        CARD=${SVG%ar21.svg}card.png
        #echo "DEBUG: processing ${SVG} to ${CARD}"

        if [ -e "${CARD}" ] ; then
            echo "DEBUG: existing card found (${CARD})"
        else
            echo "INFO: creating new card ${CARD}"
            #NO: (crops images): convert -density 1200 -resize 480x240 ${SVG} ${CARD}
            rsvg --dpi-x=1200 --dpi-y=1200 --width=480 --height=240 --format=png "${SVG}" "${CARD}"
            mogrify -comment "This image is from [VectorLogoZone](https://www.vectorlogo.zone/).  Enjoy!" "${CARD}"
        fi
    done
