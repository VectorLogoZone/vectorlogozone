#!/bin/bash
#
# completely clean an .svg file
# - requires python-scour
# - see http://codedread.com/scour/ for details
#

for filename in "$@"
do
	scour \
		--enable-comment-stripping \
		--enable-id-stripping \
		--remove-metadata \
		-i "$filename" \
		-o "$filename.tmp"

	rm "$filename"
	mv "$filename.tmp" "$filename"
done
