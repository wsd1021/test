#! /usr/bin/python
# -*- coding:utf-8 -*-

# 第一步：导入appiun模块中的webdriver类
from appium import webdriver
from time import sleep
# 面向过程

# 测试脚本与appium服务器进行连接的参数数据
d = {
  "device": "android",
  "platformName": "Android",
  "platformVersion": "7.1.1",
  "deviceName": "DQCAZPEUHQTGJZFE",
  "appPackage": "com.qk.butterfly",
  "appActivity": ".main.LauncherActivity",
  "noReset": "true"
}
# 写死的http://127.0.0.1:4732/wd/hub
# 测试脚本是appium服务器与手机建立连接的过程

dr = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_capabilities=d)
sleep(5.0)
# 元素师id，就是用id定位方法
# dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').click()


# 获取微信的文字
# 先定位上一级，在定位下面的元素，没有id就找class属性。（属于元素的多级定位）
# text1 = dr.find_element_by_id('com.qk.butterfly:id/v_login_wx').find_element_by_class_name('android.widget.TextView').text
# text2 = dr.find_element_by_id('com.qk.butterfly:id/v_login_wb').find_element_by_class_name('android.widget.TextView').text
# text3 = dr.find_element_by_id('com.qk.butterfly:id/v_login_qq').find_element_by_class_name('android.widget.TextView').text
# text4 = dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').find_element_by_class_name('android.widget.TextView').text
#
# print(text1,text2,text3,text4)
# 插入等待时间
sleep(5.0)

# send_keys()输入的是字符串
# 什么时候用send_keys？
# 1、向手机的输入框输入数据的时候   2、clickable ---》true  3、enabled ---》 true    4、foucsable --》 true

dr.find_element_by_id('com.qk.butterfly:id/v_login_pwd').click()

# 向账号的输入框输入手机号
dr.find_element_by_id('com.qk.butterfly:id/et_login_phone').send_keys('18237920363')
sleep(3.0)
# 向密码的输入框输入密码
dr.find_element_by_id('com.qk.butterfly:id/et_login_pwd').send_keys('wang1021')
sleep(3.0)
dr.find_element_by_id('com.qk.butterfly:id/tv_to_login').click()
sleep(10.0)
# 退出app,包括后台进程也关掉
dr.quit()


