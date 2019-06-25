# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:30 

from flask import Blueprint,render_template,jsonify,request

from app.admin.models import Record

from app import db
from app.common.restful import rjson

#  这里使用 restful api http://www.pythondoc.com/flask-restful/first.html

bp_admin = Blueprint('admin',__name__)

@bp_admin.route("/")
def index():
    return render_template("admin/admin.html")


# 获取全部数据

@bp_admin.route("/records",methods=['GET'])
def get_records():

    datasets = Record.query.all()
    # 查询到的是Record对象，不能序列化
    result = []

    for data in datasets:
        result.append({
            "id":data.id,
            "time":data.time,
            "year":data.year,
            "status":data.status
        })
    #
    return rjson(result,0)

# 获取某个数据
@bp_admin.route("/records/<int:id>",methods=['GET'])
def get_record(id):
    pass



# 删除数据
@bp_admin.route('/records/<int:id>',methods=['DELETE'])
def delete_record(id):
    pass

# 添加数据
@bp_admin.route("/records",methods=['POST'])
def add_record():
    # data = request.form

    id = request.args['id']
    time = request.args['time']
    year = request.args['year']
    status = request.args['status']
    item = Record()
    item.id=id
    item.time=time
    item.year=year
    item.status=status

    print(type(db.session))
    db.session.add(item)

    db.session.commit()






    return "添加成功"