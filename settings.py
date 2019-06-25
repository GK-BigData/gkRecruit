# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:19 

class Config(object):
    DEBUG=True
    DATABASE_URI=''
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@192.168.3.25:3306/recruit'

class ProductConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass
class TestConfig(Config):

    SQLALCHEMY_DATABASE_URI='mysql+pymysql://root:123456@192.168.3.25:3306/recruit'



config=TestConfig()