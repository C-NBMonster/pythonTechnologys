#coding:utf-8

#利用fileinput读取一个文件所有行

import fileinput
def process(line):
    return line.rstrip() + ' line'


for line in fileinput.input(['t1.txt', 't2.txt'], backup='t1.txt.bak',inplace=True): #inplace将输出结果回写文件
    print(process(line))
#竟然报错。。。MMD2017-12-21





















