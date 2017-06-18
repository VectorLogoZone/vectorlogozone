# Vector Logo Zone

This is the source for the [Vector Logo Zone](https://www.vectorlogo.zone/) website.

## Running

It is a static website built with Jekyll and can run anywhere.  The default deploy script uses s3cmd to copy to Amazon S3.

In order to run the python auto-update utilities, you need to `pip install python-frontmatter`.

The `mkcard.sh` script needs rsvg and imagemagick: `sudo apt-get install librsvg2-bin imagemagick`.

## To Do
 - [ ] viewer: custom background color (and save to cookie)
 - [ ] viewer: double-click to zoom/shift double-click to unzoom
 - [ ] viewer: drag to move around
 - [ ] credits: rsvg
 - [ ] credits: ImageMagick
 - [ ] 404 page should have link to search
 - [ ] redo favicon to just be "V"

 * travis should run bin/ scripts and do the deploy
 * /search.html: comment code
 * /search.html: btn-info
 * /search.html: skip if no ar21 (or use icon?)
 * new favicon
 * use wordmark.svg in navbar
 * ruby to ruby-lang
 * navbar: icons when small, text when medium/large
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
 * humans.txt
 * generate pngs if missing
 * pngcrush
 * report of missing frontmatter: twitter, facebook, github, website
 * /util/fulltext - {{content}}
 * /util/research.html
	- get favicon/apple icons/etc from homepage
	- get twitter logo
	- get facebook logo
	- get all images from homepage

## Logos that need work
 - [ ] golang (outline of gopher is too thin, doesn't scale)
 - [ ] perl (remove bitmap camel)
 - [ ] bootswatch (icon blends with white, no graphic on ar21)
 - [ ] consistent sizing/placement on horizontal logos

## Logos
 - [ ] iText
 - [ ] jenkins
 - [ ] travis
 - [ ] vagrant
 - [ ] xcode
 
 * addthis
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
 * ImageMagick
 * Microsoft - Segoe
 * MySQL
 * nodeping
 * pinboard
 * RSS
 * rsvg
 * [svg](https://www.w3.org/2009/08/svg-logos.html)
 * s3cmd (new?)
 * styleshout
 * tango icons
 * twitter
 * US Census Burean (census.gov)
 * wordpress
