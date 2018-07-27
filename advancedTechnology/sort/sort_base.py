#coding:utf-8

#map(funcname, list)
#python的map 函数使得函数能直接以list的每个元素作为参数传递到funcname中, 并返回相应的新的list。元祖也是可以的，字典不行

ls = [1,3, 5,7,9]
def sq(x):
  return x*x
re = map(sq,ls) #返回的是一个对象
for e in re:
  print(e)


#在需要对list中的每个元素做转换的时候, 会很方便
#比如,把list中的每个int 转换成str
map(str, [23,43,4545,324]) #['23', '43', '4545', '324']


#reduce(funcname, list)，Python3中不是内置函数
#与map相比 , reduce类似于一个聚合类的应用方法, 把list中的参数, 依次传递给funcname, 每次funcname的参数都是上个funcname 执行结果和下一个list中的元素,
# 所以, funcname 的 参数必须是两个. 从执行过程看, 有点像递归
from functools import reduce
def c_sum(x, y):
  return x + y
reduce(c_sum, range(1,101)) #5050


# filter(funcname, list)
# 执行过程依次将list中的元素传递到funcname函数中, 根据funcname返回的True或False 保留或丢弃元素
# 例: 返回某个list中的所有int数据
def is_int(x):
    if isinstance(x, (int)):
        return True
    else:
        return False
ob = filter(is_int, ["Yi", 2, "3", 4])  # [2, 4]
ls = []
for i in ob:
    ls.append(i)
print(ls)

#sorted( list, [comp_func]) #sorted(data, key=None, reverse=False) cmp带两个参数的比较函数，key是一个参数
#排序方法, 第二个是可选参数, 根据可选参数返回的值, 对结果进行排序, comp_func 接受两个参数(x, y), 最终返回的结果应该是-1.0,1,
# 如果返回的是-1, 表示x<y , 0表示x=y, 1表示x>y, 所以, 实际的排序可以自定义
#默认是正序排序:
ls1 = [3,4, 12, 5, 9, 1]
ls2 = [3,4, 12, 5, 9, 1]
ls1.sort() #原址排序 sort(func) func -- 这是一个可选参数，如果有将使用该函数，对列表中的对象进行排序
print(ls1)

#copy副本1
ls3=ls1[:] #把ls1的元素给ls3，

#copy副本2
ls4 = sorted(ls1) #返回一个排好序的副本

#倒序
ls2.sort(reverse=True)
print(ls2)
#operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号。
students = [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10),]
xx=sorted(students, key=lambda student : student[2])  # sort by age
print("xx:",xx)
from operator import itemgetter,attrgetter
y = sorted(students,key=itemgetter(2))
print(y)

#用 operator 函数进行多级排序(对于多为数据)
x = sorted(students,key=itemgetter(0,1,2))#个数为对应上面列表中元祖的个数
print(x)

#对字典排序
t = {'data1': 3, 'data2': 1, 'data3': 2, 'data4': 4}
print(sorted(t.items(), key=itemgetter(0), reverse=True))

















