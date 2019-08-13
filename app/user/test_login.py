# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/8/10 下午7:48 
# BY    :FormatFa

import requests
res = requests.post('http://127.0.0.1:5000/user/login', {
    'username': 'zz',
    'password': '123456'
})
print(res.text)