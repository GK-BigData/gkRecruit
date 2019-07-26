# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:18 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import config

from flask_uploads import UploadSet,configure_uploads,DOCUMENTS,IMAGES

db = SQLAlchemy()

upload_tables = UploadSet('TABLE',IMAGES+DOCUMENTS+('pdf','csv'))

def create_app():

    #初始化app
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)


    # 导入各个模块
    from app.admin import  bp_admin
    from app.main import bp_main
    from app.testroute.views import bp_test
    from app.report import report_admin

    app.register_blueprint(bp_admin,url_prefix='/admin')
    app.register_blueprint(bp_main,url_prefix='/main')
    app.register_blueprint(bp_test,url_prefix='/test')
    app.register_blueprint(report_admin,url_prefix='/report')

    # 导入model，这里似乎没用，但在migrate时，要导入才找得到model
    from app.admin.models import Record
    from app.main.models import zs
    from app.report.models import Report

    # 配置上传插件
    configure_uploads(app,upload_tables)



    return app