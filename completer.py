#!/usr/bin/python

import readline
addrs = ['madfrogme@gmail.com', 'michael@domain.com', 'david@test.com']

def completer(text, state):
	options = [x for x in addrs if x.startswith(text)]
	if state < len(options):
		return options[state]
	else:
		return None

readline.set_completer(completer)
readline.parse_and_bind("tab: complete")
while True:
	inp = raw_input("> ")
	print "You entered", inp
