import os
import sys
import urllib2
import re
"""
Make a file downloader using screen scraping
Example: scrapes the course webpage for the URLs of all the Python source files
then downloads them all.
"""
def find_link(a_tag):
    http = ""
    exp = r'href="(http://.+)"'
    print a_tag
    p = re.search(exp, a_tag)
    if p:
        http = p.group(1)
        return http
    else:
        return None

def find_a_tag(line):
    exp = r"<a href.+?/a>"
    m = re.findall(exp, line)
    return list(m)


def download_files(url, download_path):
    # read the html to parse
    page = urllib2.urlopen(url).read()    
    # find all of the http:// urls in a string
    links = get_http_links(page)    
    
    for l in links:
        print "Download this shit: " + l
        stuff = urllib2.urlopen(l).read()
        f = open(l, "wb")
        f.write(stuff)
        f.close()

def get_http_links(s):
    l = []
    tag_list = find_a_tag(s)
    for tag in tag_list:
        http_link = find_link(tag)
        if http_link:

            if "http://" in http_link:
                l.append(http_link)
    
    return l


if __name__ == "__main__":
    download_files(sys.argv[1], sys.argv[2])
