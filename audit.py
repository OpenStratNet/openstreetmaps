import xml.etree.cElementTree as ET
from collections import defaultdict
import re
import pprint
from num2words import num2words

# small sample from Duesseldorf
OSMFILE = "sample.osm" #

def audit(osmfile):
    osm_file = open(osmfile, "r")
    phone_numbers = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):
        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                print tag
                # if "phone" in tag:
                #     print"yes"
    osm_file.close()
    return phone_numbers

def test():
    st_types = audit(OSMFILE)
    pprint.pprint(dict(st_types))


if __name__ == '__main__':
    test()
