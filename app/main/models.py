# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:28 

from app import db

class zs(db.Model):
    __tablename__='zs'
    id = db.Column(db.Integer(), autoincrement=True, primary_key=True)  # 总序号

    student_name=db.Column(db.String(225),nullable=False)            #姓名
    education_number=db.Column(db.String(225),nullable=False)       #教育部考生号
    sex_name=db.Column(db.String(225),nullable=False)               #性别名称
    id_card=db.Column(db.String(225))                #身份证 -- 目前没有
    total_score_of_filing = db.Column(db.Integer)   #投档总分
    ranking=db.Column(db.String(255))                                     #排位
    major_name=db.Column(db.String(225))             #录取专业（专业名称）
    report=db.Column(db.String(225))                                     #报道注销 -- 目前没有
    report_for_cancel=db.Column(db.String(225))                           #报道/注销  -- 目前没有
    student_address=db.Column(db.String(225))                           #户口所在地（地区名称）
    graduation_secondary_school_name=db.Column(db.String(225))          #毕业中学
    nation_name=db.Column(db.String(225))                               #民族
    political_appearance_name=db.Column(db.String(225))         #政治面貌名称
    student_type=db.Column(db.String(225))                      #考生类型
    departments=db.Column(db.String(225))                       #院系
    education__time=db.Column(db.String(225))                   #学制
    source_provinces=db.Column(db.String(225))                  #来源省份
    offer_volunteer=db.Column(db.String(225))                   #录取志愿
    Professional_1=db.Column(db.String(225))                    # 专业1
    Professional_2 = db.Column(db.String(225))                  # 专业2
    Professional_3 = db.Column(db.String(225))                  # 专业3
    Professional_4 = db.Column(db.String(225))                  # 专业4
    Professional_5 = db.Column(db.String(225))                  # 专业5
    Professional_6 = db.Column(db.String(225))                  # 专业6
    # 这个外键指向record表的zsyear字段
    zsyear = db.Column(db.Integer, db.ForeignKey("record.zsyear"),nullable=False)  # 年序号




