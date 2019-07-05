# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:18 

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from settings import config

from flask_uploads import UploadSet,configure_uploads,DOCUMENTS,IMAGES

db = SQLAlchemy()

upload_tables = UploadSet('TABLE',IMAGES+DOCUMENTS+('pdf','csv'
                                                    ))

def create_app():

    #初始化app
    app = Flask(__name__)
    app.config.from_object(config)

    db.init_app(app)


    # 导入各个模块
    from app.admin.views import  bp_admin
    app.register_blueprint(bp_admin,url_prefix='/admin')
    from app.admin.models import Record
    from app.main.models import zs

    # 配置上传插件
    configure_uploads(app,upload_tables)



    return app