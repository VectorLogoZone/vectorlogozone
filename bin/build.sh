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
echo "DEBUG: xmlstarlet=$(which xmlstarlet)"
echo "DEBUG: xmlstarlet version=$(xmlstarlet --version)"

echo "INFO: generating ar21's with a white background"
bin/gen_bgwhite.sh

echo "INFO: install frontmatter"
python3 -m pip install python-frontmatter

echo "INFO: updating frontmatter"
python3 bin/frontmatter_update.py --directory=www/logos

echo "INFO: updating tags"
python3 bin/fm2tag.py --directory=www/logos --tagfile=www/_data/tags.yaml

echo "INFO: generating next/previous links"
python3 bin/gen_next_prev.py

# disabled for Cloudflare build process
#echo "INFO: generating social media banner images"
#bin/mkcard.sh

echo "INFO: running jekyll"
bundle exec jekyll build --source www --verbose --profile

echo "INFO: merging index files"
tar cvzf _site/util/sourceData.tgz _site/util/sourceData*.json
