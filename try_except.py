#!/usr/bin/python

try:
	fh=open("testfile","w")
	try:
		fh.write("This is my testfile for exception handling!!")
	finally:
		fh.close()
except IOError:
	print "Error can\'t find file or read data"
