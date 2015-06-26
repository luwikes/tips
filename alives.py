#!/usr/bin/env python
# -*- coding:utf-8 -*-
import httplib
#import urllib

def sendhttp(url='bugs.python.org'):
    conn = None
    try:
        conn = httplib.HTTPConnection(url,timeout=5)
        conn.request('GET','/')
        httpres = conn.getresponse()
        fo2 = open('url.txt','a')
        if httpres.status == 200:
            print url
            fo2.write(url+'\n')
        fo2.close
        #print httpres.reason
        #print httpres.read()
    except Exception,e:
        return
    finally:
        if conn:
            conn.close()

def main():
    fo = open('jd.com.txt','r')
    for line in fo:
        a = line.split()
        sendhttp(a[0])

if __name__ == '__main__':
    main()
