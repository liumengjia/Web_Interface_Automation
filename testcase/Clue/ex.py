#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-03-29 16:42

# @Author : liumengjia

# @File : ex.py

# @Software: PyCharm

x = -123
y = -1 * int(str(abs(x))[::-1])
#print(y)


l1 = ['13812345678','13812345679','13812345670','13812345671']

# for k,v in enumerate(l1,101):
#     print('allDebugger.' + str(k) + '='+ v)

#e = None
#print(type(e))

print(bytes(map(int, "42 42 42 32 199 235 199 243 32 85 110 75 110 111 119 110 32 179 172 202 177 13 13 10".split())).decode("gbk"))

