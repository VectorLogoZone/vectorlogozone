#!/usr/bin/python
#
# utility to update frontmatter with list of available images
#


import frontmatter
import os


def process(logohandle, logodir):

    srcfile = os.path.join(logodir, "index.md")

    if not os.path.isfile(srcfile):
        print("WARNING: no index file for '%s' (%s)" % (logohandle, srcfile))
        return

    print("INFO: processing %s" % (logohandle))

    fmsrc = frontmatter.load(srcfile)
    if "images" not in fmsrc.metadata:
        print("WARNING: no images, skipping")
        return

    fmdst = frontmatter.loads("---\nlayout: amp\n---")
    fmdst["title"] = fmsrc["title"] + " Logos"
    if logohandle + "-icon.svg" in fmsrc["images"]:
        fmdst["icon"] = logohandle + "-icon.svg"
    if logohandle + "-ar21.svg" in fmsrc["images"]:
        fmdst["ar21"] = logohandle + "-ar21.svg"
    fmdst["canonical"] = "/logos/" + logohandle + "/index.html"

    dstfile = os.path.join(logodir, "index.amp.html")

    f = open(dstfile, 'w')
    f.write(frontmatter.dumps(fmdst))
    f.write('\n')
    f.close()

logoroot = '../www/logos'
dirs = [f for f in os.listdir(logoroot) if os.path.isdir(os.path.join(logoroot, f))]
dirs.sort()
for logohandle in dirs:
    process(logohandle, os.path.abspath(os.path.join(logoroot, logohandle)))
