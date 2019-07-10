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
import xlrd
import json


from datetime import datetime

from app.common.excel_utils  import  get_columns,excel2dict,excel2list

import  sqlalchemy.sql.functions as func
from  sqlalchemy.sql.expression import *
#  这里使用 restful api http://www.pythondoc.com/flask-restful/first.html

bp_admin = Blueprint('admin',__name__)
pinyin = Pinyin()

from app.common.mycolumns import needcolumns_fields,needcolumns_name

need_columns = {}
for i in range(0, len(needcolumns_name)):
    need_columns[needcolumns_fields[i]] = needcolumns_name[i]


# 主界面，显示所有记录的界面
@bp_admin.route("/")
def index():
    return render_template("admin/admin.html")



# 修改字段导入数据 界面
@bp_admin.route("/setfield/<int:id>")
def setfield(id):

    """
    解析excel 选择字段，导入到数据库
    :param zsyear:
    :return:
    """

    nowrecord = Record.query.filter(Record.id==id).first()

    if nowrecord==None:
        return redirect(url_for('admin.index'))
    fields = nowrecord.fields


    filename = os.path.join("upload", nowrecord.filename)


    print("打开文件:",filename)
    # 获取预览数据,字典格式,键为 列名，值是数组列表
    inputcolumns = get_columns(filename)
    print(need_columns)
    print(inputcolumns)

    print("数据库的的 fields",fields)
    # fields是空的话,就进行推断,将需要的字段 和 输入的字段进行匹配
    if fields==None:
        fields=caculateFields(need_columns,inputcolumns)
    else:
        fields=fields.split(",")

    print("处理有fields",fields)
    # preview是 inputcolumns的json字符串
    return render_template("admin/setfield.html",
                           zsyear=nowrecord.zsyear,
                           need_columns=need_columns,
                           needcolumns_fields=needcolumns_fields, inputcolumns=inputcolumns,preview=json.dumps(inputcolumns),
                           fileds = fields)

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
            result.append( '')
    return result





# 获取全部数据
@bp_admin.route("/records_html",methods=['GET'])
def get_records2():

    datasets = Record.query.all()
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
def get_records():

    datasets = Record.query.all()
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
def preview(id):
    # 返回类型，返回json还是html表格
    type=request.args['type']

    item = Record.query.filter(Record.id==id).first()
    zsyear = item.zsyear

    students = zs.query.filter(zs.zsyear==zsyear).order_by(func.rand()).limit(10).all()

    print(students[:10])

    if type=='json':
        return rjson(students,0)
    else:
        return render_template('admin/preview.html',students=students , need_column=need_columns)


# 删除数据
@bp_admin.route('/records/<int:id>',methods=['DELETE'])
def delete_record(id):
    try:
        item = Record.query.filter(Record.id == id).first()
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


    print(type(db.session))
    db.session.add(item)

    db.session.commit()
    return "添加成功"





# 选择字段导入 ,
@bp_admin.route("/setfield/import",methods=['POST'])
def importdata():


    printArgs("导入数据:")
    zsyear = request.form['zsyear']
    field_columns = {}
    for col in needcolumns_fields:
        field_columns[col] = request.form[col]
    #     将选择的列保存起来，下次可以直接读取，str将所有变成字符串再join
    fields = ",".join(map( lambda  x:str(x),field_columns.values()))

    print("字段和 输入列的关系:",field_columns)





    record = Record.query.filter(Record.zsyear==zsyear).first()


    file = os.path.join('upload',record.filename)


    # excel转换为字典,只提取fields这些列名的
    excel_data = excel2list(file,columns=field_columns.values())




    try:

        #
        print("删除原始数据...")
        deleteresult = zs.query.filter(zs.zsyear==zsyear).delete()
        print("删除结果:",deleteresult)
        size = 0
        for row in excel_data:

            params={}
            for key in field_columns.keys():

                params[key] = row[ field_columns[key] ]

            params['zsyear']=zsyear
            zsitem = zs(**params)
            db.session.add(zsitem)
            size+=1

        print("开始提交数据...")

        # 更新记录数和选择的字段
        record.size=size
        record.fields=fields
        record.status='已导入数据'
        print("更新数据:",record)

        db.session.commit()
        return rjson("导入数据成功,共导入"+str(size)+"条数据", 0)
    except Exception as e:
        print("发生异常:回滚数据",e)
        db.session.rollback()
        return rjson("导入数据失败:"+str(e),1)


#     https://www.jianshu.com/p/9d6da9b76d70
@bp_admin.route("/upload",methods=['POST'])
def upload():
    pass
    print(request.files)
    print(request.args)
    print(request.form)

    # 文件名名
    tablefile = request.files['table'].filename
    zsyear = request.form['zsyear']

    # filename_py=pinyin.get_pinyin( tablefile)
    # 文件名暂时用年份来表示



    # --------------------------检查年的存不存在


    result = Record.query.filter(Record.zsyear==zsyear).first()

    if result:
        return rjson( zsyear+ "年的数据已存在",1)

    filename_py = zsyear + os.path.splitext(tablefile)[1]
    # 指定保存的文件名为拼音处理后的
    filename = upload_tables.save(request.files['table'], name=filename_py)
    print(filename)
    ab = os.path.abspath(os.path.join("upload", filename))
    print("保存路径:", ab)



    try:
        # parse_csv(ab,zsyear)

        record = Record(id=0,time=datetime.now(),zsyear=zsyear,status="未导入数据",filename=filename_py)
        print(record)
        print("查询结果:",result)

        # 尝试解析数据

        raw_columns = ','.join( get_columns(getUploadPath(filename)).keys())

        record.raw_fields=raw_columns

        db.session.add(record)




        print("开始提交数据....")
        db.session.commit()
    except Exception as e:
        print("发生异常,rollback回滚数据:",e)
        db.session.rollback()
        return rjson("上传失败:"+str(e),1)
        pass








    return  rjson( "上传成功.")



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



def getUploadPath(filename):
    return os.path.join('upload',filename)