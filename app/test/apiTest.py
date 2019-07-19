
import  requests
import pyecharts
result = requests.get('http://127.0.0.1:5000/main/charts2?zsyear=2018&charttype=funnel&datatype=guangdong&fields=户口所在地')

print(result.text)


html='''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Awesome-pyecharts</title>
            <script type="text/javascript" src="https://assets.pyecharts.org/assets/echarts.min.js"></script>

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
    file.write(html.replace('配置',result.text))
