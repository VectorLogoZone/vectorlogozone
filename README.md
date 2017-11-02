# Vector Logo Zone

This is the source for the [Vector Logo Zone](https://www.vectorlogo.zone/) website.

## Running

It is a static website built with Jekyll and can run anywhere.  The default deploy script uses s3cmd to copy to Amazon S3.

In order to run the python auto-update utilities, you need to `pip install python-frontmatter`.

The `mkcard.sh` script needs rsvg and imagemagick: `sudo apt-get install librsvg2-bin imagemagick`.

## To Do
 - [ ] CORS support
 - [ ] display favicon.svg in header bar
 - [ ] manifest.json (for offline support)
 - [ ] don't include card in count of other images (in logos/inventory.html)
 - [ ] 404 page should have link to search (or redirect to search with flash message)
 - [ ] fill in more metadata links (see the [links report](https://www.vectorlogo.zone/logos/metadata.html))
 - [ ] convert logos/index.html tabs based on first letter
 - [ ] /templates/ directory with image (and index.md) templates
 - [ ] credit: ImageMagick (when logo done)
 - [ ] credit: rsvg (when logo done)
 - [ ] png's (embedded in svg) for ar21, icon for hard ones
 - [ ] redirect for 404 in /logos/
 - [ ] separate site w/dynamic svg's based on parameters

## Continuous Integration Checks
 - [ ] no embedded rasters
 - [ ] no embedded fonts
 - [ ] handle vs directory vs filename mismatch
 - [ ] extra files that aren't _src
 - [ ] files over a certain size
 - [ ] run scour on all

## Viewer To Do
 - [ ] custom background color (and save to cookie)
 - [ ] double-click to zoom/shift double-click to unzoom
 - [ ] drag to move around
 - [ ] color analysis

 * /search.html: comment code
 * /search.html: btn-info
 * /search.html: skip if no ar21 (or use icon?)
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
 * /util/inventory - toggle for png
 * svg metadata
 * tags for each /logos/*/index.md
 * humans.txt
 * /util/fulltext - {{content}}
 * /util/research.html
	- get favicon/apple icons/etc from homepage
	- get twitter logo
	- get facebook logo
	- get all images from homepage

## More metadata
 * Instagram
 * Google+
 * Youtube
 * LinkedIn
 * Flickr
 * Slack

## Logos that need work
 - [ ] itext logo has a bit of white (on top of the 'x' and right of the 2nd 't')
 - [ ] golang (outline of gopher is too thin, doesn't scale)
 - [ ] perl (remove bitmap camel)
 - [ ] bootswatch (icon blends with white, no graphic on ar21)
 - [ ] consistent sizing/placement on horizontal logos
 - [ ] CloudFlare redid their logo
 - [ ] Apache: redid the feather
 - [ ] Google Analytics: "Google" should be bolder than "Analytics"
 - [ ] lunr.js redid their website & logo

## Logos
 - see the [missing logos report](https://www.vectorlogo.zone/logos/missing.html)


 * addthis
 * adobe flex
 * async.js
 * common lisp
 * daynightoverlay (new)
 * fugue icons (new?)
 * google guava (new)
 * gnome
 * haproxy
 * hyper.sh
 * icondrawer
 * macosx
 * SEPTA
 * s3cmd (new?)
 * styleshout
 * tango icons
 * US Census Burean (census.gov)
 * varnish

