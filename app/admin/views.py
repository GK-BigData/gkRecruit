# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:30 

from flask import Blueprint,render_template,jsonify,request,redirect,url_for
import os
from app.admin.models import Record
from app.main.models import zs
from app import db
from app.common.restful import rjson
from app import upload_tables
from xpinyin import Pinyin
import csv
import json
from app.common.excel_utils  import  get_columns,excel2dict,excel2list
import  sqlalchemy.sql.functions as func
from  sqlalchemy.sql.expression import *

from flask_login import current_user,login_required
from sqlalchemy import and_
#  这里使用 restful api http://www.pythondoc.com/flask-restful/first.html

from . import bp_admin,need_columns,needcolumns_fields
from app.common.mycolumns import needcolumns_fields,needcolumns_name
pinyin = Pinyin()


# 主界面，显示所有记录的界面
@bp_admin.route("/")
@login_required
def index():
    return render_template("admin/admin.html")


# 获取某个数据类型可以用的字段
@bp_admin.route('/setfield/fields')
def get_fields():
#     现在只有一个
    print('获取填充字段....请求参数',request.args)
    id=request.args['id']
    type = request.args['type']

    nowrecord = Record.query.filter(  and_( Record.id==id ,Record.userid==current_user.id) ).first()
    filename = os.path.join("upload", nowrecord.filename)


    inputcolumns = get_columns(filename, previewsize=10)
    print(need_columns)
    print(inputcolumns)
    preview_data = []
    for field,values in inputcolumns.items():
        preview_data.append({
            'field':field,
            'values':values
        })




    # fields是空的话,就进行推断,将需要的字段 和 输入的字段进行匹配


    fields = nowrecord.fields
    print("数据库的的 fields", fields)
    if fields == None:
        fields = caculateFields(need_columns, inputcolumns)
    else:
        fields = fields.split(",")

    if type=='zs':
        vue_fields = []
        for field, name, value in zip(needcolumns_fields, needcolumns_name, fields):
            vue_fields.append({
                'field': field,
                'name': name,
                'desc': name
            })

        return rjson({
            'fields':vue_fields,
            'values':fields,
            'preview_data':preview_data
        },0)



# 修改字段导入数据 界面
@bp_admin.route("/setfield/<int:id>")
@login_required
def setfield(id):

    """
    解析excel 选择字段，导入到数据库
    :param zsyear:
    :return:
    """

    nowrecord = Record.query.filter(  and_( Record.id==id ,Record.userid==current_user.id) ).first()

    if nowrecord==None:
        return redirect(url_for('admin.index'))
    fields = nowrecord.fields


    # filename = os.path.join("upload", nowrecord.filename)
    #
    #
    # print("打开文件:",filename)
    # # 获取预览数据,字典格式,键为 列名，值是数组列表
    # inputcolumns = get_columns(filename,previewsize=10)
    # print(need_columns)
    # print(inputcolumns)
    #
    # print("数据库的的 fields",fields)
    #
    # # fields是空的话,就进行推断,将需要的字段 和 输入的字段进行匹配
    #
    # if fields==None:
    #     fields=caculateFields(need_columns,inputcolumns)
    # else:
    #     fields=fields.split(",")
    #
    # print("处理有fields",fields)



    # preview是 inputcolumns的json字符串
    # return render_template("admin/setfield.html",
    #                        zsyear=nowrecord.zsyear,
    #                        need_columns=need_columns,
    #                        needcolumns_fields=needcolumns_fields, inputcolumns=inputcolumns,preview=json.dumps(inputcolumns),
    #                        fileds = fields)
    return render_template('admin/import.html',zsyear=nowrecord.zsyear,recordid=nowrecord.id)


def caculateFields(need_columns:dict,inputcolumns:dict)->list:
    '''
    根据字段推断出可能选什么，待优化现在只是判断字段名一致的
    :param need_columns:
    :param inputcolumns:
    :return:
    '''
    result=[]
    # need_columns.values的需要的中文键
    for col in need_columns.values():

        #输入的键里有 需要的列的话，就将这个键设置为当前选择的
        if col in inputcolumns.keys():
            result.append(col)
        else:

            # 招生字段推测

            # if col=='民族'

            result.append( '')
    return result



# 获取全部数据
@bp_admin.route("/records_html",methods=['GET'])
@login_required
def get_records2():

    datasets = Record.query.filter(Record.userid==current_user.get_id()).all()
    # 查询到的是Record对象，不能序列化
    result = []

    for data in datasets:
        print(dir(data))
        result.append({
            "id":data.id,
            "time":data.time,
            "zsyear":data.zsyear,
            "status":data.status
        })
    #
    return render_template("admin/item_record.html",records=datasets)


