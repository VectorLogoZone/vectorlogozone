#!/usr/bin/env bash
#
# clean temporary files
#

set -o errexit
set -o pipefail
set -o nounset

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_DIR="$( cd "${SCRIPT_DIR}/.." && pwd )"
LOGO_DIR="${REPO_DIR}/src/content/logos"

echo "INFO: cleanup starting at $(date -u +%Y-%m-%dT%H:%M:%SZ)"

echo "INFO: cleaning bgwhite files from ${LOGO_DIR}"
rm -rf "${LOGO_DIR}"/**/*~bgwhite.svg

echo "INFO: cleaning generated files from ${REPO_DIR}/dist"
rm -rf "${REPO_DIR}/dist"/*

echo "INFO: cleanup completed at $(date -u +%Y-%m-%dT%H:%M:%SZ)"
