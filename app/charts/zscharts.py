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
 招生报告模板
    

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
                'chartType':'table',
                'groupfield':'sex_name,departments',
                'aggfield':'count_total_score_of_filing',
                'orderBy':'null',
                'filter':'null',
                'limit':-1,
                'dataType':'group'}
        item = ReportItem('table',0,400,400,self.recordid,**data)

        chart1 = drawChart(self.query,**data)
        # option = json.loads( chart1.dump_options())
        # item.option=option
        item.rows=chart1
        return item.to_dict()
    def chart2(self):
        data = {
            'chartType':'pie',
            'aggfield': 'count_student_name',
            'groupfield': 'student_type',
            'orderBy': 'null',
            'filter': 'null',
            'limit': -1,
            'dataType':'group'
        }
        item = ReportItem('chart',0,400,400,self.recordid,**data)
        chart2 = drawChart(self.query,**data)
        option = json.loads(chart2.dump_options())

        item.option=option

        return item.to_dict()

    def chart(self,data,title=None):
        item = ReportItem('chart', 0, 400, 400, self.recordid, **data)
        chart2 = drawChart(self.query, **data,title=title)
        option = json.loads(chart2.dump_options())

        item.option = option

        return item.to_dict()

    # 获取所有options
    def options(self):
        # 基本情况
        '''
        1.全校招生总人数，报到率。分男女生比例，人数，报到率；分文、理科生比例、人数、报到率
        全校男女比例的人数 报到率 饼图
        全校文科理科的人数 报到率 饼图

        :return:
        '''
        # 测试，各学院男女人数和男女比例,返回完整结构
        self.charts['男女比例'] = self.chart({
            'chartType':'pie',
            'aggfield': 'count_student_name',
            'groupfield': 'sex_name',
            'orderBy': 'null',
            'filter': 'null',
            'limit': -1,
            'dataType':'group'
        },title='男女比例')

        self.charts['文科理科比例']=self.chart2()
        self.charts['各学院男女人数，男女比例']= self.chart1()

        return self.charts


