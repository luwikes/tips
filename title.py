from bs4 import BeautifulSoup
import urllib2

def main():

    userMainUrl = "http://www.baidu.com"
    req = urllib2.Request(userMainUrl)
    resp = urllib2.urlopen(req)
    respHtml = resp.read()
    foundLabel = respHtml.findAll("label")

    finalL =foundLabel.string

    print "biaoti=",finalL
if __name__=="__main__":

    main();
