import json

from docx.shared import Inches
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
import time
from docx import Document

def base_html():
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

def jiexi(data):
    with open(data,'r',encoding='utf-8') as file:
        j=json.loads(file.read())
        index=1
        for i in j:
            if i.get('type')=='chart':
                if i.get('option'):
                    option=i.get('option')
                    print(option)

                    ht = str(index) + '.html'
                    with open(ht, 'w') as file:
                        file.write(base_html().replace('配置',json.dumps(option)))
                        file.write('\n')

                    time.sleep(0.2)
                        #filename不允许添加路径，必须在当前目录吓的html文件
                    make_snapshot(snapshot, file_name=ht, output_name="./need/"+str(index)+".png")

                    js_path='./need/'+str(index)+'.js'
                    with open(js_path, 'w', encoding='utf-8') as need:
                        need.write(json.dumps(option, ensure_ascii=False))
                        need.write('\n')

            elif i.get('type')=='text':
                text=i.get('text')
                txt_path='./need/'+str(index)+'.txt'
                with open(txt_path,'w',encoding='utf-8') as need:
                    need.write(text)
                    need.write('\n')

            else:
                return 'error'
            index+=1

def docx(doc_title, doc_title_position):
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
    docoment.add_heading('图片的标题')
    #增加图片
    docoment.add_picture('./need/1.png', width=Inches(6.5))

    paragraph=docoment.add_paragraph()
    # 插入段落
    with open('./need/2.txt','r',encoding='utf-8') as file:
        txt=file.read()
        print(txt)
        paragraph.insert_paragraph_before(txt)

    docoment.add_heading('图片的二标题')
    docoment.add_picture('./need/3.png',width=Inches(6.5))


    save_docx_name = './need/first.docx'
    docoment.save(save_docx_name)

if __name__=='__main__':
    #data = 'a.json'
    #jiexi(data)
    docx('asc','left')
