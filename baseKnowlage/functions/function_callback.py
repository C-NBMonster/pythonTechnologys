#coding:utf-8
#这块不是很懂，以后再研究20171012

# 1,在函数中使用回调
def click(callback):
    eval(callback)()  # eval()可以讲字符串解析成可以执行的代码

def handle():
    print('在点击事件结束后调用该函数，进行处理，比如弹出框alert()')

click('handle')






























