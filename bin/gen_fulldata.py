#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["argparse", "python-frontmatter"]
# ///
#
# copy from archive into proper directories
#

import argparse
import datetime
import json
import frontmatter
import os
import pathlib
import re
import sys
import time

default_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "www"))

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")
parser.add_argument("-d", "--directory", help="directory to search", default=default_path, dest='directory')
parser.add_argument("-f", "--filenames", help="only print failing filenames", default=False, dest='filenames', action="store_true")
parser.add_argument("-v", "--verbose", help="verbose output", default=False, dest='debug', action="store_true")

args = parser.parse_args()

if args.verbose:
    sys.stdout.write("INFO: full data generation starting at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

found_files = list(pathlib.Path(os.path.join(args.directory, "logos")).glob('**/index.md'))
found_files.sort()   # only so debug output is consistent

idxCount = 0
errCount = 0

fulldata = []

for indexfn in found_files:
    idxCount += 1
    if args.debug:
        sys.stdout.write("DEBUG: checking %s\n" % (indexfn))

    indexmd = frontmatter.load(indexfn)

    if 'logohandle' not in indexmd:
        sys.stdout.write("ERROR: %s: missing logohandle\n" % indexfn)
        errCount += 1
        continue

    if 'noindex' in indexmd:
        if args.verbose:
            sys.stdout.write("INFO: %s: noindex found, skipping\n" % indexfn)
        continue

    fulldata.append(indexmd.metadata)

retVal = {
    "success": True,
    "lastmod": datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'),
    "count": len(fulldata),
    "sites": fulldata
}

fulldatafn = os.path.join(args.directory, "util", "fulldata.json")
f = open(fulldatafn, 'w')
f.write(json.dumps(retVal, indent=2))
f.close()

if args.verbose:
    sys.stdout.write("INFO: files checked: %5d\n" % idxCount)
    sys.stdout.write("INFO: errors       : %5d\n" % errCount)
    sys.stdout.write("INFO: full data generation complete at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

sys.exit(errCount)
