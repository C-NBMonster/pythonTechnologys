#coding:utf-8

import itertools

#-----------------------------------------------------
"""
itertools.accumulate(iterable[, func]) 
返回累计的和，参数可以是任何类型，包括小数或者分数的增加， 
如果提供了可选的功能参数，它应该是两个参数的函数，它将替代加法 
简而言之就是： 
如果一个list对象是list=[p0,p1,p2,p3,p4],那么通过itertools.accumulate() 
返回的结果就是[p0,p0+p1,p0+p1+p2,p0+p1+p2+p3,p0+p1+p2+p3+p4] 
"""
d=[6,21,5,3,4,8,62,54,12,0]
de=iter(d)#这个不知道什么作用
print("accumulate:",list(itertools.accumulate(d)))
#-----------------------------------------------------

#-----------------------------------------------------
"""
itertools.chain(*iterables) 
使返回元素从第一个直到筋疲力尽的迭代器，然后继续下一个，直到所有的可迭代对象枯竭。用于连续序列作为一个单一序列
"""
partlist1= 'ABC'
partlist2= 'DEF'
partlist3= 'GHI'
print("chain:",list(itertools.chain(partlist1,partlist2,partlist3)))#['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I'] 拆分再链接成列表
#-----------------------------------------------------



#-----------------------------------------------------
"""
itertools.combinations(iterable, r) 
返回r长度的子序列的元素输入迭代器，组合的字典排序顺序发出， 
所以如果输入迭代器进行排序，结合会产生元组排序，每个元素都是基于他们位置的独特元素，并不是按照他们的价值 
所以如果输入元素是独一无二的，每个组合中都没有重复的值 
"""
partlist1='1234'
print("combinations:",list(itertools.combinations(partlist1,2)))
#[('1', '2'), ('1', '3'), ('1', '4'), ('2', '3'), ('2', '4'), ('3', '4')]
#从结果可以看出，该函数作用是返回各个r长度的元素，而结果元素是有
#原来的list中的元素组合而成，组合的规律是原list中每个元素与其后的元素组合。

print("combinations_with_replacement:",list(itertools.combinations_with_replacement('ABCD', 2))) #combinations_with_replacement 与combinations一样，只不过，从本身开始组合
#-----------------------------------------------------



#-----------------------------------------------------
"""
itertools.compress(data, selectors) 
通过选择器selectors对data进行筛选，随后只返回那先经过selectors判断为true的data 
"""
partlist1='1234'
print(list(itertools.compress(partlist1,[1,1,1,0])))#这个有意思了。。。
#-----------------------------------------------------


#-----------------------------------------------------
"""
itertools.count(start, step) 
从start开始，以后每个元素都加上step。step默认值为1。 
count(10) –> 10 11 12 13 14 … 
建议大家千万别用这个函数来测试，别问我为什么，我已经重启了五次了。
"""
i = 0
for item in itertools.count(100):   #返回的是一个对象，需要遍历
    if i>10:
        break
    print(item)
    i = i+1
#-----------------------------------------------------

#-----------------------------------------------------
"""
功能：从列表中取元素，到列表尾后再从头取...感觉好蛋疼！！！
无限循环，因为cycle生成的是一个无界的失代器
"""
listone = ['a', 'b', 'c']
listtwo = ['11', '22', 'abc']
i = 0
for item in itertools.cycle(listone):
    print(item)
    i = i +1
    if i > 10:
        break

#-----------------------------------------------------
"""
itertools.dropwhile(predicate, iterable)/itertools.takewhile(predicate, iterable) 
从函数的名字就可以知道，predicate是判断条件，当predicate是true的时候迭代器中的参数都扔掉，一直到 
predicate是false的时候，输出余下的所有内容（不在判断余下的参数） 
"""
partlist1=[1,2,3,4,8,1]
print(list(itertools.dropwhile(lambda x:x<3,partlist1))) #从索引0开始，遇到不符合条件停止查询，返回不符合条件后面的元素结果，takewhile想反
#-----------------------------------------------------


"""
itertools.filterfalse(predicate, iterable) 
输出predicate为false的所有数据 
"""
partlist1=[1,2,3,4,8,1]
print(list(itertools.filterfalse(lambda x:x<3,partlist1)))  #
#[3,8,4]就是找出所有的叛徒为止



#groupby(iterable[, keyfunc])
#把迭代器中相邻的重复元素挑出来放在一起
for key, group in itertools.groupby('AAABBBCCAAA'):
    print(key, list(group))  #把相同的值单独放在一起


"""
itertools.islice(iterable, start, stop[, step]) 
这个函数就是一个切片，我前面的博客介绍过，iterable就是要截取的对象，start开始位置 
sop结束位置，最后一个为可选参数，step步长。 
"""
partlist=[1,2,3,4,8,1]
print(list(itertools.islice(partlist,2,None)))


"""
 permutations(iterable[, r]) 无序组合：combinations
有序排列
"""
for s in itertools.permutations(range(3), 2):
    print(s)



#product(*iterables, repeat=1)笛卡尔积

print(itertools.product('ab', range(3)))




"""
itertools.repeat(object[, times]) 
来看看第三个无限迭代的函数，将objext重复times次然后停止
"""
partlist1=4*4
print(list(itertools.repeat(partlist1,2))) #结果值放入列表中


"""
itertools.startmap(function,iterable) 
将iterable中的参数，经过function处理，一一返回。 
"""
print(list(itertools.starmap(pow,[(2,3),(3,2)])))  #[8, 9]


"""
itertools.tee(it,n) 
返回n个迭代器it的复制迭代器。
"""


"""
就是把多个序列或者是迭代器的元素，组合成元组。返回的元组的长度是所有输入序列中最短的
"""
a = ['a','b','c']
b = range(10)
itertools.izip_longest(a,b,fillvalue=-1)
for i in c:
    print(i)

