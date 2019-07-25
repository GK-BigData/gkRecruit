# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:19 

class Config(object):
    DEBUG=True
    DATABASE_URI=''
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:gkbigdata123456@172.16.1.255:3306:3306/recruit'

    # 配置允许上传的文件

    UPLOADED_TABLE_DEST = "upload"
    # UPLOADED_TABLE_ALLOW=("xls", "xlsx", 'csv','pdf')



class ProductConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass
class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.3.7:3306/recruit'



config=TestConfig()