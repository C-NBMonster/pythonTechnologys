#coding:utf-8

import random

print("用于生成一个0到1的随机符点数: 0 <= n < 1.0:",random.random())#用于生成一个0到1的随机符点数: 0 <= n < 1.0
print("用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限",random.uniform(3,6))#uniform(a,b)如果a > b，则生成的随机数n: a <= n <= b。如果 a <b， 则 b <= n <= a
print("用于生成一个指定范围内的随机符点数，两个参数其中一个是上限，一个是下限",random.uniform(6,3))
print("用于生成一个指定范围内的整数。其中参数a是下限，参数b是上限",random.randint(-3,-1))#randin(a,b)要求a必须小于1，否则报错。值可为负数
print("从指定范围内，按指定基数递增的集合中 获取一个随机数",random.randrange(10, 100, 2)) #random.randrange([start], stop[, step]),在结果上与 random.choice(range(10, 100, 2) 等效
print("从序列中获取一个随机元素。其函数原型为：random.choice(sequence)",random.choice(["JGood", "is", "a", "handsome", "boy"]))

list1 = [1, 2, 3, 4, 5]
#随机选取
print(random.choice(list1))
#随机打乱，改变原来列表的值
random.shuffle(list1)
print("随机打乱shuffle",list1)

#打乱列表a里元素的顺序,随机取3个元素
ab=[1,2,3,4,5]
print(random.sample(ab,3))


