# -*- coding:utf-8 -*-
from  xml.dom import  minidom
import os
#os.system('nmap -sV 172.18.64.43/24 --open -oX out.xml >/dev/null 2>&1')
os.system('nmap -v -sn -PE -n -iL ip -oN n.result >/dev/null 2>&1')
os.system("sed -e '/ost/'d -e '/Read/'d  n.result | cut -d ' '  -f 5 > iplist.txt")
os.system('nmap -sV -p 21,22,23,80-89,161,389,443,873,1433,1521,2601,2604,3128,3306,3389,4440,5432,5560,7778,6082,6379,7001,7002,8000,8008,8080,8081,8090,8099,8088,8089,8888,9000,9090,9200,11211,27017,28017,50000,50030,50070  -iL iplist.txt --open -oX out.xml >/dev/null 2>&1')

def get_attrvalue(node, attrname):
     return node.getAttribute(attrname) if node else ''#获取XML节点属性值

def get_nodevalue(node, index = 0):
    return node.childNodes[index].nodeValue if node else ''#获取XML节点值

def get_xmlnode(node,name):
    return node.getElementsByTagName(name) if node else []#获取XML节点对象集合

def xml_to_string(filename='out.xml'):
    doc = minidom.parse(filename)#加载读取XML文件
    return doc.toxml('UTF-8')

def get_xml_data(filename='out.xml'):
    doc = minidom.parse(filename) 
    root = doc.documentElement#获取XML文档对象

    host_nodes = get_xmlnode(root,'host')
    ports_list=[]
    f = file("portinfoss","w+")
    for node in host_nodes: 
        #print "-------------------------"
        f.writelines("\n-------------------------\n")
        address = get_xmlnode(node,'address')
        for addr in address:
            ip = get_attrvalue(addr,'addr')
         #   print ip
        port = get_xmlnode(node,'port')
        for p in port:
            port_id = get_attrvalue(p,'portid')
            f.writelines("\n")
            #print ip,port_id,
            f.write(ip)
            f.write("\t")
            f.write(port_id)
            f.write("\t")
            servers = get_xmlnode(p, 'service')
            for server in servers:
                server_name = get_attrvalue(server,'name')
                #print server_name
                f.write(server_name)

if __name__ == "__main__":
  get_xml_data()