# 获取全部数据
@bp_admin.route("/records",methods=['GET'])
@login_required
def get_records():

    datasets = Record.query.filter(Record.userid==current_user.get_id()).all()
    # 查询到的是Record对象，不能序列化
    result = []
    for data in datasets:
        print(dir(data))
        result.append({
            "id":data.id,
            "time":data.time,
            "zsyear":data.zsyear,
            "status":data.status
        })
    #
    return rjson(result,0)


# 获取某个预览数据
@bp_admin.route("/preview/<int:id>",methods=['GET'])
@login_required
def preview(id):
    # 返回类型，返回json还是html表格
    type=request.args['type']

    item = Record.query.filter(  and_( Record.id==id,Record.userid==current_user.get_id())  ).first()
    zsyear = item.zsyear

    students = zs.query.filter(zs.zsyear==zsyear).order_by(func.rand()).limit(10).all()

    print(students[:10])

    if type=='json':
        return rjson(students,0)
    else:
        return render_template('admin/preview.html',students=students , need_column=need_columns)


# 删除数据
@bp_admin.route('/records/<int:id>',methods=['DELETE'])
@login_required
def delete_record(id):
    try:
        item = Record.query.filter(  and_( Record.id == id,Record.userid==current_user.get_id())).first()
        # 先删除招生数据再删除记录
        zss = zs.query.filter(zs.zsyear==item.zsyear).delete()

        result = db.session.delete(item)

        print("删除结果:",zss)
        db.session.commit()
    except Exception as e:
        return rjson("错误:{}".format(str(e)), 1)
    return rjson("删除成功", 0)

# 添加数据
@bp_admin.route("/records",methods=['POST'])
@login_required
def add_record():
    # data = request.form

    id = request.args['id']
    time = request.args['time']
    zsyear = request.args['zsyear']
    status = request.args['status']
    item = Record()
    item.id=id
    item.time=time
    item.zsyear=zsyear
    item.status=status
    item.size=0
    item.userid=current_user.get_id()


    print(type(db.session))
    db.session.add(item)

    db.session.commit()
    return "添加成功"









def parse_csv(path,year):

    reader = csv.DictReader(open(path,"r"))
    # 需要的字段
    fields_name = ['考生号', '姓名', '教育部考生号', '性别', '性别名称', '录取科目号', '录取科目名称', '录取科目总分数', '加分', '加分特征', '录取专业号', '专业名称',
                   '户口所在地', '地区名称', '科类代码', '科类名称', '出生日期', '毕业中学号', '中学名称', '外省中学', '考生类别', '考生类别名称', '毕业类别', '毕业类别名称',
                   '民族', '民族名称', '政治面貌', '政治面貌名称', '录取类型', '录取编号', '录取1', '录取2', '录取2编号', '录取通知书编号', '投档总分', '专业代码',
                   '专序', '院系', '院系序号', '校区', '学制', '来源省', '来源省1', '录取志愿', '调剂', '专业1', '专业2', '专业3', '专业4', '专业5',
                   '专业6', '应往届类别', '农村城镇类别']
    fields = ['student_number', 'student_name', 'education_number', 'sex_number', 'sex_name', 'recruit_number',
              'recruit_name', 'recruit_score', 'extra_poinss', 'extra_poinss_features', 'recruit_major_number',
              'major_name', 'student_address_number', 'student_address', 'section_core', 'section_name', 'birthday',
              'graduation_secondary_school_number', 'graduation_secondary_school_name', 'provincial_middle_schools',
              'student_type_number', 'student_type_name', 'graduation_type_number', 'graduation_type_name',
              'nation_number', 'nation_name', 'political_appearance_number', 'political_appearance_name', 'offer_type',
              'offer_number', 'offer1', 'offer2', 'offer2_number', 'offer_book_number', 'total_score_of_filing',
              'major_number', 'major_array', 'departments', 'departments_number', 'School', 'education__time',
              'source_provinces', 'source_provinces1', 'offer_volunteer', 'adjust', 'Professional_1', 'Professional_2',
              'Professional_3', 'Professional_4', 'Professional_5', 'Professional_6', 'Past_Categories',
              'countryside_town']
    for row in reader:
        item = {}
        # 遍历所有数据库字段
        for i in range(0, len(fields)):
            # 如果
            if fields_name[i] in row.keys() and  row[fields_name[i]]!='':
                item[fields[i]] = row[fields_name[i]]
            else:
                item[fields[i]] = None
        item['zsyear']=year
        item['student_name']="*"
        zsitem  = zs(**item)
        db.session.add(zsitem)


# 解析数据
def parseTable(path):



    pass

def printArgs(where):
    print("from:",where)
    print("args:",request.args)
    print("form:",request.form)



