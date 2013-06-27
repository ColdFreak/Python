#!/usr/bin/python

import re

fh = open("foo","r")
print "".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]",fh.read()))
