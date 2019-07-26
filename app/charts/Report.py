# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/25 上午9:28 
# 单个元素
paramKeys = ['chartType', 'groupfield', 'aggfield', 'orderBy', 'filter', 'limit', 'dataType']
class ReportItem(object):

    def __init__(self,type,index,width,height,recordid,groupfield='',aggfield='',orderBy='null',limit='-1',filter='null',chartType='',option='',dataType='',text=''):
        """

        :param type: 元素类型,chart,text,table
        :param index:  位置
        :param width: 宽度
        :param height: 高度
        :param recordid: 记录id
        :param groupfield: 分组字段
        :param aggfield: 聚合字段
        :param orderBy: 排序字段
        :param limit: 限制条数
        :param filter: 数据过滤
        :param chartType: 图表类型
        :param option: echarts option
        :param dataType: 数据类型
        :param text: 文字的text
        """
        self.type=type
        self.index=index
        self.width=width
        self.height=height
        self.recordid=recordid
        self.groupfield=groupfield
        self.aggfield=aggfield
        self.orderBy=orderBy
        self.limit=limit
        self.filter=filter
        self.chartType=chartType
        self.option = option
        self.dataType=dataType
        self.text=text
        pass
    def to_dict(self):
        return {
            # 基本信息,类型chart图表，text ，文字,table表格
            'type': self.type,
            # 位置
            'index': self.index,
            'widht': self.width,
            'height': self.height,
            # 数据结构
            'recordid': self.recordid,
            'groupfield': self.groupfield,
            # 分组类型，默认，
            'aggfield': self.aggfield,
            # 排序字段 , count_student_name-asc,
            'orderBy': self.orderBy,
            # 限制返回条数
            'limit': self.limit,
            # 过滤数据,字段名+条件+值组成 ，条件有 like,>,<,==,>=,<=
            'filter': self.filter,

            # 图表配置,原本有options就加载原本的option
            # 自定义图表类型
            'chartType':self.chartType,
            'option': self.option,
            # 是否可以更新数据,自定义图表和内置的图表,custom,internal,自定义和内置的，
            'dataType': self.dataType,
            # 文字配置
            'text': self.text,
            # 表格配置
        }


