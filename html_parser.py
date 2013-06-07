#!/usr/bin/python

import HTMLParser
import urllib2

class LinksParser(HTMLParser.HTMLParser):
	def __init__(self):
		HTMLParser.HTMLParser.__init__(self)
		self.recording = 0
		self.data = []

	def handle_starttag(self, tag, attributes):
		if tag != 'span':
			return
		if self.recording:
			self.recording += 1
			return
		for name, value in attributes:
			if name == 'class' and value == 'trs':
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

parser = LinksParser()
f = urllib2.urlopen("http://dict.hjenglish.com/w/deception")
html = f.read()
parser.feed(html)
print parser.data
parser.close()

