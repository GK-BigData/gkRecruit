# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:28 


from flask import Blueprint, render_template, request

from app.charts.all_picture import All_Picture
from app.common.restful import rjson
import json
from app.main.models import zs
from app import db
import sqlalchemy.sql.functions as func
from sqlalchemy.sql.expression import *
from sqlalchemy.sql.expression import *
import  sqlalchemy.sql.sqltypes   as sqltype

from app.common.mycolumns import needcolumns_fields, needcolumns_name
from . import bp_main

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


dataTypes={'count':'计数','count2':'两个字段分组计算'}
chartTypes={'bar':'柱状图','pie':'饼图','rose':'玫瑰图','stackbar':'堆叠柱状图'}

@bp_main.route("/")
def index():

    return render_template('main/main.html',columns = need_columns,dataTypes=dataTypes,chartTypes=chartTypes)


@bp_main.route("/charts")
def charts():
    zsyear = request.args['zsyear']
    chartid = request.args['chartid']

    a = All_Picture(chartid, '', '', '地区名称')

    sql = zs.query.filter(zs.zsyear == zsyear)
    result = None

    if chartid == '男女比例':
        x = []
        y = []
        # dataset = db.session.execute("select sex_name,count(1) from zs group by sex_name;").fetchall()
        sql = sql.with_entities(zs.sex_name, func.count()).group_by(zs.sex_name)
        print("sql语句:", sql)
        dataset = sql.all()
        for item in dataset:
            x.append(item[0])
            y.append(item[1])
        print("查询结果")
        print(x)
        print(y)
        result = a.pie_picture(x, y)

    elif chartid == '全国各个地区人数':
        x = []
        y = []

        # sql = sql.with_entities(zs.source_provinces, func.count()).group_by(zs.source_provinces).order_by(desc(column( 'count_1')))

        sql = sql.with_entities(zs.source_provinces, func.count()).group_by(zs.source_provinces)
        print('全国各个地区人数', sql)

        dataset = sql.all()
        # dataset=db.session.execute("select student_address ,count(1) as counts from zs group by student_address order by counts desc limit 10;")

        for item in dataset:
            x.append(item[0][:2])
            y.append(item[1])

        print("全国各个地区人数")
        print(x)
        print(y)
        result = a.china_map_picture(x, y)

    elif chartid == '各学院男女人数占比雷达图':
        women_data = []
        man_data = []
        departments = []
        sql = sql.with_entities(zs.departments, zs.sex_name, func.count()).group_by(zs.departments, zs.sex_name)
        dataset = sql.all()
        print(sql)

        for item in dataset:
            print(item)
            if item[0] not in departments:
                departments.append(item[0])

            if item[1] == '男':
                man_data.append(item[2])

            if item[1] == '女':
                women_data.append(item[2])

        print(departments)
        print(man_data)
        print(women_data)
        result = a.radar_picture(women_data, man_data, departments)

    elif chartid == '学年制':
        x = []
        y = []
        # dataset = db.session.execute("select sex_name,count(1) from zs group by sex_name;").fetchall()
        sql = sql.with_entities(zs.education__time, func.count()).group_by(zs.education__time)
        print("sql语句:", sql)
        dataset = sql.all()
        for item in dataset:
            x.append(item[0])
            y.append(item[1])
        print("查询结果")
        print(x)
        print(y)
        result = a.rose_picture(x, y)

    elif chartid == '男女人数排三的专业':
        x = []
        y = []
        man_data = []
        women_data = []
        dataset = db.session.execute(
            "(select major_name,sex_name,count(major_name) as counts from zs  where sex_name='男' group by major_name order by counts desc limit 3) UNION ALL (select major_name,sex_name,count(major_name) as counts from zs  where sex_name='女' group by major_name order by counts desc limit 3);")

        for item in dataset:
            if item[1] == '男':
                x.append(item[0])
                man_data.append(item[2])

            if item[1] == '女':
                y.append(item[0])
                women_data.append(item[2])
        print(man_data)
        print(women_data)
        print(x)
        result = a.rose_picture_man_women(x, y, man_data, women_data)

        # result =a.bar_base(x,man_data=man_data,women_data=women_data)

    elif chartid == '各学院人数占比':
        x = []
        y = []
        sql = sql.with_entities(zs.departments, func.count()).group_by(zs.departments)
        dataset = sql.all()
        print("department", sql)
        for item in dataset:
            x.append(item[0])
            y.append(item[1])
        result = a.pictorialbar_base(x, y)



    elif chartid == '各个投档分区段的人数':
        x = ['450以上', '400-450', '350-400', '300-350', '200-300', '200以下']
        y = []
        # sql=sql.with_entities(zs.total_score_of_filing)
        dataset = db.session.execute(
            "select count(case when total_score_of_filing> 450 then 1 end) as `[450分以上]`, count(case when total_score_of_filing between 400 and 450 then 1 end) as `[400-450分]`, count(case when total_score_of_filing between 350 and 400 then 1 end) as `[350-400分]`, count(case when total_score_of_filing between 300 and 350 then 1 end) as `[300-350分]`, count(case when total_score_of_filing between 200 and 300 then 1 end) as `[200-300分]`, count(case when total_score_of_filing <200 then 1 end) as `[200分以下]` from zs;").fetchall()
        for item in dataset:
            for i in item:
                y.append(i)
        print(x)
        print(y)

        result = a.funnel_sort_ascending(x_data=x, y_data=y)

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
    result_dict = json.loads(result)
    return rjson(result_dict, 0)


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
        entities.append(column(group))
    #聚合字段要分割出聚合函数和字段
    for agg in aggfield:

        # sum_xxx,限制只能分割一次，因为有些字段名可能有_ ,label设置别名为传进来的原始参数，因为orderby是根据这个的
        aggtype_field=agg.split('_',1)
        print("处理聚合函数:")
        print(aggtype_field)
        if aggtype_field[0]=='count':
            entities.append(func.count(column(aggtype_field[1])).label(agg)  )
        if aggtype_field[0]=='sum':
            entities.append(func.sum(column(aggtype_field[1])).label(agg)  )
        if aggtype_field[0]=='avg':
            entities.append(func.avg(column(aggtype_field[1])).cast(sqltype.Float).label(agg) )

    # 选择,with_entites是变长参数，这里解包列表进去
    query = query.with_entities(*entities)

    #-------------------group by 分组字段处理 ------------
    group_columns = []

    for group in groupfield:
        group_columns.append(column(group))


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
    return query

