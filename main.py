import sys
import csv

import xml.etree.ElementTree as ET

from matplotlib import pyplot

UNKNOWN_VENDOR = 'Unknown'
BSSID = 'BSSID'
STATION_MAC = 'Station MAC'

vendor_xml_filename = sys.argv[1]
airodump_csv_filename = sys.argv[2]

all_prefix_lengths = set()
mac_prefix_vendor_name = {}
for type_tag in ET.parse(vendor_xml_filename).getroot():
    mac_prefix = type_tag.get('mac_prefix')
    all_prefix_lengths.add(len(mac_prefix))
    mac_prefix_vendor_name[mac_prefix] = type_tag.get('vendor_name')


def get_vendor_name(mac):
    for l in all_prefix_lengths:
        if mac[:l] in mac_prefix_vendor_name:
            return mac_prefix_vendor_name[mac[:l]]
    return UNKNOWN_VENDOR


vendor_names_count = {}
unknown_vendor_macs = []
with open(airodump_csv_filename, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        if len(row) > 0 and row[0] != BSSID and row[0] != STATION_MAC:
            vendor_name = get_vendor_name(row[0])

            if vendor_name == UNKNOWN_VENDOR:
                unknown_vendor_macs.append(row[0])

            if vendor_name not in vendor_names_count:
                vendor_names_count[vendor_name] = 0
            vendor_names_count[vendor_name] += 1

print(vendor_names_count)
print(unknown_vendor_macs)
