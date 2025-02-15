# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/8/10 上午10:27 
# BY    :FormatFa


from . import bp_user,logger
from flask import render_template,request,redirect,url_for
from app.common.restful import rjson

from app import login_manager
from app.user.models import User

from app.report.models import Report
from app.admin.models import Record

import  sqlalchemy.sql.functions  as func

from flask_login import login_user,logout_user,current_user,login_required
@bp_user.route('/login')
def index():
    return render_template('user/login.html')

@bp_user.route('logout')
def logout():
    logout_user()
    return redirect(url_for('user.index'))

@bp_user.route('/loginuser',methods=['POST'])
def loginuser():

    logger.debug(request.form.to_dict())
    id = request.form['id']
    password = request.form['password']

    #验证是否登录成功
    if id!=password:
        return rjson('用户名或密码错误',1)

    user = User.query.filter(User.id==id).first()

    if user==None:

        return rjson('用户不存在(User not exists!)',1)
    logger.debug('登录用户:%s', user)
    #登录用户，添加用户到session中，需要传入User对象
    login_user(user)

    logger.debug('登录,user:%s,password:%s',id,password)

    # return rjson('登录成功',1)，重定向到报告界面,
    url = url_for('report.index')
    print(url)
    return redirect(url)


#接受用户id，返回对象
@login_manager.user_loader
def load_user(id):
    logger.debug('login user:%s',id)
    user = User.query.filter(User.id==id).first()
    return user


@bp_user.route('/unauthrized')
def unauthorized():
    return render_template('user/unauthorized.html')
from app import db
# 获取使用者基本信息,包括 记录数，报告数,定义为在全部模板里都可用

@bp_user.app_context_processor
def info():
    report_count = Report.query.filter(Report.userid==current_user.get_id()).with_entities(func.count(Report.id)).first()[0]
    record_count = Record.query.filter(Record.userid == current_user.get_id()).with_entities(func.count(Record.id)).first()[0]
    logger.debug('获取使用折信息,记录数:%s,报告数: %s',record_count,report_count)

    return {
        'report_count':report_count,
        'record_count':record_count
    }

