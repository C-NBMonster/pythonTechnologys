#coding:utf-8
#创建字典的5种方法
#1，
dict = {'ob1':'computer', 'ob2':'mouse', 'ob3':'printer','ob4':'sreen'}
dict2 = {'o1':'computer', 'o2':'mouse', 'o3':'printer','o4':'sreen'}

#2，
dic={}
dic['name']='mirror'
#D.get(key, default)       #同dict[key]，键不存在时，返回设定的值
print(dict.get("ob4","键值不存在！"))

#代码比较少，但键必须为字符串型。常用于函数赋值
D3 = dict(name='Bob', age=45)
print("creatDict3:",D3)

#4,dict--键值序列
## 如果需要将键值逐步建成序列，则此方式比较有用,常与zip函数一起使用
D4 = dict([('name', 'Bob'), ('age', 40)]) #D = dict(zip(('name','bob'),('age',40)))

#5
#fromkeys方法使用给定的键建立新的字典，每个键默认对应的值为None，可以直接在所有字典的类型dict上调用此方法。如果不想使用默认值，也可以自己提供值。

dt=dict.fromkeys(['name','age','sex','tall'],)
print("{}.fromkeys:",dt)
dc={}.fromkeys(['name','age','sex','tall'],'mirror')#只能接受一个默认参数设置
print("{}.fromkeys,default:",dc)

#d.has_key(key)判断是否有该键，有，返回true，无，false.Python3使用in来代替
print("ob3" in dict)

#返回字典键的列表,类型是dict_keys,可直接转为列表
t =list(dict.keys())
print(t)

#以列表的形式返回字典中的值，返回值的列表中可包含重复元素,可直接转为列表
v = list(dict.values())
print(type(v),v)

#D.items()   #将所有的字典项以列表方式返回，这些列表中的每一项都来自于(键,值),但是项在返回时并没有特殊的顺序
all = dict.items()
print(type(all),all)


#增加合并字典d.update(d2)，将d2合并到d中,结果是无序的
dict.update(dict2)
print("字典合并：",dict)

#随机返回并删除字典中的一对键和值(一般删除末尾对)
#如果字典已经为空，却调用了此方法，就报出KeyError异常。
pop_obj=dict.popitem()
print(pop_obj)
print(dict)
#pop(key)
#删除指定键的值，并返回该值。如键不存在，则提示keyerror
print("pop",dict.pop("ob1"))

#清空字典，同del dict
delD = {'1':'22','2':"33"}
delD.clear()
print("字典被清空了",delD)

#复制

#copy的参考：http://www.jb51.net/article/57917.htm
import copy
dc = dict #dict的引用
cd = copy.copy(dict)#两个独立的对象，但都指向相同的子对象，也就是指向相同的值，值变，一起变
dd = copy.deepcopy(dict)#两个没关系的对象，改变其中一个，另外一个不会改变。

#cmp(dict1, dict2)如果两个字典的元素相同返回0，如果字典dict1大于字典dict2返回1，如果字典dict1小于字典dict2返回-1。python3没有cmp函数，用operator模块进行操作
dict1 = {'Name': 'e', 'Age': 30, 'Addr':'hust'}
dict2 = {'Name': 'z', 'Age': 27, 'Adds':'hust'}
import operator as op
print("字典大小比较",op.eq(dict1,dict2))


##########################################################################################
##########################################################################################
#字典内置方法


#setdefault方法在某种程度上类似于get方法，就是能够获得与给定键相关联的值，还能在字典中不含有给定键的情况下设定相应的键值
d={}
print("d.setdefault1：",d.setdefault("name","this's name"))#不存在，则赋值
print("d.setdefault2：",d.setdefault("name","name"))#存在，返回该键值指向的值

#oldd.update(excd)将字典excd添加到字典oldd中，如果有相同的键值，则覆盖原有的值
oldd = {'a':1,'b':2,'c':3}
excd = {'a':5,'d':6}
oldd.update(excd)
print("dict.update:",oldd)












