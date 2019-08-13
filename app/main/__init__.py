# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:27 
from flask import Blueprint
import logging
# 在init 文件里初始化可以 在多个views文件里引入
bp_main = Blueprint('main',__name__)
logger = logging.getLogger('app.main')
from .views import *
from .chartview import *

