#!/usr/bin/env python3
#
# check for extraneous files
#

import argparse
import datetime
# NOTE: this is python-frontmatter, not frontmatter
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

handlePattern = re.compile("^[a-z0-9][-_a-z0-9]*[a-z0-9]$")
colorPattern = re.compile("^#[0-9A-F]{6}$")

found_files = pathlib.Path(default_path).glob('**/index.md')
for fn in sorted(found_files):

    f = open(str(fn))
    fmstr = f.read()
    f.close()

    fileCount += 1

    fm = frontmatter.loads(fmstr)
    #sys.stdout.write("DEBUG: %s\n" % (repr(fm.Post)))
    if 'logohandle' not in fm.keys() or len(fm['logohandle']) == 0:
        sys.stdout.write("ERROR: no logohandle for %s (%s)\n" % (fn.parts[-2], fn))
        errCount += 1

    if fm['logohandle'] != fn.parts[-2]:
        sys.stdout.write("ERROR: mismatch dir=%s metadata=%s (%s)\n" % (fn.parts[-2], fm['logohandle'], fn))
        errCount += 1

    if not handlePattern.match(fm['logohandle']):
        sys.stdout.write("ERROR: invalid logohandle '%s' (%s)\n" % (fm['logohandle'], fn))
        errCount += 1

    if 'website' not in fm.keys() or len(fm['website']) == 0:
        sys.stdout.write("ERROR: no website for %s (%s)\n" % (fn.parts[-2], fn))
        errCount += 1

    if 'title' not in fm.keys() or len(fm['title']) == 0:
        sys.stdout.write("ERROR: no title for %s (%s)\n" % (fn.parts[-2], fn))
        errCount += 1
    elif ' - ' in fm['title'] or ' | ' in fm['title'] or ': ' in fm['title']:
        sys.stdout.write("WARNING: bad title for %s (%s): '%s'\n" % (fn.parts[-2], fn, fm['title']))
        warnCount += 1

    if 'sort' not in fm.keys() or len(fm['sort']) == 0:
        sys.stdout.write("ERROR: no sort for %s (%s)\n" % (fn.parts[-2], fn))
        errCount += 1

    if fm['sort'] != fm['sort'].lower():
        sys.stdout.write("WARNING: bad sort for %s (%s): '%s'\n" % (fn.parts[-2], fn, fm['sort']))
        warnCount += 1

    if 'youtube' in fm.keys() and 'embed' in fm['youtube']:
        sys.stdout.write("WARNING: embedded youtube for %s (%s): '%s'\n" % (fn.parts[-2], fn, fm['youtube']))
        warnCount += 1

    for key in fm.keys():
        if isinstance(fm[key], str) and fm[key] != fm[key].strip():
            sys.stdout.write("WARNING: whitespace for %s on key '%s'\n" % (fn, key))
            warnCount += 1

    if 'colors' in fm.keys():
        if isinstance(fm['colors'], str):
            sys.stdout.write("WARNING: colors is not an array for key %s\n" % (fn))
            warnCount += 1
        else:
            for color in fm['colors']:
                if not colorPattern.match(color):
                    sys.stdout.write("WARNING: invalid color %s for key %s\n" % (color, fn))
                    warnCount += 1

    if 'notes' in fm.keys():
        sys.stdout.write("WARNING: key %s still has notes\n" % (fn))
        warnCount += 1

    # LATER: check handle matches website

sys.stdout.write("INFO: %d errors, %d warnings\n" % (errCount, warnCount))

if args.verbose:
    sys.stdout.write("INFO: metacheck of %d files complete at %s\n" % (fileCount, datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))

if errCount > 0:
    sys.exit(1)
