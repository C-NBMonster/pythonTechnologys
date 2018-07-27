#coding:utf-8

import time,os
#批量重命名，加文件前缀后缀实例。
#本例的思路是先目录与文件，再分割文件与文件扩展名，最后取出后缀名（主要是做条件限制，针对哪类文件进行操作），然后参照规则，符合规则的则进行重命名操作，再重新组合文件名称
def change_name(path):
    global i
    if not os.path.isdir(path) and not os.path.isfile(path):
        return False
    if os.path.isfile(path):
        file_path = os.path.split(path) #分割出目录与文件
        print("file_path:",file_path)
        lists = file_path[1].split('.') #分割出文件与文件扩展名
        print("lists:",lists)
        file_ext = lists[-1] #取出后缀名(列表切片操作)
        print("file_ext:",file_ext)
        img_ext = ['bmp','jpeg','gif','psd','png','jpg']
        if file_ext in img_ext:
            os.rename(path,file_path[0]+'/'+lists[0]+'_fc.'+file_ext)
            i+=1 #用于统计处理了多少图片
        #或者
        #img_ext = 'bmp|jpeg|gif|psd|png|jpg'
        #if file_ext in img_ext:
        #    print('ok---'+file_ext)
    elif os.path.isdir(path):
        for x in os.listdir(path):
            change_name(os.path.join(path,x)) #os.path.join()在路径处理上很有用

img_dir = r'C:\Users\MirrorsChen\Pictures\中国最美是个村落'
img_dir = img_dir.replace('\\','/')
start = time.time()
i = 0
change_name(img_dir)
c = time.time() - start
print('程序运行耗时:%0.2f'%(c))
print('总共处理了 %s 张图片'%(i))


