#coding:utf-8

#base string opeate

#取第几个、第某几个字符
print("Hello"[0])#表示输出字符串中第一个字符
print("Hello"[-1])# 表示输出字符串中最后一个字符
print("Hello"[-3:])#表示从字符串最后一个字符开始，连取三个字符作为输出
print("Hello"[1:3])#从字符串的1位置开始，取两个字符作为输出

#几种特殊情况
print("Hello"[0:])#从第一个字符开始截取，一直截取到最后
print("Hello"[:])#同上

#查找字符的索引值
strs = "abcdefg"
strg = "abcdrfg"
print(strs.index("d"))
#获取内存地址
print(id(strs))
#获取字符串长度
print(len(strs))
#返回最大值
print(max(strs))
#返回最小值
print(min(strs))
#大小比较,python3.x没有cmp，需要引入operator模块
import operator
print(operator.eq(strs,strg))

#返回某个字符所对一个的 ASCII 值（是十进制的）
print(ord("a"))
#把 ASCII 值（是十进制的）转换为所对一个的字符
print(chr(97))

#判断是否全为字母，返回布尔值
print("python".isalpha())
#判断是否全为字母和数字，返回布尔值
print("python3.6".isalnum())
#判断是否全为空白（空格），返回布尔值
print("python ".isspace())
#判断是否全为数字，返回布尔值
print("python".isdigit())

#根据某个分隔符分割字符串，分割之后是一个列表数据
stra="aacddcsdfcgh"
print(stra.split("c"))
print(stra.split("c",2))#2表示分割两次，结果是[aa,dd,sdfc],
print('  abcbdbee  '.split())  # --> ['abcbdbee']    //未指定Sep，返回仅包含一个元素的列表，舍弃str两端的空格
print('  abcbdbee '.split('f'))  # --> ['  abcbdbee ']    //指定f为Sep（虽然找不到f），返回仅包含一个元素的列表，保留两端的空格

#去掉字符串两侧的空格strip(),lstrip(),rstrip()
print(stra.strip())

#将字符串全部转为大写
print("beatiful".upper())
#将字符串全部转为小写
print("Beatiful".lower())
#大小写转换
print('大小写转换：' + stra.swapcase())
#首字母大写
print("beatiful asome".capitalize())

#判断是否全为大写
print("Beatiful".isupper())
#判断是否全为大写
print("beatiful".islower())

#将每个单词的首字母改为大写
tt = "not a simple fuck was given"
print(tt.title())
#判断每个单词的首字母是否大写
print(tt.istitle())


# startswith()方法检查字符串是否以str开始，任选限制匹配与给定索引的开始和结束
#语法：str.startswith(str, beg=0,end=len(string));返回布尔值,后面两个是指定的检索位置
#同理有：str.endswith(str, beg=0,end=len(string))
str = "this is string example....wow!!!"
print(str.startswith( 'this' ))
print(str.startswith( 'is', 2, 4 ))
print(str.startswith( 'this', 2, 4 ))

str1 = "this is string example....wow!!!"
str2 = "is"

# rindex()方法返回所在的子str被找到的最后一个索引，后面两个参数是搜索的起始位置
#如果指定字符有多个，返回的是第一个字母的index
print(str1.rindex(str2))
print(str1.index(str2))


#对齐
# ljust() 方法返回一个原字符串左对齐,并使用空格填充至指定长度的新字符串。如果指定的长度小于原字符串的长度则返回原字符串。
#str.ljust(width[, fillchar]),指定宽度字符串，若长度小于原字符串长度，则显示原字符串，否则，用后面指定的字符串填满，默认是空格，指定字符串可选填
s = 'Yes! This is a string'
print("左对齐：" + s.ljust(len(s)+6,"*"))
print("右对齐：" + s.rjust(len(s)+6,"*"))
print("居中对齐：" + s.center(len(s)+6,"*"))

