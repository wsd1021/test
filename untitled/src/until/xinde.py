#! /usr/bin/python
# -*- coding:utf-8 -*-

from appium import webdriver
from time import sleep

class DS(object):
    d = {
        "device": "android",
        "platformName": "Android",
        "platformVersion": "7.1.1",
        "deviceName": "DQCAZPEUHQTGJZFE",
        "appPackage": "com.qk.butterfly",
        "appActivity": ".main.LauncherActivity",
        "noReset": "true"
    }
    # 建立连接的函数
    def __init__(self):
        self.dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=self.d)
    # 检查那四个文字的函数/方法
    def check_text(self):
        self.dr.find_element_by_id('')
        text1 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
        text2 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
        text3 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
        text4 = self.dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
        print(text1)
        return text1

    # 关闭app的函数
    def close_app(self):
        self.dr.quit()

if __name__ == '__main__':
    go = DS()  #创建一个DS类的实例，赋值给变量go
    go.check_text()
    go.close_app()




