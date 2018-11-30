#!/usr/bin/env python3
#
# copy from archive into proper directories
#

import argparse
import boto3
import datetime
import os
import sys
import time

default_input = "metadata.vectorlogo.zone"
default_output = "/home/amarcuse/site/vectorlogozone/www/logos"

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")
parser.add_argument("--input", help="input S3 bucket (default=%s)" % default_input, action="store", default=default_input)
parser.add_argument("--output", help="output directory (default=%s)" % default_output, action="store", default=default_output)
parser.add_argument("--nopurge", help="do not erase S3 files", default=True, dest='purge', action="store_false")

args = parser.parse_args()

if args.verbose:
    sys.stdout.write("INFO: update starting at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

bucket = boto3.Session(profile_name='vlz-metadata').resource('s3').Bucket(args.input)

for key in bucket.objects.all():
    filename = key.key
    if len(filename) < 5 or filename[0] == '.' or filename[0] == '_' or filename[-5:] != ".yaml":
        sys.stdout.write("INFO: skipping %s (filename not eligible)\n" % filename)
        continue

    sys.stdout.write("INFO: processing %s\n" % filename)

    content = key.get()['Body'].read().decode('utf-8')
    if args.verbose:
        sys.stdout.write("INFO: read %d chars\n" % len(content))

    dirname = os.path.join(args.output, filename[:-5])

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
        f.write("---\n")
        f.write(content)
        f.write("---\n")
        f.close()

        if args.purge:
            key.delete()
            sys.stdout.write("INFO: deleted S3 key '%s'\n" % key.key)

if args.verbose:
    sys.stdout.write("INFO: update complete at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
