## Had some help with the regex from some StackOverflow folks ##

# test comment #

import sys, re

fp = '/Users/misaflansb/Dropbox/ERMCO/Network/DHCP-Info/dhcpd.leases'
p = re.compile("lease ([0-9.]+) {.*?hardware ethernet ([:a-f0-9]+);.*?}", re.MULTILINE | re.DOTALL)

ip_list = []

with open(fp) as f:
    for match in p.finditer(f.read()):
        ip_list.append(match)
        print("IP: {0}  MAC: {1}".format(match.group(1), match.group(2)))

print "Total IP addresses in dhcpd.leases = {0}".format(len(ip_list))
