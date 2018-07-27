#coding:utf-8
"""
logging分为4个模块: loggers, handlers, filters, and formatters.
●loggers: 提供应用程序调用的接口
●handlers: 把日志发送到指定的位置
●filters: 过滤日志信息
●formatters: 格式化输出日志
Logger
Logger.setLevel() 设置日志级别
Logger.addHandler()和Logger.removeHandler() 增加和删除日志处理器
Logger.addFilter()和Logger.removeFilter() 增加和删除过滤器
Logger.debug(), Logger.info(), Logger.warning(), Logger.error(), and Logger.critical() 创建不同的级别的日志
getLogger() 获取日志的根实例
Handler
setLevel() 设置日志级别
setFormatter() 设置输出格式
addFilter() and removeFilter() 增加和删除过滤器
Formatter
默认形式为: %Y-%m-%d %H:%M:%S.
格式为: %()s

"""


import calendar
import logging,os
logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.DEBUG)
logging.debug('this is a message')
print(calendar.leapdays(2010, 2015))#返回两个年份之间的闰年总数


"""
logging.basicConfig([**kwargs]):
为日志模块配置基本信息。kwargs 支持如下几个关键字参数：
filename ：日志文件的保存路径。如果配置了些参数，将自动创建一个FileHandler作为Handler；
filemode ：日志文件的打开模式。 默认值为'a'，表示日志消息以追加的形式添加到日志文件中。如果设为'w', 那么每次程序启动的时候都会创建一个新的日志文件；
format ：设置日志输出格式；
datefmt ：定义日期格式；
level ：设置日志的级别.对低于该级别的日志消息将被忽略；
stream ：设置特定的流用于初始化StreamHandler；
"""


logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'),
                    level = logging.WARN, filemode = 'w',
                    format = '%(asctime)s - %(levelname)s: %(message)s')
logging.debug('debug')
#被忽略
logging.info('info')
#被忽略
logging.warning('warn')
logging.error('error')
#----- 结果
#2009-07-13 21:42:15,592 - WARNING: warn
#2009-07-13 21:42:15,640 - ERROR: error
logging.getLogger()

#获取日志级别对应的名称。例如：
print(logging.getLevelName(logging.NOTSET))
print(logging.getLevelName(10))
#logging.DEBUG
print(logging.getLevelName(logging.DEBUG))
print(logging.getLevelName(30))
#logging.WARN
print(logging.getLevelName(logging.ERROR))
print(logging.getLevelName(50))
#logging.CRITICAL
logging.shutdown()

logging.basicConfig(filename = os.path.join(os.getcwd(), 'log.txt'), level = logging.DEBUG)
log = logging.getLogger('admin')
try:
  raise Exception('this is a exception')
except:
  log.exception('exception')
#异常信息被自动添加到日志消息中

#Python同时向控制台和文件输出日志logging的方法
# 配置日志信息
logging.basicConfig(level=logging.DEBUG,
          format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
          datefmt='%m-%d %H:%M',
          filename='myapp.log',
          filemode='w')
# 定义一个Handler打印INFO及以上级别的日志到sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# 设置日志打印格式
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
console.setFormatter(formatter)
# 将定义好的console日志handler添加到root logger
logging.getLogger('').addHandler(console)
logging.info('Jackdaws love my big sphinx of quartz.')
logger1 = logging.getLogger('myapp.area1')
logger2 = logging.getLogger('myapp.area2')
logger1.debug('Quick zephyrs blow, vexing daft Jim.')
logger1.info('How quickly daft jumping zebras vex.')
logger2.warning('Jail zesty vixen who grabbed pay from quack.')
logger2.error('The five boxing wizards jump quickly.')















