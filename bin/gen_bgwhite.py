#!/usr/bin/env python3
#
# copy from archive into proper directories
#

import argparse
import os
import xml.etree.ElementTree as ET
import xml.dom.minidom

default_path = os.path.join(os.path.dirname(__file__), "..", "www", "logos")

parser = argparse.ArgumentParser()
parser.add_argument("-q", "--quiet", help="hide status messages", default=True, dest='verbose', action="store_false")
parser.add_argument("-d", "--directory", help="directory to search", default=default_path, dest='directory')
parser.add_argument("--debug", help="debugging output", default=False, dest='debug', action="store_true")

args = parser.parse_args()

def process(options, dirparam):
    logodir = os.path.abspath(dirparam)
    logohandle = os.path.basename(logodir)
      
    ar21 = os.path.join(logodir, logohandle + "-ar21.svg")
    bgwhite = os.path.join(logodir, logohandle + "-ar21~bgwhite.svg")

    if os.path.exists(ar21) == False:
        if args.debug:
            print("WARNING: no ar21 for %s" % logohandle)
        return
    
    ET.register_namespace('', "http://www.w3.org/2000/svg")
    tree = ET.parse(ar21)
    root = tree.getroot()

    new_element = ET.Element("rect")
    new_element.set("width", "120")
    new_element.set("height", "60")
    new_element.set("rx", "5")
    new_element.set("fill", "white")

    root.insert(0, new_element)
 
    # Convert the ElementTree to a string
    xml_str = ET.tostring(root, encoding='utf-8', method='xml')

    # Parse the string with minidom and pretty-print it
    dom = xml.dom.minidom.parseString(xml_str)
    pretty_xml_str = dom.toprettyxml(indent="  ")

    # Write the pretty-printed XML to the file
    f = open(bgwhite, 'w', encoding='utf-8')
    f.write(pretty_xml_str)
    f.close()

    print("INFO: created %s (%s)" % (logohandle, bgwhite))

logoroot = args.directory
dirs = [f for f in os.listdir(logoroot) if os.path.isdir(os.path.join(logoroot, f))]
dirs.sort()
for logodir in dirs:
	#print("INFO: procssing %s" % logodir)
	process('', os.path.join(logoroot, logodir))
