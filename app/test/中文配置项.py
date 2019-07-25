dict = '''
color,颜色
title,标题
series,序列
markArea,标记区域
markLine,标记线
'''
for line in dict.split('\n'):
    en_ch = line.split(',')
    if len(en_ch)!=2:
        continue
    s="  '%s':'%s',"%(en_ch[0],en_ch[1])
    print(s)