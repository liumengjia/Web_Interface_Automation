#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-03-20 16:29

# @Author : liumengjia

# @File : test_studentInfo.py

# @Software: PyCharm

import pytest
import allure
from common.test_login import TestLogin,s
from utils.test_excel import TestExcel

# 线索列表，查看学员信息

actual_result = []
status_code = []

wb = TestExcel('../../data/test_student.xlsx','studentInfo')
data = wb.test_get_data()

data1 = [item['data'] for item in data]
expect_result = [item['expect_result'] for item in data]

@allure.feature("学员列表")  # 用feature说明产品需求，可以理解为JIRA中的Epic
@allure.story("学员信息详情")  # 用story说明用户场景，可以理解为JIRA中的Story
@pytest.fixture(scope="function")
def test_studentInfo():

    url = 'https://crm-students.neibu.com/studentInfo/detail'

    for i in range(len(data1)):
        print('data是%s' % data1[i])

        r = s.get(url, params=eval(data1[i]))

        print(u'HTTP状态码:', r.status_code)
        print(u'请求的url:', r.url)
        print(u'响应内容:', r.text)

        actual_result.append(r.text)
        status_code.append(r.status_code)

test_studentInfo()

maxRow = wb.maxRow

for i, value in enumerate(actual_result,2):
    wb.sheet.cell(row=i, column=9, value=value)
    wb.test_save_data()

for j, value1 in enumerate(status_code,2):
    wb.sheet.cell(row=j, column=8, value=value1)
    wb.test_save_data()