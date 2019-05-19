#! /usr/bin/python
# -*- coding:utf-8 -*-

from jiekou_kuang.report import HTMLTestRunner
import unittest


def Baogao(name):
# 创建套件
    suit = unittest.TestSuite()
# 循环name
    for i in name:
        # 查找测试脚本文件
        dis = unittest.defaultTestLoader.discover(r'E:\Users\PycharmProjects\untitled\jiekou_kuang\m_test',pattern='test_{}.py'.format(i.strip()))
        for ii in dis:
            suit.addTest(ii)
    ff = open(r'E:\Users\PycharmProjects\untitled\jiekou_kuang\report\abc.html', 'wb')

    runner = HTMLTestRunner.HTMLTestRunner(stream=ff, title='接口测试报告', tester='小强', description='结果如下')
    runner.run(suit)
    ff.close()
if __name__ == '__main__':
    Baogao('*')

