# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:28 

import time
import os
from flask import Blueprint, render_template, request,send_from_directory,send_file

from app.charts.all_picture import All_Picture
from app.common.restful import rjson
import json
from app.main.models import zs

from app import db
import sqlalchemy.sql.functions as func
from sqlalchemy.sql.expression import *
from sqlalchemy.sql.expression import *
import  sqlalchemy.sql.sqltypes   as sqltype

from app.common.mycolumns import needcolumns_fields, needcolumns_name,chartTypes,aggType,aggfield2name
from . import bp_main,logger

from app.charts.Report import ReportItem
from flask_login import login_required,current_user

need_columns = {}
for i in range(0, len(needcolumns_name)):
    # 性别名称=sexname
    need_columns[needcolumns_name[i]] = needcolumns_fields[i]
# 字段对应的名字
field_name= {}
for i in range(0, len(needcolumns_name)):
    # sexname = 性别名称
    field_name[needcolumns_fields[i]] = needcolumns_name[i]

allcharts = ["各学院男女人数占比雷达图",
             "各学院人数占比",
             "男女比例",
             "男女专业排三的专业",
             "政治面貌",
             "各个投档分区段的人数",
             "全国各个地区人数",
             "学年制",
             ]

# 聚合类型

# 需要传入报告id
@bp_main.route("/<reportid>")
@login_required
def index(reportid):
    # report要引用到这个views的drawChart方法,如果在上面引用，report里又用到drawChart，就会找不到
    from app.report.models import Report
    # 查询报告记录
    report = Report.query.filter(Report.id==reportid).first_or_404()
    return render_template('main/main.html',columns = need_columns,chartTypes=chartTypes,report=report)


