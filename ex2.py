#!/usr/bin/python3

import re
import os
import subprocess


#The method split() returns a list of all the words in the string, using str as the separator (splits on all whitespace if left unspecified), optionally limiting the number of splits to num.
s='str1, str2, str3, str4'
print (s.split(', '))



find = re.findall("[Ll]en","len is the Length")
print ('\n',find)



if os.path.isdir("/tmp"):
	print ("\n/tmp is a directory\n")
else:
	print ("/tmp is not a directory")



subprocess.call(["ls","-l","/tmp/"])


def uname_func():
	uname = "uname"
	uname_arg = "-a"
	print ("\nGathering system information with %s command:" % uname)
	subprocess.call([uname, uname_arg])
uname_func()
