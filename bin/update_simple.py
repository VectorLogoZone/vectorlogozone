#!/usr/bin/env python3
#
# update the mapping to simple-icons
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
SIMPLE_JSON_URL="https://raw.githubusercontent.com/simple-icons/simple-icons/develop/_data/simple-icons.json"
LOGODIR = "../www/logos"
DATAFILE = "../www/_data/simple.json"

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")
parser.add_argument("--datafile", help="path to .json file (default=%s)" % DATAFILE, action="store", default=DATAFILE)
parser.add_argument("--logodir", help="logo directory (default=%s)" % LOGODIR, action="store", default=LOGODIR)
parser.add_argument("--showpending", help="show pending icons", default=False, dest='pending', action="store_true")
parser.add_argument("--showmissing", help="show missing icons", default=False, dest='missing', action="store_true")
parser.add_argument("--showguide", help="show missing/different guidelines", default=False, dest='guide', action="store_true")
parser.add_argument("--simple", help="url of simple-icons inventory (default=%s)" % SIMPLE_JSON_URL, action="store", default=SIMPLE_JSON_URL)



def load_simple(args):

    r = requests.get(args.simple, headers={'user-agent': USER_AGENT}, timeout=TIMEOUT)

    rawdata = r.json()

    retVal = dict()

    for data in rawdata["icons"]:

        data["id"] = data["title"].lower().replace(".", "-dot-").replace(" ", "").replace("!", "")

        retVal[ data["id"] ] = data

    if args.verbose:
        sys.stdout.write("INFO: %d simple-icon entries loaded\n" % len(retVal))

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

        if "guide" in fm.metadata:
            guide = fm["guide"]
        else:
            guide = ""

        data = { "logohandle": fm["logohandle"], "website": website, "guide": guide }

        retVal[fm["logohandle"]] = data

    if args.verbose:
        sys.stdout.write("INFO: %d logos loaded\n" % len(retVal))

    return retVal



args = parser.parse_args()

if args.verbose:
    sys.stdout.write("INFO: update starting at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

logos = load_logos(args)
#sys.stdout.write("INFO: websites=%s" % json.dumps(websites, sort_keys=True, indent=2))

simple = load_simple(args)
sys.stdout.write("INFO: simple=%s" % json.dumps(simple, sort_keys=True, indent=2))

output = dict()
guides = dict()
for key in logos.keys():

    if key in simple:
        simplekey = key
        output[ key ] = "%s" % simplekey
        guides[ key ] = simple[ simplekey ]["source"]
        del simple[ simplekey ]


if args.missing:
    sys.stdout.write("INFO: simple that VLZ doesn't have (%d):\n" % len(simple))
    missing = sorted(simple.keys())
    for key in missing:
        sys.stdout.write("%s\n" % key)

    sys.stdout.write("\n")

if args.pending:
    sys.stdout.write("INFO: simple that are pending on VLZ:\n")
    for key in output.keys():
        iconpath = pathlib.Path(args.logodir, key, key + "-icon.svg")
        if not iconpath.is_file():
            sys.stdout.write("%s %s\n" % (output[key][0], iconpath))

if args.guide:
    for key in sorted(guides.keys()):
        #sys.stdout.write("INFO: guides %s %s %s %s\n" % (key, guide[key], simple[ output[key] ], ""))
        vlzguide = logos[key]["guide"] if "guide" in logos[key] else ""
        simpleguide = guides[key]

        if len(vlzguide) == 0:
            sys.stdout.write("INFO: new guide %s: %s\n" % (key, simpleguide))
        elif vlzguide != simpleguide:
            sys.stdout.write("INFO: different guide %s: vlz=%s simple=%s\n" % (key, vlzguide, simpleguide))

#f = open(datafile, "r")
#data = json.load(f)
#f.close()

f = open(args.datafile, "w")
json.dump(output, f, sort_keys=True, indent=2)
f.close()
sys.stdout.write("INFO: %d rows written to %s\n" % (len(output), args.datafile))

if args.verbose:
    sys.stdout.write("INFO: update complete at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))
