import pymysql
import json
import random
from docx import Document
from docx.shared import Inches
import pyecharts
from pyecharts.charts import Bar
from snapshot_selenium import snapshot
from pyecharts.render import make_snapshot
import time

'''
连接mysql数据库，将数据传入到word文档里面
'''


class Mysql_docx:

    def __init__(self):
        self.connect = pymysql.connect(
            host='',
            user='root',
            password='gkbigdata123',
            databases='docx',
            charset='utf8',
            port=3306
        )



    # 读取数据，拿到echarts的option
    def read_mysql(self):
        conn = self.connect.cursor()
        cur = conn.execute('select * from ')
        print(cur)

        option = {

        }

        return option

    # 初始化html文件头
    def base_html(self):

        html = '''<!DOCTYPE html>
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
                       chart_703a9c49431942aebad1569993e9ec62.setOption(option_703a9c49431942aebad1569993e9ec62);
                   </script>
               </body>
               </html>'''
        return html

    # 传入option，制作HTML
    def draw_echarts(self, data):


        with open(data, 'r', encoding='utf-8') as file:
            j = json.loads(file.read())
            index = 1
            for i in j:
                if i.get('type') == 'chart':
                    if i.get('option'):
                        option = i.get('option')
                        print(option)

                        ht = str(index) + '.html'
                        with open(ht, 'w') as file:
                            file.write(self.base_html().replace('配置', json.dumps(option)))
                            file.write('\n')

                        time.sleep(0.2)
                        #调用函数，转为图片
                        output_name = str(index)+'.png'
                        self.html_echarts(html=ht,name=output_name)

                        #生成js，可后续调用
                        js_path = './js/' + str(index) + '.js'
                        self.save_js(js_path=js_path,option=option)

                #生成text文本
                elif i.get('type') == 'text':
                    text = i.get('text')
                    txt_path = './imgs/' + str(index) + '.txt'
                    with open(txt_path, 'w', encoding='utf-8') as need:
                        need.write(text)
                        need.write('\n')

                else:
                    return 'error'
                index += 1


    # 传入HTML，将其转为图片
    def html_echarts(self, html,name):

        # 选择要保存的图片的名字,需要添加后缀
        path_name = './imgs/' + name
        # filename不允许添加路径，必须在当前目录吓的html文件
        make_snapshot(snapshot, html, path_name)

    def save_js(self, option, js_path):
        with open(js_path, 'w', encoding='utf-8') as need:
            need.write(json.dumps(option, ensure_ascii=False))
            need.write('\n')


    # 传入text和imgs上的图片，将其作用在docx上，生成word文档
    def docx(self, doc_title, doc_title_position, save_docx_name):

        docoment = Document()
        section = docoment.sections[0]
        # 文档标题,默认在最左边
        if doc_title:
            # 设置选择标题
            header = section.header
            paragraph = header.paragraphs[0]

            # 如果选择了位置
            if doc_title_position:
                if doc_title_position == 'center':
                    paragraph.text = '\t' + doc_title

                if doc_title_position == 'right':
                    paragraph.text = '\t\t' + doc_title

                if doc_title_position == 'left':
                    paragraph.text = doc_title

            # 默认在最左边
            else:
                paragraph.text = doc_title
        else:
            pass



        save_docx_name = '保存的名字'
        docoment.save(save_docx_name)





if __name__ == '__main__':
    MD = Mysql_docx()
    option=MD.read_mysql()
    html=MD.draw_echarts(option)

