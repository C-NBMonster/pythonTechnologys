#coding:utf-8
#python中对文件、文件夹操作时经常用到的os模块和shutil模块常用方法
import os,glob

"""
   在python中，glob模块是用来查找匹配的文件的
    在查找的条件中，需要用到Unix shell中的匹配规则：

       *    :   匹配所所有
       ?    :   匹配一个字符
       *.*  :   匹配如：[hello.txt,cat.xls,xxx234s.doc]
       ?.*  :   匹配如：[1.txt,h.py]
       ?.gif:   匹配如：[x.gif,2.gif]
       如果没有匹配的，glob.glob(path)将返回一个空的list:[]
       缺点是只检查当前目录，不会检索子目录
"""
def get_all():
    '''获取目录[c:\\tmp]下面所有的文件'''
    return glob.glob(r'D:\Python\files\*.*')

def get_my_file():
    '''获取目录[c:\\tmp]下面文件名为4个字符的文件'''
    return glob.glob(r'D:\Python\files\????.txt')

def get_batch_file():
     '''获取目录[c:\\tmp]下面扩展名为\'.txt\'的文件'''
     return glob.glob(r'D:\Python\files\*.txt')

if __name__ == "__main__":
    print('获取目录[D:\Python\\tmp]下面所有的文件：')
    tem_files = get_all()
    print(tem_files)
    print('获取目录[c:\\tmp]下面文件名为4个字符的文件：')
    tem_files = get_my_file()
    print(tem_files)
    print('获取目录[c:\\tmp]下面扩展名为\'.txt\'的文件：')
    tem_files = get_batch_file()
    print(tem_files)