# @bp_main.route("/charts")
# def charts():
#     zsyear = request.args['zsyear']
#     chartid = request.args['chartid']
#
#     a = All_Picture(chartid, '', '', '地区名称')
#
#     sql = zs.query.filter(zs.zsyear == zsyear)
#     result = None
#
#     if chartid == '男女比例':
#         x = []
#         y = []
#         # dataset = db.session.execute("select sex_name,count(1) from zs group by sex_name;").fetchall()
#         sql = sql.with_entities(zs.sex_name, func.count()).group_by(zs.sex_name)
#         print("sql语句:", sql)
#         dataset = sql.all()
#         for item in dataset:
#             x.append(item[0])
#             y.append(item[1])
#         print("查询结果")
#         print(x)
#         print(y)
#         result = a.pie_picture(x, y)
#
#     elif chartid == '全国各个地区人数':
#         x = []
#         y = []
#
#         # sql = sql.with_entities(zs.source_provinces, func.count()).group_by(zs.source_provinces).order_by(desc(column( 'count_1')))
#
#         sql = sql.with_entities(zs.source_provinces, func.count()).group_by(zs.source_provinces)
#         print('全国各个地区人数', sql)
#
#         dataset = sql.all()
#         # dataset=db.session.execute("select student_address ,count(1) as counts from zs group by student_address order by counts desc limit 10;")
#
#         for item in dataset:
#             x.append(item[0][:2])
#             y.append(item[1])
#
#         print("全国各个地区人数")
#         print(x)
#         print(y)
#         result = a.china_map_picture(x, y)
#
#     elif chartid == '各学院男女人数占比雷达图':
#         women_data = []
#         man_data = []
#         departments = []
#         sql = sql.with_entities(zs.departments, zs.sex_name, func.count()).group_by(zs.departments, zs.sex_name)
#         dataset = sql.all()
#         print(sql)
#
#         for item in dataset:
#             print(item)
#             if item[0] not in departments:
#                 departments.append(item[0])
#
#             if item[1] == '男':
#                 man_data.append(item[2])
#
#             if item[1] == '女':
#                 women_data.append(item[2])
#
#         print(departments)
#         print(man_data)
#         print(women_data)
#         result = a.radar_picture(women_data, man_data, departments)
#
#     elif chartid == '学年制':
#         x = []
#         y = []
#         # dataset = db.session.execute("select sex_name,count(1) from zs group by sex_name;").fetchall()
#         sql = sql.with_entities(zs.education__time, func.count()).group_by(zs.education__time)
#         print("sql语句:", sql)
#         dataset = sql.all()
#         for item in dataset:
#             x.append(item[0])
#             y.append(item[1])
#         print("查询结果")
#         print(x)
#         print(y)
#         result = a.rose_picture(x, y)
#
#     elif chartid == '男女人数排三的专业':
#         x = []
#         y = []
#         man_data = []
#         women_data = []
#         dataset = db.session.execute(
#             "(select major_name,sex_name,count(major_name) as counts from zs  where sex_name='男' group by major_name order by counts desc limit 3) UNION ALL (select major_name,sex_name,count(major_name) as counts from zs  where sex_name='女' group by major_name order by counts desc limit 3);")
#
#         for item in dataset:
#             if item[1] == '男':
#                 x.append(item[0])
#                 man_data.append(item[2])
#
#             if item[1] == '女':
#                 y.append(item[0])
#                 women_data.append(item[2])
#         print(man_data)
#         print(women_data)
#         print(x)
#         result = a.rose_picture_man_women(x, y, man_data, women_data)
#
#         # result =a.bar_base(x,man_data=man_data,women_data=women_data)
#
#     elif chartid == '各学院人数占比':
#         x = []
#         y = []
#         sql = sql.with_entities(zs.departments, func.count()).group_by(zs.departments)
#         dataset = sql.all()
#         print("department", sql)
#         for item in dataset:
#             x.append(item[0])
#             y.append(item[1])
#         result = a.pictorialbar_base(x, y)
#
#
#
#     elif chartid == '各个投档分区段的人数':
#         x = ['450以上', '400-450', '350-400', '300-350', '200-300', '200以下']
#         y = []
#         # sql=sql.with_entities(zs.total_score_of_filing)
#         dataset = db.session.execute(
#             "select count(case when total_score_of_filing> 450 then 1 end) as `[450分以上]`, count(case when total_score_of_filing between 400 and 450 then 1 end) as `[400-450分]`, count(case when total_score_of_filing between 350 and 400 then 1 end) as `[350-400分]`, count(case when total_score_of_filing between 300 and 350 then 1 end) as `[300-350分]`, count(case when total_score_of_filing between 200 and 300 then 1 end) as `[200-300分]`, count(case when total_score_of_filing <200 then 1 end) as `[200分以下]` from zs;").fetchall()
#         for item in dataset:
#             for i in item:
#                 y.append(i)
#         print(x)
#         print(y)
#
#         result = a.funnel_sort_ascending(x_data=x, y_data=y)
#
#     # x=[]
#     # y=[]
#     # a = All_Picture()
#     # options = a.getchart( db,zsyear,chartid)
#     #
#     # sql = zs.query.with_entities(zs.sex_name,func.count()).group_by(zs.sex_name)
#     # print(sql)
#     # dataset = sql.all()
#     # for item in dataset:
#     #     x.append(item[0])
#     #     y.append(item[1])
#     #
#     # result = a.bar_picture(x, y)
#     # result_dict = json.loads(result)
#     # test = db.session.execute("select sex_name,count(1) from zs group by sex_name;").fetchall()
#     #
#     # print(test)
#     # print(dir(test))
#     result_dict = json.loads(result)
#     return rjson(result_dict, 0)


