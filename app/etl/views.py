# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/18 下午5:09 

from flask import Blueprint

bp_admin = Blueprint('etl',__name__)


@bp_admin.route('/fields')
def fields():

    pass
