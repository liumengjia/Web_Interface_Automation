#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-09-28 10:17

# @Author : liumengjia

# @File : test_favouriteAddGoods.py

# @Software: PyCharm

from utils import data_enc
from utils.test_excel import TestExcel
import pytest
import requests
import allure

actual_result = []

s = requests.session()

wb = TestExcel('../../data/goods.xlsx','favouriteAddGoods')
data = wb.test_get_data()
data1 = [item['data'] for item in data]
expect_result = [item['expect_result'] for item in data]
status_code = [item['status_code'] for item in data]

path,headers,data = data_enc.test_get_data()
parametrize=[(path,headers,data)]
print(parametrize)
print(len(parametrize))

class Test_favouriteAddGoods():
    @allure.story("code==200时，检查code值和msg")

    @pytest.fixture(scope="class")
    @pytest.mark.parametrize('path,headers,data',parametrize)
    def test_favouriteAddGoods(self,path,headers,data):

        r = s.post(path="path",headers="headers",data="data")
        actual_result.append(r.text)  # 把响应内容写入Excel中
        response = r.json()

        if response["code"] != 200:
            assert response["code"] == status_code[0]  # 预期结果code值
            assert response["error"]["msg"] == expect_result[2][1]  # 预期结果error中msg值
        else:
            assert response["code"] == status_code[0]  # 预期结果code值
            assert response["msg"] == expect_result[3]  # 预期结果msg值
            assert response["data"]["uid"] == expect_result[2][1]  # 预期结果data中uid值

Test_favouriteAddGoods().test_favouriteAddGoods(path,headers,data)

maxRow = wb.maxRow

# 把响应内容写入Excel中
for i,value in enumerate(actual_result,2):
    wb.sheet.cell(row=i,column=11,value=value)
    wb.test_save_data()

if __name__=='__main__':
    t = Test_favouriteAddGoods()
    t.test_favouriteAddGoods(path,headers,data)
