#coding:utf-8


#re.match(pattern, string, flags=0)尝试从字符串的起始位置匹配一个模式，如果不是起始位置匹配成功的话，match()就返回none。

"""
pattern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。参见：正则表达式修饰符 - 可选标志

"""

import re


print(re.match('www', 'www.runoob.com').span())  # 在起始位置匹配,span()返回一个元祖
print(re.match('com', 'www.runoob.com'))         # 起始位置不匹配

"""
group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
groups()	返回一个包含所有小组字符串的元组，从 1 到 所含的小组号。
"""
line = "All Cats are smarter than dogs"

#下面的表达式表示：re.m匹配多行|re.I不区分大小写，(.*) are (.*?) .*表示匹配包含are的字符串，括号表示分组
matchObj = re.match(r'(.*) are (.*?) than (.*)', line, re.M | re.I)

if matchObj:
    print("matchObj.group(3) : ", matchObj.group())#默认是0，即取所有

    print("matchObj.group(1) : ", matchObj.group(1))#取are之前的值

    print("matchObj.group(2) : ", matchObj.group(2))#取are之后的值

else:
    print( "No match!!")



#re.search(pattern, string, flags=0)扫描整个字符串并返回第一个成功的匹配的索引区段。
# 匹配成功re.search方法返回一个匹配的对象，否则返回None。
"""
attern	匹配的正则表达式
string	要匹配的字符串。
flags	标志位，用于控制正则表达式的匹配方式，如：是否区分大小写，多行匹配等等。
"""
print(re.search('www', 'www.runoob.com').span())  # 在起始位置匹配
print(re.search('com', 'www.runoob.com').span())         # 不在起始位置匹配

#re.sub用于替换字符串中的匹配项。
#re.sub(pattern, repl, string, count=0, flags=0)
"""
pattern : 正则中的模式字符串。
repl : 替换的字符串，也可为一个函数。
string : 要被查找替换的原始字符串。
count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。
"""
phone = "2004-959-559 # 这是一个国外电话号码"

# 删除字符串中的 Python注释
num = re.sub(r'#.*$', "", phone)
print("电话号码是: ", num)


# 删除非数字(-)的字符串
num = re.sub(r'\D', "", phone)
print("电话号码是 : ", num)

#compile 函数用于编译正则表达式，生成一个正则表达式（ Pattern ）对象，供 match() 和 search() 这两个函数使用。
#re.compile(pattern[, flags])



#在字符串中找到正则表达式所匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表。
#findall(string[, pos[, endpos]])
"""
string : 待匹配的字符串。
pos : 可选参数，指定字符串的起始位置，默认为 0。
endpos : 可选参数，指定字符串的结束位置，默认为字符串的长度。
"""
pattern = re.compile(r'\d+')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
result2 = pattern.findall('run88oob123google456', 0, 10)

print(result1)
print(result2)

