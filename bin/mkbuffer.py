#!/usr/bin/env python3.6
#
# download 10 cards to queue up in Buffer
#

import argparse
import datetime
import frontmatter
import os
import pathlib
import random
import requests
import sys
import time

default_path = "../www/logos"

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", help="hide debug messages", default=True, dest='verbose', action="store_false")

args = parser.parse_args()

if args.verbose:
    sys.stdout.write("INFO: fill buffer queue starting at %s\n" % datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S'))

found_files = pathlib.Path(default_path).glob('**/*-ar21.svg')
candidates = []
for ar21 in sorted(found_files):

    card = str(ar21)[:-9] + "-card.png"

    #sys.stdout.write("DEBUG: checking %s vs %s\n" % (ar21, card))

    if pathlib.Path(card).exists():
        continue

    candidates.append(card)

    #sys.stdout.write("DEBUG: candidate!");

sys.stdout.write("DEBUG: %d choices\n" % (len(candidates)))

choices = sorted(random.choices(candidates, k=10))

for choice in choices:

    id = choice.split('/')[-2]
    sys.stdout.write("INFO: https://www.vectorlogo.zone/logos/%s/index.html\n" % (id))

    r = requests.get("https://www.vectorlogo.zone/logos/%s/%s-card.png" % (id, id))

    f = open(choice, 'wb')
    f.write(r.content)
    f.close()


if args.verbose:
    sys.stdout.write("INFO: fill buffer queue complete at %s\n" % (datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')))

