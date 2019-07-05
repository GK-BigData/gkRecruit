# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:36 
from app import db



# 记录表，存放各年的数据
class Record(db.Model):


    __tablename__='record'
    id = db.Column(db.Integer(),autoincrement=True,primary_key=True)
    time = db.Column(db.DateTime(),nullable=False,primary_key=True)
    zsyear = db.Column(db.String(10))
    status = db.Column(db.String(30))
    # record表和zs表外键关联,这里的zss 代表这一年的所有zs 数据
    zss = db.relationship('zs',backref='record')



