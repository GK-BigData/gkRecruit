# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/7/16 上午9:43 
# BY    :FormatFa

from flask import Blueprint,request,render_template

bp_test = Blueprint('test',__name__)

# 返回某个html
@bp_test.route('/template/<template>')
def test(template:str):

    print('获取测试模板:',template)

    return render_template('test/'+template)
# http://127.0.0.1:5000/test/option/zs
@bp_test.route('/option/<type>')
def option(type):
    """
    options测试
    :param type:
    """

    return render_template('test/optionsTest.html')



