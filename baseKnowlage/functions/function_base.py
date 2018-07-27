#coding:utf-8
import multiprocessing as mp
#函数

# 函数定义4种方式
#1， F(arg1,arg2,…)这是最常见的定义方式，一个函数可以定义任意个参数，每个参数间用逗号分割，用这种方式定义的函数在调用的的时候也必须在函数名后的小括号里提供个数相等
#的值（实际参数），而且顺序必须相同，也就是说在这种调用方式中，形参和实参的个数必须一致，而且必须一一对应，也就是说第一个形参对应这第一个实参。
def myAbs(x):
    if x >= 0:
        return x
    else:
        return -x
a = 10
myAbs(a)

def nop():  # 空函数
    pass #什么都不做，用作占位符

#返回多个值
import math
#. F(arg1,arg2=value2,…)
#这种方式就是第一种的改进版，提供了默认值，有默认值的形参要放在没有默认值的形参之后
def move(x, y, step, angle = 0):
     nx = x + step * math.cos(angle)
     ny = y - step * math.sin(angle)
     return nx, ny
print(move(3,5,1))

#.3， F(*arg1)
#上面两种方式是有多少个形参，就传进去多少个实参，但有时候会不确定有多少个参数，则此时第三种方式就比较有用，它以一个*加上形参名的方式来表示这个函
#数的实参个数不定，可能为0个也可能为n个。
# 注意一点是，不管有多少个，在函数内部都被存放在以形参名为标识符的元组中。
#,arg1为dick类型时将键传递给函数
def func(*args):
    print(args)
print("函数不定参数:",func(1,2,3,4))


#4,形参名前加两个*表示，参数在函数内部将被存放在以形式名为标识符的dictionary中，
## 这时调用函数的方法则需要采用arg1=value1,arg2=value2这样的形式
#传入的参数为以字典形式存在kwargs中
def func2(**kwargs):
    print(kwargs)


print("传入的参数为以字典形式存在kwargs中:",func2(b=2,c=5,d="dd")) #竟然返回None。。。郁闷

def test(a,b,c,d,e):
    print(a,b,c,d,e)

y = {'a': 1, 'c': 6, 'b': 2, 'e': 1, 'd': 1}
test(*y)#将键传递给函数，传的是key值
test(**y)#将值传递给函数#这种函数处理方式等价于a = y['a'] b = y['b']


#Python 函数的参数传递时，值得注意的是参数传入时若为变量会被当作临时赋值给参数变量（值不会改变），如果是对象则会被引用(值会改变)。################################
def testpara(p1, p2):
    p1 = 10
    p2.append('hello')
l = []  # 定义一数组对像
a = 20  # 给变量a赋值
testpara(a, l)  # 变量a与对象数组l作为参数传入
print(a)  # 打印运行参数后的值
for v in l:  # 打印数组对象的成员
    print("l:",v)

#20  # 调用函数后a变量并未被复值
#hello  # 而对象l数组则增加成员hello



#温度转换
"""
def convertTemp(temp, scale):
  if scale == "c":
   return (temp - 32.0) * (5.0/9.0)
  elif scale == "f":
   return temp * 9.0/5.0 + 32
temp = int(input("Enter a temperature: "))
scale = input("Enter the scale to convert to: ")
converted = convertTemp(temp, scale)
print("The converted temp is: %d" %converted)
"""

#列表,元祖作为形参对象
def my_fuc(*b):
    print(b)

atuple = (30, 10)
alist = ['Hello', 'World!']
alist2 = ['I am', 'Mirror!']
#mp.Pool.apply(my_fuc, atuple)
#mp.Pool.apply(my_fuc, alist)
my_fuc(*atuple)
my_fuc(*alist)
my_fuc(*alist+alist2)

















