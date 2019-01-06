#!/bin/bash
#
# completely clean an .svg file
# - requires python-scour
# - see http://codedread.com/scour/ for details
#
# original size: 86 MB

set -o errexit
set -o pipefail
set -o nounset

#
# svgcleaner - https://github.com/RazrFalcon/svgcleaner
# end result: 28MB
# 
for filename in ../www/logos/**/*.svg; do
	echo -n "INFO: processing ${filename}: "
	./svgcleaner --copy-on-error "${filename}" "${filename}_tmp.svg"

	rm "${filename}"
	mv "${filename}_tmp.svg" "${filename}"
done
exit 0

#
# svgo - fails on gruntjs, doesn't compress especially well
#
for filename in ../www/logos/**/[g]*.svg; do
    svgo $filename
done
exit 1

#
# scour version: 69MB, but a bunch of logos come out blank
#
for filename in ../www/logos/**/*.svg; do
	python3 -m scour.scour \
		--enable-comment-stripping \
		--remove-metadata \
		--shorten-ids \
		-i "$filename" \
		-o "$filename.tmp"

	rm "$filename"
	mv "$filename.tmp" "$filename"
done

# options to try

# logo sizes are wrong
#--enable-viewboxing

# not effective (at least on xmlns:i="&amp;ns_ai;")
#--keep-editor-data

#--strip-xml-space

#--disable-embed-rasters
