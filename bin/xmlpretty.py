#!/usr/bin/env python3
#
# pretty print xml
#
# source: https://pymotw.com/2/xml/etree/ElementTree/create.html
#

import argparse
from xml.etree import ElementTree
from xml.dom import minidom
import os
import sys

parser = argparse.ArgumentParser(description="Pretty-print XML")
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")
parser.add_argument("filenames", help="XML files", action="store", nargs="+")

def prettyprint_file(options, filename):
    f = open(filename, "r")
    tree = ElementTree.parse(f)
    f.close()


    formatted = prettyprint(options, tree.tostring())
    sys.stdout.write(formatted)

def prettyprint(options, str):

    reparsed = minidom.parseString(str)
    return reparsed.toprettyxml(indent="\t")



args = parser.parse_args()

for filename in args.filenames:
    prettyprint(args, filename)