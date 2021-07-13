#!/bin/bash
#
# flush the CloudFlare CDN with cURL.
#

set -o errexit
set -o pipefail
set -o nounset

SCRIPT_HOME="$( cd "$( dirname "$0" )" && pwd )"
ENV_FILE="${SCRIPT_HOME}/../.env"

if [ -f "${ENV_FILE}" ];
then
    echo "INFO: loading .env"
    export $(cat "${ENV_FILE}")
fi

echo "INFO: flushing cache"
RESULT=$(
    curl \
        --data '{"purge_everything":true}' \
        --header "Authorization: Bearer ${CLOUDFLARE_API_TOKEN}" \
        --header "Content-Type: application/json" \
        --request POST  \
        --show-error \
        --silent \
        "https://api.cloudflare.com/client/v4/zones/${CLOUDFLARE_ZONE_ID}/purge_cache"
    )
echo "INFO: result is $(echo "${RESULT}" | jq --compact-output .)"

SUCCESS=$(echo "${RESULT}" | jq --raw-output .success)
if [ "${SUCCESS}" != "true" ];
then
    echo "ERROR: flush failed! (${SUCCESS})"
    exit 1
fi

echo "INFO: cache flush complete"