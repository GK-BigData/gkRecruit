# -*- encoding: utf-8 -*-

# Project :zs
# Time  :2019/6/27 下午8:20 

def func(**kwargs):
    for key,value in kwargs.items():
        print(key,value)

func(name=1)
func(**{'age':20})