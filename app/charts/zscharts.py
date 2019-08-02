# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/25 上午9:11 

import sqlalchemy.sql.expression as expr

from pyecharts.charts import Bar, Map, Pie

import json
from app.main.views import drawChart

from app.charts.Report import ReportItem
import logging

logger = logging.getLogger('main.zscharts')
# 加载招生数据的默认图表
'''
 招生报告模板
    

 '''


class zschart():
    def __init__(self, query, recordid):
        # 过滤指定record的
        print('zs chart init,', query)
        self.query = query
        self.recordid = recordid
        # self.query=query.filter(expr.column('recordid')==recordid)
        print('zs chart init2,', self.query)

        # 为了保证顺序，，用数组 ,里面是个字典，有title和report两个字段
        self.charts = []
        pass

    def chart1(self):
        data = {
            'chartType': 'table',
            'groupfield': 'sex_name,departments',
            'aggfield': 'count_total_score_of_filing',
            'orderBy': 'null',
            'filter': 'null',
            'limit': -1,
            'dataType': 'group'}
        item = ReportItem('table', 0, 400, 400, self.recordid, **data)

        chart1 = drawChart(self.query, **data)
        # option = json.loads( chart1.dump_options())
        # item.option=option
        item.rows = chart1
        return item.to_dict()

    def chart2(self):
        data = {
            'chartType': 'pie',
            'aggfield': 'count_student_name',
            'groupfield': 'student_type',
            'orderBy': 'null',
            'filter': 'null',
            'limit': -1,
            'dataType': 'group'
        }
        item = ReportItem('chart', 0, 400, 400, self.recordid, **data)
        chart2 = drawChart(self.query, **data)
        option = json.loads(chart2.dump_options())

        item.option = option

        return item.to_dict()

    def chart(self,  data,type='chart', title=None):
        item = ReportItem(type, 0, 400, 400, self.recordid, **data)
        try:
            chart2 = drawChart(self.query, **data, title=title)
        except Exception as e:
            logger.error('zs画图失败,标题:%s' % title)
            return None

        if data['chartType']=='table':
            item.rows=chart2
        else:

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

        广东各地区招生总人数，报到率。
        分男女生比例，人数，报到率；分文理科人数、比例、报到率
        过滤地区是广东的

        4.各院系招生总人数，报到率。分男女生比例，人数，报到率；分各生源地人数、比例、报到率；分文理科人数、比例、报到率

        5.各专业招生总人数，报到率。分男女生比例，人数，报到率；分各生源地人数、比例、报到率；分文理科人数、比例、报到率

        :return:
        '''
        # 测试，各学院男女人数和男女比例,返回完整结构
        title = '男女比例'
        self.charts.append(
            {
                'element': self.chart({
                    'chartType': 'pie',
                    'aggfield': 'count_student_name',
                    'groupfield': 'sex_name',
                    'orderBy': 'null',
                    'filter': 'null',
                    'limit': -1,
                    'dataType': 'group'
                }),
                'title': title
            })

        self.charts.append({
            'title':'文科理科比例',
            'element':self.chart2()
        })

        self.charts.append({
            'title':'各学院男女人数，男女比例',
            'element':self.chart1()
        })

        title = '广东地区男女比例'
        self.charts.append({
           'title':title,
            'element':self.chart({
            'chartType': 'pie',
            'aggfield': 'count_student_name',
            'groupfield': 'sex_name',
            'orderBy': 'null',
            'filter': 'source_provinces-contains-广东',
            'limit': -1,
            'dataType': 'group'
        })

        })

        # 广东地区
        title = '广东地区文科理科'
        self.charts.append(
            {
                'title':title,
                'element':self.chart(
                    {
                        'chartType': 'pie',
                        'aggfield': 'count_student_name',
                        'groupfield': 'student_type',
                        'orderBy': 'null',
                        'limit': -1,
                        'dataType': 'group',
                        'filter': 'source_provinces-contains-广东'
                    }
                )
            }
        )


        # 各院系招生人数
        title = '各院系招生总人数'
        self.charts.append(
            {
                'title':title,
                'element':self.chart({
            'aggfield': 'count_student_name',
            'groupfield': 'sex_name, departments',
            'chartType': 'stackbar',
            'orderBy': 'null',
            'limit': '-1',
            'dataType': 'group',
            'filter': 'null'
        })
            }
        )



        # 各院系各生源

        # 各专业
        title = '专业招生总人数'
        self.charts.append({
            'title':title,
            'element':self.chart({
            'aggfield': 'count_student_name',
            'groupfield': 'sex_name, major_name',
            'chartType': 'horizontal_stackbar',
            'orderBy': 'null',
            'limit': '-1',
            'dataType': 'group',
            'filter': 'null'
        })
        })


        # top 10




        title = '招生人数Top10院系'
        # 1.按院系招生人数、报到率排名
        self.charts.append({
            'title':title,
            'element':self.chart(
            {'aggfield': 'count_student_name',
             'groupfield': 'departments',
             'chartType': 'bar',
             'orderBy': 'count_student_name-desc',
             'limit': '-1',
             # 'recordid': '1',
             'dataType': 'group',
             'filter': 'null'
             },title=title)
        }
        )

        # 专业人数Top 10
        title = '专业人数Top10'
        self.charts.append({
            'title':title,

            'element':self.chart(
                {'aggfield': 'count_student_name', 'groupfield': 'major_name', 'chartType': 'bar', 'orderBy': 'count_student_name-desc', 'limit': '10',
                 'dataType': 'group', 'filter': 'null'},title=title
)
        })
        # 广东各地区
        self.charts.append({
            'title':'广东各地区招生人数',
            'element':self.chart(
                {'aggfield': 'count_student_name', 'groupfield': 'student_address', 'chartType': 'bar',
                 'orderBy': 'count_student_name-desc', 'limit':'10',
                 'dataType': 'group', 'filter': 'source_provinces-contains-广东'},title='广东各地区招生人数'


        )
        })


        self.charts.append({
            'title':'各学院文科理科分数区间人数',
            'element':self.chart(
                {'aggfield': 'count_student_name', 'groupfield': 'departments,interval-total_score_of_filing-0-100-200-300', 'chartType': 'stackbar',
                 'orderBy': 'null', 'limit': '-1', 'dataType': 'group', 'filter': 'null'},type='chart',title='各学院文科理科分数区间人数',
            )
        })
        # -----------------学生质量,录取区间

        return self.charts
