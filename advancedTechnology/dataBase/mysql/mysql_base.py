#_*_ coding:utf-8 _*_

import pymysql

# 创建连接
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='ccc123', db='world', charset='utf8')
# 创建游标
cursor = conn.cursor()

# 执行SQL，并返回收影响行数
effect_row = cursor.execute("select * from city")
search_result = cursor.fetchall()
for i in search_result:
    print(i)
# 执行SQL，并返回受影响行数
# effect_row = cursor.execute("update tb7 set pass = '123' where nid = %s", (11,))

# 执行SQL，并返回受影响行数,执行多次
# effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u1","u1pass","11111"),("u2","u2pass","22222")])
#可以获取到最新自增的ID，也就是最后插入的一条数据ID

effect_row = cursor.executemany("insert into tb7(user,pass,licnese)values(%s,%s,%s)", [("u3","u3pass","11113"),("u4","u4pass","22224")])
conn.commit()
#获取自增id
new_id = cursor.lastrowid
print("new_id:",new_id)


#移动游标
#操作都是靠游标，那对游标的控制也是必须的
#cursor.scroll(1,mode='relative') # 相对当前位置移动
#cursor.scroll(2,mode='absolute') # 相对绝对位置移动


#调用存储过程
#a、调用无参存储过程
#游标设置为字典类型
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)
#无参数存储过程
cursor.callproc('p2')  #等价于cursor.execute("call p2()")
cursor.callproc('p1', args=(1, 22, 3, 4))
#获取执行完存储的参数,参数@开头
cursor.execute("select @p1,@_p1_1,@_p1_2,@_p1_3")  #{u'@_p1_1': 22, u'@p1': None, u'@_p1_2': 103, u'@_p1_3': 24}
row_1 = cursor.fetchone()

#b、调用有参存储过程








# 提交，不然无法保存新建或者修改的数据
conn.commit()

# 关闭游标
cursor.close()
# 关闭连接
conn.close()


















