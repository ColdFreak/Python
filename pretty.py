#!/usr/bin/env python3


s = ""
lastc = ''

indent = 0


f = open("file.c")
f2 = open("new.c", "w")


lines = f.readlines()

for line in lines:

	if line.strip().startswith('#') :
		s += line
		s += '\n'
		continue	
	if line in ['\n', '\r\n'] :
	 	s += line
	 	continue

	li = line.split()

	for element in li:
		
		for ch in element : 

			if ch == '{':
				
				indent += 1
				s += ch
				s += '\n'
				s += '\t'* indent
				
			elif ch == ';':
				s += ch
				s += '\n'
				s += '\t'* indent

			elif ch == '}':
				indent -= 1
				s += '\n'
				s += '\t' * indent
				s += ch
				lastc = ch

			elif lastc == '}':
				s += '\n'
				s += '\t' * indent
				s += ch
				lastc = ''

			elif element.index(ch) == len(element)-1 :
				s += ch
				s += ' '
				break



			else:

				s += ch
				


f2.write(s)
			
		



