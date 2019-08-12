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
from app.admin.models import Record

from app.common.restful import rjson
import time
from . import logger
from datetime import datetime

import  sqlalchemy.sql.functions as func
from sqlalchemy.sql.expression import *
from sqlalchemy import or_


from app.report.template_report import get_report_template

# 导入需要登录和当前用户
from flask_login import login_required,current_user

# 模板的类型，暂时只有招生数据的模板
report_templates={
    'zs':'招生数据',
    'null':'空'
}

# 主界面，显示所有记录的界面

@report_admin.route("/")
@login_required
def index():

    # 查询数据源
    dataset = Record.query.filter( Report.userid==current_user.get_id() ).all()
    records = {}
    for data in dataset:
        records[data.id] = '%s %s %s'%(data.id,data.zsyear,data.status)

    records['-1']='无'
    data = Report.query.all()
    result = []
    for item in data:
        result.append({'title':item.title,'id':item.id,'time':item.time})
    return render_template("report/report.html",data=data,templates=report_templates,records=records,current_user=current_user)

@report_admin.route('/data')
@login_required
def data():
    # 找出没有被删除的,isdelete>0的
    data = Report.query.filter( Report.userid==current_user.get_id()).with_entities(Report.id,Report.title, func.date_format( Report.time,'%Y-%m-%d %H:%i:%S').label('time')).filter( or_( Report.isdelete<1 , Report.isdelete==None))
    logger.debug('获取数据,sql'+str(data))
    data=data.all()
    result = []
    for item in data:
        result.append({'title':item.title,'id':item.id,'time':item.time})

    return rjson(result,0)

# 获取所有报告
@report_admin.route('/reports',methods=['GET'])
def reports():
    pass
# 删除报告
@report_admin.route('/reports/<int:id>',methods=['DELETE'])
@login_required
def delete_reprots(id):
    logger.debug('删除报告:%s',id)
    try:
        item = Report.query.filter( and_( Report.id == id,Report.userid==current_user.get_id())).first_or_404()
        logger.debug(item)
        item.isdelete=1
        db.session.add(item)
        db.session.commit()
    except Exception as e:
        logger.warning('删除报告异常:'+str(e))
    return rjson('删除成功',1)



#获取单个报告
@report_admin.route('/reports/<id>')
@login_required
def get_reports(id):
    time.sleep(5)
    report = Report.query.filter( and_( Report.id == id,Report.userid==current_user.get_id())).first_or_404()
    return rjson({
        'id':report.id,
        'data':report.data
    })

# 更新或者添加报告
@report_admin.route('/reports',methods=['POST'])
@login_required
def update_report():

    id = None
    try:
        id = request.form.get('id')
    except:
        pass

    print('id:',id)
    template='null'
    data = ''
    # 报告id



    # 添加数据
    if id==None:
        logger.debug('id 为空,添加报告数据..')
        # 新建需要提供模板和标题
        try:
            template = request.form.get('template', 'null')
            title = request.form.get('title')
            recordid = request.form.get('recordid')

        except Exception as e:
            logger.warning('update_report 更新,缺少参数', exc_info=True)
        nowtime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # 有模板表示要创建模板
        if template!='null':
            query  = zs.query.filter(zs.recordid==recordid)
            data = get_report_template(query,template,recordid)
            pass

        report = Report(id=id, data=data,title=title, template=template,time=nowtime,userid=current_user.get_id())

    else:

        report = Report.query.filter( and_( Report.id == id ,Report.userid==current_user.get_id())).first()
        if report==None:
            return rjson('id %d 不存在',1)
        # 更新有的数据
        if 'data' in request.form.keys():
            report.data = request.form['data']
        if 'title' in request.form.keys():
            report.title = request.form['title']
        if 'template' in request.form.keys():
            report.template = request.form['template']
        logger.debug('更新数据...')

    report.userid=current_user.id
    db.session.add(report)
    db.session.commit()


    return rjson('更新数据成功',1)
