#!/usr/bin/env python3
#
# check for extraneous files
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

args = parser.parse_args()

if args.verbose:
    sys.stdout.write("INFO: extra file check starting at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

found_files = pathlib.Path(default_path).glob('**/*')
for fn in found_files:
    #sys.stdout.write("DEBUG: checking %s\n" % (fn))

    #if "_src" in fn.parts[-1]:
    #    continue

    if not fn.is_file():
        continue

    if fn.suffix == ".svg":
        # svgs have their own name checker
        continue

    if fn.parts[-1] in { 'index.md', 'index.amp.html' }:
        continue

    if fn.parts[-1].endswith("-card.png"):
        continue

    sys.stdout.write("ERROR: unknown file '%s'\n" % (fn))

if args.verbose:
    sys.stdout.write("INFO: extra file check complete at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
