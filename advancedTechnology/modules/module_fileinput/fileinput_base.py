#coding:utf-8

"""
fileinput模块可以遍历文本文件的所有行.它的工作方式和readlines很类似,不同点在于,它不是将全部的行读到列表中而是创建了一个xreadlines对象.

下面是fileinput模块中的常用函数
1.input() #它会返回能够用于for循环遍历的对象.
2.filename() #返回当前文件的名称
3.lineno() #返回当前(累计)的行数
4.filelineno() #返回当前文件的行数
5.isfirstline() #检查当前行是否是文件的第一行
6.close() #关闭序列


"""



import fileinput
import timeit
def func_fileinput():
    for eachline in fileinput.input("D:/dll_list.txt"):
        print("fileinput",eachline)

def file_open():
    file = open("D:/dll_list.txt","r")
    for word in file.readlines():
        print("readlines:",word)

w1 = timeit.timeit(func_fileinput,number=1)
w2 = timeit.timeit(file_open,number=1)
print(" fileinput time is: %s" % w1)
print(" filereadlines time is: %s" % w2)

#通过实践计算，还是readlines性能好些，速度更快
