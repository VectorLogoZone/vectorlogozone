#!/usr/bin/env bash
#
# generate ar21's with a white background
#

set -o errexit
set -o pipefail
set -o nounset

if [ ! command -v xmlstarlet &> /dev/null ]; then
    echo "ERROR: xmlstarlet is not installed"
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

FILES=$(find "${LOGODIR}" -type f -name '*-ar21.svg' | sort)

for FILE in $FILES; do
    FILE_NOEXT="${FILE%.*}"
    SHORTNAME=$(basename "${FILE_NOEXT}")
    OUTPUT="${FILE_NOEXT}~bgwhite.svg"
    if [ -f "${OUTPUT}" ]; then
        echo "INFO: ${SHORTNAME} already created, skipping"
        continue
    fi
    echo "INFO: converting ${SHORTNAME}"
    xmlstarlet edit \
        --insert '/_:svg/*[1]' --type elem --name 'rect' --value '' \
        --insert '/_:svg/*[1]' --type attr --name 'width' --value '120' \
        --insert '/_:svg/*[1]' --type attr --name 'height' --value '60' \
        --insert '/_:svg/*[1]' --type attr --name 'rx' --value '5' \
        --insert '/_:svg/*[1]' --type attr --name 'fill' --value 'white' \
    "${FILE}" > "${OUTPUT}"
done