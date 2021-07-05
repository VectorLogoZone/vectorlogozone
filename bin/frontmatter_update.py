#!/usr/bin/python
#
# utility to update frontmatter with list of available images
#

import argparse
import frontmatter
import os

default_path = "../www/logos"

parser = argparse.ArgumentParser()
parser.add_argument("--directory", help="directory with logo subdirectories", action="store", default=default_path)
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")

args = parser.parse_args()

def process(options, dirparam):
	logodir = os.path.abspath(dirparam)
	logohandle = os.path.basename(logodir)

	#print("INFO: processing %s (%s)" % (logohandle, logodir))
	files = [f for f in os.listdir(logodir) if os.path.isfile(os.path.join(logodir, f))]

	images = []
	skipped = 0

	for f in files:
		if f.endswith(".svg") == False and f.endswith(".png") == False:
			if f.endswith(".ai") or f.endswith(".pdf") or f.endswith(".eps"):
				print("INFO: skipping " + f)
				skipped = skipped + 1
			continue
		if f.endswith("_src.svg") or f.endswith(".png"):
			print("INFO: skipping " + f)
			skipped = skipped + 1
			continue
		if f.startswith(logohandle + '-') == False:
			print("INFO: skipping " + f)
			skipped = skipped + 1
			continue

		images.append(f)

	if len(images) == 0:
		print("WARNING: no images for %s" % logohandle)
		return


	indexfn = os.path.join(logodir, "index.md")
	if os.path.exists(indexfn) == False:
		print("WARNING: no index.md for %s" % logohandle)
		return
		#indexmd = frontmatter.loads("---\n---\n")
	else:
		indexmd = frontmatter.load(indexfn)

	indexmd['images'] = images
	#indexmd['skipped'] = skipped

	if "logohandle" not in indexmd.keys():
		indexmd["logohandle"] = logohandle

	if "title" not in indexmd.keys():
		indexmd["title"] = logohandle.capitalize()

	if "sort" not in indexmd.keys():
		indexmd["sort"] = indexmd["title"].lower()

	f = open(indexfn, 'w')
	f.write(frontmatter.dumps(indexmd))
	f.write('\n')
	f.close()
	#print("%s" % frontmatter.dumps(indexmd))

logoroot = args.directory
dirs = [f for f in os.listdir(logoroot) if os.path.isdir(os.path.join(logoroot, f))]
dirs.sort()
for logodir in dirs:
	#print("INFO: procssing %s" % logodir)
	process('', os.path.join(logoroot, logodir))
