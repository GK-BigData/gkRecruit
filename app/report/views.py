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
import time
# 主界面，显示所有记录的界面
@report_admin.route("/")
def index():
    data = Report.query.all()
    print(data)
    result = []
    for item in data:
        result.append({'title':item.title,'id':item.id,'time':item.time})
    return render_template("report/report.html",data=data)

@report_admin.route('/data')
def data():
    data = Report.query.all()
    print(data)
    result = []
    for item in data:
        result.append({'title':item.title,'id':item.id,'time':item.time})

    return rjson(result,0)

# 获取所有报告
@report_admin.route('/reports',methods=['GET'])
def reports():
    pass
#获取单个报告
@report_admin.route('/reports/<id>')
def get_reports(id):
    time.sleep(5)
    report = Report.query.filter(Report.id == id).first_or_404()
    return rjson({
        'id':report.id,
        'data':report.data
    })

# 更新或者添加报告
@report_admin.route('/reports',methods=['POST'])
def update_report():

    time.sleep(10)

    # 报告id
    id = request.form['id']
    data = request.form['data']

    print('更新报告,id:', id)

    report = Report.query.filter(Report.id==id).first_or_404()

    report.data = data

    db.session.add(report)
    db.session.commit()


    return rjson('更新数据成功',1)
