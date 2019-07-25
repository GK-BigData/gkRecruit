from flask import Blueprint,render_template,jsonify,request,redirect,url_for
import os
from app.report.models import Report
from app.main.models import zs
from app import db
from app.common.restful import rjson

from app import upload_tables
from xpinyin import Pinyin

from . import report_admin,need_columns,needcolumns_fields
from app.report.models import Report
from app.common.restful import rjson
# 主界面，显示所有记录的界面
@report_admin.route("/")
def index():

    return render_template("report/report.html")

@report_admin.route('/data')
def data():
    data = Report.query.all()
    print(data)
    result = []
    for item in data:
        result.append({'title':item.title,'id':item.id,'time':item.time})

    return rjson(result,0)