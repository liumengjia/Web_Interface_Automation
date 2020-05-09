#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @Time : 2020-03-18 23:30 

# @Author : liumengjia

# @File : test_response.py 

# @Software: PyCharm

expect_result={
  'count_tab': 13,
  'total': 13,
  'list': [{
    'created_at': '2019-12-19 16:10:01',
    'updated_at': '2019-12-19 16:15:01',
    'company': {
      'full_name': '北京新东方迅程网络科技股份有限公司',
      'short_name': '新东方迅程'
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
      'full_name': '新东方教育科技集团有限公司',
      'short_name': '新东方科技'},
    'task_sex': 1,
    'task_name': '测试任务1',
    'task': {
      'type_child_name': '线索自动分配',
      'users_type_txt': '用户a'}
  }],
  'page_size': 10,
  'page': 1
}

response={
  'count_tab': 13,
  'total': 13,
  'list': [{
    'created_at': '2019-12-19 16:10:01',
    'updated_at': '2019-12-19 16:15:01',
    'company': {
      'full_name': '北京新东方迅程网络科技股份有限公司',
      'short_name': '新东方迅程'
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
      'full_name': '新东方教育科技集团有限公司',
      'short_name': '新东方教育'},
    'task_sex': 1,
    'task_name': '测试任务2',
    'task': {
      'type_child_name': '线索自动分配',
      'users_type_txt': '用户b'}
  }],
  'page_size': 10,
  'page': 1
}

list1=[]

def test_response(expect_result,response):
    temp_data={}
    temp_data['error_data']=" "

    for key in expect_result:

        # 如果期望结果的值是字典，进入递归判断
        if isinstance(expect_result[key],dict):
            if not test_response(expect_result[key],response.get(key)):
                return False
            else:
                pass

        # 如果期望结果的值是列表，进入递归判断
        elif isinstance(expect_result[key],list):
            for expect_index,expect_value in enumerate(expect_result[key]):     # 遍历期望结果的索引和值
                for response_index,response_value in enumerate(response[key]):  # 遍历实际结果的索引和值
                    if not response[key]:
                        raise "{}返回数据为空".format(key)

                    # 如果期望结果的值是字典，继续递归判断
                    if isinstance(expect_value,dict):
                        test_response(expect_result[key][response_index],response[key][response_index])

                    # 如果期望结果的值是列表，
                    elif isinstance(expect_value,list):
                        if expect_result[key][expect_index]==response[key][expect_index]:
                            break
                        else:
                            e = "期望结果是"+str(expect_result[key][expect_index])+ "\n" + "实际结果是" +str(response[key][response_index])
                            raise Exception(e)

                    else:
                        if expect_result[key][expect_index]==response[key][expect_index]:
                            break
                        else:
                            e = "期望结果是" + str(expect_value) + "\n" + "实际结果是" + str(response_value)
                            raise Exception(e)
                return False

        # 如果期望结果的值非字典，非列表
        else:
            if key in response:
                if expect_result[key] == response[key]:
                    continue
                else:
                    temp_data['error_data'] = "{}:{},{}:{}".format(key, expect_result[key], key, response.get(key))
                    e = "期望结果是" + str(expect_result[key]) + " " + "实际结果是" + str(response.get(key))
                    list1.append(e)
                    print(e)
                    print('-----------')
            else:
                temp_data['error_data'] = "{}:{},{}:{}".format(key, expect_result[key], key, response.get(key))
                e = "期望结果是" +str(expect_result[key]) + "\n" + "实际结果是" +str(response.get(key))
                raise Exception(e)

    return True

test_response(expect_result,response)

if list1:
    print(list1)
else:
    print("pass")