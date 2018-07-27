#coding:utf-8
#文件读写
import time

"""
file_hander(文件句柄或者叫做对象)= open(filename,mode)
open mode：
模式    说明
w：     以写方式打开，
a：     以追加模式打开 (从 EOF 开始, 必要时创建新文件)
r+：    以读写模式打开
w+：    以读写模式打开 (参见 w )
a+：    以读写模式打开 (参见 a )
rb：    以二进制读模式打开
wb：    以二进制写模式打开 (参见 w )
ab：    以二进制追加模式打开 (参见 a )
rb+：   以二进制读写模式打开 (参见 r+ )
wb+：   以二进制读写模式打开 (参见 w+ )
ab+：   以二进制读写模式打开 (参见 a+ )
"""

#读
#不能把open语句放在try块里，因为当打开文件出现异常时，文件对象file_object无法执行close()方法。
fo = open(r"D:\Python\files\txt.txt","r",encoding="utf-8")
try:
    fContent = fo.read()
finally:
    fo.close()
print(fContent)

#写，w模式是写入，如果文件不存在，则创建
#注意，调用writelines写入多行在性能上会比使用write一次性写入要高。
tName = "D:\\Python\\files\\" + str(time.strftime('%Y%m%d%H%M%S',time.localtime())) + ".txt"
print(tName)
fw = open(tName,"w")
fw.write("just test for 'w' mode.\nif it's OK,we can go to next operation")
fw.close()

#附加
fa = open(tName,"a")
fa.write("这是附加的信息")
fa.close()













