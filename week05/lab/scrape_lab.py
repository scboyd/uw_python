"""
scrape.py
Screen-scraping demo: open a page, find all http urls in hyperlinks. 
Note: Does not do well if the hyperlink isn't <a href=http://... /a> format
"""

import urllib2
import sys
import re

def find_link(a_tag):
    http = ""
    exp = r'href="(.+)"'
    http = re.search(exp, a_tag).group(1)
    return http

def find_a_tag(line):
    exp = r"<a href.+?/a>"
    m = re.findall(exp, line)
    return list(m) 

url = sys.argv[1] # website 
page = urllib2.urlopen(url).read()  # now page is one big string
a_tag_list = find_a_tag(page)
for tag in a_tag_list:
    http_link = find_link(tag)
    if "http://" in http_link:
        print http_link

#start = page.find('<a ')    # use string method to find first start tag


#print page[start:start+60]  # print 60 characters starting at tag



