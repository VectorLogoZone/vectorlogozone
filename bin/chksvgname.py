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
import tarfile
import time

default_path = "../www/logos"

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")

allowed_image_types = {'ar21', 'horizontal', 'icon', 'image', 'official', 'tile', 'vertical', 'wordmark', '_src' }

args = parser.parse_args()

if args.verbose:
    sys.stdout.write("INFO: svg filename check starting at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

found_svgs = pathlib.Path(default_path).glob('**/*.svg')
for svgfn in found_svgs:
    #sys.stdout.write("DEBUG: checking %s\n" % (svgfn))

    if "_src" in svgfn.parts[-1]:
        continue

    dirhandle = svgfn.parts[-2]

    filere = re.search(r'(.*)-([a-z0-9_~]*)\.svg', svgfn.parts[-1])
    if filere is None:
        sys.stdout.write("ERROR: unable to parse '%s' (%s)\n" % (svgfn.parts[-1], svgfn))
        continue

    filehandle = filere.group(1)
    if dirhandle != filehandle:
        sys.stdout.write("ERROR: handle mismatch %s vs %s (%s)\n" % (dirhandle, filehandle, svgfn))

    imagetype = filere.group(2)
    tilde = imagetype.find('~')
    if tilde != -1:
        imagetype = imagetype[0:tilde]
    if imagetype not in allowed_image_types:
        sys.stdout.write("ERROR: unknown image type '%s' (%s)\n" % (imagetype, svgfn))

if args.verbose:
    sys.stdout.write("INFO: svg filename check complete at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
