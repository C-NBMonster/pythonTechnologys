#coding:utf-8


from datetime import *
import time
print(time.time()) #打印时间戳
print(time.localtime())#打印本地时间元组
print(time.gmtime())#答应UTC+0时区的时间元组
print(time.ctime())#打印asctime格式化时间
print(time.mktime(time.localtime()))#将时间元组转换为时间戳
print(time.asctime())#打印格式化时间
print(time.strftime('%d/%b/%Y:%X'))#打印指定格式的时间格式
#把时间字符串和它的格式翻译成时间元组
print(time.strptime('28/Jul/2013:04:33:29', '%d/%b/%Y:%X'))
print('%0.5f'%time.clock()) #打印处理器时间
for i in list(range(100000)):
  pass
print('%0.5f'%time.clock())#打印处理器时间
tm = time.time()
#print(time.hour,time.minute,time.second,time.microsecond)









