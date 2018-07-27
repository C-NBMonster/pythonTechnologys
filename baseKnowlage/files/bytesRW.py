#coding:utf-8
#主要是介绍利用configparser读取与修改ini文件

import configparser
import struct
from struct import *
file = open(r"D:/Python/files/debug.txt", "wb")
bt = b"values"
file.write(pack("idhs", 12345, 67.89, 15,bt)) #idh不带小数,格式中的字符数=后面的值个数
file.close()

fp = open(r"D:/Python/files/debug.txt", "rb")
(a,b,c,s) = unpack("idhs",fp.read()) #s只读到v，后面的字符不读取
print(a,b,c,s)
fp.close()


myfile=open(r'D:\Python\files\txt.txt','rb').read(1)
print(struct.unpack('c',myfile))
print(struct.unpack('b',myfile))



























