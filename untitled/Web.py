#! /usr/bin/python
# -*- coding:utf-8 -*-

# selenium  是一个开源的web自动化的测试工具集
# 版本：selenium1.0 , selenium2.0 , selenium3.0
# 为什么要用selenium？
# 开源，免费
# 多浏览器支持：Firefox、Chrome、IE、Opera、Safari
# 多平台支持：
# 多语言支持：
# 对Web页面有良好的支持
# 简单（API简单）

# selenium IDE 是嵌入到Firefox 浏览器中的一个插件，实现简单的浏览器操作的录制与回放功能

# selenium Grid :是一种自动化的测试辅助工具，能加快WebAPP的功能测试，可以很方便地同时在多台机器上和异构环境中并行运行多个测试用例
# selenium RC ：是selenium，支持多种不同的语言编写自动化测试脚本，负责控制浏览器的行为


# 针对各个浏览器而开发，通过原生浏览器或者浏览器扩展直接控制浏览器。简单来说就是集成了原生浏览器的所有接口直接控制浏览器
# selenium RC 在浏览器中运行JavaScript应用，使用浏览器内置的JavaScript翻译器来翻译和执行自动化脚本


from selenium import webdriver
from time import sleep

# 定义一个要打开的浏览器
dr = webdriver.Chrome()

# 请求网页
dr.get('https://baidu.com')
sleep(3.0)
# dr.switch_to.frame('login_frame')


# 定位一组，定位多个数据
ww = dr.find_elements_by_class_name('mnav')
for i in ww:
    print(i.text)

# 层级定位（多用于复杂的定位场景下）：先定位一个顶层元素，然后再定位这个元素下面的元素





# dr.get('http://www.jd.com')
# sleep(2.0)
#   通过 id 来定位
# dr.find_element_by_id('kw').send_keys('python')
# sleep(3.0)

# # 为了跟python中的class，class_name区分
# # 单个定位的时候要保证class的值是唯一的
# dr.find_element_by_class_name('').click()
#
# # 3、name  通过name来定位
# dr.find_element_by_name('wd').send_keys('')

# dr.find_element_by_id('su').click()

# # 4、link_text  通过文本来定位(要保证文本的唯一性)
# dr.find_element_by_link_text('hao123').click()

# 5、partial link text   模糊文本定位
# dr.find_element_by_partial_link_text('hao').click()

# 6、tag_name  定位（通过标签页的名称定位）
# dr.find_elements_by_tag_name()
# 7、xpath 定位（路径标记语言）（通过路径定位）
# dr.find_element_by_xpath('//* [@id="kw"]').click()

# 8、css 定位
# dr.find_element_by_css_selector('').click()








# 定位之后的动作  1、send_keys（） 输入  2、click 点击（）
#                 3、clear 清除（）      4、text  文本







# # 回到上一次打开的网页
# dr.back()
# sleep(2.0)
# # 前进
# dr.forward()
# sleep(2.0)
# 获取网页标题,一般用作断言（判断请求到的网页的标题是否符合预期结果）
# print(dr.title)
#
# # 获取请求网址
# print(dr.current_url)
#
# # 设置浏览器大小
# dr.set_window_size(1000,600)
# sleep(2.0)
#
# # 设置浏览器的位置
# dr.set_window_position(200,200)
# sleep(2.0)
#
# # 最大化浏览器
# dr.maximize_window()
# sleep(2.0)
#
# # 最小化浏览器
# dr.minimize_window()
# sleep(2.0)

# 关闭浏览器
# dr.quit()





















