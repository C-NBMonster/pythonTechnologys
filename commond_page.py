#coding:utf-8

from datetime import *
"""
1、datetime模块定义了两个常量：datetime.MINYEAR和datetime.MAXYEAR，分别表示datetime所能表示的最 小、最大年份。其中，MINYEAR = 1，MAXYEAR = 9999。
2、datetime模块定义了下面这几个类：
datetime.date：表示日期的类。常用的属性有year, month, day；
datetime.time：表示时间的类。常用的属性有hour, minute, second, microsecond；
datetime.datetime：表示日期时间。
datetime.timedelta：表示时间间隔，即两个时间点之间的长度。
datetime.tzinfo：与时区有关的相关信息。
"""
#date类---------------------------------------------
"""
date类表示一个日期。日期由年、月、日组成（地球人都知道~~）。date类的构造函数如下：
class datetime.date(year, month, day)：参数的意义就不多作解释了，只是有几点要注意一下：
year的范围是[MINYEAR, MAXYEAR]，即[1, 9999]；
month的范围是[1, 12]。（月份是从1开始的，不是从0开始的~_~）；
day的最大值根据给定的year, month参数来决定。例如闰年2月份有29天；
"""

import time
print(date.max)#date对象表示日期的最小单位。这里是天。
print(date.min)#date对象所能表示的最大、最小日期；
print(date.today())#返回一个表示当前本地日期的date对象；
print(date.fromtimestamp(time.time()))#根据给定的时间戮，返回一个date对象；
#print(datetime.fromordinal(ordinal))将Gregorian日历时间转换为date对象；（Gregorian Calendar ：一种日历表示方法，类似于我国的农历，西方国家使用比较多，此处不详细展开讨论。）
print(date.year,date.month,date.day)
date= datetime.today()
#now = date( 2010, 04, 06 )
#tomorrow = now.replace(day = 07 )#生成一个新的日期对象，用参数指定的年，月，日代替原有对象中的属性。（原有对象仍保持不变）
#print('now:' , now, ', tomorrow:' , tomorrow)
print(date.timetuple)#返回日期对应的time.struct_time对象
#print(date.toordinal())#返回日期对应的Gregorian Calendar日期；
print(date.weekday())#返回weekday，如果是星期一，返回0；如果是星期2，返回1，以此类推；
print(date.isoweekday())#返回weekday，如果是星期一，返回1；如果是星期2，返回2，以此类推；
print(date.isocalendar())#返回格式如(year，month，day)的元组；
print(date.isoformat())#返回格式如'YYYY-MM-DD'的字符串；
print(date.strftime("%b %d %Y %H:%M:%S"))


"""
date2 = date1 + timedelta  # 日期加上一个间隔，返回一个新的日期对象（timedelta将在下面介绍，表示时间间隔）
date2 = date1 - timedelta   # 日期隔去间隔，返回一个新的日期对象
timedelta = date1 - date2   # 两个日期相减，返回一个时间间隔对象
date1 < date2  # 两个日期进行比较
"""
now = date.today()
tomorrow = now.replace(day = 7 )
delta = tomorrow - now
print('now:', now, ' tomorrow:', tomorrow)
print('日期相减:' , delta)
print("日期相加:",now + delta)
print("日期比较:",tomorrow > now)








