# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/4 下午4:50 

import xlrd
from app.common.excel_utils import  excel2dict,excel2list
book = xlrd.open_workbook("/home/formatfa/Documents/Project/zs/upload/2018.xlsx")

print(book)

print(book.sheet_names())

sheet = book.sheet_by_index(0)

print(sheet)

print(sheet.row_values(0))
print(sheet.nrows)
print(sheet.ncols)
dict = excel2dict("/home/formatfa/Documents/Project/zs/upload/2018.xlsx",columns=['姓名','民族'])
print(dict.keys())
print(dict['民族'])

list = excel2list("/home/formatfa/Documents/Project/zs/upload/2018.xlsx")
print(list[0])