# 获取各个数据类型对应的sql
def get_sql(query, charttype: str,  groupfield: list,aggfield: list):


    # 计数类型,字段数只能是 一个或者两个,

    # 判断聚合函数,最后一列作为聚合列
    # 聚合的列
    #----------------select 段
    #先选择,要的字段，即group 字段 ，和 聚合字段 组成
    entities=[]
    # 分组字段直接用列名
    for group in groupfield:
        # 检查分组类型,限制最多分组2次
        field_type_param = group.split('-',2)
        logger.debug('处理分组字段：%s',field_type_param)

        # 普通分组
        if len(field_type_param) == 1:
            entities.append(column(group.strip()))
        else:
            #         判断分组类型,
            if field_type_param[0] == 'interval':
                # elt函数参数,elt函数用于改成对于的>100这样
                elt_params = []
                # 整数分组,获取分组参数
                interval_param = [column(field_type_param[1])]
                all = field_type_param[2].split('-')
                for index,item in enumerate( all):
                    interval_param.append(int(item))
                #     添加elt的参数
                    if index!=len(all)-1:
                        elt_params.append(item+','+all[index+1])
                    else:
                        elt_params.append(item + ',')
                # interval作为elt的第一个参数

                print(elt_params)

                entities.append(func.elt(func.interval(*interval_param),*elt_params).label(group))
                pass

        # entities.append(column(group))
    logger.debug('处理完聚合函数前:%s', str(query))
    #聚合字段要分割出聚合函数和字段
    for agg in aggfield:

        # sum_xxx,限制只能分割一次，因为有些字段名可能有_ ,label设置别名为传进来的原始参数，因为orderby是根据这个的
        aggtype_field=agg.split('-',1)
        logger.debug("处理聚合函数:,分割结果:%s",aggtype_field)
        print(aggtype_field)
        if aggtype_field[0]=='count':
            entities.append(func.count(column(aggtype_field[1].strip())).label(agg)  )
        if aggtype_field[0]=='sum':
            entities.append(func.sum(column(aggtype_field[1].strip())).cast(sqltype.Float).label(agg)  )
        if aggtype_field[0]=='avg':
            entities.append(func.avg(column(aggtype_field[1].strip())).cast(sqltype.Float).label(agg) )
    # 选择,with_entites是变长参数，这里解包列表进去

    query = query.with_entities(*entities)
    logger.debug('处理完聚合函数后:%s', query)
    #-------------------group by 分组字段处理 ----------------,普通分组和整数分段分组

    group_columns = []

    for group in groupfield:
        group_columns.append(column(group.strip()))




    query = query.group_by(*group_columns)

    # # 分组聚合
    # if len(fields)==1:
    #     col = fields[0]
    #     query = query.with_entities(column(col), aggcol).group_by(column(col))
    # else:
    #     col_1 = fields[0]
    #     col_2 = fields[1]
    #     query = query.with_entities(column(col_1), column(col_2),aggcol).group_by(
    #         column(col_1),column(col_2))
    # count最后只有一个series,先初始化
    # 计数给另外的名字



    # # 总人数
    # elif datatype == 'sum':
    #     # 传入所需要计数的字段，将其转换为英文
    #     col_1 = fields[0]
    #
    #     # 全校招生总人数 -- 传入考生号
    #     if col_1 == 'education_number':
    #         all_school = db.query_expression(func.count(col_1))
    #
    #     # 广东省各地区招生总人数
    #     elif col_1 == '':
    #         pass
    #
    #         # 广东省各地区招生总人数
    #
    #     # 外省各省总人数
    #     elif col_1 == '':
    #         pass
    print(query)
    return {
        'sql':query,
        'entities':list(map(lambda x:x.name, entities))
    }

