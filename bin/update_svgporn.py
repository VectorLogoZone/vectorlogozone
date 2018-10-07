#!/usr/bin/env python3
#
# update the mapping to svgporn
#

import argparse
import datetime
import frontmatter
import json
import os
import pathlib
import requests
import sys
import time
import urllib.parse

USER_AGENT="VectorLogoZone Icon Fetcher/1.0"
TIMEOUT=15
SVGPORN_JSON_URL="https://raw.githubusercontent.com/gilbarbara/logos/master/logos.json"
LOGODIR = "../www/logos"
DATAFILE = "../www/_data/svgporn.json"

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")
parser.add_argument("--datafile", help="path to .json file (default=%s)" % DATAFILE, action="store", default=DATAFILE)
parser.add_argument("--logodir", help="logo directory (default=%s)" % LOGODIR, action="store", default=LOGODIR)
parser.add_argument("--showpending", help="show pending icons that exist in SVGPORN", default=False, dest='pending', action="store_true")
parser.add_argument("--showmissing", help="show missing icons that exist in SVGPORN", default=False, dest='missing', action="store_true")
parser.add_argument("--svgporn", help="url of svgporn inventory (default=%s)" % SVGPORN_JSON_URL, action="store", default=SVGPORN_JSON_URL)



def load_svgporn(args):

    r = requests.get(args.svgporn, headers={'user-agent': USER_AGENT}, timeout=TIMEOUT)

    rawdata = r.json()

    retVal = dict()

    for data in rawdata:
        website = data["url"]
        if website.startswith("http:"):
            website = website[:4] + 's' + website[4:]
        if website.startswith("https://www."):
            website = "https://" + website[12:]
        retVal[ website ] = data["files"]

    if args.verbose:
        sys.stdout.write("INFO: %d svgporn entries loaded\n" % len(retVal))

    return retVal



def load_logos(args):

    retVal = dict()

    found_files = pathlib.Path(args.logodir).glob('**/index.md')
    for fn in found_files:
        f = open(str(fn))
        fmstr = f.read()
        f.close()

        fm = frontmatter.loads(fmstr)

        website = fm["website"]
        if website.startswith("http:"):
            website = website[:4] + "s" + website[4:]
        if website.startswith("https://www."):
            website = "https://" + website[12:]

        data = { "logohandle": fm["logohandle"], "website": website }

        retVal[fm["logohandle"]] = data

    if args.verbose:
        sys.stdout.write("INFO: %d logos loaded\n" % len(retVal))

    return retVal



args = parser.parse_args()

if args.verbose:
    sys.stdout.write("INFO: update starting at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

logos = load_logos(args)
#sys.stdout.write("INFO: websites=%s" % json.dumps(websites, sort_keys=True, indent=2))

svgporn = load_svgporn(args)
#sys.stdout.write("INFO: svgporn=%s" % json.dumps(svgporn, sort_keys=True, indent=2))

output = dict()
for key in logos.keys():
    website = logos[key]["website"]

    if website in svgporn:
        output[ logos[key]["logohandle"] ] = svgporn[ website ]
        del svgporn[ website ]


if args.missing:
    sys.stdout.write("INFO: svgporn that VLZ doesn't have (%d):\n" % len(svgporn))
    missing = sorted(svgporn.keys())
    for website in missing:
        sys.stdout.write("%s\n" % website)

    sys.stdout.write("\n")

if args.pending:
    sys.stdout.write("INFO: svgporn that are pending on VLZ:\n")
    for key in output.keys():
        iconpath = pathlib.Path(args.logodir, key, key + "-icon.svg")
        if not iconpath.is_file():
            sys.stdout.write("curl https://cdn.svgporn.com/logos/%s %s\n" % (output[key][0], iconpath))

#f = open(datafile, "r")
#data = json.load(f)
#f.close()

f = open(args.datafile, "w")
json.dump(output, f, sort_keys=True, indent=2)
f.close()
sys.stdout.write("INFO: %d rows written to %s\n" % (len(output), args.datafile))

if args.verbose:
    sys.stdout.write("INFO: update complete at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
