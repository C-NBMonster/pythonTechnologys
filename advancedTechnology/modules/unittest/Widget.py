#coding:utf-8

class Widget:
  def __init__(self, size = (40,40)):
    self.size = size
  def getSize(self):
    return self.size
  def reSize(self,width,height):
    if width <0 or height < 0:
      raise ValueError('illegal size')
    else:
      self.size = (width,height)
      return self.size
  def dispose(self):
    pass


