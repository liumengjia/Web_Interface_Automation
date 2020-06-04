# Web_Interface_Automation
基于Pytest+Request+Allure的接口自动化开源框架（Excel篇）

----
#### 框架流程
读取Excel测试数据-生成测试用例-执行测试用例-生成Allure报告

----
#### 模块类的设计
`common包` 存放公用模块，登录方法等；根据请求类型的不同执行不同的方法test_request.py；

`config包` 存放测试环境，预发环境，生产环境等不同环境的配置信息；

`data包` 存放测试用例数据，各模块接口用例，线索、工单、学员接口用例等；

`testcase包` 存放测试接口脚本，各模块接口脚本，线索接口，学员接口，工单接口等；

`json包` 存放请求中涉及到的data、cookies等json数据；

`utils包` 存放公共函数的封装

获取Excel表格数据，test_excel.py；

获取Excel表格数据，方法二，test_excel1.py；

响应结果断言，期望结果和实际结果对比，test_response.py；

响应结果断言，期望结果和实际结果对比，方法二，test_result.py；

响应数据支持多层嵌套提取，test_response_extract.py

从json文件中获取想要的数据，test_json.py；

`result包` 保存测试结果数据的目录

`report包` 存放测试完成之后生成的测试报告，可以查看报告定位问题

`logs包` 存放测试完成之后生成的日志文件，可以查看日志定位问题

----


