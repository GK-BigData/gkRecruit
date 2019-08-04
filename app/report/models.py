# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:28

from app import db

from sqlalchemy.orm.relationships import RelationshipProperty

# 记录表，存放各年的数据
class Report(db.Model):

    __tablename__='report'
    #唯一标识符
    id = db.Column(db.Integer,autoincrement=True,primary_key=True)
    #报告生成的标题
    title=db.Column(db.String(45))
    #报告生成的时间
    time = db.Column(db.DateTime(),nullable=False)
    # 报告模板类型
    template = db.Column(db.String(10),nullable=True)
    # 删除里后标记为1,实际上并没有删除
    isdelete = db.Column(db.Boolean,default=False)
    # 报告数据 
    data = db.Column(db.JSON())



    # report表和zs表外键关联,这里的report 代表这一年的所有zs 数据
    # report = db.relationship('zs', backref='record', lazy='dynamic', foreign_keys='zs.recordid')






