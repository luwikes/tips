#!/bin/sh
nmap -v -sn -PE -n -iL ip -oN n.result 
#nmap -v -sn -PE -n --min-hostgroup 256 --min-parallelism 256 -iL ip -oN n.result 
#nmap -v -sn -PE -n --min-hostgroup 1024 --min-parallelism 1024 -oN n.result  210.73.73.1/24
sed -e '/ost/'d -e '/Read/'d  n.result | cut -d " " -f 5 > iplist.txt
rm -f n.result
#nmap -sT -sV -p 21,22,23,80,161,389,443,873,1433,1521,2601,2604,3128,3306,3389,4440,5432,5560,7778,6082,6379,7001,7002,8000,8008,8080,8081,8090,8099,8088,8089,8888,9000,9090,9200,11211,27017,28017,50000,50030,50070 --max-hostgroup 10 --max-parallelism 10 --max-rtt-timeout 1000ms --host-timeout 800s --max-scan-delay 2000ms -iL iplist.txt -oN port.txt --open 
#nmap -sV -p 21,22,23,80,161,389,443,873,1433,1521,2601,2604,3128,3306,3389,4440,5432,5560,7778,6082,6379,7001,7002,8000,8008,8080,8081,8090,8099,8088,8089,8888,9000,9090,9200,11211,27017,28017,50000,50030,50070 --script=auth --script=brute --script=default --script=vuln --script=http* --min-hostgroup 256 --min-parallelism 256 -iL iplist.txt -v --open -oN port.txt 
#nmap -sV -p 21,22,23,80,161,389,443,873,1433,1521,2601,2604,3128,3306,3389,4440,5432,5560,7778,6082,6379,7001,7002,8000,8008,8080,8081,8090,8099,8088,8089,8888,9000,9090,9200,11211,27017,28017,50000,50030,50070 --script=auth --script=default --script=vuln --script=http-backup-finder.nse --script=http-config-backup.nse  -iL iplist.txt -v --open -oN port.txt 
nmap -sV -p 21,22,23,80,161,389,443,873,1433,1521,2601,2604,3128,3306,3389,4440,5432,5560,7778,6082,6379,7001,7002,8000,8008,8080,8081,8090,8099,8088,8089,8888,9000,9090,9200,11211,27017,28017,50000,50030,50070 --script=default  -iL iplist.txt -v --open -oN port.txt 
#nmap -sV -p 21,22,23,80,161,389,443,873,1433,1521,2601,2604,3128,3306,3389,4440,5432,5560,7778,6082,6379,7001,7002,8000,8008,8080,8081,8090,8099,8088,8089,8888,9000,9090,9200,11211,27017,28017,50000,50030,50070 --script=auth --script=brute --script=default --script=vuln --script=http* -iL iplist.txt -v --open -oN port.txt 
#sed -in-place -e '/Host/'d -e '/Not/'d -e '/PORT/'d -e '/SF/'d -e '/NEXT/'d -e '/please/'d  port.txt
sed -e '/Host/'d -e '/Not/'d -e '/PORT/'d -e '/SF/'d -e '/NEXT/'d -e '/please/'d  port.txt > portinfo.txt
rm -f iplist.txt prot.txt
