#!/usr/bin/env python3


s = ""
lastc = ''

indent_keyword = ['{', ')', ';', ':', 'if', 'else', 'do' ]
indent = 0

for_flag = 0

semicolon_count = 0

f = open("boo.c")
f2 = open("new.c", "w")


lines = f.readlines()

for line in lines:
	
	if line.strip().startswith('for'):
		if '{' != line[len(line.strip())-1]:
			indent += 1
		for_flag = 1
	
	elif line.strip().startswith('/*') and line.strip().endswith('*/'):
		s += '\n'
		s += line
		s += '\n'
		s += '\t' * indent
		continue
	elif line.strip().startswith('#') :
		s += '\n'
		s += line
		s += '\n'
		s += '\t' * indent
		continue	
	elif line in ['\n', '\r\n'] :
	 	continue

	if line.strip().endswith('*/') and not line.strip().startswith('/*'):
		s += '\n'
		s += '\t' * indent
		s += line.strip()
		s += '\n'
		s += '\t' * indent
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
				if for_flag == 1 and semicolon_count < 2 :
					semicolon_count += 1
					s += ch
					continue
				else:
					for_flag = 0
					semicolon_count = 0
				s += ch
				s += '\n'
				s += '\t'* indent

			elif ch == '}':
				indent -= 1
				s += '\n'
				s += '\t' * indent
				s += ch
				s += '\n'
				s += '\t' * indent
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

