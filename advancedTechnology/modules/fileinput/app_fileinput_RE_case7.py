#coding:utf-8

#利用fileinput及re做分析: 提取符合条件的电话号码

import re
import fileinput

pattern = '[010|021]-\d{8}'  # 提取区号为010或021电话号码，格式:010-12345678

for line in fileinput.input('t4.txt'):
    if re.search(pattern, line):
        print('=' * 50)

        print('Filename:' + fileinput.filename() + ' | Line Number:' + str(fileinput.lineno()) + ' | ' + line)




















