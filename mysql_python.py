#!/usr/bin/python

import _mysql
import sys

try:
	con = _mysql.connect('localhost', 'root', 'abc', 'test')
				
	con.query("SELECT VERSION()")
	result = con.use_result()
	print "MySQL VERSION: %s" % result.fetch_row()[0]
					    
except _mysql.Error, e:
					  
	print "Error %d: %s" % (e.args[0], e.args[1])
	sys.exit(1)

finally:
	
	if con:
		con.close()
