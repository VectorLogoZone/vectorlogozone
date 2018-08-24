#!/usr/bin/env python3
#
# check for extraneous files
#

import argparse
import datetime
import frontmatter
import os
import pathlib
import re
import sys
import tarfile
import time

default_path = "../www/logos"

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", help="hide debug messages", default=True, dest='verbose', action="store_false")

args = parser.parse_args()

if args.verbose:
    sys.stdout.write("INFO: metacheck check starting at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

fileCount = 0
errCount = 0
warnCount = 0

found_files = pathlib.Path(default_path).glob('**/index.md')
for fn in found_files:

    f = open(str(fn))
    fmstr = f.read()
    f.close()

    fileCount += 1

    fm = frontmatter.loads(fmstr)
    #sys.stdout.write("DEBUG: %s\n" % (repr(fm.Post)))
    if 'logohandle' not in fm.keys():
        sys.stdout.write("ERROR: no logohandle for %s (%s)\n" % (fn.parts[-2], fn))
        errCount += 1

    if fm['logohandle'] != fn.parts[-2]:
        sys.stdout.write("ERROR: mismatch dir=%s metadata=%s (%s)\n" % (fn.parts[-2], fm['logohandle'], fn))
        errCount += 1

    if 'website' not in fm.keys():
        sys.stdout.write("ERROR: no website for %s (%s)\n" % (fn.parts[-2], fn))
        errCount += 1

    if 'title' not in fm.keys():
        sys.stdout.write("ERROR: no title for %s (%s)\n" % (fn.parts[-2], fn))
        errCount += 1

    if len(fm['title']) == 0 or ' - ' in fm['title'] or ' | ' in fm['title']:
        sys.stdout.write("ERROR: bad title for %s (%s): '%s'\n" % (fn.parts[-2], fn, fm['title']))
        errCount += 1

    if 'sort' not in fm.keys():
        sys.stdout.write("ERROR: no sort for %s (%s)\n" % (fn.parts[-2], fn))
        errCount += 1

    if 'youtube' in fm.keys() and "embed" in fm["youtube"]:
        sys.stdout.write("WARNING: embedded youtube for %s (%s): '%s'\n" % (fn.parts[-2], fn, fm['youtube']))
        warnCount += 1


    # LATER: check handle matches website

sys.stdout.write("INFO: %d errors, %d warnings\n" % (errCount, warnCount))

if args.verbose:
    sys.stdout.write("INFO: metacheck of %d files complete at %s\n" % (fileCount, datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))

# LATER: exit with errlevel
if errCount > 0:
    sys.exit(1)