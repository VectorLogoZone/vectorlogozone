#!/bin/bash
#
# flush the CloudFlare CDN with cURL.  Needs CLOUDFLARE_EMAIL, CLOUDFLARE_API_KEY and CLOUDFLARE_ZONE_ID to be set
#
#LATER: check that env vars exist, etc

curl -X DELETE "https://api.cloudflare.com/client/v4/zones/${CLOUDFLARE_ZONE_ID}/purge_cache" \
    -H "X-Auth-Email: ${CLOUDFLARE_EMAIL}" \
    -H "X-Auth-Key: ${CLOUDFLARE_API_KEY}" \
    -H "Content-Type: application/json" \
    --data '{"purge_everything":true}'
