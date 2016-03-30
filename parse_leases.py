import os, sys, re

if len(sys.argv) == 2:
    fp = str(sys.argv[1])
elif len(sys.argv) > 2:
    print 'This tool takes no more than one argument (not counting the .py script) which is the filename.' \
          'Usage: python parse_leases.py /User/someuser/filepath.txt'
else:
    fp = raw_input("Please enter the file path: ")
    fp = str(fp)

p = re.compile("lease ([0-9.]+) {.*?hardware ethernet ([:a-f0-9]+);.*?}", re.MULTILINE | re.DOTALL)

ip_list = []

with open(fp) as f:
    for match in p.finditer(f.read()):
        ip_list.append(match)
        print("IP: {0}  MAC: {1}".format(match.group(1), match.group(2)))

print "Total IP addresses in dhcpd.leases = {0}".format(len(ip_list))
