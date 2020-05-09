#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-01-20 17:07

# @Author : liumengjia

# @File : test_assignClue.py

# @Software: PyCharm

from common.test_login import TestLogin,s
from utils.test_excel import TestExcel

# 线索列表分配一个线索

actual_result = []
status_code = []

wb = TestExcel('../../data/test_clue.xlsx','assignClue')
data = wb.test_get_data()

data1 = [item['data'] for item in data]
expect_result = [item['expect_result'] for item in data]

def test_assignClue():

    url = "https://crm-sea.neibu.koolearn.com/clueManage/assignClue"

    for i in range(len(data1)):
        print('data是%s'%data1[i])

        r = s.post(url,params=eval(data1[i]))

        print (u'HTTP状态码:',r.status_code)
        print (u'请求的URL:',r.url)
        print (u'响应内容:',r.text)

        actual_result.append(r.text)
        status_code.append(r.status_code)

test_assignClue()

maxRow = wb.maxRow

for i,value in enumerate(actual_result,2):
    wb.sheet.cell(row=i,column=9,value=value)
    wb.test_save_data()

for j,value1 in enumerate(status_code,2):
    wb.sheet.cell(row=j,column=8,value=value1)
    wb.test_save_data()