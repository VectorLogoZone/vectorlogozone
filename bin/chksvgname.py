#!/usr/bin/env python3
#
# copy from archive into proper directories
#

import argparse
import datetime
import os
import pathlib
import re
import sys
import time

default_path = os.path.join(os.path.dirname(__file__), "..", "www", "logos")

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")
parser.add_argument("-d", "--directory", help="directory to search", default=default_path, dest='directory')
parser.add_argument("--debug", help="debugging output", default=False, dest='debug', action="store_true")

allowed_image_codes = {'ar21', 'horizontal', 'icon', 'image', 'official', 'tile', 'vertical', 'wordmark', '_src' }

args = parser.parse_args()

if args.verbose:
    sys.stdout.write("INFO: svg filename check starting at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

found_svgs = list(pathlib.Path(default_path).glob('**/*.svg'))
found_svgs.sort()   # only so debug output is consistent

imgCount = 0
srcCount = 0   
errCount = 0

for svgfn in found_svgs:
    #sys.stdout.write("DEBUG: checking %s\n" % (svgfn))
    imgCount += 1
    if args.debug:
        sys.stdout.write("DEBUG: checking %s\n" % (svgfn))

    if "_src" in svgfn.parts[-1]:
        srcCount += 1
        continue

    dirhandle = svgfn.parts[-2]

    filere = re.search(r'(.*)-([a-z0-9]+)(~[a-z0-9_]+)?\.svg', svgfn.parts[-1])
    if filere is None:
        errCount += 1
        sys.stdout.write("ERROR: unable to parse '%s' (%s)\n" % (svgfn.parts[-1], svgfn))
        continue

    filehandle = filere.group(1)
    if dirhandle != filehandle:
        errCount += 1
        sys.stdout.write("ERROR: handle mismatch %s vs %s (%s)\n" % (dirhandle, filehandle, svgfn))

    imagecode = filere.group(2)
    if imagecode not in allowed_image_codes:
        errCount += 1
        sys.stdout.write("ERROR: unknown image code '%s' (%s)\n" % (imagecode, svgfn))

if args.verbose:
    sys.stdout.write("INFO: files checked: %5d\n" % imgCount)
    sys.stdout.write("INFO: files skipped: %5d\n" % srcCount)
    sys.stdout.write("INFO: errors       : %5d\n" % errCount)
    sys.stdout.write("INFO: svg filename check complete at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

sys.exit(errCount)