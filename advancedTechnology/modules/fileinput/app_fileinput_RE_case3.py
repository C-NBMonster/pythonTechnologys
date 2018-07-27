#coding:utf-8

#利用fileinput实现文件内容替换，并将原文件作备份

import fileinput,os
print(os.getcwd())

for line in fileinput.input('t1.txt',backup='.bak',inplace=1):
    print(line.rstrip().replace('PHP','Perl'))  #或者print line.replace('Python','Perl')





















