#!/bin/bash
#
# run locally
#

set -o errexit
set -o pipefail
set -o nounset


SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_DIR="${SCRIPT_DIR}"

echo "INFO: starting local server at $(date -u +%Y-%m-%dT%H:%M:%SZ)"

echo "INFO: dir=${REPO_DIR}"

if [ ! -d "${REPO_DIR}/node_modules" ]; then
    echo "INFO: installing javascript dependencies"
    cd "${REPO_DIR}"
    npm install
fi

npm run dev
