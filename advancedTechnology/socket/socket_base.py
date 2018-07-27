#coding:utf-8

import socket,socketserver

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #创建实例
s.connect('localhost',8000)

#发送数据
#发送数据有两个方法send和sendall，send不能保证所有的数据都发送完了，它会返回已发送数据的长度，程序要循环发送数据直到所有数据都已发送完毕。
def mysend(s, msg):
  total_len = len(msg)
  total_sent = 0
  while total_sent < total_len:
    sent = s.send(msg[total_sent:])
    if sent == 0:
      raise RuntimeError("socket connection broken")
    total_sent += sent


#sendall能够保证所有的数据都已发送完毕，除非发送过程中出现了错误，它实际上也是循环发送数据直到所有数据发送完成。
s.sendall('test')  #这个直接发在Python3中会报错。

#接受数据
"""
在Python 3中返回的是bytes对象，在Python 2中返回的是string。注意函数返回的数据长度是小于或者等于参数指定的长度的，要接收到指定长度的数据，需要循环接收数据
"""
def myreceive(s, msglen):
  chunks = []
  bytes_recd = 0
  while bytes_recd < msglen:
    chunk = s.recv(min(msglen - bytes_recd, 2048))
    if chunk == b'':
      raise RuntimeError("socket connection broken")
    chunks.append(chunk)
    bytes_recd = bytes_recd + len(chunk)
  return b''.join(chunks)





























