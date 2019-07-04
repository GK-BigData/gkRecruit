# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/27 上午9:37 

import csv

file = open("/home/formatfa/Documents/Project/zs/upload/2018.csv",'r')
fields_name = ['考生号', '姓名', '教育部考生号', '性别', '性别名称', '录取科目号', '录取科目名称', '录取科目总分数', '加分', '加分特征', '录取专业号', '专业名称', '户口所在地', '地区名称', '科类代码', '科类名称', '出生日期', '毕业中学号', '中学名称', '外省中学', '考生类别', '考生类别名称', '毕业类别', '毕业类别名称', '民族', '民族名称', '政治面貌', '政治面貌名称', '录取类型', '录取编号', '录取1', '录取2', '录取2编号', '录取通知书编号', '投档总分', '专业代码', '专序', '院系', '院系序号', '校区', '学制', '来源省', '来源省1', '录取志愿', '调剂', '专业1', '专业2', '专业3', '专业4', '专业5', '专业6', '应往届类别', '农村城镇类别']
fields = ['student_number', 'student_name', 'education_number', 'sex_number', 'sex_name', 'recruit_number', 'recruit_name', 'recruit_score', 'extra_poinss', 'extra_poinss_features', 'recruit_major_number', 'major_name', 'student_address_number', 'student_address', 'section_core', 'section_name', 'birthday', 'graduation_secondary_school_number', 'graduation_secondary_school_name', 'provincial_middle_schools', 'student_type_number', 'student_type_name', 'graduation_type_number', 'graduation_type_name', 'nation_number', 'nation_name', 'political_appearance_number', 'political_appearance_name', 'offer_type', 'offer_number', 'offer1', 'offer2', 'offer2_number', 'offer_book_number', 'total_score_of_filing', 'major_number', 'major_array', 'departments', 'departments_number', 'School', 'education__time', 'source_provinces', 'source_provinces1', 'offer_volunteer', 'adjust', 'Professional_1', 'Professional_2', 'Professional_3', 'Professional_4', 'Professional_5', 'Professional_6', 'Past_Categories', 'countryside_town']
reader = csv.DictReader(file)
for item in reader.fieldnames:
     print(item)
print(len(reader.fieldnames))
print(reader.line_num)
print(dir(reader))
#
for row in reader:
     item = {}
     for i in range(0,len(fields)):

          if fields_name[i] in row.keys():
               item[fields[i]] = row[fields_name[i]]
          else:
               item[fields[i]] = None
     print(item)





print('\t'.join(fields_name))
print('\t'.join(fields))
#
print('''考生号
姓名
教育部考生号
性别
性别名称
录取科目号
录取科目名称
录取科目总分数
加分
加分特征
录取专业号
专业名称
户口所在地
地区名称
科类代码
科类名称
出生日期
毕业中学号
中学名称
外省中学
考生类别
考生类别名称
毕业类别
毕业类别名称
民族
民族名称
政治面貌
政治面貌名称
录取类型
录取编号
录取1
录取2
录取2编号
录取通知书编号
投档总分
专业代码
专序
院系
院系序号
校区
学制
来源省
来源省1
录取志愿
调剂
专业1
专业2
专业3
专业4
专业5
专业6
应往届类别
农村城镇类别
'''.split("\n"))

print('''student_number
student_name
education_number
sex_number
sex_name
recruit_number
recruit_name
recruit_score
extra_poinss
extra_poinss_features
recruit_major_number
major_name
student_address_number
student_address
section_core
section_name
birthday
graduation_secondary_school_number
graduation_secondary_school_name
provincial_middle_schools
student_type_number
student_type_name
graduation_type_number
graduation_type_name
nation_number
nation_name
political_appearance_number
political_appearance_name
offer_type
offer_number
offer1
offer2
offer2_number
offer_book_number
total_score_of_filing
major_number
major_array
departments
departments_number
School
education__time
source_provinces
source_provinces1
offer_volunteer
adjust
Professional_1
Professional_2
Professional_3
Professional_4
Professional_5
Professional_6
Past_Categories
countryside_town
'''.split("\n"))

