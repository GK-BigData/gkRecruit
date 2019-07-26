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
    def __init__(self,query,recordid):
        # 过滤指定record的
        print('zs chart init,',query)
        self.query=query
        self.recordid=recordid
        # self.query=query.filter(expr.column('recordid')==recordid)
        print('zs chart init2,', self.query)
        self.charts={


        }
        pass

    def chart1(self):
        data = {
                'chartType':'bar',
                'groupfield':'sex_name,departments',
                'aggfield':'count_total_score_of_filing',
                'orderBy':'null',
                'filter':'null',
                'limit':-1,
                'dataType':'group'}
        item = ReportItem('chart',0,400,400,self.recordid,**data)

        chart1 = drawChart(self.query,**data)
        option = json.loads( chart1.dump_options())

        item.option=option
        return item.to_dict()

    # 获取所有options
    def options(self):
        # 基本情况


        # 测试，各学院男女人数和男女比例,返回完整结构
        self.charts['各学院男女人数，男女比例']= self.chart1()




        return self.charts