def drawChart(query, chartType: str= '', dataType:str= '', groupfield: str= '', aggfield:str= '', filter:str= '', orderBy='', limit=-1,title=None,sql=None):

    logger.debug('drawChart,title:%s',title)
    print('数据类型:',dataType)



    groupfield_name = []
    aggfield_name = []

    dataset = None
    if dataType=='group':
        groupfield = groupfield.split(",")
        aggfield = aggfield.split(",")

        # 将分组字段和聚合字段转换为中文，如果可以的话
        for group in groupfield:
            if group in field_name.keys():
                groupfield_name.append(field_name[group])
            else:
                groupfield_name.append(group)
        for agg in aggfield:
            type_field = agg.split('-',1)
            aggname = ''
            logger.debug('聚合字段处理,分割结果:%s',type_field)
            if type_field[0] in aggType:
                aggname+=aggType[type_field[0]]
            else:
                aggname += type_field[0]

            if type_field[1] in field_name.keys():
                aggname+=field_name[type_field[1]]
            else:
                aggname += type_field[1]
            aggfield_name.append( aggname)


        #返回sql和选择的字段
        sql_entites = get_sql(query, chartType, groupfield, aggfield)
        # 元组表示错误
        if type(sql_entites) == tuple:
            return sql_entites
        sql = sql_entites['sql']
        entities = sql_entites['entities']

        print(sql_entites)
        if filter!='null':
            filter = filter.split(',')
            # --------------处理过滤----------
            for fil in filter:
                field_op_value=fil.split('-')
                print('处理过滤:',field_op_value)
                if field_op_value[1]=='==':
                    sql = sql.filter(column(field_op_value[0]).cast(sqltype.Integer)==int(field_op_value[2]))
                if field_op_value[1]=='>=':
                    sql = sql.filter(column(field_op_value[0]).cast(sqltype.Integer)>=int(field_op_value[2]))
                if field_op_value[1] == '<=':
                    sql = sql.filter(column(field_op_value[0]).cast(sqltype.Integer) <= int(field_op_value[2]))
                if field_op_value[1] == '>':
                    sql = sql.filter(column(field_op_value[0]).cast(sqltype.Integer) > int(field_op_value[2]))
                if field_op_value[1] == '<':
                    sql = sql.filter(column(field_op_value[0]).cast(sqltype.Integer) >= int(field_op_value[2]))
                if field_op_value[1] == '!=':
                    sql = sql.filter(column(field_op_value[0]).cast(sqltype.Integer) != int(field_op_value[2]))
                if field_op_value[1] == 'like':
                    sql = sql.filter(column(field_op_value[0]).like('%'+field_op_value[2]))
                if field_op_value[1] == 'contains':
                    sql = sql.filter(column(field_op_value[0]).contains('%' + field_op_value[2]))


        if orderBy != 'null':
            field_order = orderBy.split('+')
            col = column(field_order[0])
            # 降序
            if field_order[1] == 'desc':
                col = desc(col)
            #     升序
            else:
                col = asc(col)

            sql = sql.order_by(col)


        try:

            if int(limit) != -1:
                sql = sql.limit(int(limit))
        except Exception as e:
            print('limit 异常:',limit)
        print("请求sql:", sql)



        dataset = sql.all()
    #     不是分组，默认为sql语句
    elif dataType=='sql':
        result = db.session.execute(sql)
        dataset = result.fetchall()
        pass


    print('图表类型:',chartType)
    # 表格的直接返回dataset
    if chartType=='table':
        print(dataset)
        dataset.insert(0, aggfield2name( tuple(entities)))

        logger.debug("获取表格数据,头处理结果:%s",str(aggfield2name( tuple(entities))))
        return dataset


    # 不提供标题就根据字段生成默认标题
    if title==None:
        # 需要转换为中文
        title =   '按%s 分组,%s'%(''.join(groupfield_name),''.join(aggfield_name))
    select = All_Picture(groupfield, title, '', '', '地区名称')  # 设置标题等

    x = []
    y = []
    series_name = []

    # 类型1 ,简单分组计数
    '''
    全校男女比例
    全校政治面貌比例
    全校学年制比例
    全校各学院人数占比
    全校全国各个地区人数
    '''
    # 获取sql

    if dataset==None:
        logger.warning('dataset 数据集是None,图表类型:%s,数据类型:%s,标题:%s',chartType,dataType,title)
        raise Exception('dataset 数据集是None,图表类型:%s,数据类型:%s,标题:%s'%(chartType,dataType,title))


    logger.debug('获取图表%s,sql结果:'%title)
    logger.debug(dataset)

    if len(groupfield)==1:
        # count最后只有一个series,先初始化
        x.append([])
        y.append([])
        print('一个分组:')

        print(dataset)

        # 传递过来的是英文，装换为中文字段名字，作为图例,如果没有就算了

        if groupfield[0] in field_name:
            series_name=[ field_name[ groupfield[0]] ]
        else:
            series_name = [groupfield[0]]
        for item in dataset:
            x[0].append(item[0])
            # # y这些聚合的可能有几种，如一个平均，一个总和
            # for i in range(1,len(item)):
            #     y[0].append(item[i])
            y[0].append(item[1])


    #两个分组
    else:
        x.append([])
        print('两个分组，结果:')
        print(dataset)
        # 要求不能排序
        for item in dataset:
            if item[0] not in series_name:
                series_name.append(item[0])
                y.append([0] * len(x[0]))
            index = series_name.index(item[0])
            if item[1] not in x[0]:
                x[0].append(item[1])
                y[index].append(0)
            xindex = x[0].index(item[1])
            y[index][xindex] = item[2]

        # 填充系列长度到x轴的长度
        for index in range(0, len(y)):
            if len(y[index]) != len(x[0]):
                need_len = len(x[0]) - len(y[index])
                y[index].extend(need_len * [0])
    # #特殊的图表
    # # 自定义sql -- 分数区段->指向漏斗图
    # elif datatype == 'sql':
    #     x = ['450以上', '400-450', '350-400', '300-350', '200-300', '200以下']
    #     y = []
    #     # sql=sql.with_entities(zs.total_score_of_filing)
    #     dataset = db.session.execute(
    #         "select sex_name,count(case when total_score_of_filing> 450 then 1 end) as `[450分以上]`, count(case when total_score_of_filing between 400 and 450 then 1 end) as `[400-450分]`, count(case when total_score_of_filing between 350 and 400 then 1 end) as `[350-400分]`, count(case when total_score_of_filing between 300 and 350 then 1 end) as `[300-350分]`, count(case when total_score_of_filing between 200 and 300 then 1 end) as `[200-300分]`, count(case when total_score_of_filing <200 then 1 end) as `[200分以下]` from zs group by sex_name;").fetchall()
    #     for item in dataset:
    #         for i in item:
    #             y.append(i)
    #
    #     return  select.funnel_sort_ascending(x_data=x, y_data=y)
    #
    # #总人数
    # elif datatype == 'sum':
    #     #传入所需要计数的字段，将其转换为英文
    #     col_1 = fields[0]
    #
    #
    #     #全校招生总人数 -- 传入考生号
    #     if col_1=='education_number':
    #         all_school=db.query_expression(func.count(col_1))
    #
    #     # 广东省各地区招生总人数
    #     elif col_1=='':
    #         pass
    #
    #         #广东省各地区招生总人数
    #
    #     # 外省各省总人数
    #     elif col_1=='':
    #         pass



    # ----------数据处理后
    print("查询处理后数据:")
    print("series:", series_name)
    print("x:",x)
    print("y:", y)


    #饼图
    if chartType == 'pie':
        '''
            男女比例
            学年制比例      
        '''
        return select.pie_picture(series_name,x, y)


    #玫瑰图
    elif chartType== 'rose':
        '''
            政治面貌比例
        '''
        print(series_name)
        return select.rose_picture(series_name,x,y)

    #柱状图

    elif chartType == 'bar':
        '''
            院系招生人数TOP10
            专业招生人数TOP10
            广东省各地区招生人数TOP10
            外省招生人数TOP10
            按专业报考志愿排序人数TOP10
        '''
        # 只要一个x轴
        return select.bar_picture(series_name, x[0], y,stack=False)
    # 堆叠柱状图
    elif chartType == 'stackbar':
        return select.bar_picture(series_name, x[0], y, stack=True)
    elif chartType=='horizontal_bar':
        return select.bar_picture(series_name, x[0], y, stack=False,reverse=True)

    elif chartType=='horizontal_stackbar':
        return select.bar_picture(series_name, x[0], y, stack=True,reverse=True)
    #条形图
    elif chartType == 'pictorialbar':
        '''
            全校各学院人数占比
        '''
        return select.pictorialbar_base(x,y)



    #地图
    elif chartType == 'china_map':
        '''
            全国各地区人数比例
            
        '''
        return select.china_map_picture(series_name, x,y)


    #雷达图
    elif chartType == 'radar':
        '''
            各院系男女人数、比例
            各院系文理科人数、比例
        '''
        print("radar:", series_name)
        print(y)
        print(x)
        return select.radar_picture(series_name, y, x)

    #漏斗图
    elif chartType== 'funnel':
        '''
            全校广东学生文理科分数区间人数 -- 使用datatype == 'sql'
            
        '''
        return select.funnel_sort_ascending(x_data=x[0], y_data=y[0])

    #表格
    elif chartType== 'table':
        '''
            广东省各地区男女生比例  count2,两个group by。 
            广东省各地区文理科比例
            外省各省男女比例
            各院系各地区人数
        '''
        return select.table_picture(headers='',data='')


    #HTML返回总人数
    elif chartType== 'html':
        pass



