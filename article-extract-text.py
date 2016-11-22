#!/usr/bin/python3
#Takes article body and title

# Initialize things needed
import argparse
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# Initial variable setup
parser = argparse.ArgumentParser(description="HTML file to use")
parser.add_argument('-f', dest = 'file')
args = parser.parse_args()
div_content = soup.find_all(id='content')
html_doc = open(format(args.file), "rb")

# Check if character encoding is funky
try:
	soup = BeautifulSoup(html_doc, "html.parser")
except UnicodeDecodeError:
	soup = BeautifulSoup(html_doc, "html.parser", from_encoding="gb2312")

def check_style():
	"Checks which title style is the article"
	has_ftitle = soup.find_all(class_='f-title')
	has_hei22 = soup.find_all(class_='hei22')
	if has_ftitle:
		return has_ftitle
	elif has_hei22:
		return has_hei22
	
title_style = check_style()

for article_title_content in title_style:
	print(article_title_content.get_text())

print()

for article_content in div_content:
	for article_content_text in article_content.find_all('p'):
		print(article_content_text.get_text())

# vim: smartindent breakindent tw=80
