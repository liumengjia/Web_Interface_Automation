#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-09-28 14:12 

# @Author : liumengjia

# @File : data_enc.py 

# @Software: PyCharm

from utils.test_excel import TestExcel

def test_get_data():
    wb = TestExcel('../data/user.xlsx','accountPwdLogin')
    data = wb.test_get_data()

    path = [item['path'] for item in data]
    headers = [item['headers'] for item in data]
    data = [item['data'] for item in data]

    return path,headers,data

if __name__=='__main__':
    print(test_get_data())