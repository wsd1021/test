#! /usr/bin/python
# -*- coding:utf-8 -*-

from selenium import webdriver
from time import sleep

# 定义一个要打开的浏览器
dr = webdriver.Chrome()
# dr.get('https://qzone.qq.com/')
# sleep(3.0)
# # iframe   网页框架
# # 切换到框架  id，name
# # 先定位到框架
# # dr.find_element_by_xpath('')
# dr.switch_to.frame('login_frame')
# sleep(2.0)
#
# # 退出到框架,tuichudao   退出到最初的页面
# dr.switch_to_default_content()
#
# # 切换到上一级框架
# dr.switch_to.parent_frame()
#
#
#
# dr.find_element_by_id('switcher_plogin').click()
# sleep(2.0)
# dr.find_element_by_id('u').send_keys('2386263770')
# sleep(1.0)
# dr.find_element_by_id('p').send_keys('wang1021')
# dr.find_element_by_id('login_button').click()
#
# # 点击退出时会弹出框  叫alert
# dr.find_element_by_xpath('//*[@id="tb_logout"]/i').click()
# sleep(2.0)
# # 切换到alert上去，自动点击确定
# we = dr.switch_to.alert()
# # 获取alert上的文本
# print(we.text)
# # 点击确定
# we.accept()





# dr = webdriver.Chrome()
# dr.get('https://www.ctrip.com')
# sleep(2.0)
# ww = dr.find_element_by_xpath('//*[@id="searchHotelLevelSelect"]').find_elements_by_tag_name('option')
#
# for i in ww:
#     print(i.text)
#     i.click()
#     sleep(2.0)





# dr.get('file:///C:/Users/你管1021/Desktop/abc.html')
# sleep(2)
# dr.find_element_by_xpath('/html/body/input').click()
# sleep(2)
# # 将控制器切换到弹出框
# ww = dr.switch_to_alert()
# # 获取弹出框的文本
# print(ww.text)
# # 点击确定
# # ww.accept()
# # 点击取消
# # ww.dismiss()
# sleep(2)
# ww.send_keys('en')
# sleep(2)
# ww.accept()

dr.get('https://www.douban.com')  #一号窗口
sleep(2)
# # 获取第一个窗口的标识(句柄)
# print(dr.current_window_handle)



dr.find_element_by_xpath('//*[@id="anony-nav"]/div[1]/ul/li[1]/a').click()  # 二号窗口

# 浏览器本身是无法决定什么时候打开哪一个窗口！
# 按照窗口打开的顺序给窗口标号（唯一标识这个窗口的字符串）

# 获取所有窗口的标识（句柄）
ww = dr.window_handles
print(ww)
# 切换窗口
dr.switch_to.window(ww[-1])
print(dr.title)



