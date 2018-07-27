#coding:utf-8

#利用fileinput读取一个文件所有行

import fileinput
for line in fileinput.input(r'D:\Pythonbb\prac\prac_excel.py'):
        print( fileinput.filename(),'|','Line Number:',fileinput.lineno(),'|: ',line  )

