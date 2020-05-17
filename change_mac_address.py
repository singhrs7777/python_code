#!/usr/bin/env python3
import subprocess
import optparse
import re

def change_mac(interface, mac_address):
    print("[+] Changing mac address for", interface, "to", mac_address)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", mac_address])
    subprocess.call(["ifconfig", interface, "up"])

def parse_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface name")
    parser.add_option("-m", "--mac", dest="mac_add", help="New Mac address of the interface")
    (options, argument) = parser.parse_args()
    if not options.interface:
        parser.error("Please enter interface name, use --help")
    elif not options.mac_add:
        parser.error("Please enter mac address, use --help")
    return options

options = parse_arguments()
change_mac(options.interface, options.mac_add)
ifconfig_result = subprocess.check_output(["ifconfig", options.interface])
extracted_mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result.decode())
if(extracted_mac_address.group(0)==options.mac_add):
    print("[+] Mac address of ", options.interface," got successfully changed")
else:
    printf("Mac address didn't changed")
