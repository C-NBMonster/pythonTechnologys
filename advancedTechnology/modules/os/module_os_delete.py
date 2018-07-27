#coding:utf-8
import struct,time
import os,sys,shutil
paths = r"D:\Python\files\mkfiles"

def del_files(path):
  for root , dirs, files in os.walk(path):
    for name in files:
      if name.endswith(".CR2"):
        os.remove(os.path.join(root, name))
        print ("Delete File: ",os.path.join(root, name))


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

#删除当前目录下除当前脚本以外的文件和文件夹的方法
cur_file = os.path.basename(sys.argv[0])#先获取本文件的绝对路径，再获取本文件名
dir_content = [x for x in os.listdir(".") if x != cur_file]#listdir(".")返回当前路径下的文件列表
for f in dir_content:
  if os.path.isdir(f):#如果是路径
    shutil.rmtree(f)#删除路径
  else:#不是
    os.remove(f)#删除

#删除指定后缀文件
def delete_files(dir,topdown=True):
  for root, dirs, files in os.walk(dir, topdown):
    for name in files:
      pathname = os.path.splitext(os.path.join(root, name))
      if (pathname[1] != ".py" and pathname[1] != ".hpp" and pathname[1] != ".h"):
        os.remove(os.path.join(root, name))
        print(os.path.join(root,name))
dir = os.getcwd()
print(dir)
#delete_files(dir)
#will delete the self .py file after run !!!-_-
#os.removedirs(dir)
#delete the empty directory recursively


#介绍了删除文件夹下所有文件和子文件夹的示例

"""
产生异常的可能原因:
(1)filename 不存在
(2)对filename文件， 没有操作权限或只读。
"""
def delete_file_folder(src):
    '''delete files and folders'''
    if os.path.isfile(src):
        try:
            os.remove(src)
        except:
            pass
    elif os.path.isdir(src):
        for item in os.listdir(src): #先删除文件
            itemsrc=os.path.join(src,item)
            delete_file_folder(itemsrc)
        try:
            os.rmdir(src)#再删除文件
        except:
            pass


























