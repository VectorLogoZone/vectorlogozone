# Contributing to [VectorLogoZone](https://www.vectorlogo.zone/)

[![number of contributors](https://img.shields.io/github/contributors/VectorLogoZone/vectorlogozone.svg?colorB=green)](https://github.com/VectorLogoZone/vectorlogozone/graphs/contributors)
[![last commit](https://img.shields.io/github/last-commit/VectorLogoZone/vectorlogozone.svg)](https://github.com/VectorLogoZone/vectorlogozone/commits/gh-pages)
[![open issues](https://img.shields.io/github/issues-raw/VectorLogoZone/vectorlogozone.svg)](https://github.com/VectorLogoZone/vectorlogozone/issues)
[![open PRs](https://img.shields.io/github/issues-pr-raw/VectorLogoZone/vectorlogozone.svg)](https://github.com/VectorLogoZone/vectorlogozone/pulls)

One of the main reasons for [VectorLogoZone](https://www.vectorlogo.zone/) is consistency: the logos should look great when they are all on the same page. Please follow these guidelines when you make the images.

## Image types

Required:

- **Rectangle** (`-ar21`) - a 120x60 rectangle with the logo and the name, with some padding
- **Icon** (`-icon`) - a 64x64 with just the logo (i.e. no name) on a transparent (white) background, with no padding other than to make it square

Optional:

- **Tile** (`-tile`) - a 512x512 image with a simple logo on a colored background. The guidelines (as well as many of the images) come from [SuperTinyIcons](https://github.com/edent/supertinyicons), though I am more strict about a non-white background, and less strict about the 1K size limit.
- **Image** (`-image`) - a 64 high image: the same as the icon, but resized so that it is 64 high with no padding
- **Horizontal** (`-horizontal`) - 60 high, similar to the `-ar21`, but wider so really long names can be next to the logo
- **Wordmark** (`-wordmark`) - 60 high, just the name in the correct font, in black, with padding
- **Official** (`-official`) - The official logo, unchanged except cropped and resized to a maximum of 256 height or width.

Other

- **Card** (`-card`) - this is a 480x240 raster image that is automatically generated from the `-ar21` image during the website deployment. It should not be checked into git.

## General Logo Guidelines

These guidelines apply to all images except the `-official` images.

- No company/legal suffixes (such as Corp, GmbH, Ltd, SA, NV)
- No legal turds (such as ©, ™)
- No taglines
- Transparent background
- Dark foreground, so it looks good on a white/light background (except `-tile`).
- Convert text to curves: you cannot depend people already having a specific font installed.
- No embedded raster data (PNG or JPEG or anything else)
- No external links/references/etc.

## Metadata

### Naming guidelines

Each logo has a unique id (`logohandle` in the metadata) that is used in the directory and file name.

Use the base domain name without the `www.`. If the top-level domain is `.com` or `.org`, drop that as well.

If the home page is a subdirectory or subdomain, put an underscore and then the subdirectory/subdomain. For example, `commons.wikimedia.org` should be `wikimedia_commons`, and `www.w3.org/XML` should be `w3_xml`.

If there is another major website with the exact same name at a different top-level domain (or the likelihood of one), don't drop it. For example, `hyper.sh` should be `hyper_sh`.

### Basic Metadata

- guidelines - link to official logos and/or usage guidelines
- images - list of available images. NOTE: This is automatically filled in during website deployment.
- logohandle - (required) unique id for this project/company. See [Naming Guidelines](#naming-guidelines) above.
- sort - (required) how it should be sorted in a list. Always lowercase.
- title - (required) project/company name (as short as possible)
- website - (required) project/company website

### Sort order

The `sort` is usually the same as the `logohandle`, but can be different if the website isn't the common name. For example: Bootstrap's website is `www.getbootstrap.com`, but it should be sorted as `bootstrap`.

## Social Media Links

Links to this project/company on various websites. I'm generally interested in sites where there should be a publicly accessible logo.

- blog
- facebook
- github - just the bare organization name or org/repo
- googleplus
- instagram
- linkedin
- pinterest
- reddit
- tumblr
- twitter - just the bare id (no @ sign)
- wikipedia
- youtube

### Other Social Media Links

These are some less common social media sites that some projects/companies use. Feel free to add any that are linked from the main website.

- discord
- discourse
- dockerhub
- dribbble
- flickr
- gitter
- glassdoor
- medium
- meetup
- slack
- slideshare
- soundcloud
- stackexchange
- stackoverflow
- vimeo
- vine
- weibo
- xing

### Font

The `font` property supports the following sub-properties:

- name - name of the font (required if font is present)
- url - url of the font
- google - link to font at Google Fonts
- microsoft - link to font at Microsoft
- myfonts - link to font on MyFonts
- freename - name of a free font that looks the same
- freeurl - url of a free font that looks the same

### Additional data

- colors - array of colors used in the logo
- tags - array of tags, not currently maintained.

## Tools

Font identification:

- [WhatTheFont](http://www.myfonts.com/WhatTheFont/) - upload a sample image. They also have an active [forum](http://www.myfonts.com/WhatTheFont/forum/) where fonts experts will help.</p>
- [IdentiFont](http://www.identifont.com/) - answer a series of questions about specific characters. Be sure to use the character filter.</p>
- [WhatFont bookmarklet](http://www.chengyinliu.com/whatfont.html) - really nice and easy way to see the fonts used on an HTML page</p>
