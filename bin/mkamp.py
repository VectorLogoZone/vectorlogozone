#!/usr/bin/python3
#
# utility to update frontmatter with list of available images
#

import commonmark
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

    fmdst = frontmatter.loads("---\nlayout: amp\nnoindex: true\n---")
    fmdst["redirect_to"] = "https://www.vectorlogo.zone/logos/%s/index.html" % logohandle

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
