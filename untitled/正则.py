#! /usr/bin/python
# -*- coding:utf-8 -*-
# 正则表达式
# import re
# a = 'qwe123qwe56'
# complie  编译，将[0-9]*编译成正则语言
# p = re.compile('[0-9]{2,4}')
# 只匹配指定内容的时候给正则条件加括号
# p1 = re.compile('q(.*)q')
# findall  从某个地方查找所有符合正则的字符串
# 两种用法  1、re.findall()   2、条件.findall()
# 如果findall有两个参数，第一个参数就是正则条件 ，第二个参数就是查找范围
# c = re.findall(p,a)
# 如果finalll只有一个参数，那就是查找范围
# c1= p1.findall(a)
# 贪婪模式：尽可能去匹配更多的内容
# p1 = re.compile('q(.*)q')
# 非贪婪模式：尽可能匹配少的内容
# a = 'qwe\nQ12q323Q'
# .可以匹配除换行符以外的任意字符，
# re.S(给.加功能，可以匹配换行符在内的任意字符)
# re.I(给条件加功能，不区分大小写)
# p1 = re.compile('Q(.*?)q',re.I)
# 查找所有符合条件的结果
# c1 = p1.findall(a)
# print(c1)






