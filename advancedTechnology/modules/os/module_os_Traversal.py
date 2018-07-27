#coding:utf-8
#python中对文件、文件夹操作时经常用到的os模块和shutil模块常用方法
import os,shutil,fnmatch
import time
#通过传入需要遍历的目录，列出目录下的所有文件并统计文件数，os提供的path模块能对目录非常灵活的操作。
import sys
def listdir(dir,file):
  file.write(dir + '\n')
  fielnum = 0
  list = os.listdir(dir) #列出目录下的所有文件和目录
  for line in list:
    filepath = os.path.join(dir,line)
    if os.path.isdir(filepath): #如果filepath是目录，则再列出该目录下的所有文件
      myfile.write('  ' + line + '\\'+'\n')
      for li in os.listdir(filepath):
        myfile.write('   '+li + '\n')
        fielnum = fielnum + 1
    elif os.path:  #如果filepath是文件，直接列出文件名
      myfile.write('  '+line + '\n')
      fielnum = fielnum + 1
  myfile.write('all the file num is '+ str(fielnum))
dir = input('please input the path:')
myfile = open('list.txt','w')


#python三种遍历文件方法
#方法一：os.walk()该方法遍历完指定文件路径下的所有文件夹与文件。
#os模块提供的walk方法很强大，能够把给定的目录下的所有目录和文件遍历出来。
#方法：os.walk(path),遍历path，返回一个对象，他的每个部分都是一个三元组,('目录x'，[目录x下的目录list]，目录x下面的文件)
#topdown决定遍历的顺序，如果topdown为True，则先列举top下的目录，然后是目录的目录，依次类推，反之，则先递归列举出最深层的子目录，然后是其兄弟目录，然后子目录。
def walk_dir(dir,fileinfo,topdown=True):
  for root, dirs, files in os.walk(dir, topdown): #os.walk返回的是一个对象，必须要进行遍历root是一个字符串，即当前目录，dirs是一个列表，子目录列表，files也是一个列表，文件名列表
    for name in files:
      print(os.path.join(name)) #效果跟print(name)一样。os.path.join主要用于返回一个路径，根据系统自动选择路径标识符
      fileinfo.write(os.path.join(root,name) + '\n')
    for name in dirs:
      print(os.path.join(name))
      fileinfo.write(' ' + os.path.join(root,name) + '\n')
dir = input('please input the path:')
fileinfo = open('list.txt','w')
walk_dir(dir,fileinfo)

#方法二：listdir,次方法只能显示某一级目录下的文件夹和文件，不遍历子文件
s = os.sep
root = "e:" + s + "一级目录" + s
for i in os.listdir(root):
    print(i)
    if os.path.isfile(os.path.join(root, i)):
        print(i)

#方法三
#os.walk()这种方法在Python3中不存在了，应该是合并到os.walk()中了。
def traverseDirByOSWalk(path):
    path = os.path.expanduser(path)
    for (dirname, subdir, subfile) in os.walk(path):
        #print('dirname is %s, subdir is %s, subfile is %s' % (dirname, subdir, subfile))
        print('[' + dirname + ']')
        for f in subfile:
            print(os.path.join(dirname, f))

# 方法四
#glob.glob(path)返回带目录的文件名.通配符和shell相似.path不能包含shell变量.
import glob
def traverseDirByGlob(path):
    path = os.path.expanduser(path)
    for f in glob.glob(path + '/*'):
        print(f.strip())


# 将文件属性中的时间改为‘2011-1-12 00：00：00格式'
def formattime(localtime):
    endtime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(localtime))
    return endtime


def searchdir(arg, dirname, names):
    for filespath in names:
        # 得到文件路径
        fullpath = os.path.join(dirname, filespath)
        print(fullpath)
        # 得到文件属性
        statinfo = os.stat(fullpath)
        # 文件大小
        sizefile = statinfo.st_size
        # 创建时间
        creattime = formattime(statinfo.st_ctime)
        # 修改时间
        maketime = formattime(statinfo.st_mtime)
        # 浏览时间
        readtime = formattime(statinfo.st_atime)
        # 判断是文件夹还是文件
        if os.path.isdir(fullpath):
            filestat = 'DIR'
        else:
            filestat = 'FILE'
        open('D:\\test.txt', 'a').write('【%s】路径：%s 文件大小(B)：%s 创建时间：%s 修改时间：%s 浏览时间：%s\r\n'
                                        % (filestat, fullpath, sizefile, creattime, maketime, readtime))

def count_dll():   #遍历指定条件下的文件并输出到文件中。
    f = open(r'D:/dll_list.txt', 'w')
    for root, dirs, files in os.walk('c:\\'):
        for name in files:
            if fnmatch.fnmatch(name, '*.dll'): #符合条件的就添加到输出
                f.write(os.path.join(root, name))
                f.write('\n')
    f.close()
    print('done...')

#python遍历文件夹并删除特定格式文件的示例
def del_files(path):
    for root, dirs, files in os.walk(path):
        for name in files:
            if name.endswith(".tmp"):
                os.remove(os.path.join(root, name))

    print("Delete File: " + os.path.join(root, name))











