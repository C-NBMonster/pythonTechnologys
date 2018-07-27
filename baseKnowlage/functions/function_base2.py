#coding:utf-8
#Python中实现结构相似的函数调用方法,本文讲解使用dict和lambda结合实现结构相似的函数调用,给出了不带参数和带参数的实例

#不带参数
msgCtrl = "1 : pause\n2 : stop\n3 : restart\nother to quit\n"

ctrlMap = {
    '1': lambda: doPause(),
    '2': lambda: doStop(),
    '3': lambda: doRestart()}


def doPause():
    print('do pause')

def doStop():
    print('do stop')

def doRestart():
    print('do restart')

while True:
    print(msgCtrl)
    cmdCtrl = input('Input : ')
    if cmdCtrl not in ctrlMap.keys(): break #如果传入的值不在键列表中，则中断循环
    ctrlMap[cmdCtrl]()

#带参数
msgCtrl = "1 : +\n2 : -\n3 : *\nother to quit\n"

ctrlMap = {
    '1': lambda x,y: x+y,
    '2': lambda x,y: x-y,
    '3': lambda x,y: x*y}

while True:
    print(msgCtrl)
    cmdCtrl = input('Input : ')
    if cmdCtrl not in ctrlMap.keys(): break #如果传入的值不在键列表中，则中断循环
    print(ctrlMap[cmdCtrl](8,4),"\n")


#默认参数允许创建函数可选的参数。如果没有传入值的话，在函数运行前，参数就被赋了默认值。
















