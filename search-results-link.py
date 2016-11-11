#!/usr/bin/python3
#takes TOC archive index and gets links for wget to download

import argparse
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

parser = argparse.ArgumentParser(description="HTML file to use")
parser.add_argument('-f', dest = 'file')
parser.add_argument('-t', dest = 'publication')
args = parser.parse_args()
html_doc = open(format(args.file))

soup = BeautifulSoup(html_doc, "html.parser")

if args.publication == 'xinhua':
	x = soup.find_all(class_='style1a')
	for span in x:
		for link in span.find_all('a'):
			print(link['href'])

# vim: smartindent breakindent tw=80
