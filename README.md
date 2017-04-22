# Vector Logo Zone

This is the source for the [Vector Logo Zone](http://www.vectorlogo.zone/) website.

## Running

It is a static website built with Jekyll and can run anywhere.  The default deploy script uses s3cmd to copy to Amazon S3.

In order to run the python auto-update utilities, you need to `pip install python-frontmatter`.

The `mkcard.sh` script needs rsvg and imagemagick: `sudo apt-get install librsvg2-bin imagemagick`.

## To Do
 - [ ] perl: delete white background in embedded gif
 - [ ] padding on select vertical logos
 - [ ] consistent sizing/placement on horizontal logos
 - [ ] viewer: custom background color (and save to cookie)
 - [ ] credits: rsvg
 - [ ] credits: ImageMagick
 - [ ] /logos/missing.html: report of logos without icon or ar21
 - [ ] VLZ ar21 image: image should have "VLZ", not just "V"
 - [ ] 404 page should have link to search

 * travis should run bin/ scripts and do the deploy
 * /search.html: comment code
 * /search.html: btn-info 
 * new favicon
 * use wordmark.svg in navbar
 * ruby to ruby-lang
 * navbar: icons when small, text when medium, both when large
 * navbar: "VLZ" when tiny
 * advertising
 * fill in FAQs
 * /index.html - only a subset of logos
 * /index.html - last slide is custom svg w/count, mini logos, etc
 * Windows 8.1 Tiles
 * alternatives page: /support/alternative.html
 * link to template
 * /_includes/footer.html - Legal - CC0?  CC-BY-SA?
 * discus: remove or make it work
 * /util/inventory - toggle for png
 * svg metadata
 * categories for each /logos/*/index.md
 * verify bing
 * verify google webmastertools
 * humans.txt
 * generate pngs if missing
 * pngcrush
 * more frontmatter in /logos/*/index.md: twitter, facebook
 * /util/fulltext - {{content}}
 * /util/research.html
	- get favicon/apple icons/etc from webpage
	- get twitter logo
	- get facebook logo
	- get all images from homepage
	
## Logos that need work
 - [ ] golang (
 - [ ] nearlyfreespeech (icon reformat)
 0 [ ] labelmakr (icon reformat)
 - [ ] perl (remove bitmap camel)
 - [ ] bootswatch (icon blends with white, no graphic on ar21)

## Logos

 - [ ] appharbor
 - [ ] godaddy
 - [ ] Heroku
 - [ ] iText
 - [ ] Unicode
 - [ ] 1and1
 - [ ] urlrewritefilter
 
 * adobe flex
 * apache batik (new?)
 * apache POI (new?)
 * apache tomcat
 * ATOM
 * AWK
 * common lisp
 * debian
 * disqus
 * fugue icons (new?)
 * google adsense
 * google AppEngine
 * google guava (new)
 * icondrawer
 * Microsoft - Segoe
 * MySQL
 * nodeping
 * pinboard
 * RSS
 * s3cmd (new?)
 * styleshout
 * tango icons
 * twitter
 * wordpress



