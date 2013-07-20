#!/bin/bash
#
# deploy to NearlyFreeSpeech.net
#

jekyll build --source www 

rsync \
	--archive \
	--compress \
	--delete \
	--exclude '*_src*' \
	--exclude '*.sh' \
	--ignore-times \
	--itemize-changes \
	--rsh "ssh -i /etc/fileformatnet/nfsnet.pem" \
	--verbose \
	_site/ \
	fileformat_hackerlogos@ssh.phx.nearlyfreespeech.net:/home/public/

#
# old version that deploys to github-pages
#
# this depends on the local branch being gh-pages (i.e. git checkout gh-pages)
#
#git push origin +:
