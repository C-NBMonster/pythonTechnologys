#coding:utf-8
import struct,time
import os,sys
paths = r"D:\Python\files\mkfiles"
if(os.path.exists(paths)): #判断文件是否存在
    print(paths,"已存在！")
else:
    if os.path.isfile(paths):#判断是不是文件
        print(paths,"是一个文件名")
    else:
        os.makedirs(paths) #创建文件
if os.path.exists(paths):
    print("创建文件成功！")

#获得文件创建时间和修改时间的方法
class TypeError (Exception):
  pass
if __name__ == '__main__':
 if (len(os.sys.argv) < 1):
   raise TypeError()
 else:
   print("os.sys.argv[0]: %s" % os.sys.argv[0])
   # os.sys.argv[0] is the current file, in this case, file_ctime.py
 f = os.sys.argv[0]
 mtime = time.ctime(os.path.getmtime(f))
 ctime = time.ctime(os.path.getctime(f))
 print("Last modified : %s, last created time: %s" % (mtime, ctime))

#
f=open('a.txt','a')
f.write(os.popen('netstat -n').read())#执行cmd脚本，并将返回内容写入文件
f.close()

#批量生成文件夹
base = r'D:\Python\files\mkfiles\mkf'
i = 1
for j in list(range(30)):
    file_name = base + str(i)
    os.mkdir(file_name)
    while i == 30:
        if os.path.exists(file_name):
            print("Create foldders OK")
            break
    i = i + 1






