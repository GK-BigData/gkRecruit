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

bp_main = Blueprint('main',__name__)

allcharts=["各学院男女人数占比雷达图",
           "各学院人数占比柱状图",
           "男女比例",
           "男女人数专业排三的专业",
           "政治面貌",
           "投档分直方图",
           "全国各个地区人数",
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
        sql=sql.with_entities(zs.student_address,func.count()).group_by(zs.student_address)
        print('全国各个地区人数',sql)
        dataset=sql.limit(10)
        for item in dataset:
            x.append(item[0])
            y.append(item[1])
        print("全国各个地区人数")
        print(x)
        print(y)
        result=a.bar_picture(x,y)




    #
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



