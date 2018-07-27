#coding:utf-8

slist = ['a','b',0,1,3]

#追加元素，在不确定定义的列表长度的时候，用这个，否则容易出错
slist.append("df")
print("append:",slist)
#将对象插入到指定位置,如指定索引超出原列表长度，则在列表末尾天加
aList = [123, 'xyz', 'zara', 'abc']
aList.insert(2, 2009)
print("Final List : ", aList)

#pop() 函数用于移除列表中的一个元素（默认最后一个元素），并且返回该元素的值,也可删除指定位置索引的值
aList = [123, 'xyz', 'zara', 'abc']
print(aList.pop(1))
print(aList)

# 用于移除列表中某个值的第一个匹配项。
#list.remove(obj)
aList = [123, 'xyz', 'zara', 'abc', 'xyz']
aList.remove('xyz')
print("remove:",aList)

#该元素在列表中出现的个数
#str.count(sub, start= 0,end=len(string))
str = "this is string example....wow!!!"
sub = "i"
print("str.count(sub, 4, 40) : ", str.count(sub, 4, 40))
sub = "wow"
print("str.count(sub) : ", str.count(sub))

#Python index() 方法检测字符串中是否包含子字符串 str ，如果指定 beg（开始） 和 end（结束） 范围，
# 则检查是否包含在指定范围内，该方法与 python find()方法一样，只不过如果str不在 string中会报一个异常。
#str.index(str, beg=0, end=len(string))
str1 = "this is string example....wow!!!"
str2 = "exam"
print(str1.index(str2))
print(str1.index(str2, 10))
#print(str1.index(str2, 40)) #编译不过，提示错误找不着子字符串

#L.extend(list)  #追加list，即合并list到L上，L末尾加上
list1 = ['Google', 'Runoob', 'Taobao']
list2 = list(range(5)) # 创建 0-4 的列表
list1.extend(list2)  # 扩展列表
print("扩展后的列表：", list1)

#排序
print(list1.sort())
#倒叙
print(list1.reverse())




































