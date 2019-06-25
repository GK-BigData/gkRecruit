# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:18 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import config

db = SQLAlchemy()

def create_app():

    app = Flask(__name__,static_folder='static')
    app.config.from_object(config)


    # 导入各个模块
    from app.admin.views import  bp_admin
    app.register_blueprint(bp_admin,url_prefix='/admin')

    return app