#!/usr/bin/python3
#Takes article body and title

# Initialize things needed
import argparse
import re
from bs4 import BeautifulSoup
from bs4 import SoupStrainer

# Initial variable setup
parser = argparse.ArgumentParser(description="HTML file to use")
parser.add_argument('-f', dest = 'file')
args = parser.parse_args()
html_doc = open(format(args.file), "rb")

# Check if character encoding is funky
try:
	soup = BeautifulSoup(html_doc, "html.parser")
except UnicodeDecodeError:
	soup = BeautifulSoup(html_doc, "html.parser", from_encoding="gb2312")

def get_div_content():
	"Checks which content id it is"
	div_content_a = soup.find_all(id='content')
	div_content_b = soup.find_all(id='Content')
	if div_content_a:
		div_content = div_content_a
	elif div_content_b:
		div_content = div_content_b
	return div_content

def get_article_title():
	"Checks which title style is the article"
	has_ftitle = soup.find_all(class_='f-title')
	has_hei22 = soup.find_all(class_='hei22')
	has_bltitle = soup.find_all(id='bltitle')
	has_capital_Title = soup.find_all(id='Title')
	has_whtitle = soup.find_all(id='whtitle')
	if has_ftitle:
		return has_ftitle
	elif has_hei22:
		return has_hei22
	elif has_bltitle:
		return has_bltitle
	elif has_capital_Title:
		return has_capital_Title
	elif has_whtitle:
		return has_whtitle
	else:
		return None

def get_article_date():
	"Get article's date and time"
	date_pattern = re.compile("\d+\-\d+-\d+")
	has_sj = soup.find_all(class_='sj')
	has_pubtime = soup.find_all(id='pubtime')
	has_lanx12 = soup.find_all(class_='lanx12')
	if has_sj:
		has_date = has_sj
	elif has_pubtime:
		has_date = has_pubtime
	elif has_lanx12:
		has_date = has_lanx12
	date_obj = has_date[0].get_text()
	date_re = date_pattern.search(date_obj)
	stripped_date = date_re.group()
	return stripped_date
	

print(get_article_date())
print()
print(get_article_title()[0].get_text())
print()

try:
	print(get_div_content()[1].get_text())
except IndexError:
	print(get_div_content()[0].get_text())

# vim: smartindent breakindent tw=80
