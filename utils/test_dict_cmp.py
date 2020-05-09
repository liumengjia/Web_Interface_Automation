#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-03-21 17:48 

# @Author : liumengjia

# @File : test_dict_cmp.py

# @Software: PyCharm

expect_result={
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
    'task_name': '测试任务1',
    'task': {
      'type_child_name': '软件开发a',
      'users_type_txt': '用户a'}
  }],
  'page_size': 10,
  'page': 1
}

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
    'task_name': '测试任务2',
    'task': {
      'type_child_name': '软件开发d',
      'users_type_txt': '用户d'}
  }],
  'page_size': 10,
  'page': 1
}

def test_cmp(expect_result,response):
    temp_data = {}
    temp_data["error_data"] = " "
    flag=0

    for key in expect_result:
        if isinstance(expect_result[key],dict):
            if not test_cmp(expect_result[key],response.get(key)):
                return False

        elif isinstance(expect_result[key],list):
            for expect_index,expect_value in enumerate(expect_result[key]):
                for response_index,response_value in enumerate(response[key]):
                    if not response[key]:
                        raise "{}返回数据为空".format(key)

                    if test_cmp(expect_result[key][expect_index],response[key][response_index]):
                        # 当存在相同数据，flag为真，结束该轮循环
                        flag = 1
                        break

                if not flag:
                            return False

        else:
            if expect_result[key] == response.get(key):
                continue
            else:
                temp_data['error_data']="{}:{},{}:{}".format(key,expect_result[key],key,response.get(key))
                #print(temp_data)
                print("期望结果是" +str(expect_result[key]) + "\n" + "实际结果是" + str(response.get(key)))
                return False

    return True

test_cmp(expect_result,response)

