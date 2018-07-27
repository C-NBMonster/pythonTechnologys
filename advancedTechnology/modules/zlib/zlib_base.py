#coding:utf-8
"""
zlib.compress(string[, level])
zlib.decompress(string[, wbits[, bufsize]])
zlib.compress用于压缩流数据。参数string指定了要压缩的数据流，参数level指定了压缩的级别，它的取值范围是1到9。
压缩速度与压缩率成反比，1表示压缩速度最快，而压缩率最低，而9则表示压缩速度最慢但压缩率最高。
zlib.decompress用于解压数据。参数string指定了需要解压的数据，wbits和bufsize分别用于设置系统缓冲区大小(window buffer )与输出缓冲区大小(output buffer)。

"""
import zlib, urllib.request

fp = urllib.request.urlopen('http://slide.sports.sina.com.cn/k/slide_2_786_169447.html#p=1')
str = fp.read()
fp.close()

# ---- 压缩数据流。
str1 = zlib.compress(str, zlib.Z_BEST_COMPRESSION)
str2 = zlib.decompress(str1)
print(len(str))

print(len(str1))
print(len(str2))


