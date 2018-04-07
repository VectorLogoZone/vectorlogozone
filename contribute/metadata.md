# Metadata


## File and directory names

The `logohandle` is the unique identifier for a logo on VLZ.  I use it as the directory name and the beginning of each svg file name.

Use the base domain name without the `www` or top-level domain.
For example: The Free Software Foundations' website is `www.fsf.org`, so the logo handle should be `fsf`.

If the home page is a subdirectory or subdomain, put an underscore and then the subdirectory/subdomain.
For example, `commons.wikimedia.org` should be `wikimedia_commons`, and `www.w3.org/XML` should be `w3_xml`.

If there is another major website with the exact same name at a different top-level domain (or the likelihood of one), don't drop it.
For example, `hyper.sh` should be `hyper_sh`.

## Sort order

The `sort` is usually the same as the `logohandle`, but can be different if the website isn't the common name.
For example: Bootstrap's website is `www.getbootstrap.com`, but it should be sorted as `bootstrap`.

## Social media links

Any social media websites that would have examples of the logos are optional but welcome.   The `max` template has most of them.

Unless the website has a very strict naming convention (very strict=100%), use the full URL.  Github, Google+ and Twitter are the only
that I know of that can be just the id.

## Templates

[metadata-max.txt](metadata-max.txt) - a sample file with all possible links
[metadata-min.txt](metadata-min.txt) - a sample file with the bare minimum

