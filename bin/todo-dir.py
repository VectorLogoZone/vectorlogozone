#!/usr/bin/env python3
#
# copy from archive into proper directories
#

import argparse
import datetime
import os
import sys
import tarfile
import time

default_input = "../tmp"
default_output = "/home/amarcuse/site/vectorlogozone/www/logos"

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")
parser.add_argument("--input", help="input directory (default=%s)" % default_input, action="store", default=default_input)
parser.add_argument("--output", help="output directory (default=%s)" % default_output, action="store", default=default_output)
#parser.add_argument("--nocleanup", help="do not erase temporary files", default=True, dest='cleanup', action="store_false")

args = parser.parse_args()

if args.verbose:
    sys.stdout.write("INFO: update starting at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

files = [f for f in os.listdir(args.input)]
for filename in files:
    if len(filename) < 5 or filename[0] == '.' or filename[0] == '_' or filename[-4:] != ".txt":
        sys.stdout.write("INFO: skipping %s\n" % filename)
        continue

    fullpath = os.path.join(args.input, filename)
    sys.stdout.write("INFO: processing %s\n" % fullpath)

    f = open(fullpath, "r")
    if f is None:
        sys.stdout.write("WARNING: no data in %s\n" % filename)
        continue

    content = f.read()
    f.close()
    if args.verbose:
        sys.stdout.write("INFO: read %d chars\n" % len(content))

    dirname = os.path.join(args.output, filename[:-4])

    if os.path.exists(dirname):
        if args.verbose:
            sys.stdout.write("INFO: using existing directory '%s'\n" % dirname)
    else:
        if args.verbose:
            sys.stdout.write("INFO: creating directory '%s'\n" % dirname)
        os.makedirs(dirname)

    indexname = os.path.join(dirname, "index.md")
    if os.path.exists(indexname):
        sys.stdout.write("WARNING: existing file not overwritten '%s'\n" % indexname)
    else:
        if args.verbose:
            sys.stdout.write("INFO: creating file '%s'\n" % indexname)
        f = open(indexname, "w")
        f.write(content)
        f.close()

if args.verbose:
    sys.stdout.write("INFO: update complete at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
