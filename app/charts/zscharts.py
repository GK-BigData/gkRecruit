# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/25 上午9:11 

import sqlalchemy.sql.expression as expr

from pyecharts.charts import Bar,Map,Pie

# 加载招生数据的默认图表
'''
 招生所有 图表
    

 '''

class zschart():
    def __init__(self,query,recordid):
        # 过滤指定record的
        self.query=query.filter(expr.column('recordid')==recordid)
        self.charts={


        }
        pass


    # 获取所有options
    def options(self):
        # 基本情况




        pass


