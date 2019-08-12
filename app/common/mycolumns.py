# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/10 上午10:34 
# BY    :FormatFa


needcolumns_name = ['姓名', '教育部考生号', '性别名称', '身份证号', '投档总分', '排位', '录取专业', '报到注销', '报到/注销', '户口所在地', '毕业中学', '民族名称', '政治面貌名称', '考生类型', '院系', '学制', '来源省', '录取志愿', '专业1', '专业2', '专业3', '专业4', '专业5', '专业6']
needcolumns_fields=['student_name', 'education_number', 'sex_name', 'id_card', 'total_score_of_filing', 'ranking', 'major_name', 'report', 'report_for_cancel', 'student_address', 'graduation_secondary_school_name', 'nation_name', 'political_appearance_name', 'student_type', 'departments', 'education__time', 'source_provinces', 'offer_volunteer', 'Professional_1', 'Professional_2', 'Professional_3', 'Professional_4', 'Professional_5', 'Professional_6']
field_name = { field:name for field,name in zip(needcolumns_fields,needcolumns_name)}
aggType={'count':'计数','sum':'总和','avg':'平均值'}

chartTypes={'bar':'柱状图','horizontal_bar':'水平柱状图','pie':'饼图','rose':'玫瑰图','stackbar':'堆叠柱状图','horizontal_stackbar':'水平堆叠柱状图','table':'表格','china_map':'中国地图'}

# 聚合字段转名字
def aggfield2name(aggfield):
    result = []
    for field in aggfield:

        # 整数分割，特殊处理
        if field.startswith('interval-'):
            type_field = field.split('-')
            #第二个是字段名，应该是有的
            result.append('整数分组-'+field_name[type_field[1]])
            continue

        type_field = field.split('-',1)
        if len(type_field)==2:
                result.append(aggType[type_field[0]]+"_"+field_name[type_field[1]])

        else:
            #只有一个字段的
            if field in field_name:
                result.append(field_name[field])
            #后面可能有只有count这样的
            elif field in aggType:
                result.append(aggType[field])
            #实在没有就用英文
            else:
                result.append(field)
    return result



def field2name(type):
    pass