#! /usr/bin/python
# -*- coding:utf-8 -*-

# import pymysql
# conn = pymysql.connect(host = '192.168.2.174',
#                        port = 3306,
#                        user = 'root',
#                        passwd = '123456')
# 创建游标  #类似于  vim光标
# abc = conn.cursor()
# 执行SQL语句
# abc.execute('use wang;')
# abc.execute('show tables;')
#
# abc.execute('show databases;')
#
# abc.execute('use python_test;')
# abc.execute('create table py_test(name char(255),age int,sex char(255));')
# for i in range(100):
#     abc.execute('insert into py_test values("{}",{},"{}");'.format('小张',20,'女'))
# # 提交
#     conn.commit()
# abc.execute('select * from py_test;')
# # fetchall   获取上一个sql语句执行的结果
# b = abc.fetchall()
# fetchmany() 获取上一个SQL语句执行的结果
# abc.fetchmany(5)  # 默认值获取结果中的第一个数据，参数写几，就读取前几个结果
# fetchone()  获取上一个SQL语句执行的结果,每次只获取一个结果，本身具有迭代功能
# print(abc.fetchone())
# print(abc.fetchmany(4))
# print(abc.fetchone())
# # 断开连接
# conn.close()


# import pymysql
# conn = pymysql.connect(host = '192.168.2.174',
#                        port = 3306,
#                        user = 'root',
#                        passwd = '123456')
# abc = conn.cursor()
# while True:
#     a = input('>>>>>')
#     try:
#         if 'show' in a:
#             abc.execute('{}'.format(a))
#             b = abc.fetchall()
#             print(b)
#         elif 'use' in a:
#             abc.execute('{}'.format(a))
#             print('database changed')
#         elif a == 'exit' or a == 'quit':
#             print('bye~')
#             break
#         else:
#             abc.execute('{}'.format(a))
#     except Exception as e:
#         print(e)
#         continue




# 把表格中的文件传入到数据库
# import pymysql
# import xlrd
# f = xlrd.open_workbook('xinxi.xls')
# sheet = f.sheets()[0]
# hang = sheet.nrows
# lie = sheet.ncols
# conn = pymysql.connect(host = '192.168.2.174',
#                        port = 3306,
#                        user = 'root',
#                        passwd = '123456')
# abc = conn.cursor()
# abc.execute('use python_test;')
# abc.execute('create table dianying (name varchar(255),'
#             'daoyan varchar(255),time varchar(255),country varchar(255),pingjia varchar(255));')
# list = []
# for i in range(1,hang):
#     for ii in range(lie):
#         s = sheet.cell(i,ii)
#         s = str(s)
#         s = s.replace('text:','')
#         list.append(s)
#     abc.execute('insert into dianying values("{}","{}","{}","{}","{}");'
#                 .format(list[0],list[1],list[2],list[3],list[4]))
#     list = []
#     conn.commit()
# a = abc.fetchall()

# # TCP客户端
# import socket
#
# # 创建一个套接字
# sock = socket.socket()
# # 不需要绑定ip，直接建立连接
# sock.connect(('192.168.2.175',5000))
# msg = '你好啊！！！'
# sock.send(msg.encode('utf-8'))
# reg = sock.recv(1024)
# print(reg.decode('utf-8'))
# # 断开连接
# sock.close()

# UDP客户端
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 不需要建立连接
host = ('192.168.2.175',8888)
msg = 'everybody'
s.sendto(msg.encode('utf-8'),host)
reg = s.recv(1024)
print(reg.decode('utf-8'))
s.close()



