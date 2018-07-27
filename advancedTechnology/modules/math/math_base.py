#coding:utf-8

"""
math中的函数不可以用于太过复杂的数的运算, 如果需要复杂数的运行最好使用cmath模块中同名函数,
如果想要更加高级的数学功能，可以考虑选择标准库之外的numpy和scipy模块，它们不但支持数组和矩阵运算，还有丰富的数学和物理方程可供使用

"""

import math

print("常量PI：",math.pi)
print("常量E：",math.e)
print("math.ceil(x) : 对x向上取整，返回最小整数值大于或者等于x:",math.ceil(324.45))
print("math.floor(x) : 对x向下取整, 返回整数值小于或者等于x:",math.floor(324.55))
print("math.pow(x,y) : 指数运算，得到x的y次方:",math.pow(2,4))
print("math.log(x[, base]) : 对数运算，默认基底为e的对数运算。使用base参数时，改变对数的基底, 变为以base为底的对数运算:",math.log(10),math.log(8,2))
print("math.sqrt(x) 平方根计算:",math.sqrt(9))
print("math.fabs(x) 取绝对值:",math.fabs(-23))
print("math.factorial(x) 求阶乘, 即x!:",math.factorial(4))
print("math.exp(x) 求e的x次方:",math.exp(3))

"""
三角函数
以下函数都接收一个弧度(radian)为单位的x作为参数
math.acos(x) #求arccos(x)
math.asin(x) #求arcsin(x)
math.atan(x) #求arctan(x)
math.cos(x)  #求cos(x)
math.sin(x)  #求sin(x)
math.tan(x)  #求tan(x)

math.degrees(x) 角度制转化为弧度制
math.radians(x) 弧度制转化为角度制
math.sinh(x), math.cosh(x), math.tanh(x), math.asinh(x), math.acosh(x), math.atanh(x)
还有些函数基本没用过
"""
print("math.degrees(x) 角度制转化为弧度制",math.degrees(math.pi / 2))



























