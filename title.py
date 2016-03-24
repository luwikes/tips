from bs4 import BeautifulSoup
import urllib2

def findTitle(url='http://www.baidu.com'):

        try:
                req = urllib2.Request(url)
                resp = urllib2.urlopen(req,timeout=5)
                respHtml = resp.read()
                soup = BeautifulSoup(respHtml)
                print url.strip('\n'),soup.title.string

        except Exception,e:
                return

def main():
        fo = open('httpre','r')
        for line in fo:
                u='http://'+line
                findTitle(u)
if __name__=="__main__":
        main();
