#! /usr/bin/python
# -*- coding:utf-8 -*-
# 9*9乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         a = '{}*{}={}'.format(j,i,i*j)
#         print(a,end='\t')
#     print()

# 任意范围的质数之和
# def he(a=2,b=10):
#     sum = 0
#     for i in range(a, b+1):
#         for j in range(2, i):
#             if i % j == 0:
#                 break
#         else:
#             sum += i
#     print(sum)
# he(b=100)

# 任意数的阶乘之和
# def jiecheng(a=5):
#     b = 1
#     sum = 0
#     for i in range(1,a+1):
#         b *= i
#         sum = sum + b
#     print(sum)
# jiecheng(4)

# 判断三角形 钝角、直角、锐角
# num1 = int(input('第一条边：'))
# num2 = int(input('第二条边：'))
# num3 = int(input('第三条边：'))
# if num1 > num3 or num2 > num3:
#     raise TypeError('num3不是最大值,请重新输入')
# elif (num1 + num2 > num3) and (num1+num3 > num2) and (num2+num3 > num1):
#     if num1**2 + num2**2 > num3**2:
#         print('是锐角三角形')
#     elif num1**2 + num2**2 < num3**2:
#         print('是钝角三角形')
#     else:
#         print('是直角三角形')
# else:
#     print('不是三角形')

# 判断以什么开头，以什么结尾
# a = input('请输入一个字符串：')
# if a.startswith('abc') and a.endswith('123'):
#     print('是以abc开头,123结尾')
# else:
#     print('不是')


from jiekou_kuang.report import HTMLTestRunner
import requests
import unittest
import xlrd
f = xlrd.open_workbook('b.xls')
sheet = f.sheets()[0]
hang = sheet.nrows

class Maid(unittest.TestCase):

    def denglu(self,user,password):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"

        payload = '{"phone":"%s","password":"%s",' \
                  '"zone":"86","loginType":0,"isAuto":0,' \
                  '"deviceId":"ec:89:14:54:93:007"}'%(user,password)
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "90834b61-e0c4-44ee-9652-a87b698b93cd,ed8a20cd-d86c-4ad8-a8e5-26f5e8d2501c",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'content-length': "150",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }
        response = requests.request("POST", url, data=payload, headers=headers)
        res = response.json()
        return res

    def setUp(self):  # 执行每个测试用例前执行一次（初始化测试环境）
        print('开始')
    def tearDown(self): #执行每个测试用例后执行一次（清理测试环境）
        print('结束')

    def test_1(self):
        qq = self.denglu(int(sheet.cell(1, 0).value), int(sheet.cell(1, 1).value))
        self.assertEqual(qq['code'],0)
        print('成功')


    def test_2(self):
        for i in range(2, hang):
            ww = self.denglu(int(sheet.cell(i, 0).value), int(sheet.cell(i, 1).value))
            print(ww)
            self.assertNotEqual(ww['code'],0)
            print('失败')


if __name__ == '__main__':
    # unittest.main()
    #  创建一个测试套件
    suit = unittest.TestSuite()
    # 将测试用例添加到测试套件中
    # suit.addTest(Maid('test_1'))
    # suit.addTest(Maid('test_2'))
    # 将Maid类中所有以test开头的函数都添加到测试套件中
    suit.addTest(unittest.makeSuite(Maid))
    # 打开一个空文件
    ff = open('abc.html','wb')
    # 定义测试报告的信息
    runner = HTMLTestRunner.HTMLTestRunner(stream=ff, title='接口测试报告', tester='小强', description='结果如下')
    # 执行测试套件
    runner.run(suit)
    ff.close()



















# import unittest
# class qwe(unittest.TestCase):
#     def setUp(self):    #执行每个测试用例前执行一次（初始化测试环境）
#         print('开始')
#     def tearDown(self): #执行每个测试用例后执行一次（清理测试环境）
#         print('结束')
#     def test_1(self):
#         a = 4 + 5
#         print(123)
#         self.assertEqual(a,9)
#     def test_2(self):
#         b = 6 - 5
#         print(456)
#         self.assertEqual(b,1)
# if __name__ == '__main__':
#     unittest.main()