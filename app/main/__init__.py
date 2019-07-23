# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:27 
from flask import Blueprint
# 在init 文件里初始化可以 在多个views文件里引入
bp_main = Blueprint('main',__name__)

from .views import *
from .chartview import *