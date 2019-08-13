# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/8/10 上午10:27 
# BY    :FormatFa


from flask_login import UserMixin
from app import db

class User(db.Model,UserMixin):

    id=db.Column(db.String(20),primary_key=True)
    password = db.Column(db.String(100),nullable=False)
    email = db.Column(db.String(20))

    def __repr__(self):
        return '<user %r>' % id