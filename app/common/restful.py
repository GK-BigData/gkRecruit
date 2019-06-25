# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/25 下午5:16 
from flask import jsonify
# 返回json的数据，包含状态码
def rjson(data,code=0,msg=''):
    '''数据字典 ，返回的状态码 '''
    return jsonify({
        'code':code,
        'data':data,
        'msg':''
    })