#查找字符函数
#print s.find('is')#返回S中出现substr的第一个字母的标号，如果S中没有substr则返回-1。start和end作用就相当于在S[start:end]
#如何find括号中的是形参，找到返回0，找不到返回-1
print(s.find('is',0,len(s)))#找到返回该字符的标号
seq2 = "a"
s.find(seq2)#找到返回0，找不到返回-1

#rfind()与find一样，只不过查找的顺序是从右边开始
#如果查找的是多字符，如：aa，则返回第一个字符的索引位置
print(s.rfind("a"))

##计算substr在S中出现的次数
print(s.count('s',0,len(s)))
## 方法把字符串中的 tab 符号('\t')转为空格，tab 符号('\t')默认的空格数是 8。
str = "this is\tstring example....wow!!!"
print ("原始字符串: " + str)
print ("替换 \\t 符号: " +  str.expandtabs())
print ("使用16个空格替换 \\t 符号: " +  str.expandtabs(16))

#拼接字符串，join
#把seq代表的序列──字符串序列，用S连接起来,运行看效果
s1 = "-"
s2 = ""
seq = ("r", "u", "n", "o", "o", "b") # 字符串序列
print (s1.join( seq ))
print (s2.join( seq ))

#另外，一个连续输出的小技巧
print('=?' * 10)

#字符串替换
print(s.replace("is","was",1))#需要被替换子字符串，用来替换的字符串，替换次数

#S.splitlines([keepends])
#按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。该方法多用于处理文件
print('ab c\n\nde fg\rkl\r\n'.splitlines())
print('ab c\n\nde fg\rkl\r\n'.splitlines(True))

#字符串映射
#Str.maketrans(from, to)
#返回一个256个字符组成的翻译表，其中from中的字符被一一对应地转换成to，所以from和to必须是等长的。
#如果有三个参数，则第三个参数的意思是删除原字符串中的相应字符。
#String.maketrans(from, to)
#S.translate(table[, deletechars])
# 使用上面的函数产后的翻译表，把S进行翻译，并把deletechars中有的字符删掉。需要注意的是，如果S为unicode字符串，那么就不支持 deletechars参数，
# #可以使用把某个字符翻译为None的方式实现相同的功能。此外还可以使用codecs模块的功能来创建更加功能强大的翻译表。
intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)

str = "this is string example....wow!!!"
print(str.translate(trantab))

#maketrans制定规则，translate应用规则

#字符串还有一对编码和解码的函数：
#S.encode([encoding, [errors]])
# 其中encoding可以有多种值，比如gb2312 gbk gb18030 bz2 zlib big5 bzse64等都支持。errors默认值为"strict"，意思是UnicodeError。
# #可能的值还有'ignore', 'replace', 'xmlcharrefreplace', 'backslashreplace' 和所有的通过codecs.register_error注册的值。这一部分内容涉及codecs模块，不是特明白
#S.decode([encoding, [errors]])
tgb = s.encode("gb2312","strict")
print("tgb:",tgb)
print(tgb.decode("utf-8","strict"))

#str.zfill(width)返回一个长度为width的数字字符串，最左边填充0。如果width小于等于原字符串长度，则返回原字符串。主要用于数字类字符串的格式化。
print('abc'.zfill(5))  # --> '00abc'    //一般不会做这种格式化，没什么意义
print('123'.zfill(4))  # --> '00123'


#拆分 & 组合类方法：

#str.partition()返回一个元组，而且分隔符Sep是元组中的一个元素；而str.split(0返回一个列表，分隔符Sep不在列表中
#str.partition(sep)：
#该方法用于拆分字符串，返回一个包含三个元素的元组。如果未能在原字符串中找到Sep，则元组的三个元素为：原字符串，空串，空串；
#否则，从原字符串中遇到的第一个Sep字符开始拆分，元组的三个元素为：Sep之前的字符串，Sep字符，Sep之后的字符串；如
print('abcdee'.partition('f'))   #--> ('abcdee', '', '')
print('abcdeehedjke,fad'.partition('e'))  # --> ('abcd', 'e', 'e')

#str.rpartition(sep)：同理






