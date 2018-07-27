#coding:utf-8
import itertools as it
#base string opeate

'''判断aset中是否含有seq里的一个或者多个项
  seq可以是字符串或者列表
  aset应该是字符串或者列表
'''
def a_containsAnyOf_b(seq,aset):
    if seq in aset:
        return True
    else:
        return False
print("this's a_containsAnyOf_b():---------")
print(a_containsAnyOf_b("11","1223"))

'''判断seq中的所有项是否都在aset里,跟上一个方法一样
  seq可以是字符串或者列表
  aset应该是字符串或者列表
'''
def a_AllIn_b(seq,aset):
    for item in seq:
        if item not in aset:
            return False
    return True

print("this's a_AllIn_b():---------")
print(a_AllIn_b("dc","acdc"))
print(a_AllIn_b("dc","acc"))


'''判断aset是否包含seq里的所有项 --跟in一样
    seq可以是字符串或者列表
    aset应该是字符串或者列表
         任何一个set对象a，a.difference(b)等价于a-set(b),即返回a中所有不属于b的元素'''
def a_containsAll_b(seq,aset):
    return not set(aset).difference(seq)

print("this's a_containsAll_b():---------")
print(a_containsAll_b("acdc","dc"))
print(a_containsAll_b("dc","acc"))

#生成所有字符的可复用的字符串
sumory_allchars=str.maketrans('','')
def makefilter(keep):
  '''返回一个函数，此函数接受一个源字符串作为参数\
    并返回字符串的一个部分拷贝\
    此拷贝只包括keep中的字符，keep必须是一个普通的字符串\
    调用示例：makefilter('abca ')('abcdefgh ijkal cba')\
    在后面的字符串中保留前面出现的字符 abc a cba
  '''
  #按照sumory_allchars规则剔除sumory_allchars字符串中的keep里的字符
  #这里得到keep在sumory_allchars的补集
  deletechars=sumory_allchars.translate(sumory_allchars,keep)
  #生成并返回需要的过滤函数（作为闭包）
  def realdelete(sourseStr):
    return sourseStr.translate(sumory_allchars,deletechars)
  return realdelete

  '''删除list中的重复项,方法是遍历原list，然后添加到临时表中，如果临时表中有则不放入，通过not in 方法来实现'''
lTest=[1,1,2,3,"c","c","a"]
def list_removesame(list):
  templist=[]
  for c in list:
    if c not in templist:
      templist.append(c)
  return templist

print("this's list_removesame:-----")
print(list_removesame(lTest))


#以下没有消化----2017-08-22

def replace_strby_dict(sourseStr, dict, marker='"', safe=False):
    '''使用字典替换源字符串中的被marker包裹的相应值'''
    # 如果safe为True，那么字典中没找到key时不替换
    if safe:
        def lookup(w):
            return dict.get(w, w.join(marker * 2))
            # w.join(marker*2)用marker包裹w
    # 如果safe为False，那么字典中没找到key时抛异常\
    # 若将dict[w]换为dict.get(w)则没找到时返回None
    else:
        def lookup(w):
            return dict[w]
    # 根据marker切分源字符串
    splitparts = sourseStr.split(marker)
    # 取出切分后的奇数项
    # 因为切分后，列表中源字符串中marker包裹的项肯定位于基数部位
    # 就算是'"first"s is one'这样的字符串也是如此
    # 分割后的第0项为空串，第1项为first
    splitparts[1::2] = map(lookup, splitparts[1::2])
    return ''.join(splitparts)


def simply_replace_strby_dict(sourseStr, dict, safe=True):
    '''根据dict内容替换sourseStr原串中$标记的子字符串\
    dict= {'name':'sumory','else':'default'}
    $$5 -> $5
    $else -> default
    ${name}'s method -> sumory's method
    '''
    style = string.Template(sourseStr)
    # 如果safe，在dict中找不到的话不会替换，照样保留原串
    if safe:
        return style.safe_substitute(dict)
    # false，找不到会抛异常
    else:
        return style.substitute(dict)


##################################################
def scanner(object, linehandler):
    '''用linehandler方法遍历object的每一项'''
    for line in object:
        linehandler(line)


def printfilelines(path):
    '''读取path路径下的文件屏逐行打印'''
    fileobject = open(path, 'r')  # open不用放到try里
    try:
        for line in fileobject:
            print(line.rstrip('\n'))
    finally:
        fileobject.close()


def writelisttofile(path, ilist):
    fileobject = open(path, 'w')
    try:
        fileobject.writelines(ilist)
    finally:
        fileobject.close()


import zipfile


def listzipfilesinfo(path):
    z = zipfile.ZipFile(path, 'r')
    try:
        for filename in z.namelist():
            bytes = z.read(filename)
            print('File:%s Size:%s' % (unicode(filename, 'cp936').decode('utf-8'), len(bytes)))
    finally:
        z.close()


import os, fnmatch


def list_all_files(root, patterns='*', single_level=False, yield_folders=False):
    '''列出目录（或者及其子目录下的文件）'''
    # 分割模式到列表
    patterns = patterns.split(';')
    for path, subdirs, files in os.walk(root):
        if yield_folders:
            files.extend(subdirs)
        files.sort()
        for name in files:
            for pat in patterns:
                if fnmatch.fnmatch(name, pat):
                    yield '/'.join(unicode(os.path.join(path, name), 'cp936').split('\\'))
                    break
        if single_level:
            break


def swapextensions(root, before, after):
    if before[:1] != '.':
        before = '.' + before
    extensionlen = -len(before)
    if after[:1] != '.':
        after = '.' + after
    for path, subdirs, files in os.walk(root):
        for oldfile in files:
            if oldfile[extensionlen:] == before:
                oldfile = os.path.join(path, oldfile)
                newfile = oldfile[:extensionlen] + after
                os.rename(oldfile, newfile)




