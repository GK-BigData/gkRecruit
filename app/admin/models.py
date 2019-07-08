# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:36 
from app import db



# 记录表，存放各年的数据
class Record(db.Model):


    __tablename__='record'
    id = db.Column(db.Integer(),autoincrement=True,primary_key=True)
    time = db.Column(db.DateTime(),nullable=False)
    # 添加唯一约束，zs表用到他
    zsyear = db.Column(db.Integer,nullable=False,unique=True)
    status = db.Column(db.String(30))

    # 本地保存文件名
    filename=db.Column(db.String(20),nullable=False)
    # 记录数
    size = db.Column(db.Integer)

    # 从记录里选择需要的字段的，记录，下次更新数据时，直接读取上次的选择
    fields=db.Column(db.Text)


    # record表和zs表外键关联,这里的zss 代表这一年的所有zs 数据
    zss = db.relationship('zs',backref='record',lazy='dynamic')



