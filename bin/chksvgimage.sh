#!/usr/bin/env bash
#
# lint the svg images
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

SCRIPT_HOME="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_HOME="$(basename $SCRIPT_HOME)"
DEFAULT_LOGODIR="$(realpath $SCRIPT_HOME/../www/logos)"

LOGODIR="${1:-${DEFAULT_LOGODIR}}"
if [ ! -d "${LOGODIR}" ]; then
    echo "ERROR: logo directory not found: ${LOGODIR}"
    exit 1
fi

echo "INFO: starting at $(date -u +%Y-%m-%dT%H:%M:%SZ)"

fflint svg \
    --namespace=false \
    --progress=false \
    --text=false \
    "${LOGODIR}/**/*.svg"


echo "INFO: complete at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
