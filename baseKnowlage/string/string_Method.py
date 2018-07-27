#coding:utf-8

#base string opeate

#rstrip()删除字符串末尾被指定的字符，默认是空格，如末尾有多个相同的字符，则一并删除
str1="djcc"
str2="adcd"
print("this's rstrip() function---------")
print(str1.rstrip("c"))
print(str1.rstrip("d"))


#replace()用新字符替换字符串中被指定的字符,str.replace(old, new[, max]),max表示替换多少个,如不指定，全部替换

str3="this is history,it is not fake"
print("this's replace function----------")
print(str3.replace("is","was"))
print(str3.replace("is","was",3))#索引从1开始，0不算

#









