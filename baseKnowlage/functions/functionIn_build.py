#coding=utf-8
from functools import reduce
"""
对象通过提供__call__(slef, [,*args [,**kwargs]])方法可以模拟函数的行为，如果一个对象x提供了该方法，
就可以像函数一样使用它，也就是说x(arg1, arg2...) 等同于调用x.__call__(self, arg1, arg2)。模拟函数的对象可以用于创建仿函数(functor) 或代理(proxy)
"""
#不是很明白说的什么！！！
class DistanceForm(object):
  def __init__(self, origin):
    self.origin = origin
    print("origin :"+str(origin))
  def __call__(self, x):
    print("x :"+str(x))
p = DistanceForm(100)
p(2000)

#dir列出指定对象或类的属性,方法
print("dir without arguments:", dir())
print("dddd",dir(DistanceForm))

#Python内置了一些非常有趣、有用的函数，如：filter、map、reduce，都是对一个集合进行处理，filter很容易理解用于过滤，map用于映射，reduce用于归并. 是Python列表方法的三架马车。
#filter函数的功能相当于过滤器。调用一个布尔函数bool_func来迭代遍历每个seq中的元素；返回一个使bool_seq返回值为true的元素的序列。python3中返回可迭代的对象
N=list(range(10))
print("filter:",list(filter(lambda x:x>5,N)))

#map函数func作用于给定序列的每个元素，并用一个列表来提供返回值。python3中返回可迭代的对象

N1=[1,2,3]
N2=[6,5,4]
print("map:",list(map(lambda x,y:x+y,N1,N2)))

#reduce函数，func为二元函数，将func作用于seq序列的元素，每次携带一对（先前的结果以及下一个序列的元素），
## 连续的将现有的结果和下一个值作用在获得的随后的结果上，最后减少我们的序列为一个单一的返回值。
#通俗点讲就是累加累减乘除什么的。
## reduce(function, sequence, starting_value)：对sequence中的item顺序迭代调用function，如果有starting_value，还可以作为初始值调用，
N=range(1,101)
print(reduce(lambda x,y:x+y,N,50))
N1=list(range(1,10))
print("filter:",list(filter(lambda x:x>5,N1)))
print("reduce1:",reduce(lambda x,y:x*y,range(1,5)))
#把上一步的结果变成一个阶乘列表
print("reduce2:",reduce(lambda m,n:m+n,map(lambda a:reduce(lambda x,y:x*y,range(1,a+1)),range(1,6))))
#用filter将100~200以内的质数过滤出来

print("filter2:",list(filter(lambda N:len(list(filter(lambda M:N%M==0,range(2,int(N**0.5)+1))))==0,range(100,201))))


#创建一个值为real + imag * j的复数或者转化一个字符串或数为复数。如果第一个参数为字符串，则不需要指定第二个参数。
complex(1,2)
complex("2")

#pow(x,y(z))函数返回以x为底，y为指数的幂。如果给出z值，该函数就计算x的y次幂值被z取模的值。
print("算",pow(2,4))

#divmod(x,y)函数完成除法运算，返回商和余数余数都为负数（元组类型），x,y同号，整商为正；异号，整商+1，且为负；任意一个数为负数，
print("divmod:","*"*20)
print(divmod(2,3))
print(divmod(-2,3))
print(divmod(2,-3))
print(divmod(-2,-3))

#round(x[,n])函数返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
print(round(3.556))#不指定则取整
print(round(3.457,1))

#min()函数返回给定参数的最小值，参数可以为序列。max同理
print("min:",min(1,2,3,0,4))
print("min list:",min([1,2,4],[1,2,]))

#callable()函数用于测试对象是否可调用，如果可以则返回1(真)；否则返回0(假)。可调用对象包括函数、方法、代码对象、类和已经定义了 调用 方法的类实例。
print("callable:",callable(chr))

#isinstance(object,class-or-type-or-tuple)
str1= "dd"
print(isinstance(str1,str))






























