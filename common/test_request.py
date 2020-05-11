#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-02-12 22:53 

# @Author : liumengjia

# @File : test_request.py

# @Software: PyCharm

import requests
import json

from common.test_login import TestLogin,s

class TestRequest():
    # 使用__init__方法实现：只要实例化类时候就会调用__init__方法
    def __init__(self,url,params,data,method):
        self.res = self.test_request(url,params,data,method)

    def test_post(self,url,data):
        res = s.post(url=url,data=data)
        return res.json()

    def test_get(self,url,params):
        res = s.get(url=url,params=params)
        return res.json()

    def test_request(self,url,params,data,method):
        res = None
        if method == "get":
            res = self.test_get(url,params)
        else:
            res = self.test_post(url,data)
        return res

if __name__=="__main__":
    url = "http://crm-sea.neibu.com/"

    # 使用__init__方法实现：只要实例化类时候就会调用__init__方法
    res = TestRequest(url,params=None,data=None,method="post")
    print(type(res))
    print(res)
