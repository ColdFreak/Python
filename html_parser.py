#!/usr/bin/python3

import sys
from html.parser import HTMLParser
from urllib.request import urlopen
import subprocess
import re

class LinksParser(HTMLParser):
	def __init__(self):
		HTMLParser.__init__(self)
		self.recording = 0
		self.data = []

	def handle_starttag(self, tag, attributes):
		if tag != 'bdo':
			return
		if self.recording:
			self.recording += 1
			return
#		for name, value in attributes:
#			if name == 'class' and value == 'phonetic':
#				break
#			else:
#				return
		self.recording = 1

	def handle_endtag(self, tag):
		if tag == 'bdo' and self.recording:
			self.recording -= 1

	def handle_data(self, data):
		if self.recording:
			self.data.append(data)

word_url = "http://dict.cn/"+sys.argv[1]
audio_url = "http://tts.yeshj.com/uk/s/"+sys.argv[1]
dev_null = open('/dev/null', 'w')

# download mp3 file to /tmp
mp3file = urlopen(audio_url)
mp3_name = "/tmp/"+sys.argv[1]+".mp3"
output_mp3 = open(mp3_name, 'wb')
output_mp3.write(mp3file.read())
output_mp3.close()

# extract pronounciation 
parser = LinksParser()
f = urlopen(word_url)
html = f.read()
html = html.decode('UTF-8')
parser.feed(html)

# 
word_meanings = re.findall('</span><strong>(.*)</strong></li>',html, re.MULTILINE)


# if you try to search a non-sense word like 'asdfsdfs', nothing will be in the date list
try:
	print (sys.argv[1], parser.data[0])
except IndexError:
	sys.exit(0)

for match in word_meanings:
	print (match)

# play mp3 file and redirect stdout to /dev/null then wait process to complete
process = subprocess.Popen(['play', mp3_name], stdout=dev_null, stderr=dev_null)
retcode = process.wait()

parser.close()

