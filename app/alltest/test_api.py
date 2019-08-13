# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/8/10 上午11:10 
# BY    :FormatFa
import unittest
import requests

class LoginTest(unittest.TestCase):
    def tearDown(self):
        print('teardown....')

    def setUp(self):
        print('set up')

    def testLogin(self):
        print('测试登录')
        res = requests.post('http://127.0.0.1:5000/user/login',{
            'username':'zz',
            'password':'123456'
        })
        print(res.text)
        pass

if __name__=='__main__':
    #unittest.main()
    res = requests.post('http://127.0.0.1:5000/user/login', {
        'username': 'zz',
        'password': '123456'
    })



