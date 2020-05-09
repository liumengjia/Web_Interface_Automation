#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-03-21 19:42 

# @Author : liumengjia

# @File : test_response_extract.py

# @Software: PyCharm

response={
  'count_tab_4': 13,
  'total': 13,
  'list': [{
    'created_at': '2019-12-19 16:10:01',
    'updated_at': '2019-12-19 16:15:01',
    'company': {
      'full_name': '项目',
      'short_name': '项目简'
    },
    'task_sex': 1,
    'task_user_id_card': '610523198806273676',
    'task': {
      'type_child_name': '软件开发',
      'users_type_txt': '用户'
    }
  }, {
    'created_at': '2019-12-17 11:25:02',
    'updated_at': '2019-12-17 11:30:02',
    'company': {
      'full_name': '项目',
      'short_name': '项目简'},
    'task_sex': 1,
    'task_name': '任务1',
    'task': {
      'type_child_name': '软件开发',
      'users_type_txt': '用户'}
  }],
  'page_size': 10,
  'page': 1
}

extract_data = []

def test_response_extract(response,keys=[]):

  if isinstance(response,list):
    for value in response:
      if isinstance(value,list) or isinstance(value,dict):
        test_response_extract(value,keys)

  elif isinstance(response,dict):
    for key,value in response.items():
      if key in keys:
        extract_data.append(value)
      else:
        test_response_extract(value,keys)

  else:
    pass

test_response_extract(response,['created_at','updated_at'])

print(extract_data)