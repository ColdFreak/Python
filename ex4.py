#!/usr/bin/python3

import re
re_string = "{{(.*?)}}"
some_string = "this is a string with {{words}} embedded in\
{{curly brackets}} to show an {{example}} of {{regular expressions}}, {{}}"
for match in re.findall(re_string, some_string):
	print ("MATCH->", match)


# compiled regular expression object 
re_obj = re.compile("{{(.*?)}}")
some_string = "this is a string with {{words}} embedded in\
{{curly brackets}} to show an {{example}} of {{regular expressions}}, {{}}"
for match in re_obj.findall(some_string):
	print ("MATCH->", match)

