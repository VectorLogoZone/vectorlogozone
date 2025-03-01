#!/usr/bin/env python3
#
#

import argparse
import frontmatter
import os
import yaml

default_path = "../www/logos"

parser = argparse.ArgumentParser()
parser.add_argument("--directory", help="directory with logo subdirectories", action="store", default=default_path)
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")

args = parser.parse_args()

logoroot = args.directory
dirs = [f for f in os.listdir(logoroot) if os.path.isdir(os.path.join(logoroot, f))]
dirs.sort()
for logodir in dirs:
    #print("INFO: procssing %s" % logodir)

    indexfn = os.path.join(logoroot, logodir, "index.md")
    if os.path.exists(indexfn) == False:
        print("WARNING: no index.md for %s" % logodir)
        continue

    indexmd = frontmatter.load(indexfn)

    if "git" not in indexmd.keys():
        print("DEBUG: skipping %s (%s)" % (indexmd["title"], indexmd["logohandle"]))
        continue
    print("DEBUG: processing %s (%s)" % (indexmd["title"], indexmd["logohandle"]))

    indexmd["codehost"] = "https://github.com/%s" % indexmd["git"]
    del indexmd["git"]

    #print("%s" % frontmatter.dumps(indexmd))

    frontmatter.dump(indexmd, indexfn)
