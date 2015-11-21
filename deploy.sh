#!/bin/bash
#
# deploy to NearlyFreeSpeech.net
#

jekyll build --source www 

# to test, add:
#	--dry-run \

s3cmd \
	sync \
	--delete-removed \
	--exclude '*~' \
	--exclude '*_src*' \
	--exclude '*.sh' \
	--no-preserve \
	--recursive \
	--verbose \
	_site/ \
	s3://www.vectorlogo.zone
