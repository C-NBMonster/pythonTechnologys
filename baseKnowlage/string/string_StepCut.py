#coding:utf-8

#step cut

#步长截取
str="abcdefg"
print(str[::2])#表示从第一个字符开始截取，间隔2个字符取一个，第一个也算。
print(str[1::2])
print(str[::-1])


#只要不是字母和数字的就会被分割开来。\w表示所有大小写字母，数字
import re
DATA = "Hey, you - what are you doing here! welcome to jb51?"
print(re.findall(r"[\w']+", DATA))


