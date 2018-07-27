#coding:utf-8

slist = ['a','b',0,1,3]

#利用下表获取列表中的值
print(slist[0])
#删除列表的第一个值
del slist[0]
#在列表中插入一个值
slist[0:0]=["abc"]
print(slist)
#获取列表长度
print(len(slist))
#遍历列表
for el in slist:
    print(el)
#新建递增列表
lis = list(range(10))
lis2 = list(range(1,10,3))#3是间隔
print("递增列表："+lis + "\n" + lis2)

#用某个固定值初始化列表
initial_value = 0
list_length = 5
sample_list = [initial_value for i in range(list_length)]
sample_list = [initial_value]*list_length

#两个列表相加，相当于合并
ll = [1,2]+[3,4] #为[1,2,3,4]。同extend()
print("两个列表相加合并：",ll)

#列表复制
#L1 = L      #L1为L的别名，用C来说就是指针地址相同，对L1操作即对L操作。函数参数就是这样传递的
#L1 = L[:]   #L1为L的克隆，即另一个拷贝。
l1=[1,2,3,4]
l2=l1
l3=l1[:]

#遍历两个数组
nn = ['dd','dc','fd','cda']
nc = ['gf','da','fd','fda']

for i,j in zip(nn,nc):
  print(i,"<-->",j)











