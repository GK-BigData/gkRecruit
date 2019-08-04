# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:18 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import config

from flask_uploads import UploadSet,configure_uploads,DOCUMENTS,IMAGES
import logging

db = SQLAlchemy()

upload_tables = UploadSet('TABLE',IMAGES+DOCUMENTS+('pdf','csv'))

# 配置主日志打印，模块共享这个,子模块获取app.xx
app_logger = logging.getLogger('app')
app_logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 添加标准输出流handler
stream_handler = logging.StreamHandler()
stream_handler.setFormatter(formatter)
app_logger.addHandler(stream_handler)

# 文件handler,写出日志到文件
file_handler = logging.FileHandler('日志.log')
file_handler.setFormatter(formatter)
app_logger.addHandler(file_handler)


# 测试
app_logger.debug('app init初始化 debug')
app_logger.info('app init初始化 info')
app_logger.warning('app init初始化 warn')
try:
    a = 1/0
except Exception as e:
    app_logger.error('app init初始化 info',exc_info=True)



def create_app():

    #初始化app
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)


    # 导入各个模块
    from app.main import bp_main
    from app.admin import  bp_admin

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