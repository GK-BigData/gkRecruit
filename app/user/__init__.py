# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/8/10 上午10:27 
# BY    :FormatFa
#用户登录管理

from flask import Blueprint
import logging

bp_user = Blueprint('user',__name__)
logger = logging.getLogger('app.user')

from .views import *
