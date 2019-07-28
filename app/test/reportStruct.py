# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/25 上午8:58 
# BY    :FormatFa

report = [

    # 图表元素
    {
        # 基本信息,类型chart图表，text ，文字,table表格
        'type':'chart',
        # 位置
        'index':0,
        'widht':400,
        'height':400,
        # 数据结构
        'recordid':1,
        'groupfield':'sex_name,source_provinces',
        # 分组类型，默认，
        'aggfield':'count_student_name',
        #排序字段 , count_student_name-asc,
        'orderBy':'null',
        #限制返回条数
        'limit':'-1',
        # 过滤数据,字段名+条件+值组成 ，条件有 like,>,<,==,>=,<=
        'filter':'sex_name-like-男',

        # 图表配置,原本有options就加载原本的option
        # 自定义图表类型
        'chartType':'',
        'option':'',
        # 是否可以更新数据,自定义图表和内置的图表,custom,internal,自定义和内置的，
        'dataType':'custom',
        # 文字配置
        'text':'',
        # 表格配置

    },
    {
'type':'chart',
        text:ff
    }

]
