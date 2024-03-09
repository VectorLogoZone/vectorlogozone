#!/usr/bin/env bash
#
# lint the metadata in index.md files
#

set -o errexit
set -o pipefail
set -o nounset

if [ ! command -v fflint &> /dev/null ]; then
    echo "ERROR: fflint is not installed"
    echo "try:"
    echo "    go install github.com/FileFormatInfo/fflint/cmd/fflint@latest"
    exit 1
fi

SCRIPT_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_HOME="$(basename $SCRIPT_HOME)"
DEFAULT_LOGODIR="$(realpath $SCRIPT_HOME/../www/logos)"

LOGODIR="${1:-${DEFAULT_LOGODIR}}"
if [ ! -d "${LOGODIR}" ]; then
    echo "ERROR: logo directory not found: ${LOGODIR}"
    exit 1
fi

echo "INFO: starting at $(date -u +%Y-%m-%dT%H:%M:%SZ)"

fflint frontmatter \
    --strict=true \
    --required=title,website,logohandle,sort \
    --optional=blog,colors,discord,dribbble,facebook,flickr,font,googleplus,git,github,gitlab,gitter,guide,images,instagram,keywords,linkedin,noindex,other,pinterest,reddit,redirect_from,slack,slideshare,snapchat,soundcloud,stackexchange,stackoverflow,tags,tiktok,tumblr,twitter,wikipedia,vimeo,vine,weibo,xing,youtube \
    --sorted=true \
    "${LOGODIR}/*/index.md"

echo "INFO: complete at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
