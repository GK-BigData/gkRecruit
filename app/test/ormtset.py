# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/5 上午11:13 
# BY    :FormatFa

from app.main.models import zs


sql = zs.query.groupby(zs.sex_name)

print(sql)
