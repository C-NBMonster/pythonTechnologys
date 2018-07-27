#coding:utf-8
"""
fileinput模块可以对一个或多个文件中的内容进行迭代、遍历等操作。
该模块的input()函数有点类似文件readlines()方法，区别在于:
前者是一个迭代对象，即每次只生成一行，需要用for循环迭代。
后者是一次性读取所有行。在碰到大文件的读取时，前者无疑效率更高效。
用fileinput对文件进行循环遍历，格式化输出，查找、替换等操作，非常方便。


fileinput模块可以遍历文本文件的所有行.它的工作方式和readlines很类似,不同点在于,它不是将全部的行读到列表中而是创建了一个xreadlines对象.
下面是fileinput模块中的常用函数
input()     #它会返回能够用于for循环遍历的对象.
filename() #返回当前文件的名称
lineno()    #返回当前(累计)的行数
filelineno() #返回当前文件的行数
isfirstline() #检查当前行是否是文件的第一行

"""
"""
fileinput.input (files=None, inplace=False, backup='', bufsize=0, mode='r', openhook=None)
files:                  #文件的路径列表，默认是stdin方式，多文件['1.txt','2.txt',...]  
inplace:                #是否将标准输出的结果写回文件，默认不取代  
backup:                 #备份文件的扩展名，只指定扩展名，如.bak。如果该文件的备份文件已存在，则会自动覆盖。  
bufsize:                #缓冲区大小，默认为0，如果文件很大，可以修改此参数，一般默认即可  
mode:                   #读写模式，默认为只读  
openhook:               #该钩子用于控制打开的所有文件，比如说编码方式等;  
"""
import fileinput
import sys
import glob
import string
'''  处理一个文本文件  '''
#for line in fileinput.input("D:\Pythonbb\prac\prc_froAll.py").readline().encode(encoding='gbk',errors='ignore'):
    #print(line)
'''处理多个文本文件 并输出行号'''

for line in fileinput.input(glob.glob(r"D:\Pythonbb\prac\*.txt")).readline().encode(encoding='gbk',errors='ignore'):
    if fileinput.isfirstline():
       print("------ reading %s ------\n" % fileinput.filename())
    print(str(fileinput.lineno())," ",line)
    #找出行数最多的文件名--作业


