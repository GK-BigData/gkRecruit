
import  requests
import pyecharts
result = requests.get('http://127.0.0.1:5000/main/charts2?zsyear=2018&charttype=pie&datatype=count&fields=政治面貌')
print(result.text)

