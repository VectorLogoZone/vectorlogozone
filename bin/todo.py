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

default_input = "./vlz-todo.tgz"
default_output = "/home/amarcuse/site/vectorlogozone/www/logos"

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")
parser.add_argument("--input", help="input file (default=%s)" % default_input, action="store", default=default_input)
parser.add_argument("--output", help="output directory (default=%s)" % default_output, action="store", default=default_output)
parser.add_argument("--nocleanup", help="do not erase temporary files", default=True, dest='cleanup', action="store_false")

args = parser.parse_args()

if args.verbose:
    sys.stdout.write("INFO: update starting at %s" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

tar = tarfile.open(args.input, "r:gz")
for member in tar.getmembers():
    filename = member.name[4:]
    if len(filename) < 5 or filename[0] == '.' or filename[0] == '_' or filename[-4:] != ".txt":
        sys.stdout.write("INFO: skipping %s\n" % filename)
        continue

    sys.stdout.write("INFO: processing %s\n" % filename)
    f = tar.extractfile(member)
    if f is None:
        sys.stdout.write("WARNING: no data in %s\n" % filename)
        continue

    content = str(f.read(), "utf-8")
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
