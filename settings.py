# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:19 

class Config(object):
    DEBUG=True
    DATABASE_URI=''

class ProductConfig(Config):
    pass

class DevelopmentConfig(Config):
    pass
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI=''

config=TestConfig()