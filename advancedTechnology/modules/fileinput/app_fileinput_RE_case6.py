#coding:utf-8

#利用fileinput及re做日志分析: 提取所有含日期的行

import re
import fileinput
import sys

pattern = '\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'

for line in fileinput.input('t3.log', backup='.bak', inplace=1):
    if re.search(pattern, line):
        sys.stdout.write("=> ")
        sys.stdout.write(line)





















