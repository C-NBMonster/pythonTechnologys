#coding:utf-8

#字符串应用例子

#实现查找两个字符串中相同字符并输出的方法
#思想：遍历，使用in判断共存关系，append到列表输出
seq1="abcdefg"
seq2="abcdefghijk"
con = []
def conmon_str1_str2(str1,str2):
    for s in seq1:
        if s in seq2:
            con.append(s)
    return con
print(conmon_str1_str2(seq1,seq2))

#字符串转换成摩斯码
chars = ",.0123456789?abcdefghijklmnopqrstuvwxyz"
codes = """--..-- .-.-.- ----- .---- ..--- ...-- ....- ..... -.... --... ---..
      ----. ..--.. .- -... -.-. -... . ..-. --. .... .. .--- -.- .-.. --
      -. --- .--. --.- .-. ... - ..- ...- .-- -..- -.-- --.."""
keys = dict(zip(chars, codes.split()))
def char2morse(char):
  return keys.get(char.lower(), char)
print(' '.join(char2morse(c) for c in 'SOS'))

#将"2011-09-28 10:00:00"转化为时间戳
import time
#转为时间戳
a = "2011-09-28 10:00:00"
time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))

#将时间戳转换为时间
x = time.localtime(1317091800.0)
time.strftime('%Y-%m-%d %H:%M:%S',x)


#字符串替换
s = 'abcd'
a = ["a", "b", "c"]
b = ["c", "d", "e"]

s2=s.translate(str.maketrans(''.join(a),''.join(b)))
print(s)
print(s2)
#格式化
print("{name} is {age}".format(name="bob",age="15"))







