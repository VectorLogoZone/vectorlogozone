#!/usr/bin/python
#
# utility to update frontmatter with list of available images
#


import frontmatter
import os


def process(options, dirparam):
	logodir = os.path.abspath(dirparam)
	logohandle = os.path.basename(logodir)

	print("INFO: processing %s (%s)" % (logohandle, logodir))
	files = [f for f in os.listdir(logodir) if os.path.isfile(os.path.join(logodir, f))]

	images = []

	for f in files:
		if f.startswith(logohandle + '-') == False:
			continue
		if f.endswith(".svg") == False and f.endswith(".png") == False:
			continue

		images.append(f)

	if len(images) == 0:
		print("WARNING: no images for %s" % logohandle)
		return


	indexfn = os.path.join(logodir, "index.md")
	if os.path.exists(indexfn) == False:
		print("WARNING: no index.md for %s" % logohandle)
		indexmd = frontmatter.loads("")
	else:
		indexmd = frontmatter.load(indexfn)

	indexmd['images'] = images

	f = open(indexfn, 'w')
	frontmatter.dump(indexmd, f)
	f.close()
	#print("%s" % frontmatter.dumps(indexmd))

logoroot = '../www/logos'
dirs = [f for f in os.listdir(logoroot) if os.path.isdir(os.path.join(logoroot, f))]
dirs.sort()
for logodir in dirs:
	print("INFO: procssing %s" % logodir)
	process('', os.path.join(logoroot, logodir))
