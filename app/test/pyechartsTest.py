# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/22 下午7:32 
# BY    :FormatFa

from pyecharts.charts import Bar,Line


b = Bar()
b.add_xaxis(['one','two','three'])
b.add_yaxis('s1',[1,2,3])


l = Line()
l.add_xaxis(['one','two','three','four'])
l.add_yaxis('s2',[1,2,3])

l.overlap(b)
print(b)
print(l.dump_options())

l.render('test.html')

