#!/usr/bin/python

import sys, urllib2
from bs4 import BeautifulSoup


url = "http://dict.cn/"+sys.argv[1]

content = urllib2.urlopen(url).read()

soup = BeautifulSoup(content)

phonetic = soup.find('div', class_ = 'phonetic')
basic = soup.find('div', class_ = 'layout basic')

pronunciations = phonetic.find_all('bdo')
meanings = basic.find_all('strong')

pro = pronunciations[0].find(text=True)
print pro
for meaning in meanings:
	text = meaning.find(text=True)
	print text

