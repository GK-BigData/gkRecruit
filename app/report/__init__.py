
from flask import Blueprint
report_admin = Blueprint('report',__name__)

from app.common.mycolumns import needcolumns_fields,needcolumns_name

need_columns = {}
for i in range(0, len(needcolumns_name)):
    # need_columns['sex_name']=性别名称
    need_columns[needcolumns_fields[i]] = needcolumns_name[i]

from . import views
