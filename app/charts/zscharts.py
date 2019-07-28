# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/25 上午9:11 

import sqlalchemy.sql.expression as expr

from pyecharts.charts import Bar,Map,Pie


import json
from app.main.views import drawChart

from app.charts.Report import ReportItem
# 加载招生数据的默认图表
'''
 招生所有 图表
    

 '''

class zschart():
    def __init__(self,query):
        # 过滤指定record的
        print('zs chart init,',query)
        self.query=query
        # self.query=query.filter(expr.column('recordid')==recordid)
        print('zs chart init2,', self.query)
        self.charts={


        }
        pass

    def chart1(self):
        chart1 = ReportItem()
        chart1 = drawChart(self.query,'bar','group','sex_name,departments','count_total_score_of_filing','null','null',-1)
        return chart1.dump_options()

    # 获取所有options
    def options(self):
        # 基本情况


        # 测试，各学院男女人数和男女比例,返回完整结构
        self.charts['各学院男女人数，男女比例']= json.loads( self.chart1())


        return self.charts


