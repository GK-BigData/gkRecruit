# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:30 

from flask import Blueprint,render_template



bp_admin = Blueprint('admin',__name__)

@bp_admin.route("/")
def index():
    return "测试"