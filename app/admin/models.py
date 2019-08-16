# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:36 
from app import db

from sqlalchemy.orm.relationships import RelationshipProperty

# 记录表，存放各年的数据
class Record(db.Model):

    __tablename__='record'
    id = db.Column(db.Integer(),autoincrement=True,primary_key=True)
    time = db.Column(db.DateTime(),nullable=False)


    status = db.Column(db.String(30))

    # 本地保存文件名
    filename=db.Column(db.String(255),nullable=False)
    # 前端显示文件标签
    title = db.Column(db.String(255),nullable=False)
    # 记录数
    size = db.Column(db.Integer)
    # 从记录里选择需要的列，记录，下次更新数据时，直接读取上次的选择
    fields=db.Column(db.Text)

    # 数据原始的字段,记录数据的类型，可以是内置的或者自定义的
    type=db.Column(db.String(20))
    raw_fields = db.Column(db.Text)
    userid = db.Column(db.ForeignKey('user.id'),nullable=False)

    # record表和zs表外键关联,这里的zss 代表这一年的所有zs 数据
    zss = db.relationship('zs',backref='record',lazy='dynamic',foreign_keys='zs.recordid')

