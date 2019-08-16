# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/19 上午10:13 
# BY    :FormatFa

# etl上传数据这些

from . import bp_admin,need_columns,needcolumns_fields

from flask import Blueprint,render_template,jsonify,request,redirect,url_for
import os
from app.admin.models import Record
from app.main.models import zs
from app import db
from app.common.restful import rjson
from app import upload_tables

from app.common.excel_utils  import  get_columns,excel2dict,excel2list

import  sqlalchemy.sql.functions as func
from  sqlalchemy.sql.expression import *

import csv
import json
from datetime import datetime
from flask_login import current_user,login_required

from . import logger
from xpinyin import Pinyin

# 选择字段导入 ,
@bp_admin.route("/setfield/import",methods=['POST'])
@login_required
def importdata():




    recordid = request.form['recordid']

    field_columns = {}
    for col in needcolumns_fields:
        field_columns[col] = request.form[col]
    #     将选择的列保存起来，下次可以直接读取，str将所有变成字符串再join
    fields = ",".join(map( lambda  x:str(x),field_columns.values()))

    print("字段和 输入列的关系:",field_columns)


    record = Record.query.filter( and_(  Record.id==recordid, Record.userid==current_user.get_id())  ) .first()


    file = os.path.join('upload',record.filename)


    # excel转换为字典,只提取fields这些列名的
    excel_data = excel2list(file,columns=field_columns.values())




    try:

        #
        print("删除原始数据...")
        deleteresult = zs.query.filter(zs.recordid==recordid).delete()
        print("删除结果:",deleteresult)
        size = 0
        for row in excel_data:

            params={}
            for key in field_columns.keys():

                params[key] = row[ field_columns[key] ]


            params['recordid']=record.id
            #params['userid']=current_user.get_id()
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



py = Pinyin()
#     https://www.jianshu.com/p/9d6da9b76d70
@bp_admin.route("/upload",methods=['POST'])
@login_required
def upload():


    # 文件名名
    tablefile = request.files['table'].filename

    logger.debug('上传文件:%s',tablefile)

    # filename_py=pinyin.get_pinyin( tablefile)
    # 文件名暂时用年份来表示


    # --------------------------检查年的存不存在


    # result = Record.query.filter( and_(  Record.id==recordid, Record.userid==current_user.get_id())  ).first()
    #
    # if result:
    #     return rjson( zsyear+ "年的数据已存在",1)

    filename_py = py.get_pinyin(tablefile)
        #'2018' + os.path.splitext(tablefile)[1]
    # 指定保存的文件名为拼音处理后的
    filename = upload_tables.save(request.files['table'], name=filename_py)

    ab = os.path.abspath(os.path.join("upload", filename))
    logger.debug("保存路径:%s,拼音名:%s", ab,type(filename_py))

    try:


        record = Record(id=0,time=datetime.now(),status="未导入数据",filename=filename_py, title=tablefile, userid=current_user.get_id())


        # 尝试解析数据

        raw_columns = ','.join( get_columns(getUploadPath(filename)).keys())

        record.raw_fields=raw_columns

        db.session.add(record)




        print("开始提交数据....")
        db.session.commit()
    except Exception as e:
        logger.debug("发生异常,rollback回滚数据:%s",e,exc_info=True)
        db.session.rollback()
        return rjson("上传失败:"+str(e),1)









    return  rjson( "上传成功.")

def getUploadPath(filename):
    return os.path.join('upload',filename)