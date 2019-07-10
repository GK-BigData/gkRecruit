# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:28 


from flask import Blueprint,render_template,request

from app.charts.all_picture import All_Picture
from app.common.restful import rjson
import json
from app.main.models import zs
from app import db
import  sqlalchemy.sql.functions as func
from  sqlalchemy.sql.expression import *

from sqlalchemy.sql.expression import *

bp_main = Blueprint('main',__name__)
from app.common.mycolumns import needcolumns_fields,needcolumns_name
need_columns = {}
for i in range(0, len(needcolumns_name)):
    need_columns[needcolumns_name[i]] = needcolumns_fields[i]

allcharts=["各学院男女人数占比雷达图",
           "各学院人数占比",
           "男女比例",
           "男女专业排三的专业",
           "政治面貌",
           "各个投档分区段的人数",
           "全国各个地区人数",
           "学年制",
           ]

@bp_main.route("/")
def index():
    return render_template('main/main.html')

@bp_main.route("/charts")
def charts():

    zsyear=request.args['zsyear']
    chartid=request.args['chartid']

    a = All_Picture(chartid,'','','地区名称')

    sql = zs.query.filter(zs.zsyear==zsyear)
    result=None

    if chartid=='男女比例':
        x = []
        y=[]
        # dataset = db.session.execute("select sex_name,count(1) from zs group by sex_name;").fetchall()
        sql = sql.with_entities(zs.sex_name,func.count()).group_by(zs.sex_name)
        print("sql语句:",sql)
        dataset = sql.all()
        for item in dataset:
            x.append(item[0])
            y.append(item[1])
        print("查询结果")
        print(x)
        print(y)
        result = a.pie_picture(x,y)

    elif chartid=='全国各个地区人数':
        x=[]
        y=[]

        #sql = sql.with_entities(zs.source_provinces, func.count()).group_by(zs.source_provinces).order_by(desc(column( 'count_1')))

        sql = sql.with_entities(zs.source_provinces, func.count()).group_by(zs.source_provinces)
        print('全国各个地区人数',sql)

        dataset=sql.all()
        #dataset=db.session.execute("select student_address ,count(1) as counts from zs group by student_address order by counts desc limit 10;")

        for item in dataset:
            x.append(item[0][:2])
            y.append(item[1])

        print("全国各个地区人数")
        print(x)
        print(y)
        result=a.china_map_picture(x,y)

    elif chartid=='各学院男女人数占比雷达图':
        women_data=[]
        man_data=[]
        departments=[]
        sql=sql.with_entities(zs.departments,zs.sex_name,func.count()).group_by(zs.departments,zs.sex_name)
        dataset=sql.all()
        print(sql)

        for item in dataset:
            print(item)
            if item[0] not in departments:
                departments.append(item[0])

            if item[1]=='男':
                man_data.append(item[2])

            if item[1]=='女':
                women_data.append(item[2])


        print(departments)
        print(man_data)
        print(women_data)
        result=a.radar_picture(women_data,man_data,departments)

    elif chartid=='学年制':
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

    elif chartid=='男女人数排三的专业':
        x=[]
        y=[]
        man_data=[]
        women_data=[]
        dataset=db.session.execute("(select major_name,sex_name,count(major_name) as counts from zs  where sex_name='男' group by major_name order by counts desc limit 3) UNION ALL (select major_name,sex_name,count(major_name) as counts from zs  where sex_name='女' group by major_name order by counts desc limit 3);")
        for item in dataset:
            if item[1]=='男':
                x.append(item[0])
                man_data.append(item[2])

            if item[1]=='女':
                y.append(item[0])
                women_data.append(item[2])
        print(man_data)
        print(women_data)
        print(x)
        result=a.rose_picture_man_women(x,y,man_data,women_data)

        #result =a.bar_base(x,man_data=man_data,women_data=women_data)

    elif chartid=='各学院人数占比':
        x=[]
        y=[]
        sql=sql.with_entities(zs.departments,func.count()).group_by(zs.departments)
        dataset=sql.all()
        print("department",sql)
        for item in dataset:
            x.append(item[0])
            y.append(item[1])
        result=a.pictorialbar_base(x,y)

    elif chartid=='政治面貌':
        x = []
        y = []
        # dataset = db.session.execute("select sex_name,count(1) from zs group by sex_name;").fetchall()
        sql = sql.with_entities(zs.political_appearance_name, func.count()).group_by(zs.political_appearance_name)
        print("sql语句:", sql)
        dataset = sql.all()
        for item in dataset:
            x.append(item[0])
            y.append(item[1])
        print("查询结果")
        print(x)
        print(y)
        result = a.pie_picture(x, y)

    elif chartid=='各个投档分区段的人数':
        x=['450以上','400-450','350-400','300-350','200-300','200以下']
        y=[]
        #sql=sql.with_entities(zs.total_score_of_filing)
        dataset=db.session.execute("select count(case when total_score_of_filing> 450 then 1 end) as `[450分以上]`, count(case when total_score_of_filing between 400 and 450 then 1 end) as `[400-450分]`, count(case when total_score_of_filing between 350 and 400 then 1 end) as `[350-400分]`, count(case when total_score_of_filing between 300 and 350 then 1 end) as `[300-350分]`, count(case when total_score_of_filing between 200 and 300 then 1 end) as `[200-300分]`, count(case when total_score_of_filing <200 then 1 end) as `[200分以下]` from zs;").fetchall()
        for item in dataset:
            for i in item:
                y.append(i)
        print(x)
        print(y)

        result =a.funnel_sort_ascending(x_data=x,y_data=y)

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
    return rjson(result_dict,0)


def drawChart(query, charttype:str,datatype:str,fields:str,orderby='',limit=-1):
    ''''''

    fields = fields.split(",")

    a = All_Picture('', '', '', '地区名称')

    x=[]
    y=[]
    dataset=[]
    # 类型1 ,简单分组计数
    if datatype=='count':
        col = need_columns[fields[0]]
        dataset = query.with_entities(column(col),func.count()).group_by(column(col))
        '''
        (男,100)
        '''
        for item in dataset:
            x.append(item[0])
            y.append(item[1])


        pass
    elif datatype=='count2':
        pass
    # 自定义sql
    elif datatype=='sql':
        pass

    if charttype=='pie':
        return a.pie_picture(dataset)
    elif charttype=='bar':
        return a.bar_picture(x,y)





@bp_main.route("/test")
def test():
    print(dir(zs))

    sql = zs.query.with_entities(zs.sex_name,func.count()).group_by(zs.sex_name).all()
    print(sql)
    return "aaa"
# 获取所有图表列表测试
@bp_main.route("/charts2")
def charts2():

    zsyear=request.args['zsyear']

    charttype=request.args['charttype']
    datatype = request.args['datatype']
    fields=request.args['fields']



    sql = zs.query.filter(zs.zsyear==zsyear)

    result=drawChart(sql,charttype,datatype,fields)


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
    return  rjson(result_dict,0)
