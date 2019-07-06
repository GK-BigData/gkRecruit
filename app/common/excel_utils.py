# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/4 下午4:55 

import xlrd

'''Excel工具'''
def get_columns(path,sheet_index=0)->dict:
    '''
    读取前10个元素
    :param path:文件路径
    :param sheet_index:excel的第几个工作表
    :return:
    '''
    book = xlrd.open_workbook(path)

    sheet = book.sheet_by_index(sheet_index)

#     第一行作为列名
    columns =  sheet.row_values(0)
    results={}
    # 初始化字典元素
    for col in columns:
        results[col]=[]
    #     1开始跳过第一行
    for i in range(1,min(sheet.nrows,10)):

        for col,index in enumerate(columns):
            results[col].append(sheet.cell_value(i,index))
    return results



def excel2list(path:str,sheet_index=0,columns=None)->list:

    book = xlrd.open_workbook(path)

    sheet = book.sheet_by_index(sheet_index)

    # excel表的字段
    excelColumns = sheet.row_values(0)

    # 需要的字段
    if columns==None:
        # 需要字段不提供就使用全部字段
        columns = sheet.row_values(0)

    result = []
    for i in range(1,sheet.nrows):

        item = {}
        for col in columns:
            index = excelColumns.index(col)
            item[col]=sheet.cell_value(i,index)
        result.append(item)
    return result

def excel2dict(path:str,sheet_index=0,columns=None)->dict:

    book = xlrd.open_workbook(path)

    sheet = book.sheet_by_index(sheet_index)

    # excel表的字段
    excelColumns = sheet.row_values(0)

    # 需要的字段
    if columns==None:
        # 需要字段不提供就使用全部字段
        columns = sheet.row_values(0)

    result = {}
    for col in columns:

    #     字段在excel表的列的索引
        index = excelColumns.index(col)

        values = []
        for i in range(1,sheet.nrows):
            values.append(sheet.cell_value(i,index))
        result[col]=values

    return result