#coding:utf-8

#利用fileinput将CRLF文件转为LF

import fileinput
import sys

for line in fileinput.input(inplace=True):
    # 将Windows/DOS格式下的文本文件转为Linux的文件
    if line[-2:] == "\r\n":
        line = line + "\n"
    sys.stdout.write(line)




















