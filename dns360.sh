#!/bin/bash
wget http://webscan.360.cn/sub/index/?url=$1 -O $1.txt
grep strong $1.txt > $1.txt2
cat $1.txt2 | cut -d "=" -f 6 | cut -d "'" -f 1 > $1.txt
rm -f $1.txt2
