#coding:utf-8

#base string opeate

#python中的字符串用单引号''和双引号""标示
strA = 'this is a string'
strB = "this is a message!"
#打印两个字符串
print("打印两个字符串")
print('strA = ' + strA)
print('strB = ' + strB)
print("#############################")
strC = 'I don\'t know anything'
strD = '\'Yes\',I know.'
print("字符串中的转义字符")
print('strA = ' + strC)
print('strB = ' + strD)
print("#############################")
strE = '这是我的blog，欢迎大家来\n我的博客溜达'
print("字符串中的换行")
print('strA = ' + strE)
print("#############################")
strF = 'this is ''message'
strG = 'Hongten'
strH = strG * 3
print('字符串可以用\'+\'号连接(或者说粘合)，也可以用\'*\'号循环')
print('strF原有形式为：\'this is \'\'message\'')
print('粘合后的strF：' + strF)
print('strG原值为：\'Hongten\',strH = strG * 3,此时strH为：' + strH)
print("#############################")
strI = 'hongtenzone@foxmail.com'
print('字符串可以使用下标(索引)查询')
print('源字符串strI = \'hongtenzone@foxmail.com\'')
print('字符串strI的长度，len(strI) = ')
print(len(strI))
print('strI[0] = ' + strI[0])
print('strI[10] = ' + strI[10])
print('strI[-1] = '+strI[len(strI) - 1])
print('strI[-1] = ' + strI[-1])
print('strI[len(strI) - 1] = ' + strI[len(strI) - 1])
print("#############################")
print('Python 字符串不能改写。按字符串索引赋值会产生错误:')
print('strI[0] = \'x\',这样就会产生错误啦')
print("#############################")
print('过大的索引代替为字符串大小，下界比上界大的返回空字符串')
print('strI[0:100] = ' + strI[0:100])
print("#############################")
print('索引可以是负数，计数从右边开始')
print('strI[-2] = ' + strI[-2])
print('strI[-23:] = ' + strI[-23:])
print("#############################")
print('不过-0 还是0，所以它不是从右边计数的！')
print('strI[0] = ' + strI[0])
print('strI[-0] = ' + strI[-0])