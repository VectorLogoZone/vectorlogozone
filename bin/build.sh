#!/usr/bin/env bash
#
# build the site!
#

set -o errexit
set -o pipefail
set -o nounset

#echo "INFO: installing rsvg and imagemagick"
#sudo apt-get install -y librsvg2-bin

echo "INFO: build starting at $(date -u +%Y-%m-%dT%H:%M:%SZ)"

echo "DEBUG: uname=$(uname -a)"

export PYTHON_UNBUFFERED=1


echo "INFO: generating ar21's with a white background"
python3 bin/gen_bgwhite.py

echo "INFO: install frontmatter"
python3 -m pip install python-frontmatter

echo "INFO: updating frontmatter"
python3 bin/frontmatter_update.py --directory=src/content/logos

echo "INFO: generated full metadata export"
python3 bin/gen_fulldata.py

echo "INFO: updating tags"
python3 bin/fm2tag.py --directory=src/content/logos --tagfile=src/data/tags.yaml

echo "INFO: generating next/previous links"
python3 bin/gen_next_prev.py

# disabled for Cloudflare build process
#echo "INFO: generating social media banner images"
#bin/mkcard.sh

echo "INFO: installing javascript dependencies"
npm install

echo "INFO: running astro build"
npm run build

echo "INFO: merging index files"
tar cvzf _site/util/sourceData.tgz _site/util/sourceData*.json
