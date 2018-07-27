#coding:utf-8
import xlrd,xlwt
from pyExcelerator import Workbook
from pyExcelerator import Worksheet
from pyExcelerator import Row

tt = xlrd.open_workbook(r"D:/Python/files/tExcel.xlsx")
table1 = tt.sheets()[0] #通过索引顺序获取
table2 = tt.sheet_by_index(1) #通过索引顺序获取
table3 = tt.sheet_by_name(u'Sheet2')#通过名称获取

#获取行数,列数
rows = table1.nrows
cols = table1.ncols
print("行:",rows,"列：",cols)

#获取整行和整列的值（数组）
listA = []
for i in range(rows-1):

    dd = table1.row_values(i)
    listA.append(dd)
    #print(table2.col_values(i))
print(listA)
#单元格
cell_A1 = table1.cell(0,0).value
cell_C4 = table1.cell(1,2).value
print(cell_A1,cell_C4)

#使用行索引
#cell_A1 = table2.row(0)[0].value
#cell_A2 = table2.col(1)[0].value

#获取第一行第一列数据
cell_value = table1.cell_value(0,0)
print(cell_value)

#写入Excel
w = Workbook()  #创建一个工作簿
ws = w.add_sheet('Hey, Hades')  #创建一个工作表
ws.write(0,0,'bit') #在1行1列写入bit
ws.write(0,1,'huang') #在1行2列写入huang
ws.write(1,0,'xuan') #在2行1列写入xuan
w.save('mini.xls')  #保存




