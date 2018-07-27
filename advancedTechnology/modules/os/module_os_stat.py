#coding:utf-8
import struct,time
import os

#获得文件属性

path = r"D:\Python\Python35\LICENSE.txt"
print("#文件最后访问时间--os.stat.st_atime:",os.stat(path).st_atime)
print("#文件最后访问时间的时间戳格式--os.stat.st_atime_ns:",os.stat(path).st_atime_ns)
print("#文件被创建的时间--os.stat.st_ctime:",os.stat(path).st_ctime)
print("#文件被创建的时间的时间戳格式--os.stat.st_ctime_ns:",os.stat(path).st_ctime_ns)
print("#设备号--os.stat.st_dev:",os.stat(path).st_dev)
print("#st_ino号--os.stat.st_ino:",os.stat(path).st_ino)
print("#number of hard links--os.stat.st_ino:",os.stat(path).st_nlink)
print("# all user's id--os.stat.st_uid:",os.stat(path).st_uid)
print("# all user's group id--os.stat.st_gid:",os.stat(path).st_gid)
print("# 文件大小--os.stat.st_size:",os.stat(path).st_size)
print("#文件最后修改时间--os.stat.st_mtime:",os.stat(path).st_mtime)
print("#文件权限模式--os.stat.st_mode:",os.stat(path).st_mode)
