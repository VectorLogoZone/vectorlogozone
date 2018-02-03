#!/usr/bin/python
#
# utility to update frontmatter with list of available images
#

import CommonMark
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
    fmdst["title"] = fmsrc["title"] + " Logos"
    fmdst["amphandle"] = fmsrc["logohandle"]
    fmdst["images"] = fmsrc["images"]
    fmdst.content = CommonMark.commonmark(fmsrc.content)
    fmdst["amp"] = True

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
