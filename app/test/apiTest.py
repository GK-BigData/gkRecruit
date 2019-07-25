
import  requests
import pyecharts
import json
result = requests.post('http://127.0.0.1:5000/main/charts2?zsyear=2018&charttype=funnel&datatype=sql&fields=院系',
                       data={
                           'aggfield':'count_sex_name',
                            'groupfield':'interval-total_score_of_filing-0-100-200',
                           'chartType':'funnel',
                           'recordid':1,
                           'orderBy':'null',
                           'limit':-1,
                           # 'filter':'sex_name-like-男',
                           'filter':'null',
                           'dataType':'group'

                       })

# 整数分组测试
# result = requests.post('http://127.0.0.1:5000/main/charts2?zsyear=2018&charttype=funnel&datatype=sql&fields=院系',
#                        data={
#                            'aggfield':'count_sex_name',
#                             'groupfield':'interval-total_score_of_filing-0-100-200',
#                            'chartType':'bar',
#                            'recordid':1,
#                            'orderBy':'null',
#                            'limit':-1
#                        })


print(result.text)


html='''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
            <script type="text/javascript" src="echarts.js"></script>

</head>
<body>
    <div id="703a9c49431942aebad1569993e9ec62" style="width:900px; height:500px;"></div>
    <script>
        var chart_703a9c49431942aebad1569993e9ec62 = echarts.init(
            document.getElementById('703a9c49431942aebad1569993e9ec62'), 'light', {renderer: 'canvas'});
        var option_703a9c49431942aebad1569993e9ec62 = 配置;
        console.log(option_703a9c49431942aebad1569993e9ec62);
        chart_703a9c49431942aebad1569993e9ec62.setOption(option_703a9c49431942aebad1569993e9ec62.data);
    </script>
</body>
</html>'''


with open('a.html','w') as file:
    obj = json.loads(result.text)
    file.write(html.replace('配置',result.text))
