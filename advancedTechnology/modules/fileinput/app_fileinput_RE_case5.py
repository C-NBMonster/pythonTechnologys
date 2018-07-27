#coding:utf-8

#利用fileinput将CRLF文件转为LF

import fileinput
import glob

for line in fileinput.input(glob.glob("t1.txt")):
    if fileinput.isfirstline():
        print('-' * 20, 'Reading %s...' % fileinput.filename(), '-' * 20)

    print(str(fileinput.lineno()) + ': ' + line.upper())





















