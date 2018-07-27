#coding:utf-8
"""
zlib.compress(string[, level])
zlib.decompress(string[, wbits[, bufsize]])
zlib.compress用于压缩流数据。参数string指定了要压缩的数据流，参数level指定了压缩的级别，它的取值范围是1到9。
压缩速度与压缩率成反比，1表示压缩速度最快，而压缩率最低，而9则表示压缩速度最慢但压缩率最高。
zlib.decompress用于解压数据。参数string指定了需要解压的数据，wbits和bufsize分别用于设置系统缓冲区大小(window buffer )与输出缓冲区大小(output buffer)。

"""
import zlib, urllib.request



fp = urllib.request.urlopen('http://mil.eastday.com/a/171226151859143.html')
# 访问的到的网址。
data = fp.read()
fp.close()

# ---- 压缩数据流
str1 = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
str2 = zlib.decompress(str1)
print('原始数据长度：', len(data))
print('-' * 30)

print('zlib.compress压缩后：', len(str1))

print('zlib.decompress解压后：', len(str2))

print('-' * 30)


# ---- 使用Compress, Decompress对象对数据流进行压缩/解压缩
com_obj = zlib.compressobj(zlib.Z_BEST_COMPRESSION)
decom_obj = zlib.decompressobj()

str_obj = com_obj.compress(data)
str_obj += com_obj.flush()
print('Compress.compress压缩后：', len(str_obj))


str_obj1 = decom_obj.decompress(str_obj)
str_obj1 += decom_obj.flush()
print('Decompress.decompress解压后：', len(str_obj1))

print('-' * 30)


# ---- 使用Compress, Decompress对象，对数据进行分块压缩/解压缩。
com_obj1 = zlib.compressobj(zlib.Z_BEST_COMPRESSION)
decom_obj1 = zlib.decompressobj()
chunk_size = 30

# 原始数据分块
str_chunks = [data[i * chunk_size:(i + 1) * chunk_size]
              for i in range((len(data) + chunk_size) % chunk_size)]

str_obj2 = ''
for chunk in str_chunks:
    str_obj2 += com_obj1.compress(chunk).decode("gbk","ignore")

str_obj2 += com_obj1.flush().decode("gb18030","ignore")
print('分块压缩后：', len(str_obj2))


# 压缩数据分块解压
str_chunks = [str_obj2[i * chunk_size:(i + 1) * chunk_size]
              for i in range((len(str_obj2) + chunk_size) % chunk_size)]
str_obj3 = ''

for chunk in str_chunks:
    str_obj3 += decom_obj1.decompress(chunk).decode("gb18030","ignore")
str_obj3 += decom_obj1.flush().encode("gb18030","ignore")
print('分块解压后：', len(str_obj3))




