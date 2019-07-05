# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:28 


from flask import Blueprint,render_template

from app.charts.all_picture import All_Picture
from app.common.restful import rjson
import json
from app.main.models import zs
from app import db


import  sqlalchemy.sql.functions as func

bp_main = Blueprint('main',__name__)




@bp_main.route("/")
def index():
    return render_template('main/main.html')

@bp_main.route("/chart1/")
def chart1():
    zsyear=0
    chartid=''


    x=[]
    y=[]
    a = All_Picture()
    options = a.getchart( db,zsyear,chartid)

    sql = zs.query.with_entities(zs.sex_name,func.count()).group_by(zs.sex_name)
    print(sql)
    dataset = sql.all()
    for item in dataset:
        x.append(item[0])
        y.append(item[1])

    result = a.bar_picture(x, y)
    result_dict = json.loads(result)
    test = db.session.execute("select sex_name,count(1) from zs group by sex_name;").fetchall()

    print(test)
    print(dir(test))
    return rjson(result_dict,0)



