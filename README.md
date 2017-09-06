# Vector Logo Zone

This is the source for the [Vector Logo Zone](https://www.vectorlogo.zone/) website.

## Running

It is a static website built with Jekyll and can run anywhere.  The default deploy script uses s3cmd to copy to Amazon S3.

In order to run the python auto-update utilities, you need to `pip install python-frontmatter`.

The `mkcard.sh` script needs rsvg and imagemagick: `sudo apt-get install librsvg2-bin imagemagick`.

## To Do
 - [ ] manifest.json (for offline support)
 - [ ] don't include card in count of other images (in logos/inventory.html)
 - [ ] viewer: custom background color (and save to cookie)
 - [ ] viewer: double-click to zoom/shift double-click to unzoom
 - [ ] viewer: drag to move around
 - [ ] 404 page should have link to search (or redirect to search with flash message)
 - [ ] fill in more metadata links (see the [links report](https://www.vectorlogo.zone/logos/metadata.html))
 - [ ] convert logos/index.html tabs based on first letter
 - [ ] expose template.md as /request.txt, note about adding new logos
 - [ ] inventory to skip ones with 0 images
 - [ ] png's (embedded in svg) for ar21, icon for hard ones
 - [ ] travis: run subprograms
 - [ ] redirect for 404 in /logos/
 - [ ] separate site w/dynamic svg's based on parameters

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

## Logos that need work
 - [ ] golang (outline of gopher is too thin, doesn't scale)
 - [ ] perl (remove bitmap camel)
 - [ ] bootswatch (icon blends with white, no graphic on ar21)
 - [ ] consistent sizing/placement on horizontal logos
 - [ ] CloudFlare redid their logo
 - [ ] Apache: redid the feather

## Logos
 - see the [missing logos report](https://www.vectorlogo.zone/logos/missing.html)

 * Twitter
 * Reddit
 * YCombinator
 * StumbleUpon
 * Tumbler
 * Facebook
 * Pinterest
 * LinkedIn
 * json.org
 
 * addthis
 * adobe flex
 * async.js
 * ATOM
 * chrome
 * common lisp
 * disqus
 * Federal Reserve
 * firefox
 * fugue icons (new?)
 * Glitch/Gomix
 * google guava (new)
 * gnome
 * hyper.sh
 * icondrawer
 * Let's Encrypt
 * macosx
 * MapQuest
 * marcuse.org (at least icon)
 * Microsoft - Segoe
 * Mozilla
 * npm
 * Postman
 * Pusher
 * react.js
 * RSS
 * rsvg
 * safari
 * [svg](https://www.w3.org/2009/08/svg-logos.html)
 * SEPTA
 * slack
 * s3cmd (new?)
 * stackoverflow
 * styleshout
 * tango icons
 * twitter
 * US Census Burean (census.gov)
 * wordpress

