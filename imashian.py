#!/usr/bin/env python

from bs4 import BeautifulSoup
import urllib2

news_url = "http://www.imashian.com/news"

f = urllib2.urlopen(news_url)
html = f.read()

soup = BeautifulSoup(html)

ul_part = soup.find('ul', id = 'feed')
div_part = ul_part.find_all('div', class_ = "title")
for v in div_part:
	print v.find('a').get('href')
