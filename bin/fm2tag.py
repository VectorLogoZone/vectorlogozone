#!/usr/bin/python
#
#

import argparse
import frontmatter
import os
import yaml

default_tagfn = '../www/_data/tags.yaml'
default_path = "../www/logos"

parser = argparse.ArgumentParser()
parser.add_argument("--directory", help="directory with logo subdirectories", action="store", default=default_path)
parser.add_argument("--tagfile", help="file with tag data", action="store", default=default_tagfn)
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")

args = parser.parse_args()

stream = open(args.tagfile, 'r')
tags = yaml.load(stream)
stream.close()

for tag in tags.keys():
	tags[tag]["count"] = 0

print(yaml.dump(tags, default_flow_style=False))

logoroot = args.directory
dirs = [f for f in os.listdir(logoroot) if os.path.isdir(os.path.join(logoroot, f))]
dirs.sort()
for logodir in dirs:
	#print("INFO: procssing %s" % logodir)

	indexfn = os.path.join(logoroot, logodir, "index.md")
	if os.path.exists(indexfn) == False:
		print("WARNING: no index.md for %s" % logodir)
		continue

	indexmd = frontmatter.load(indexfn)

	if "tags" not in indexmd.keys():
		continue

	print("INFO: %d tags found" % (len(indexmd["tags"])))

	for tag in indexmd["tags"]:
		if tag in tags.keys():
			tags[tag]["count"] += 1
		else:
			print("WARNING: new tag %s" % tag)
			tags[tag] = {"count": 1, "title": tag }

stream = open(args.tagfile, 'w')
stream.write(yaml.dump(tags, default_flow_style=False))
stream.close()
