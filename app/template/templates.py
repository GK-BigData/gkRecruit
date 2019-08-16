# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/8/16 上午8:51 
# BY    :FormatFa

templates={'zs':'招生数据','custom':'自定义'}

# 获取模板的数据，字段形式 返回 姓名->student_name形式
def getFieldDict(template):
    fields = getFields(template)
    result = {}
    for field in fields:
        result[field[0]] = field[1]
    return result
# 获取模板的字段信息
def getFields(template):
    if template=='zs':
        return [('姓名', 'student_name'), ('教育部考生号', 'education_number'), ('性别名称', 'sex_name'), ('身份证号', 'id_card'),
                ('投档总分', 'total_score_of_filing'), ('排位', 'ranking'), ('录取专业', 'major_name'), ('报到注销', 'report'),
                ('报到/注销', 'report_for_cancel'), ('户口所在地', 'student_address'),
                ('毕业中学', 'graduation_secondary_school_name'),
                ('民族名称', 'nation_name'), ('政治面貌名称', 'political_appearance_name'), ('考生类型', 'student_type'),
                ('院系', 'departments'), ('学制', 'education__time'), ('来源省', 'source_provinces'),
                ('录取志愿', 'offer_volunteer'),
                ('专业1', 'Professional_1'), ('专业2', 'Professional_2'), ('专业3', 'Professional_3'),
                ('专业4', 'Professional_4'),
                ('专业5', 'Professional_5'), ('专业6', 'Professional_6')]

    return None

if __name__=='__main__':
    print(getFieldDict('zs'))




