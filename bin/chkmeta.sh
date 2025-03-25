#!/usr/bin/env bash
#
# lint the metadata in index.md files
#

set -o errexit
set -o pipefail
set -o nounset

if [ ! command -v fflint &> /dev/null ]; then
    echo "ERROR: fflint is not installed"
    echo ""
    echo "Download from:"
    echo "https://github.com/FileFormatInfo/fflint/releases/latest"
    exit 1
fi

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_DIR="$( cd "${SCRIPT_DIR}/.." && pwd )"
DEFAULT_LOGODIR="${REPO_DIR}/www/logos"

LOGODIR="${1:-${DEFAULT_LOGODIR}}"
if [ ! -d "${LOGODIR}" ]; then
    echo "ERROR: logo directory not found: ${LOGODIR}"
    exit 1
fi

SCHEMA=$(realpath "${LOGODIR}/../schemas/metadata.schema.json")
if [ ! -f "${SCHEMA}" ]; then
    echo "ERROR: schema not found: ${SCHEMA}"
    exit 1
fi

echo "INFO: starting at $(date -u +%Y-%m-%dT%H:%M:%SZ)"

SOCIALKEYS=$(cat "${REPO_DIR}/www/_data/socialmedia.yaml" | yq '[.[].id] | join(",")')
OPTIONALKEYS="colors,font,guide,images,keywords,noindex,other,redirect_from,tags"
REQUIREDKEYS="logohandle,sort,title,website"
#    --optional=activitypub,blog,bluesky,codehost,colors,discord,dribbble,facebook,flickr,flipboard,font,googleplus,gitter,guide,images,instagram,keywords,linkedin,noindex,other,pinterest,reddit,redirect_from,slack,slideshare,snapchat,soundcloud,stackexchange,stackoverflow,tags,telegram,threads,tiktok,tumblr,twitter,wikipedia,vimeo,vine,weibo,xing,youtube \

fflint frontmatter \
    --strict=true \
    --required=${REQUIREDKEYS} \
    --optional="${SOCIALKEYS},${OPTIONALKEYS}" \
    --sorted=true \
    --schema="${SCHEMA}" \
    "${LOGODIR}/*/index.md"

echo "INFO: complete at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
