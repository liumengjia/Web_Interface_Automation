#!/usr/bin/python
#coding=utf-8
# @Time : 2020-01-19 18:34

# @Author : liumengjia

# @File : test_addNewClue.py

# @Software: PyCharm

from common.test_login import TestLogin,s
from utils.test_excel import TestExcel

# 手动录入,新线索入库

actual_result = []
status_code = []

wb = TestExcel('../../data/test_clue.xlsx','addNewClue')
data = wb.test_get_data()

data1 = [item['data'] for item in data]
expect_result = [item['expect_result'] for item in data]

def test_addNewClue():

    url = "http://crm-sea.neibu.koolearn.com/clue/addNewClue"

    for i in range(len(data1)):
        print('data是%s'%data1[i])

        r = s.get(url,params=eval(data1[i]))

        print(u'HTTP状态码:', r.status_code)
        print(u'请求的url:', r.url)
        print(u'响应内容:', r.text)

        actual_result.append(r.text)
        status_code.append(r.status_code)

test_addNewClue()

maxRow = wb.maxRow

for i,value in enumerate(actual_result,2):
    wb.sheet.cell(row=i,column=9,value=value)
    wb.test_save_data()

for j,value1 in enumerate(status_code,2):
    wb.sheet.cell(row=j,column=8,value=value1)
    wb.test_save_data()

# for row in range(2,maxRow+1):
#     for value in range(len(actual_result)):
#         wb.test_write_data(row,9,actual_result[value])
#         wb.test_save_data()
#
#     for value1 in range(len(status_code)):
#         wb.test_write_data(row,8,status_code[value1])
#         wb.test_save_data()
