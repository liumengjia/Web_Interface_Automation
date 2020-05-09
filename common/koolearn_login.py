#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-01-20 16:34

# @Author : liumengjia

# @File : koolearn_login.py

# @Software: PyCharm

import requests
import json

#登录koolearn官网

s = requests.session()

class Login():
    def login(self,uname,pwd):
        url = "https://login.neibu.koolearn.com/sso/member/login.do"

        h2 = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Connection": "keep-alive",
            "Content-Length": "157",
            "Content-Type": "application/x-www-form-urlencoded",
            #"Cookie":"JSESSIONID=%s" % (r2["JSESSIONID"]),
            "Origin":"https://www.neibu.kooup.com",
            "Referer":"https://www.neibu.kooup.com/",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
        }

        body = {
            "uid":uname,
            "password":pwd,
            #"lt": result["lt"],
            "messageType":"login_callback_1579400121597_459990",
            "app_key":"s.kooup.com",
            "method":"parent",
            "porigin":"https://www.neibu.kooup.com",
            #"_eventId":"submit",
            #"submit":"登录"
        }

        r4 = s.post(url,headers=h2,data=body,allow_redirects=False,verify=False)

        print (u'http状态码：',r4.status_code)
        print (u'请求的url：',r4.url)
        print (u'获取信息头：',r4.headers)
        print (u'响应内容：',r4.text)

if __name__ == "__main__":
    login1 = Login()
    login1.login(uname='15200000005',pwd='m200809')

