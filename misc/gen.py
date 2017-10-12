#!/usr/bin/python
import string
import random   
M = 16**4

firstid = 1
lastid = 100

print "COPY net_net (id, cidr, ip_first, ip_last, organization, description, note) FROM stdin;"

for i in xrange(firstid, lastid):
    ip, cidr, ip_first, ip_last, organization, description, note = (None, None, None, None, None, None, None)

    if random.randint(0,100) > 33:
        ip =  '.'.join('%s'%random.randint(0, 255) for i in range(3))
        cidr = "%s.0/24" % (ip, )
        ip_first = "%s.1" % (ip,)
        ip_last = "%s.255" % (ip,)
    else:
        ip =  "2001:cafe:" + ":".join(("%x" % random.randint(0, M) for i in range(2)))
        cidr = "%s::/64" % (ip, )
        ip_first = "%s::1" % (ip,)
        ip_last = "%s::ffff" % (ip,)

    organization = random.choice(['Plzen', 'Praha', 'Ostrava', 'Brno', 'Olomouc', 'Jihlava'])
    description = ''.join(random.choice(string.lowercase) for x in range(8))
    note = ''.join(random.choice(string.lowercase) for x in range(16))

    print "%s\t%s\t%s\t%s\t%s\t%s\t%s" % (i, cidr, ip_first, ip_last, organization, description, note)

print "\."

print "SELECT pg_catalog.setval('net_net_id_seq', %s, true);" % (lastid-1)
