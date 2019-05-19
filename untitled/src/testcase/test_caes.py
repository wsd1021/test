#! /usr/bin/python
# -*- coding:utf-8 -*-

from src.func.fuc_1 import weixin,qq,weibo,mima
from appium import webdriver
import HTMLTestRunner
import unittest
from time import sleep
from src.until.hahaha import REPORT_DIR
from src.testcase.wang import get_logger

# 给日志一个变量
g = get_logger(name = 'test_case.py')

 # 测试脚本与appium服务器进行连接的参数数据
class Text(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        d = {
            "device": "android",
            "platformName": "Android",
            "platformVersion": "7.1.1",
            "deviceName": "DQCAZPEUHQTGJZFE",
            "appPackage": "com.qk.butterfly",
            "appActivity": ".main.LauncherActivity",
            "noReset": "True"
        }

        # app建立连接
        cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
        sleep(5.0)
        g.info('app成功建立连接！')

    @classmethod
    def tearDownClass(cls):
        cls.dr.quit()
        g.info('app关闭')

# 测试用例代码
    def test_1(self):
        # 验证微信的用例
        g.info('执行测试用例')
        text = weixin(self.dr)
        # 断言
        self.assertEqual(text,'微信')
    def test_2(self):
        g.info('执行测试用例')
        text = qq(self.dr)
        # 断言
        self.assertEqual(text,'QQ')
    def test_3(self):
        g.info('执行测试用例')
        text = weibo(self.dr)
        # 断言
        self.assertEqual(text,'微博')
    def test_4(self):
        g.info('执行测试用例')
        text = mima(self.dr)
        # 断言
        self.assertEqual(text,'密码')

#运行测试脚本，生成测试报告
if __name__ == '__main__':

    suite = unittest.TestSuite()
    suite.addTest(Text('test_1'))
    suite.addTest(Text('test_2'))
    suite.addTest(Text('test_3'))
    suite.addTest(Text('test_4'))
    #将测试结果写入HTML文件
    #生成测试报告
    # 路径写死
    r_pash = r'E:\Users\PycharmProjects\untitled\src\report\报告.html'
    # # 路径写活
    # r_pash_1 = REPORT_DIR + '报告.html'
    ff = open(r_pash, 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=ff,
                                           title='接口测试报告',
                                           tester='小强',
                                           description='结果如下',
                                           verbosity=2)
    #verbosity 默认是0, 2使控制台输出信息更加详细
    runner.run(suite)
    ff.close()








