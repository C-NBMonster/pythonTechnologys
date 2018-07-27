#coding:utf-8
#python中对文件、文件夹操作时经常用到的os模块和shutil模块常用方法
import os,shutil

print("1.os.getcwd()得到当前工作目录，即当前Python脚本工作的目录路径:", os.getcwd())
print("2.os.listdir()返回指定目录下的所有文件和目录名:",os.listdir(r"D:\Python\Projects\ZD"))#以列表形式返回
print("3.os.remove(路径)函数用来删除一个文件:") #如果目录不存在，FileNotFoundError
print("4.删除多个目录：os.removedirs(r'c：\python')")
print("5.os.path.isfile()检验给出的路径是否是一个文件：",os.path.isfile(r"D:\Python\Projects\ZD"))#返回布尔值
print("6.os.path.isdir()检验给出的路径是否是一个目录：",os.path.isdir(r"D:\Python\Projects\ZD"))#返回布尔值
print("7.os.path.isabs()判断是否是绝对路径：",os.path.isabs(r"D:\Python\Projects\ZD"))#返回布尔值
print("8.os.path.exists()检验给出的路径是否真地存:",os.path.exists(r"D:\Python\Projects\ZD"))#返回布尔值
print("9.os.path.split()返回一个路径的目录名和文件名:",os.path.split(r"D:\Python\Projects\ZD"))#这个函数很奇葩，就是以元祖形式返回参数的上级目录，和当前文件夹的名字('D:\\Python\\Projects', 'ZD')

"""
10.分离扩展名：os.path.splitext()
11.获取路径名：os.path.dirname()
12.获取文件名：os.path.basename()
13.运行shell命令: os.system()
14.读取和设置环境变量:os.getenv() 与os.putenv()
15.给出当前平台使用的行终止符:os.linesep    Windows使用'\r\n'，Linux使用'\n'而Mac使用'\r'
16.指示你正在使用的平台：os.name       对于Windows，它是'nt'，而对于Linux/Unix用户，它是'posix'
17.重命名：os.rename(old， new)
18.创建多级目录：os.makedirs(r"c：\python\test")
19.创建单个目录：os.mkdir("test")
20.获取文件属性：os.stat(file)
21.修改文件权限与时间戳：os.chmod(file)
22.终止当前进程：os.exit()
23.获取文件大小：os.path.getsize(filename)
"""

#二、文件操作方法大全
os.mknod("test.txt")        #创建空文件
fp = open("test.txt",w)     #直接打开一个文件，如果文件不存在则创建文件
fp.read([size])                     #size为读取的长度，以byte为单位
fp.readline([size])                 #读一行，如果定义了size，有可能返回的只是一行的一部分
fp.readlines([size])                #把文件每一行作为一个list的一个成员，并返回这个list。其实它的内部是通过循环调用readline()来实现的。如果提供size参数，size是表示读取内容的总长，也就是说可能只读到文件的一部分。
fp.write(str)                       #把str写到文件中，write()并不会在str后加上一个换行符
fp.writelines(seq)                  #把seq的内容全部写到文件中(多行一次性写入)。这个函数也只是忠实地写入，不会在每行后面加上任何东西。
fp.close()                          #关闭文件。python会在一个文件不用后自动关闭文件，不过这一功能没有保证，最好还是养成自己关闭的习惯。  如果一个文件在关闭后还对其进行操作会产生ValueError
fp.flush()                          #把缓冲区的内容写入硬盘
fp.fileno()                         #返回一个长整型的"文件标签"
fp.isatty()                         #文件是否是一个终端设备文件（unix系统中的） fileobject.isatty()
fp.tell()                           #返回文件操作标记的当前位置，以文件的开头为原点
fp.next()                           #返回下一行，并将文件操作标记位移到下一行。把一个file用于for … in file这样的语句时，就是调用next()函数来实现遍历的。
fp.seek(offset[,whence])            #将文件打操作标记移到offset的位置。

#fp.truncate([size])                 #把文件裁成规定的大小，默认的是裁到当前文件操作标记的位置。如果size比文件的大小还要大，依据系统的不同可能是不改变文件，也可能是用0把文件补到相应的大小，也可能是以一些随机的内容加上去。
path = "D:/dll_list.txt"
fo = open(path, "r+")
print("Name of the file: ", fo.name)
line = fo.readline()
print("Read Line: %s" % (line))
# Now truncate remaining file.
fo.truncate(20)
# Try to read file now
line = fo.readline()
print("Read Line: %s" % (line))
# Close opend file
fo.close()
#-----------------------------------------------------------------------------------------------------------------------
#三、目录操作方法大全
#1.创建目录
os.mkdir("file")
#2.复制文件：
shutil.copyfile("oldfile","newfile")        #oldfile和newfile都只能是文件
shutil.copy("oldfile","newfile")            #oldfile只能是文件夹，newfile可以是文件，也可以是目标目录
#3.复制文件夹：
#4.shutil.copytree("olddir","newdir")        #olddir和newdir都只能是目录，且newdir必须不存在
#5.重命名文件（目录）
os.rename("oldname","newname")              #文件或目录都是使用这条命令
#6.移动文件（目录）
shutil.move("oldpos","newpos")
#7.删除文件
os.remove("file")
#8.删除目录
os.rmdir("dir")                             #只能删除空目录
shutil.rmtree("dir")                        #空目录、有内容的目录都可以删
#9.转换目录
os.chdir("path")                            #换路径






















