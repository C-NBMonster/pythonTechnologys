#coding:utf-8

"""
但当Python需要通过网络与其他的平台进行交互的时候，必须考虑到将这些数据类型与其他平台或语言之间的类型进行互相转换问题。
打个比方：C++写的客户端发送一个int型(4字节)变量的数据到Python写的服务器，Python接收到表示这个整数的4个字节数据，
怎么解析成Python认识的整数呢？ Python的标准模块struct就用来解决这个问题。

"""
import struct

"""
struct.pack用于将Python的值根据格式符，转换为字符串（因为Python中没有字节(Byte)类型，可以把这里的字符串理解为字节流，或字节数组）。
其函数原型为：struct.pack(fmt, v1, v2, …)，参数fmt是格式字符串。v1, v2, …表示要转换的python值
"""
a = 20
b = 400

str = struct.pack("ii", a, b)
# 转换后的str虽然是字符串类型，但相当于其他语言中的字节流（字节数组），可以在网络上传输
print('length:', len(str))

print(str)

print(repr(str))

"""
struct.unpack做的工作刚好与struct.pack相反，用于将字节流转换成python数据类型。它的函数原型为：struct.unpack(fmt, string)，该函数返回一个元组
"""
str = struct.pack("ii", 20, 400)
a1, a2 = struct.unpack("ii", str)
print('a1:', a1)

print('a2:', a2)


# ---- result:
# a1: 20
# a2: 400
print(struct.calcsize("ii"))  #用于计算格式字符串所对应的结果的长度，如：struct.calcsize(‘ii')，返回8。因为两个int类型所占用的长度是8个字节。


"""
用于计算格式字符串所对应的结果的长度，如：struct.calcsize(‘ii')，返回8。因为两个int类型所占用的长度是8个字节。
"""
import struct
from ctypes import create_string_buffer

buf = create_string_buffer(12)
print(repr(buf.raw))

struct.pack_into("iii", buf, 0, 1, 2, -1)
print(repr(buf.raw))

print(struct.unpack_from('iii', buf, 0))



