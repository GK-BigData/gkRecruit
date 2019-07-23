# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:27
# 后台管理页面
from flask import Blueprint
bp_admin = Blueprint('admin',__name__)

from app.common.mycolumns import needcolumns_fields,needcolumns_name

need_columns = {}
for i in range(0, len(needcolumns_name)):
    # need_columns['sex_name']=性别名称
    need_columns[needcolumns_fields[i]] = needcolumns_name[i]

from . import views
from . import etlviews