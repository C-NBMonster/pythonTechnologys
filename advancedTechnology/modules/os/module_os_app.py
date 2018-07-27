#coding:utf-8

import time,os
import os.path
import shutil
import time, datetime

#1，将某个文件中的文件复制到指定文件中

def copyFiles(sourceDir, targetDir):
   if sourceDir.find(".svn") > 0:
     return
   for file in os.listdir(sourceDir):
     sourceFile = os.path.join(sourceDir, file)
     targetFile = os.path.join(targetDir, file)
     if os.path.isfile(sourceFile):
       if not os.path.exists(targetDir):
         os.makedirs(targetDir)
       if not os.path.exists(targetFile) or(os.path.exists(targetFile) and (os.path.getsize(targetFile) != os.path.getsize(sourceFile))):
           open(targetFile, "wb").write(open(sourceFile, "rb").read())
     if os.path.isdir(sourceFile):
       First_Directory = False
       copyFiles(sourceFile, targetFile)

#删除一级目录下的所有文件
def removeFileInFirstDir(targetDir):
   for file in os.listdir(targetDir):
     targetFile = os.path.join(targetDir, file)
     if os.path.isfile(targetFile):
       os.remove(targetFile)

#复制一级目录下的所有文件到指定目录
def coverFiles(sourceDir, targetDir):
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir, file)
        targetFile = os.path.join(targetDir, file)
        # cover the files
        if os.path.isfile(sourceFile):
            open(targetFile, "wb").write(open(sourceFile, "rb").read())


#往指定目录写文本文件：
def writeVersionInfo(targetDir):
  open(targetDir, "wb").write("Revison:")


#返回当前的日期，以便在创建指定目录的时候用：
def getCurTime():
   nowTime = time.localtime()
   year = str(nowTime.tm_year)
   month = str(nowTime.tm_mon)
   if len(month) < 2:
     month = '0' + month
   day = str(nowTime.tm_yday)
   if len(day) < 2:
     day = '0' + day
   return (year + '-' + month + '-' + day)


#然后就是主函数的实现了：

if __name__ =="__main__":
   print("Start(S) or Quilt(Q) \n")
   flag = True
   Debug_File_Path = ''
   Target_File_Path = ''
   Release_File_Path = ''
   Firebird_File_Path =''
   AssistantGui_File_Path = ''
   while (flag):
     answer = input()
     if 'Q' == answer:
       flag = False
     elif 'S'== answer :
       formatTime = getCurTime()
       targetFoldername = "Build " + formatTime + "-01"
       Target_File_Path += targetFoldername
       copyFiles(Debug_File_Path,  Target_File_Path)
       removeFileInFirstDir(Target_File_Path)
       coverFiles(Release_File_Path, Target_File_Path)
       #moveFileto(Firebird_File_Path, Target_File_Path)
       #moveFileto(AssistantGui_File_Path, Target_File_Path)
       writeVersionInfo(Target_File_Path+"\\ReadMe.txt")
       print("all sucess")
     else:
       print("not the correct command")



#通过传入需要遍历的目录，列出目录下的所有文件并统计文件数，os提供的path模块能对目录非常灵活的操作。
dir = "F:/设计师俱乐部2.0"
def listdir(dir,file):
  file.write(dir + '\n')
  filenum = 0
  list = os.listdir(dir) #列出目录下的所有文件和目录
  for line in list:
    filepath = os.path.join(dir,line)
    if os.path.isdir(filepath): #如果filepath是目录，则再列出该目录下的所有文件
      myfile.write('  ' + line + '\\'+'\n')
      for li in os.listdir(filepath):
        myfile.write('   '+li + '\n')
        filenum = filenum + 1
    elif os.path:  #如果filepath是文件，直接列出文件名
      myfile.write('  '+line + '\n')
      filenum = filenum + 1

  myfile.write('all the file num is '+ str(filenum))
#dir = input('please input the path:')
myfile = open('list.txt','w')
listdir(dir,myfile)
myfile.close()

#遍历目录os.walk方法
def walk_dir(dir,fileinfo,topdown=True):
  for root, dirs, files in os.walk(dir, topdown):
    for name in files:
      print(os.path.join(name))
      fileinfo.write(os.path.join(root,name) + '\n')
    for name in dirs:
      print(os.path.join(name))
      fileinfo.write(' ' + os.path.join(root,name) + '\n')
dir = input('please input the path:')
fileinfo = open('list.txt','w')
walk_dir(dir,fileinfo)