@bp_main.route("/test")
def test():
    print(dir(zs))

    sql = zs.query.with_entities(zs.sex_name, func.count()).group_by(zs.sex_name).all()
    print(sql)
    return "aaa"


# 获取所有图表列表测试
@bp_main.route("/charts2",methods=['POST'])
@login_required
def charts2():

    print('表单:',request.form)
    print('args:',request.args)

    if 'recordid' not in request.form:
        return rjson('recordid 没有选择',1)

    # 4个参数
    try:
        recordid = request.form['recordid']
        charttype = request.form['chartType']
  #      datatype = request.form['dataType']
        groupfield = request.form['groupfield']
        aggfield = request.form['aggfield']
        filter = request.form['filter']

    except Exception as e:

        return rjson(str(e)+" "+str(e.args),1)
    orderBy = request.form['orderBy']
    limit = request.form['limit']

    logger.debug(dir(request.form))
    logger.debug('charts2 参数:%s'%request.form.to_dict())
    sql = zs.query.filter(zs.recordid == recordid)


    result = drawChart(sql, charttype, 'group', groupfield, aggfield, filter, orderBy, limit)

    # 如果返回的是元组，则表示返回的是错误信息
    if type(result) == tuple:
        return rjson(result[0], result[1])
    if result==None:
        return rjson("返回null", 1)

    # 如果是画图
    if charttype!='table':

        # option装字典
        result_dict = json.loads(result.dump_options())
        params = {}
        for key in ['chartType', 'groupfield', 'aggfield', 'orderBy', 'filter', 'limit', 'dataType']:
            if key in request.form:
                params[key] = request.form[key]
        # 要返回报告的数据结构
        item = ReportItem('chart', 0, 400, 400, 1, **params)
        # 设置生成的option
        item.option = result_dict

        pass
    elif charttype=='table':
        # 直接是返回dataset
        print('表格类型:')
        print(result)
        params = {}
        for key in ['chartType', 'groupfield', 'aggfield', 'orderBy', 'filter', 'limit', 'dataType']:
            if key in request.form:
                params[key] = request.form[key]
        # 要返回报告的数据结构
        item = ReportItem('table', 0, 800, 400, 1, **params)
        # 设置生成的option
        item.rows = result

        pass




    # x=[]
    # y=[]
    # a = All_Picture()
    # options = a.getchart( db,zsyear,chartid)
    #
    # sql = zs.query.with_entities(zs.sex_name,func.count()).group_by(zs.sex_name)
    # print(sql)
    # dataset = sql.all()
    # for item in dataset:
    #     x.append(item[0])
    #     y.append(item[1])
    #
    # result = a.bar_picture(x, y)
    # result_dict = json.loads(result)
    # test = db.session.execute("select sex_name,count(1) from zs group by sex_name;").fetchall()
    #
    # print(test)
    # print(dir(test))
    return rjson(item.to_dict(), 0)

