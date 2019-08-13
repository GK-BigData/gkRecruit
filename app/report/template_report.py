# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/8/4 上午9:46 

# 报告模板
import json
from app.charts.zscharts import  zschart
from app import db
def get_report_template(query,template,recordid):
    # 获取报告的模板
    # 招生
    if template=='zs':
        zs = zschart(query, recordid)
        options = zs.options()
#         options是title和element组成的字典列表，这里只需要element
        elements =[]
        for option in options:
            elements.append(option['element'])

        return json.dumps(elements)



