#!/usr/bin/python
#
#


import frontmatter
import os
import yaml

tagfn = '../www/_data/tags.yaml'


stream = open(tagfn, 'r')
tags = yaml.load(stream)
stream.close()

for tag in tags.keys():
	tags[tag]["count"] = 0

print(yaml.dump(tags, default_flow_style=False))

logoroot = '../www/logos'
dirs = [f for f in os.listdir(logoroot) if os.path.isdir(os.path.join(logoroot, f))]
dirs.sort()
for logodir in dirs:
	print("INFO: procssing %s" % logodir)

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

stream = open(tagfn, 'w')
stream.write(yaml.dump(tags, default_flow_style=False))
stream.close()
