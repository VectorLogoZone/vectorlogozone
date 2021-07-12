#!/usr/bin/env python3
#
# generate datafile for next/prev links
#

import argparse
import datetime
import frontmatter
import os
import pathlib
import sys
import time
import yaml

script_path = pathlib.Path(os.path.split(sys.argv[0])[0])
default_path = (script_path / '..' / 'www' / 'logos').resolve()

default_output = (script_path / '..' / 'www' / '_data' / 'nextprev.yaml').resolve()

parser = argparse.ArgumentParser()
parser.add_argument("--directory", help="directory with logo subdirectories (default=%s)" % default_path, action="store", default=default_path)
parser.add_argument("--output", help="output file (default=%s)" % default_output, action="store", default=default_output)
parser.add_argument("-q", "--quiet", help="hide debug messages", default=True, dest='verbose', action="store_false")

args = parser.parse_args()

if args.verbose:
    sys.stdout.write("INFO: next/prev calc starting at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

found_files = sorted(pathlib.Path(args.directory).glob('**/index.md'))
if args.verbose:
    sys.stdout.write("DEBUG: found %d files in %s\n" % (len(found_files), default_path))
fms = []
for fn in found_files:

    #sys.stdout.write("DEBUG: checking %s\n" % (fn))

    fm = frontmatter.load(fn)

    if 'noindex' in fm and fm['noindex']:
        if args.verbose:
            sys.stdout.write("DEBUG: skipping %s (noindex)\n" % fn)
        continue

    fms.append(fm)

data = {}
for index in range(0, len(fms)):

    item = {}

    if index > 0:
        item['prev'] = {
            'logohandle': fms[index-1]['logohandle'],
            'title': fms[index-1]['title']
        }

    if index < len(fms) - 1:
        item['next'] = {
            'logohandle': fms[index+1]['logohandle'],
            'title': fms[index+1]['title']
        }

    data[fms[index]['logohandle']] = item

if args.verbose:
    sys.stdout.write("DEBUG: saving %d entries to %s\n" % (len(data), args.output))
f = open(args.output, 'w')
f.write("# auto-generated on %s\n" % (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))
yaml.dump(data, f)
f.close()

    #sys.stdout.write("DEBUG: candidate %s\n" % fn);

#sys.stdout.write("DEBUG: %d choices\n" % (len(candidates)))

if args.verbose:
    sys.stdout.write("INFO: next/prev calc complete at %s\n" % (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))

