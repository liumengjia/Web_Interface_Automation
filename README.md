# crm接口自动化

（1）common：存放通用方法，security登录，koolearn登录；

根据请求类型的不同执行不同的方法test_request.py；

（2）config：存放配置环境变量，neibu环境，release环境，预发环境等

（3）data：存放测试用例数据，线索接口用例，学员接口用例，工单接口用例等；

（4）testcase：存放各模块接口请求，线索接口，学员接口，工单接口等；

（5）json：存放请求中涉及到的data、cookies等数据；

（6）logs：存放测试完成之后生成的日志文件，可以查看日志定位问题；

（7）utils：通用方法的封装，

获取Excel表格数据，test_excel.py；

获取Excel表格数据，方法二，test_excel1.py；

响应结果断言，期望结果和实际结果对比，test_response.py；

响应结果断言，期望结果和实际结果对比，方法二，test_dict_cmp.py；

响应数据支持多层嵌套提取，test_response_extract.py

从json文件中获取想要的数据，test_json.py；

（8）report：存放测试完成之后生成的测试报告，可以查看报告定位问题；
