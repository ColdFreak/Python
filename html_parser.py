#!/usr/bin/python3

import sys
from html.parser import HTMLParser
from urllib.request import urlopen

class LinksParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.recording = 0
		self.data = []

	def handle_starttag(self, tag, attributes):
		if tag != 'span':
			return
		if self.recording:
			self.recording += 1
			return
		for name, value in attributes:
			if name == 'class' and value == 'phonetic':
				break
			else:
				return
		self.recording = 1

	def handle_endtag(self, tag):
		if tag == 'span' and self.recording:
			self.recording -= 1

	def handle_data(self, data):
		if self.recording:
			self.data.append(data)

word_url = "http://dict.cn/"+sys.argv[1]
parser = LinksParser()
f = urlopen(word_url)
html = f.read()
html = html.decode('UTF-8')
parser.feed(html)
#for i in parser.data:
#	print i
print (sys.argv[1], parser.data[1])

parser.close()

