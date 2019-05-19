# #! /usr/bin/python
# # -*- coding:utf-8 -*-
#
#
# #面向对象
from appium import webdriver
from time import sleep
import unittest

class ds(unittest.TestCase):
    # 测试脚本与appium服务器进行连接的参数数据
    d = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "7.1.1",
        "deviceName": "DQCAZPEUHQTGJZFE",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "True"
    }
#
#     初始化测试环境的方法/函数
    def setUp(self):
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.d)
        sleep(10)
#     # 所有的用力执行之前，跑一次，就跑一次
#     @classmethod
#     def setUpClass(cls):
#         cls.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_capabilities=cls.d)
#         sleep(10)
#
#     # 所有的用力执行完毕，跑一次，就跑一次    # @classmethod : 固定写法
#     @classmethod
#     def tearDownClass(cls):
#         cls.dr.quit()
#
#
#     # 断言微信文字是否存在
#     def test_1(self):
#         text1 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
#         self.assertEqual(text1, '微信')
#         print(text1)
#     def test_2(self):
#         text2 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name(
#             'android.widget.TextView').text
#         self.assertEqual(text2, '微博')
#         print(text2)
#
#     def test_3(self):
#         text3 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
#         self.assertEqual(text3,'QQ')
#         print(text3)
#     def test_4(self):
#         text4 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
#         print(text4)
#
#
#
#         self.assertEqual(text4,'密码')
#
#     # 关闭APP函数
#     # def tearDown(self):
#     #     self.dr.quit()
#
# if __name__ == '__main__':
#     unittest.main(verbosity=2)











    def login(self,phone,password):
        self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()
        # 向账号的输入框输入手机号
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys(phone)
        sleep(3.0)
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').clear()
        # 向密码的输入框输入密码
        self.dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys(password)
        sleep(3.0)
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
        sleep(10.0)
        # 退出app,包括后台进程也关掉
    #
    # def test_1(self):
    #     self.login('15103819460','13137246872zls')
    #     sleep(10.0)
    #     print('开始断言')
    #     text = self.dr.find_element_by_id('com.qk.butterfly:id/tv_tag1').text
    #     self.assertEqual(text,'热门')


    # app退出登录
    def logout(self):
        # find_element_by_class_name()  定位一个class属性的元素，要求该元素唯一
        # find_elements_by_class_name()  定位多个class属性的元素，元素是多个
        a = self.dr.find_element_by_id('android:id/tabs').find_elements_by_class_name('android.widget.RelativeLayout')
        a[3].click()
        sleep(3.0)
    # 模拟人工上划
    def huoqu_shanghua(self):
        # 1、获取屏幕的分辨率
        size = self.dr.get_window_size()

        x1 = size['width'] * 0.5  # x坐标 50

        y1 = size['height'] * 0.25  # 起始y坐标 50

        y2 = size['height'] * 0.75  # 150
        for i in range(2):
            self.dr.swipe(x1, y2, x1, y1)
            sleep(3.0)
    def shezhi_tuichu(self):
        self.dr.find_element_by_id('com.qk.butterfly:id/v_me_setting').click()
        self.dr.find_element_by_id('com.qk.butterfly:id/v_set_out').click()
        self.dr.find_element_by_id('com.qk.butterfly:id/tv_ok').click()
        sleep(2.0)


    def close_app(self):
        self.dr.quit()

if __name__ == '__main__':
    go = ds()
    go.setUp()
    # go.login('18237920363','wang1021')
    go.logout()
    go.huoqu_shanghua()
    go.shezhi_tuichu()
    go.close_app()


