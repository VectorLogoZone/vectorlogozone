#!/usr/bin/env python3.6
#
# script to update favicon metadata
#

import frontmatter
import json
import os
import requests
import requests_html
import sys
import urllib.parse

USER_AGENT="VectorLogoZone FavIcon Fetcher/1.0"
TIMEOUT=15

def favicon(website):
    session = requests_html.HTMLSession()

    try:
        r = session.get(website, headers={'user-agent': USER_AGENT}, timeout=TIMEOUT)
    except requests.exceptions.RequestException:
        r = None

    try:
        if r:
            favicon = r.html.find('link[rel="shortcut icon"]', first=True)
            if favicon is not None and "href" in favicon.attrs:
                return urllib.parse.urljoin(website, favicon.attrs['href'])

            favicon = r.html.find('link[rel="icon"]', first=True)
            if favicon is not None:
                return urllib.parse.urljoin(website, favicon.attrs['href'])
    except:
        # LATER: logging
        r = None

    favicon = urllib.parse.urljoin(website, "favicon.ico")

    try:
        r = requests.get(favicon, headers={'user-agent': USER_AGENT}, timeout=TIMEOUT)
    except requests.exceptions.RequestException:
        return "-"

    if r.status_code == 200 and 'content-type' in r.headers and r.headers['content-type'].startswith("image/"):
        return favicon

    parts = urllib.parse.urlparse(website)
    if parts.path != '/':
        favicon = urllib.parse.urlunparse((parts.scheme, parts.netloc, "/favicon.ico", "", "", ""))
        try:
            r = requests.get(favicon, headers={'user-agent': USER_AGENT}, timeout=TIMEOUT)
        except requests.exceptions.RequestException:
            return "-"

        if r.status_code == 200 and r.headers['content-type'].startswith("image/"):
            return favicon

    return "-"



def process(data, logohandle, logodir):

    srcfile = os.path.join(logodir, "index.md")

    if not os.path.isfile(srcfile):
        print("WARNING: no index file for '%s' (%s)" % (logohandle, srcfile))
        return

    print("INFO: %s" % (logohandle))

    fmsrc = frontmatter.load(srcfile)
    if "website" not in fmsrc.metadata:
        print("WARNING: no website, skipping")
        return

    data[logohandle] = favicon(fmsrc["website"])


logoroot = "../www/logos"
datafile = "../www/_data/favicons.json"

f = open(datafile, "r")
data = json.load(f)
f.close()

dirs = [f for f in os.listdir(logoroot) if os.path.isdir(os.path.join(logoroot, f))]
dirs.sort()
count = 0
for logohandle in dirs:
    count = count + 1
    if logohandle in data and data[logohandle] != '-':
        continue
    process(data, logohandle, os.path.abspath(os.path.join(logoroot, logohandle)))

    #if count % 20 == 0:
    f = open(datafile, "w")
    json.dump(data, f, sort_keys=True, indent=2)
    f.close()

f = open(datafile, "w")
json.dump(data, f, sort_keys=True, indent=2)
f.close()
