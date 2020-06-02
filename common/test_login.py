#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-01-16 16:53

# @Author : liumengjia

# @File : test_login.py

# @Software: PyCharm

import requests
import json
from lxml import etree
import urllib3

# 登录security

s = requests.session()  # 保持会话，保持cookie

urllib3.disable_warnings()

h1 = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0",
    "Content-Type": "application/x-www-form-urlencoded",
    "Upgrade-Insecure-Requests": "1"
}

class TestLogin():
    # def __init__(self):
    #     print("初始化开始")
    #     #self.login()
    #     self.login(uname='superadmin', pwd='000000')
    #     print("初始化完成")

    def test_get_lt(self):  # 获取lt方法
        result = {}
        url1 = "https://cas-sso.neibu.com"
        service = "http://security-maintain.neibu.com/security/j_spring_cas_security_check"
        loginurl = url1 + '/login?service=%s' % (service)

        r = s.get(loginurl, headers=h1, allow_redirects=False, verify=False)

        r1 = r.cookies.get_dict()

        dom = etree.HTML(r.content.decode("utf-8"))

        try:
            result["lt"] = dom.xpath('//input[@name="lt"]')[0].get("value")
            #print(result)
        except:
            print("lt参数获取失败")
        return result,r1

    def test_login(self,uname,pwd):
        result, r2 = self.test_get_lt()

        url2 = "https://cas-sso.neibu.com"
        service2 = "http://security-maintain.neibu.com/security/j_spring_cas_security_check"
        url3 = url2 + "/login;jsessionid=%s?service=%s" % (r2["JSESSIONID"], service2)

        h2 = {
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Accept-Encoding": "gzip, deflate, br",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Connection": "keep-alive",
            "Content-Length": "157",
            "Content-Type": "application/x-www-form-urlencoded",
            "Cookie":"JSESSIONID=%s" % (r2["JSESSIONID"]),
            "Origin":"https://cas-sso.neibu.com",
            "Referer":"https://cas-sso.neibu.com/login?service=http%3A%2F%2Fsecurity-maintain.neibu.com%2Fsecurity%2Fj_spring_cas_security_check",
            "Upgrade-Insecure-Requests":"1",
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:72.0) Gecko/20100101 Firefox/72.0"
        }

        body = {
            "username":uname,
            "password":pwd,
            "lt": result["lt"],
            "_eventId":"submit",
            "submit":"登录"
        }

        r = s.post(url3,headers=h2,data=body,allow_redirects=True,verify=False)

        # print (u'http状态码：',r4.status_code)
        # print (u'响应内容：',r.text)

#if __name__ == "__main__":
login1 = TestLogin().test_login(uname="admin",pwd="123456")