def drawChart(query, charttype: str, groupfield: str,aggfield:str, orderby='', limit=-1):

    groupfield = groupfield.split(",")
    aggfield = aggfield.split(",")
    #处理fields

    title = ','.join(groupfield)+'-'+'-'+charttype
    select = All_Picture(groupfield, title, '', '', '地区名称')  # 设置标题等

    x = []
    y = []
    series_name = []
    dataset = []

    # 类型1 ,简单分组计数
    '''
    全校男女比例
    全校政治面貌比例
    全校学年制比例
    全校各学院人数占比
    全校全国各个地区人数
    '''
    # 获取sql
    sql = get_sql(query,charttype,groupfield,aggfield)

    # 元组表示错误
    if type(sql)==tuple:
        return sql

    if orderby!='null':
        field_order = orderby.split('-')
        col = column(field_order[0])
        # 降序
        if field_order[1]=='desc':
            col = desc(col)
        #     升序
        else:
            col=asc(col)


        sql = sql.order_by(col)

    if limit!='-1':
        sql=sql.limit(int(limit))

    print("请求sql:",sql)
    # 计数类型的

    if len(groupfield)==1:
        # count最后只有一个series,先初始化
        x.append([])
        y.append([])
        print('一个分组:')
        dataset = sql.all()
        print(dataset)

        # 传递过来的是英文，装换为中文字段名字，作为图例
        series_name=[ field_name[ groupfield[0]] ]
        for item in dataset:
            x[0].append(item[0])
            y[0].append(item[1])
    #两个分组
    else:
        x.append([])
        dataset = sql.all()
        print('两个分组，结果:')
        print(dataset)
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
    if charttype == 'pie':
        '''
            男女比例
            学年制比例      
        '''
        return select.pie_picture(series_name,x, y)


    #玫瑰图
    elif charttype=='rose':
        '''
            政治面貌比例
        '''
        print(series_name)
        return select.rose_picture(series_name,x,y)

    #柱状图

    elif charttype == 'bar':
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
    elif charttype == 'stackbar':
        return select.bar_picture(series_name, x[0], y, stack=True)
    #条形图
    elif charttype == 'pictorialbar':
        '''
            全校各学院人数占比
        '''
        return select.pictorialbar_base(x,y)


    #地图
    elif charttype == 'china_map':
        '''
            全国各地区人数比例
            
        '''
        return select.china_map_picture(x,y)


    #雷达图
    elif charttype == 'radar':
        '''
            各院系男女人数、比例
            各院系文理科人数、比例
        '''
        print("radar:", series_name)
        print(y)
        print(x)
        return select.radar_picture(series_name, y, x)

    #漏斗图
    elif charttype=='funnel':
        '''
            全校广东学生文理科分数区间人数 -- 使用datatype == 'sql'
            
        '''
        return select.funnel_sort_ascending(x_data=x, y_data=y)

    #表格
    elif charttype=='table':
        '''
            广东省各地区男女生比例  count2,两个group by。 
            广东省各地区文理科比例
            外省各省男女比例
            各院系各地区人数
        '''
        return select.table_picture(headers='',data='')


    #HTML返回总人数
    elif charttype=='html':
        pass



@bp_main.route("/test")
def test():
    print(dir(zs))

    sql = zs.query.with_entities(zs.sex_name, func.count()).group_by(zs.sex_name).all()
    print(sql)
    return "aaa"


# 获取所有图表列表测试
@bp_main.route("/charts2",methods=['POST'])
def charts2():

    print('表单:',request.form)
    print('args:',request.args)

    if 'recordid' not in request.form:
        return rjson('recordid 没有选择',1)

    # 4个参数
    try:
        recordid = request.form['recordid']
        charttype = request.form['chartType']
        # datatype = request.form['dataType']
        groupfield = request.form['groupfield']
        aggfield = request.form['aggfield']

    except Exception as e:

        return rjson(str(e)+" "+str(e.args),1)
    orderBy = request.form['orderBy']
    limit = request.form['limit']



    sql = zs.query.filter(zs.recordid == recordid)
    result = drawChart(sql, charttype,groupfield,aggfield,orderBy,limit)
    # 如果返回的是元组，则表示返回的是错误信息
    if type(result)==tuple:
        return rjson(result[0],result[1])
    if result==None:
        return rjson("返回null", 1)
    result_dict = json.loads(result)


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
    return rjson(result_dict, 0)
