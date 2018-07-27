#coding:utf-8
import urllib.request as ur

google = ur.urlopen('http://www.baidu.com')
print('http header:/n', google.info())
print('http status:', google.getcode())
print('url:', google.geturl())
# for line in google: # 就像在操作本地文件
# print (line)
google.close()
# urlretrieve方法直接将远程数据下载到本地
def cbk(a, b, c):
    '''回调函数
    @a: 已经下载的数据块
    @b: 数据块的大小
    @c: 远程文件的大小
    '''
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print('%.2f%%' % per)


url = 'http://www.sina.com.cn'
local = 'd://sina.html'
ur.urlretrieve(url, local, cbk)

"""
urllib.quote(string[, safe])：对字符串进行编码。参数safe指定了不需要编码的字符;
urllib.unquote(string) ：对字符串进行解码；
urllib.quote_plus(string[, safe] ) ：与urllib.quote类似，但这个方法用
'+'
来替换
' ‘，而quote用' % 20′来代替
' ‘
urllib.unquote_plus(string) ：对字符串进行解码；
urllib.urlencode(query[, doseq])：将dict或者包含两个元素的元组列表转换成url参数。例如
字典
{‘name
': ‘dark-bull', ‘age
': 200}将被转换为”name=dark-bull&age=200″
urllib.pathname2url(path)：将本地路径转换成url路径；
urllib.url2pathname(path)：将url路径转换成本地路径；
"""

data = 'name = ~a+3'

data1 = ur.quote(data)










