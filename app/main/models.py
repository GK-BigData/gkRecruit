# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 上午10:28 

from app import db

class zs(db.Model):
    __tablename__='zs'
    zsyear = db.Column(db.Integer())  # 总序号
    id = db.Column(db.Integer(),autoincrement=True,primary_key=True)   #总序号

    student_number = db.Column(db.String(),nullable=False)   #考生号
    student_name=db.Column(db.String(225),nullable=False)       #姓名
    education_number=db.Column(db.String(225),nullable=False)       #教育部考生号
    sex_number=db.Column(db.String(225),nullable=False)             #性别
    sex_name=db.Column(db.String(225),nullable=False)               #性别名称
    recruit_number=db.Column(db.String(225),nullable=False)         #录取科目号
    recruit_name=db.Column(db.String(225),nullable=False)           #录取科目名称
    recruit_score=db.Column(db.Float,nullable=False)            #录取科目总分数
    extra_poinss=db.Column(db.Float)                            #加分
    extra_poinss_features=db.Column(db.String(225))             #加分特征
    recruit_major_number=db.Column(db.String(225),nullable=False)   #录取专业号
    major_name=db.Column(db.String(225),nullable=False)             #专业名称
    student_address_number=db.Column(db.String(225),nullable=False) #户口所在地
    student_address=db.Column(db.String(225))                           # 地区名称
    section_core=db.Column(db.String(225))                          #科类代码
    section_name=db.Column(db.String(225),nullable=False) #科类名称
    birthday=db.Column(db.Time,nullable=False)
    graduation_secondary_school_number=db.Column(db.String(225))
    graduation_secondary_school_name=db.Column(db.String(225))
    provincial_middle_schools=db.Column(db.String(225))
    student_type_number=db.Column(db.String(225))
    student_type_name=db.Column(db.String(225))
    graduation_type_number=db.Column(db.String(225)) #毕业类别
    graduation_type_name=db.Column(db.String(225)) #毕业名字
    nation_number=db.Column(db.String(225)) #名族编号
    nation_name=db.Column(db.String(225))
    political_appearance_number=db.Column(db.String(225)) #政治面貌编码
    political_appearance_name=db.Column(db.String(225)) #政治面貌名称
    offer_type=db.Column(db.String(225)) #录取类型
    offer_number=db.Column(db.String(225)) #录取编号
    offer1=db.Column(db.String(225)) #录取1
    offer2 = db.Column(db.String(225))  # 录取2
    offer2_number = db.Column(db.String(225))  # 录取2编号
    offer_book_number=db.Column(db.String(225)) #录取通知书编号
    total_score_of_filing=db.Column(db.Integer,nullable=False) #投档总分
    major_number=db.Column(db.String(225)) #专业代码
    major_array=db.Column(db.String(225)) #专业序列
    departments=db.Column(db.String(225)) #学院
    departments_number=db.Column(db.String(225)) #学院编码
    School=db.Column(db.String(225)) #校区
    education__time=db.Column(db.String(225)) #学制
    source_provinces=db.Column(db.String(225)) #来源省份
    source_provinces1 = db.Column(db.String(225))  # 来源省份
    offer_volunteer=db.Column(db.String(225)) #录取志愿
    adjust=db.Column(db.String(225)) #调剂
    Professional_1=db.Column(db.String(225)) #专业1
    Professional_2 = db.Column(db.String(225))  # 专业2
    Professional_3 = db.Column(db.String(225))  # 专业3
    Professional_4 = db.Column(db.String(225))  # 专业4
    Professional_5 = db.Column(db.String(225))  # 专业5
    Professional_6 = db.Column(db.String(225))  # 专业6
    Past_Categories=db.Column(db.String(225))   #应往届类别
    countryside_town=db.Column(db.String(225)) #农村城镇类别



