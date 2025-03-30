#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["argparse", "python-frontmatter", "pyyaml"]
# ///
#
# copy from archive into proper directories
#

import argparse
import datetime
import frontmatter
import os
import pathlib
import re
import sys
import time
import yaml

default_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "www"))

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")
parser.add_argument("-d", "--directory", help="directory to search", default=default_path, dest='directory')
parser.add_argument("-v", "--verbose", help="verbose output", default=False, dest='debug', action="store_true")

args = parser.parse_args()

if args.verbose:
    sys.stdout.write("INFO: meta link check starting at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

sm_file = os.path.join(args.directory, "_data", "socialmedia.yaml")
if not os.path.exists(sm_file):
    sys.stdout.write("ERROR: unable to find %s\n" % sm_file)
    sys.exit(1)

sm_f = open(sm_file, 'r')
sm_yaml = yaml.safe_load(sm_f)
sm_f.close()
if args.debug:
    sys.stdout.write("DEBUG: loaded %d records from %s\n" % (len(sm_yaml), sm_file))

metamap = {}
for sm in sm_yaml:
    if 'pattern' in sm:
        metamap[sm['id']] = re.compile(sm['pattern'])

if args.debug:
    sys.stdout.write("DEBUG: loaded %d patterns from %s\n" % (len(metamap), sm_file))

found_files = list(pathlib.Path(args.directory).glob('**/index.md'))
found_files.sort()   # only so debug output is consistent

idxCount = 0
errCount = 0


for indexfn in found_files:
    idxCount += 1
    if args.debug:
        sys.stdout.write("DEBUG: checking %s\n" % (indexfn))

    indexmd = frontmatter.load(indexfn)

    for key in indexmd.keys():
        if key in metamap:
            pattern = metamap[key]
            if pattern.match(indexmd[key]) == None:
                errCount += 1
                sys.stdout.write("ERROR: %s %s: %s (%s)\n" % (indexmd['logohandle'], key, indexmd[key], indexfn))
            else:
                if args.debug:
                    sys.stdout.write("DEBUG: success %s %s: %s\n" % (indexmd['logohandle'], key, indexmd[key]))

if args.verbose:
    sys.stdout.write("INFO: files checked: %5d\n" % idxCount)
    sys.stdout.write("INFO: errors       : %5d\n" % errCount)
    sys.stdout.write("INFO: meta link check complete at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

sys.exit(errCount)
