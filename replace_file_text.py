#!/usr/bin/python

import sys, os

nargs = len(sys.argv)
if not 3<= nargs <=5:
	print "usage: %s search_tex replace_text [, infile [, outfile]]" % sys.path.basename(sys.argv[0])
else:
	stext = sys.argv[1]
	rtext = sys.argv[2]
	infile = sys.stdin
	outfile = sys.stdout
	if nargs > 3:
		infile = open(sys.argv[3])
	if nargs > 4:
		outfile = open(sys.argv[4], 'w')
	for s in infile:
		outfile.write(s.replace(stext, rtext))
	outfile.close()
	infile.close()
	
		