from app.charts.zscharts import zschart

# 获取基本的图
@bp_main.route('/options/<type>')
def options(type):

    logger.debug('获取内置options,类型:%s'%type)
    # 招生数据
    if type=='zs':
        sql = zs.query.filter(zs.recordid==3)
        chart = zschart(sql,1)
        options = chart.options()
        # chart1 = drawChart(sql, 'bar', 'group', 'sex_name,departments', 'count_total_score_of_filing', 'null',
        #                    'null', -1)
        # print("返回option",options)
        return rjson(options,0)

# 导出的目录
export_dir=os.path.abspath('../report/download')

# 根据报告id , 导出报告,返回导出是否成功
@bp_main.route('/export/<int:id>')
@login_required
def export(id):

    if not os.path.exists(export_dir):
        logger.debug('建立下载文件夹:%s',export_dir)
        os.makedirs(export_dir)

    from app.report.models import Report
    report = Report.query.with_entities(Report.id,Report.data,Report.title,func.unix_timestamp(Report.title).label('time')).filter(Report.id==id).first()
    filename = '%s_%s_%s.docx' % (report.id,report.title,report.time)

    path = os.path.join(export_dir,filename)

    # 报告的数据
    jsondata = report.data
    jiexi_result = doc.jiexi(jsondata, report.title, path)
    logger.debug('导出结果:%s',jiexi_result)
    if os.path.exists(path):
        return rjson('导出成功',0)
    else:
        return rjson('导出失败',1)


from app.python_docx.mysql_docx import Mysql_docx

doc = Mysql_docx()
@bp_main.route('/download/<int:id>')
@login_required
def download(id):
    from app.report.models import Report
    report = Report.query.with_entities(Report.id, Report.title,
                                        func.unix_timestamp(Report.title).label('time')).filter(Report.id == id).first()
    filename = '%s_%s_%s.docx' % (report.id, report.title, report.time)
    path = os.path.join(export_dir, filename)
    logger.debug('下载报告路径：%s',path)
    return send_file(path,attachment_filename=filename,as_attachment=True)