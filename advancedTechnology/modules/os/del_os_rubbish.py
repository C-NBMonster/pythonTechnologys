#coding:utf-8
import os
#删除系统垃圾文件
if os.name == 'nt':
 if 'HOMEPATH' in os.environ:
    home = os.environ['HOMEDRIVE'] + os.environ['HOMEPATH']
 else:
     home = os.environ['HOMEPATH']
workpath = os.path.join(home,'Local Settings')
#递归删除文件
#里面和下面的函数用try是抛出删除正在使用的零时文件出错
path = r"C:\Users\MirrorsChen\AppData"
def delfile(path):
 for file in os.listdir(path):
    if os.path.isfile(os.path.join(path,file)):
        try:
          print("\n删除垃圾文件： %s" % (os.path.join(path,file)))
          os.remove(os.path.join(path,file))
        except:
            pass
    elif os.path.isdir(os.path.join(path,file)):
        delfile(os.path.join(path,file))
    else:
        pass
delfile(os.path.join(workpath,'Temp'))
delfile(os.path.join(workpath,'Temporary Internet Files'))
#删除文件家的时候必须为空文件夹，而且只能从最里层删起
def deldir(pa):
 for i in os.listdir(pa):
    if os.path.isdir(os.path.join(pa,i)):
        if len(os.listdir(os.path.join(pa,i))) > 0:
            deldir(os.path.join(pa,i))
            try:
                os.rmdir(os.path.join(pa,i))
            except:
                pass
        else:
            try:
                print("\n删除文件夹 %s" % (os.path.join(pa,i)))
                os.rmdir(os.path.join(pa,i))
            except:
                pass
deldir(os.path.join(workpath,'Temp'))
deldir(os.path.join(workpath,'Temporary Internet Files'))
print("""
 系统产生的零时垃圾文件清理完毕！
 """)
input("请按回车键退出！")
