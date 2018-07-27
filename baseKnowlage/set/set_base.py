#cod:utf-8
""""
set是一个无序且不重复的元素集合。
集合对象是一组无序排列的可哈希的值，集合成员可以做字典中的键。集合支持用in和not in操作符检查成员，由len()内建函数得到集合的基数(大小)， 用 for 循环迭代集合的成员。
但是因为集合本身是无序的，不可以为集合创建索引或执行切片(slice)操作，也没有键(keys)可用来获取集合中元素的值。
set和dict一样，只是没有value，相当于dict的key集合，由于dict的key是不重复的，且key是不可变对象因此set也有如下特性：
不重复
元素为不可变对象
"""

s = set()
s = {11,22,33,44}  #注意在创建空集合的时候只能使用s=set()，因为s={}创建的是空字典

#定义
a=set('boy') #字符串
b=set(['y', 'b', 'o','o'])#列表
c=set({"k1":'v1','k2':'v2'})#字典
d={'k1','k2','k2'}
e={('k1', 'k2','k2')}#元组
print(a,type(a))
print(b,type(b))
print(c,type(c))
print(d,type(d))
print(e,type(e))

#比较
se = {11, 22, 33}
be = {22, 55}
temp1 = se.difference(be)        #找到se中存在，be中不存在的集合，返回新值
print("difference:",temp1)        #{33, 11}
print(se)        #{33, 11, 22}

temp2 = se.difference_update(be) #找到se中存在，be中不存在的集合，覆盖掉se（去掉公共部分）
print("difference_update",temp2)        #None
print(se)           #{33, 11}

#删除
se = {11, 22, 33}
se.discard(11)
se.discard(44)  # 移除不存的元素不会报错
print("discard",se)

se = {11, 22, 33}
se.remove(11)
#se.remove(44)  # 移除不存的元素会报错,3.6报了
print("remove:",se)

se = {11, 22, 33}  # 移除末尾元素并把移除的元素赋给新值
temp = se.pop()
print("pop",temp)  # 33
print(se) # {11, 22}


#取交集
se = {11, 22, 33}
be = {22, 55}

temp1 = se.intersection(be)             #取交集，赋给新值
print("intersection,交集：",temp1)  # 22
print(se)  # {11, 22, 33}

temp2 = se.intersection_update(be)      #取交集并更新自己
print("intersection_update,",temp2)  # None
print(se)  # 22
#判断
se = {11, 22, 33}
be = {22}

print(se.isdisjoint(be))        #False，判断是否不存在交集（有交集False，无交集True）
print(se.issubset(be))          #False，判断se是否是be的子集合
print(se.issuperset(be))        #True，判断se是否是be的父集合

#合并
se = {11, 22, 33}
be = {22}

temp1 = se.symmetric_difference(be)  # 合并不同项(讲两个集合中的不同项合并成一个集合)，并赋新值
print("合并，symmetric_difference",temp1)    #{33, 11}
print(se)       #{33, 11, 22}

temp2 = se.symmetric_difference_update(be)  # 合并不同项，并更新自己
print("symmetric_difference_update",temp2)    #None
print(se)       #{33, 11}


#取并集
se = {11, 22, 33}
be = {22,44,55}

temp=se.union(be)   #取并集，并赋新值
print(se)       #{33, 11, 22}
print("并集，union",temp)     #{33, 22, 55, 11, 44}

#更新
se = {11, 22, 33}
be = {22,44,55}

se.update(be)  # 把se和be合并，得出的值覆盖se
print(se) #{33, 22, 55, 11, 44}
se.update([66, 77])  # 可增加迭代项
print(se) #{33, 66, 22, 55, 11, 44, 77}

#集合的转换
se = set(range(4))
li = list(se)
tu = tuple(se)
st = str(se)
print(li,type(li)) #[0, 1, 2, 3] <class 'list'>
print(tu,type(tu)) #(0, 1, 2, 3) <class 'tuple'>
print(st,type(st)) #{0, 1, 2, 3} <class 'str'>



