'''
@author: mirrorChen
@license: (C) Copyright 2013-2018, Node Supply Chain Manager Corporation Limited.
@contact: chenjingxu3@dafycredit.com
@software: JYB_Android_AT
@file: walk_func.py
@time: 2018/7/11 17:22
@desc:
'''
import os

dir = os.getcwd()
print(dir)
topdown = True
def walk_dir(dir,fileinfo,topdown):
  for root, dirs, files in os.walk(dir, topdown): #os.walk返回的是一个对象，必须要进行遍历root是一个字符串，即当前目录，dirs是一个列表，子目录列表，files也是一个列表，文件名列表
    for name in files:
      print(os.path.join(name)) #效果跟print(name)一样。os.path.join主要用于返回一个路径，根据系统自动选择路径标识符
      fileinfo.write(os.path.join(root,name) + '\n')
    for name in dirs:
      print(os.path.join(name))
      fileinfo.write(' ' + os.path.join(root,name) + '\n')
#dir = input('please input the path:')
fileinfo = open('list.txt','w')
walk_dir(dir,fileinfo,True)