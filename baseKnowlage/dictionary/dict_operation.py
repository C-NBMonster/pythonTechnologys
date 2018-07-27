#coding:utf-8

#字典操作

#遍历字典键
#F1
D = {'x':1, 'y':2, 'z':3,'d':4,'a':5}

print("F1:"+"=="*20)
for k in D:
    print(k,"=>",D[k])

#F2
print("F2:"+"=="*20)
print(D.items())
for k, v in D.items():
    print(k,"=>",v)

#F3
for v in D.values():
    print(v)


#字典的常用用途之一代替switch

#x = int(input("Enter the 1st number: "))
#y = int(input("Enter the 2nd number: "))


def operator(o="*",x=3,y=4):
    dict_oper = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y}
    return dict_oper.get(o)(x, y)
    #o = input("Enter operation here(+ - * /): ")
print("this's switch func:"+"***"*30)
print(operator("*"))

#假设有两个dictx和y，合并成一个新的dict，不改变x和y的值，例如
x = {'a': 1, 'b': 2}
y = {'b': 3, 'c': 4}

#期望得到一个新的结果Z，如果key相同，则y覆盖x。期望的结果是
z = {**x, **y} #Python3.5的语法
#python2-3.4
z = x.copy()
z.update(y)

#写函数合并多个字典
def merge_dicts(*dict_args):

    """
    Given any number of dicts, shallow copy and merge into a new dict,
    precedence goes to key value pairs in latter dicts.
    """
    result = {}
    for dic in dict_args:
        result.update(dic)
    return result

#合并两个字典的值，并去掉值中重复的值
#需要做到三件事：

#1. 将字符串转化为数值列表
#2. 合并两个列表并添加新的键值
#3. 去除重复元素

x={'a':'1,2,3','b':'2,3,4'}

#需要合并为：x={‘c':'1,2,3,4'}
x['c']=list(set(eval(x['a'])+eval(x['b'])))
del x['a']
del x['b']
print(x)








