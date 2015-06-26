#!/usr/bin/python
import urllib2
from bs4 import BeautifulSoup

def cl(id):
    url = "http://www.wooyun.org/corps/page/"+str(id)
    req = urllib2.Request(url)
    req.add_header('User-Agent','fake-client')#null user-agent forbidden
    resp = urllib2.urlopen(req)
    html = resp.read()
    soup = BeautifulSoup(html)
    for i in soup.find_all(rel="nofollow"):
        print str(i).split('"')[1]

def main():
    for i in xrange(1,36):
       cl(i)

if __name__ == "__main__":
    main()
