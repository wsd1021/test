#! /usr/bin/python
#-*- coding:utf-8 -*-

# a = "nishfch"
# print(type(a))
# {}  占位   format填充
# %   占位   %填充    %s能填充任意数据    %d只能填充数字
# a = "hello,我叫%s，今年%d岁"  #大括号代表占位符 ，大括号个数不限制
# 格式化字符串
# b = input('请输入你的名字：') #变量不固定
# d = int(input("请输入你的年龄："))
# 填充字符串
# c=a.format(age=b,name=d)
# c=a %(b,d)
# print (c)
# a = ' qwert '
# print(a)

# 去除字符串左右的空格
# b = a.rstrip()
# print(b)

# a = (12, 'ddsf', 'kdwho', 45, 8409, 24153, 32, 3243, 51452, 4524, 21435,
#      576, 543545, 4, 3, 43, 4, 33, 432, 4, 32, 32)
# b = a.count(32)
# c = a.index(32)
# print(b)
# print(c)

# a = [21,32,4,'3sd','ete','ewf',2132]
# a.insert(3,100)   #第一个是下标号，第二个是要添加的数据
# print(a)

# import copy
# a = [21,32,4,2132,[23,343,9844]]
# b = copy.deepcopy(a)
# a.append(123)
# a[-1].append(6789)
# print (a)
# print (b)

# a = {'name':'xiaoming','age':21}
# b = {'fdsa':'iusa'}
# a.update(b)
# print(a)
# a = set()
# print(a)
# print(type(a))
# a = 'nhdqoicnjmlsa'
# print('jk' not in a)
# if 条件：
#      执行语句
# elif 条件：
#      执行语句
# else:
#      执行语句
#
# 输入一个成绩判断成绩是否及格
# a = input('请输入成绩')
# a = int(a)
# if 100 >= a >= 80:
#     print('优秀')
# elif a < 80 and a >= 60:
#     print('及格')
# else:
#     print('不及格')
# if 条件：
#     if 条件：
#         执行语句
# a = input('请输入一个数字')
# a = int(a)
# if a % 3 != 0 and a % 2 != 0:
#     print(123)
# elif a%3==0:
#     if a%2==0:
#         print('hello,world')
#     else:
#         print('hello')
# else:
#     print('world')
# a = input('请输入一个字符串')
# if a[0]==a or a[0]=='A':
#     if a[-1]=='c':
#         print(110)
#    else:
#        print(120)
#
# 判断字符串以什么开头，以什么结尾
# a = input('请输入一个字符串')
# if a[0]=='a' or a[0]=='A' and a[-1]=='c':
#     print(110)
# elif a[0]=='a':
#     print(120)
# elif a[-1]=='c':
#     print(130)
# else:
#     print(250)
#
# 范围为1~10
# for i in range(1,10):
#     if i == 7:
#         continue
#     else:
#         print(i)
# else:
#     print('hello')

# 计算100以内奇数之和和偶数只和的差
# 计算： 1-2+3-4+5-6...-98+99=?
# a = 0
# for i in range(0,100):
#     if i%2 == 0:
#         a -= i
#     else:
#         a += i
# print(a)
# 从1~10的范围里随机产生一个数
# import random
# a = random.randint(1,10)
# for i in range(3):
#     b = input('>>>')
#     b = int(b)
#     if b > a :
#        print('大了,还有%d次机会' % (2-i))
#     elif b < a :
#        print('小了,还有%d次机会' % (2-i))
#     elif b == a :
#        print('正确')
#        break
# else:
#     print('废物')
#
# 9*9乘法表
# for i in range(1,10):
#     for j in range(1,1+i):
#         a = '%d*%d=%d' % (i,j,i*j)
#         print(a,end='\t')
#     print()
# a = [11,55,66,33,77,88,22,44,99];b = [];c = []
# for i in a:
#     if i > 55:
#         c.append(i)
#     else:
#         b.append(i)
# b.sort();c.sort()
# print(b);print(c)

# 质数之和

# a = 0
# for i in range(2,101):
#     for j in range(2,i+1):
#         b = i%j
#         if b == 0:
#             break
#     if i == j:
#        a += i
# print(a)

# 1000以内因数之和等于他本身的数
# for a in range(1,1000):
#     c = 0
#     for b in range(1,a):
#         d = a%b
#         if d == 0:
#             c += b
#     if c == a:
#         print(a)
# 水仙花数
# for a in range(1,10):
#     for b in range(10):
#         for c in range(10):
#             d = a*100+b*10+c
#             e = a**3+b**3+c**3
#             if d == e:
#                 print(d)
# 判断三角形类型
# a=int(input("请输入第一条边:"))
# b=int(input("请输入第二条边:"))
# c=int(input("请输入第三条边:"))
# if (a+b>c) and (a+c>b) and (b+c>a) and c > a and c > b:
#     if a*a + b*b == c*c:
#         print("直角三角形")
#     elif (a*a + b*b < c*c):
#         print("钝角三角形")
#     else:
#         print("锐角三角形")
# elif (a+b>c) and (a+c>b) and (b+c>a):
#     print("c不是最大值，请重新输入")
# else:
#     print('不是三角形')
# a = ['电脑','手机','计算机']
# enumerate ： 将列表中每个数据的下标位置和数据对应显示
# for i,j in enumerate(a):
#     print(i+1,j)
# b = int(input('请输入购买序号：'))
# print(a[b-1])
# while 条件：   ： 根据条件循环
# a = 4
# while a >= 2:
#     if a == 2:
#         break
#     print('hello')
#     a -= 1
# else:
#     print(123)
# for循环  通常循环一些有下标位置的数据，或者是某一范围的循环
# while循环  通常是来做一些无限循环的，或根据某个条件进行循环时
# a = int(input('>>>>>'))
# for i in range(a-20):
#     print('hello')
# else:
#     print('错误')
# while a > 20:
#     print('hello')
#     a -= 1
# 用while语句写出 1 ~ 100 的和
# sum = 0;a = 0
# while a <= 100:
#     sum += a
#     a += 1
# print(sum)

# a = int(input('>>>>>>'))
# while True:
#     c = []
#     a = input('请输入一组数据，以逗号隔开;')
#     if '-' not in a:
#         b = a.split(',')
#         for i in b:
#             c.append(int(i))
#         d = sum(c)/len(c)
#         print('平均数为:{}'.format(d))
#         for j in c:
#             if d > j:
#                 print('低于平均数的有：{}'.format(j))
#     else:
#         break
# 阶乘之和
# a = int(input('请输入一个数字：'))
# b = 1
# sum = 0
# for i in range(1,a+1):
#     b *= i
#     sum = sum + b
# print(sum)
# 去重并排序
# a = [1,3,2,4,4,6,5,8,9,5,45,7,32,23,5,43,42,32,43,45,43,32]
# b = []
# for i in a:
#     if i not in b:
#         b.append(i)
# for j in range(1,len(b)):
#     for x in range(len(b)-1):
#         if b[x] > b[x+1]:
#             b[x],b[x + 1] = b[x + 1],b[x]
# print(b)

# 冒泡排序法
# def 函数():
#     a = input('请输入一组数：')
#     b=a.split(',')
#     for i in range(1,len(b)):
#         for j in range(len(b)-1):
#             if int(b[j]) > int(b[j+1]):
#                 b[j],b[j+1] = b[j+1],b[j]
#     print(b)
# 函数()

# def sum(b):
#     for i in range(1, len(b)):
#         for j in range(len(b)-1):
#             if int(b[j]) > int(b[j+1]):
#                 b[j],b[j+1] = b[j+1],b[j]
#     print(b)
# sum([21,324,35,4,2,4])
# def sum(**kwargs):
#     print(type(kwargs))
# sum(name ="nihao",age=20,sex='男')

# def qwe(b):
#     a = 0
#     for i in range(1,b+1):
#         a += i
#     print(a)
#     return a     #return后边的是给调用者赋的值
# # 调用的代码：只有一个功能就是调用函数，本身没有任何数据
# c = qwe(100)
# qwe(int(input('>>>>')))
# print(c)
# 判断字符串是否是回文
# s = input('请输入一组字符串,以逗号隔开：')
# b = s.split(',')
# b.reverse()
# a = b.copy()
# a = ','.join(a)
# print(a)
# if a == s:
#     print('您输入的字符串是回文')
# else:
#     print('您输入的字符串不是回文')
# 不用int将字符串变整数
# a = '123'    #  1*100   2*10     3*1
# a = a[::-1]
# b = 0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j) == a[i]:
#             b = b+j*10**i
# print(b)
# 不用int将字符串变整数
# a = input('>>>>>>>')
# b = 0
# for i in range(len(a)):
#     for j in range(10):
#         if str(j) == a[i]:
#             b = b+j*10**(len(a)-1-i)
#             break
# print(b)
# 列表推导式
# a = []
# for i in range(10):
#     a.append(i)
# print(a)
# # 可以写成
# b = [i for i in range(10) if i > 6 and i < 9]
# print(b)

# a = lambda x=20, y=15: print(y-x)
# a()
# 报错的原因：路径中有转义字符
# 注：在写文件路径时，要注意转义
# 解决方法 1、在反斜杠前加一个反斜杠    2、在路径前加 r
# f = open('a.txt','r',encoding='utf-8')
# for i in range(30):
#     f.write('user{}\n'.format(i))   # 写入的数据只能是字符串,并且只能是一个字符串
#
# f.close()
# for i in range(1,10):
#     for j in range(1,1+i):
#         f.write('%d*%d=%d\t' % (j,i,i*j))
#     f.write('\n')
# f = open('a.txt','r',encoding='utf-8')
# print(f.read())
# f.close()
# f = open('b.txt','rb')
# print(f.read())
# f.close()
# 打印列表中最大值与第二大的值
# a = [1,4,3,2,4,5,5,7,6,7]
# b = a.copy()
# b = list(set(b))
# b.sort()
# for i in a:
#     if i == b[-1] or i == b[-2]:
#         print(i)
# 上课讲的
# with open('a.txt','w',encoding='utf-8') as f:
#     pass
# def qwe(b):
#     a = 0
#     for i in range(1,b+1):
#         a += i
#     print(a)
#     return a
# a = lambda x: x + 2
# # __name__  : 获取当前执行的文件名
# if __name__ == "__main__":   # 判断执行的文件是否是本文件
#     print('hello')

# 统计a.txt文件有多少行，排除空行和注释掉的行
# with open('a.txt','r',encoding='utf-8') as a:
#     c = 0
#     b = a.readlines()
#     for i in b:
#         if i.startswith('#') or i == '\n':
#             c += 1
#     print(len(b) - c)

# 匿名函数
# try ....except...语句
# 如果try里面执行的语句报错就执行except里面的执行语句
# try:
#     a = 23
#     print(a+'12')
# except Exception as e:
#     print(e)
# else:
#     print('hahaha')
# finally:
#     print(1234)

# try.....except.....finally...语句
# 不论执行try语句还是执行except语句,都执行finally语句
# 将数字转换为ASCII表中的字符
# print(chr(97))
# # 将ASCII表中的字符转换为数字
# print(ord('a'))
# # 十进制转十六进制
# print(hex(79))
# # 十进制转八进制
# print(oct(79))
# # 十进制转二进制
# print(bin(79))

# 十进制数不用函数转换为十六进制数
# a = [str(x) for x in range(10)] + [chr(x) for x in range(97,103)]
# b = int(input('请输入一个十进制数'))
# f = ''
# while True:
#     c = b%16
#     b = b//16
#     f += a[c]
#     if b == 0:
#         break
# print(f[::-1])

# 把一个列表用列表推导式写出来
# a=[str(i) for i in range(0,10)]
# b=[chr(i) for i in range(97,103)]
# a=a + b
# print(a)
# a = [1,4,3,5,7,43,45,2,34,321]
# b = [i for i in a if i < 1000]
# print(b)
# 最大的数放在最后一位，最小的数放在第一位
# a = [13, 243, 21, 134, 24, 43, 2, 12, 4, 32, 22, 24, 46]
# b = a.index(min(a));c = a.index(max(a))
# a[0],a[b] = a[b],a[0]
# a[-1], a[c] = a[c], a[-1]
# print(a)
# 有顺序的列表中随机加入一个数字，在正确位置
# a = [1, 2, 3, 4, 5, 7, 8, 9, 13, 15]
# b = int(input('请输入一个数字：'))
# for i in range(len(a)):
#     if b <= a[i]:
#         a.insert(i,b)
#         break
#     elif b > a[-1]:
#         a.insert(a[-1],b)
#     else:
#         continue
# print(a)
# 买鸡的题
# for x in range(101):
#     for y in range(101):
#         for z in range(101):
#             if 2*x + y + 0.5*z == 100  and x+y+z == 100:
#                 print(x,y,z)
# 任意四个数字，组成不相同的三位数
# a = input('请输入任意四位数：')
# a =a.split(',')
# e=[]
# for i in a:
#     e.append(int(i))
# f = []
# for x in e:
#     b = x*100
#     for y in e:
#         c = y*10
#         for z in e:
#             if x != y != z != x:
#                 f.append(b+c+z)
# print(len(f))
# print(f)
# 将列表中的元素向左挪一位
# # a = [1, 2, 3, 6, 43, 24, 64, 23, 21, 43, 7, 8]
# # for j in range(1,len(a)):
# #     a[j], a[j-1] = a[j-1], a[j]
# # print(a)
# 一个函数，传两个参数a，b；a是数组，b是一个数字；找出a数组中两数之和等于b，打印出来
# def sum(a,b):
#     for i in range(len(a)):
#         for j in range(i+1,len(a)):
#             if a[i]+a[j] == b:
#                 print(a[i],a[j])
# sum([1,2,3,4,5,6,7,8,9],10)


# divmod()  #整除求余
# a, b = divmod(100,16)
# print(a,b)

# class 小爱():
#     def __打电话(self):
#         print('打电话')
#
#     def __发短信(self):
#         print('发短信')
#
#     def 播放音乐(self):
#         print('播放音乐')
# class 小na(小爱):
#     def 打电话(self):
#         print('打电话')
#         print('视频通话')
# xiao = 小爱()
# xiao.播放音乐()
# 类名命名规则 == 函数名命名规则，为了跟函数区分，默认的类名首字母大写
# 调用类里面的函数
# xiao就叫做类的实例，对象


# class 小爱():
#     def __init__(self,a):    # 初始化属性
#         self.name = a
#     def 打电话(self,a):
#         print('打电话给{}'.format(self.name))
#         print(a)
#     def 发短信(self):
#         print('发短信给{}'.format(self.name))
#     def 播放音乐(self):
#         print('播放音乐给{}'.format(self.name))
# xiao = 小爱('小李')
# da = 小爱('wang')
# da.发短信(4)
# xiao.发短信()
# da.打电话(123)


# 向Excel表格中写入数据
# import xlwt
# # 打开一个excel表格文件
# f = xlwt.Workbook(encoding='utf-8')
# # 添加一个标签页（'标签页名称'）
# sheet = f.add_sheet('python_test')
# # 向标签页中写入数据
# for i in range(1,10):
#     for j in range(1,i+1):
#         sheet.write(i-1,j-1,'{}*{}={}'.format(j,i,i*j))
# # (第一个数字代表行，第二个数字代表列，第三个内容代表写入的数据)
# # 保存文件
# f.save('a.xls')


# 读取excel表格中的数据
# import xlrd
# 打开读取的Excel表格文件
# f = xlrd.open_workbook('a.xls')
# 获取表格文件中有多少个标签页
# print(f.nsheets)
# 获取excel表格中所有标签页的名称
# b = f.sheet_names()
# print(b)
# 进入要读取的标签页
# sheet = f.sheet_by_name('python_test')
# 通过索引值来进入操作的标签页
# sheet = f.sheets()[0]
# # 读取标签页中的第几行
# b = sheet.row_values(0)
# # 获取标签页中有多少行
# c = sheet.nrows
# # 读取标签页中的第几列
# b = sheet.col_values(0)
# # 获取标签页中有多少列
# c = sheet.ncols
# 只读取某一个格子里面的数据
# s = sheet.cell(0,0).value
# print(s)
# 读取文件中有多少行（排除空行和注释掉的行）
# with open('a.txt','r',encoding='utf-8') as a:
#     c = 0
#     b = a.readlines()
#     for i in b:
#         if i.startswith('#') or i == '\n':
#             c += 1
#     print(len(b) - c)

# 把txt文件中的数据添加到excel表中
# with open('a.txt', 'r', encoding='utf-8') as x:
#     import xlwt
#     f = xlwt.Workbook(encoding='utf-8')
#     sheet = f.add_sheet('插入数据')
#     c = x.read()
#     o = c.split('\n')
#     for i in range(len(o)):
#         a = o[i]
#         b = a.split(',')
#         for j in range(len(b)):
#             sheet.write(i,j,b[j])
#     f.save('a.xls')

# import xlrd
# f = xlrd.open_workbook('a.xls')
# sheet = f.sheet_by_name('插入数据')
# a = sheet.nrows
# with open('b.txt', 'w', encoding='utf-8') as x:
#     for i in range(a):
#         b = sheet.row_values(i)
#         for j in range(len(b)):
#             if b[-1] ==b[j]:
#                 x.write(b[j] + '\n')
#                 else:
#                 x.write(b[j] + ',')

# www.baidu.com  包和模块的区别？

# 追加excel数据
# from xlutils.copy import copy
# import xlrd
# # 打开一个excel文件
# f = xlrd.open_workbook('a.xls')
# # 复制文件
# new_f = copy(f)
# # 获取要操作的标签页
# sheet = new_f.get_sheet(0)
# sheet.write(7,0,'人生啊,茫茫啊，随波逐流，无影踪')
# new_f.save('a.xls')

# 时间模块
import time
# 时间戳
# 表示从公元1970年8点开始到现在经过的时间(s)
# a = time.time()
# 以元组的格式显示本地时间
# 如果传入参数，显示的就是传入的参数的时间（只接受时间戳）
# a = time.localtime(15530)
# # 以本地化时间显示
# b = time.strftime('%Y.%m.%d %H:%M:%S-%w',a)
# print(b)
# 将元组时间转换为时间戳,必须写9个数字
# a = (2019,3,26,15,2,45,23,4,324)
# b = time.mktime(a)
# print(b)
# 将现在时间转化为元组时间(前后对应，且前后格式要一样)
# a = time.strptime('2010-12-12','%Y-%m-%d')
# print(a)
# 休息时间(s)后再执行
# time.sleep(2)

# 手动输入一个时间（年月日） 1.判断是否是闰年 2.打印星期几 3.打印今天是一年的第几天
# import time
# year = int(input('请输入年份:'))
# month = int(input('请输入月份:'))
# day = int(input('请输入日数:'))
# if (year % 400 == 0) or ((year % 4 == 0):
#     print('{}年是闰年'.format(year))
# else:
#     print('{}年不是闰年'.format(year))
# a = time.strptime('{}-{}-{}'.format(year,month,day),'%Y-%m-%d')
# print('今天是周',a[-3]+1,';','今天是今年的第',a[-2],'天')

# 手动输入一个日期，输出这个日期的前一天

# year = int(input('请输入年份:'))
# month = int(input('请输入月份:'))
# day = int(input('请输入天数:'))
# a = [4,6,9,11]
# b = [1,3,5,7,8,10,12]
# c = month-1
# if month ==1 and day == 1:
#     print(year-1, '.', 12, '.', 31)
# elif (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)) and month == 3 and day == 1:
#     print(year,'.',2,'.',29)
# elif year % 4 != 0 and month == 3 and day == 1:
#     print(year,'.',2,'.',28)
# elif month in a and day == 1:
#     print(year,'.',month-1,'.',31)
# elif month in b and c not in b and c != 2 and day == 1:
#     print(year, '.', month - 1, '.', 30)
# elif month in b and c in b and c != 2 and day == 1:
#     print(year, '.', month - 1, '.', 31)
# else:
#     print(year, '.', month , '.', day-1)

# import time
# a=int(input('请输入年份：'))
# b=int(input('请输入月份：'))
# c=int(input('请输入日期:'))
# z=time.strptime('{} {} {}'.format(a,b,c),'%Y %m %d')
# n=time.mktime(z)
# n1=86400
# cha=n-n1
# s=time.localtime(cha)
# x = time.strftime('%Y.%m.%d',s)
# print(x)

# # 读取excel表格中的第一行到第五行
# import xlrd
# f = xlrd.open_workbook('a.xls')
# sheet = f.sheet_by_name('插入数据')
# for i in range(5):
#     b = sheet.row_values(i)
#     print(b)

# 爬虫
# 写爬虫的步骤
# 1.分析网址     2.过滤想要的内容      3.将过滤的内容保存
# https://www.qiushibaike.com/text/page/2/
# 对服务器造成压力
# import requests
# import re
# import xlwt
# # class qiushi(object):
# #     def qiushibaike(self):
# z = []
# for l in range(1, 6):
#     a = 'https://www.qiushibaike.com/text/page/{}/'.format(l)
#     # 发送请求
#     oo = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'
#                         ' AppleWebKit/537.36 (KHTML, like Gecko)'
#                         ' Chrome/71.0.3578.98 Safari/537.36'}      #彻底的模仿浏览器
#     b = requests.get(a,headers=oo)
#     # 接受响应  1、 .text(得到的是网页源代码) 字符串   2、content（以字节的方式接收）
#     c = b.content.decode('utf-8')
#     # guolv
#     d = re.compile('<div class="content">(.*?)</span>', re.S)
#     f = d.findall(c)
#     dd = re.compile('<h2>(.*?)</h2>', re.S)
#     fff = dd.findall(c)
#     ff = []
#     ffff = []
#     for i in f:
#         i = i.replace('<span>', '')
#         i = i.strip()
#         i = i.replace('<br/>', '')
#         ff.append(i)
#     for j in fff:
#         j = j.replace('\n', '')
#         ffff.append(j)
#     for x in range(len(ff)):
#         ff.insert(x*2, '作者:{}'.format(ffff[x]))
#     for o in ff:
#         z.append(o)
#     with open('c.txt','w',encoding='utf-8') as y:
#         for g in z:
#             y.write(str(g)+'\n')
# xx = xlwt.Workbook(encoding='utf-8')
# sheet = xx.add_sheet('sheet1')
# xxx = len(z)//2
# for r in range(xxx):
#     for rr in range(2):
#         sheet.write(r,rr,'{}'.format(z[0]))
#         z.pop(0)
# xx.save('c.xls')
# qiushi().qiushibaike()

# import re
# import requests
# class tupian(object):
#
#     def qingqiu(self,page):
#         url = 'https://www.qiushibaike.com/imgrank/page/{}/'.format(page)
#         head = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                           'AppleWebKit/537.36 (KHTML, like Gecko) '
#                           'Chrome/71.0.3578.98 Safari/537.36'
#         }
#         res = requests.get(url,headers=head)
#         html = res.content.decode('utf-8')
#         return html
#     def guolv(self,abc):
#         lianjie = []
#         patt = re.compile(r'<div class="thumb">(.*?)</a>',re.S)
#         items = patt.findall(abc)
#         for i in items:
#             new_a = re.compile(r'<img src="(.*?)"')
#             aaa = new_a.findall(i)
#             lianjie.extend(aaa)
#         return lianjie
#     def save(self,shu):
#         for a,i in enumerate(shu):
#             # 图片是一个链接，请求图片的链接，将相应的回复保存
#             res = requests.get('https:'+i)
#             #接受相应的结果只能用content
#             qq = res.content
#             with open('第{}页的{}.jpg'.format(ii,a+1),'wb')as f:
#                 f.write(qq)
# tu = tupian()
# for ii in range(1,6):
#     abc = tu.qingqiu(ii)
#     sh = tu.guolv(abc)
#     tu.save(sh)

# import re
# import requests
# class tupian(object):
#     def qingqiu(self,page):
#         url = 'https://movie.douban.com/top250?start={}&filter='.format(25*a)
#         head = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                           'AppleWebKit/537.36 (KHTML, like Gecko) '
#                           'Chrome/71.0.3578.98 Safari/537.36'
#         }
#         # 发送请求
#         res = requests.get(url,headers=head)
#         html = res.content.decode('utf-8')
#         return html
#     def guolv(self,html1):
#     # 过滤内容
#         lianjie = [];mingzi = []
#         patt = re.compile(r'<div class="pic">(.*?)</a>',re.S)
#         items = patt.findall(html1)
#         for tu in items:
#             new_tu = re.compile(r'src="(.*?)" class="">')
#             aaa = new_tu.findall(tu)
#             lianjie.extend(aaa)
#         name = re.compile(r'alt="(.*?)"')
#         aa = name.findall(html1)
#         for i in aa:
#             mingzi.append(i)
#         for x, d in enumerate(lianjie):
#             dd = requests.get(d)
#             ddd = dd.content
#             with open('{}.jpg'.format(mingzi[x]), 'ab') as f:
#                 f.write(ddd)
# tu = tupian()
# for a in range(5):
#     qing = tu.qingqiu(a)
#     tu.guolv(qing)
# import os
# 自带的库，是与操作系统交互的（通过os模块控制操作系统）
# 删除文件
# os.remove('a.xls')
# os.popen  执行Windows命令
# b = os.popen('ipconfig/all')
# print(b.read())
# 获取当前所在位置
# print(os.getcwd())
# 切换目录
# os.chdir(r'D:')
# print(os.getcwd())
# 获取当前文件夹下面的文件,一个点是当前目录，两个点是上一级目录
# a = os.listdir('.')
# for i in a:
#     if i.endswith('.py'):
#         print(i)
import os
# # 将文件与路径分隔开,
# a = os.path.split(r'E:\Users\PycharmProjects\untitled\day1.py')
# # 将文件后缀名与路径分隔开要加上ext
# b = os.path.splitext(r'E:\Users\PycharmProjects\untitled\day1.py')
# print(a,b)
# # 判断文件是否是一个目录
# a = os.path.isdir('../untitled')
# print(a)
# # 判断文件是否是一个普通文件
# b = os.path.isfile('day1.py')
# print(b)
# 创建文件夹
# os.mkdir('aaa')
# 创建递归文件夹
# os.makedirs('aaa/bbb/ccc')
# 删除空文件夹
# os.rmdir('ccc')
# 删除递归文件夹
# os.removedirs('aaa/bbb/ddd')
# 包和模块的区别
#  包 ： 是一个目录，封装的是模块，必须含有 __init__.py文件
#  模块 ： 是一个.py文件，封装的代码
# 面向对象和面向过程 区别 和 特点
#  面向过程 ：一步一步实现解决问题的步骤 ； 性能高，不易扩展
#  面向对象 ：将函数分类封装，使开发更高效 ； 易扩展、易于维护、性能低

# 封装ssh协议，可以实现远程控制
# import paramiko
#
# 创建一个远程客户端
# ssh123 = paramiko.SSHClient()
# # 跳过验证，不到know_hosts文件中去查找
# ssh123.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# 连接主机
# ssh123.connect(hostname='192.168.2.174',
#                port = 22,
#                username='root',
#                password='123456')
# 执行命令 ： ssh123.exec_command()
#  只能执行有结果的命令
# stuin,stuout,stueer = ssh123.exec_command('ls -al')
# # stuin ： 执行的命令
# # stuout ： 执行的结果
# # stueer ： 执行的报错
# print(stuout.read().decode())
# ssh123.close()

# while True:
#     a = input('>>>>>>')
#     try:
#         if a == 'exit' or a == 'quit':
#             break
#         else:
#             stuin,stuout,stueer = ssh123.exec_command('{}'.format(a))
#             print(stuout.read().decode())
#     except Exception as e:
#         print(e)
#         continue

# 传输文件
# 建立一个传输通道
# ssh123 = paramiko.Transport(('192.168.2.174',22))
# # 连接主机
# qwe = ssh123.connect(username='root',password='123456')
# # 创建一个sftp客户端
# sftp = paramiko.SFTPClient.from_transport(ssh123)
# # 从linux下载文件到windows
# # 第一个参数 ： 要下载的文件   第二个参数 ： 存储的本地位置
# sftp.get('anaconda-ks.cfg', './anaconda-ks.cfg')
# # 从Windows上传文件到linux
# sftp.put('day1.py','/home/day1.py')
# ssh123.close()

#        socket     简单
# 套接字，提供了通信双方最底层的功能（# 发送，接收）
# 封装的是TCP/IP模型     为了通信
# 两台主机实现通信

# # day1.py定义为server端(服务端)（客户端在mysql.py文件里）
# import socket
# # 创建一个套接字（创建一个有发送能力和接受能力的功能）
# # 默认使用tcp协议(SOCK_STREAM) \ UDP协议(SOCK_DGRAM)
# # socket.AF_INET(IPv4协议)  、 AF_INET（IPv6协议）
# # 使用的是IPv4和TCP协议
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 绑定ip地址和端口
# s.bind(('192.168.2.175', 5000))  # 接收的是一个元组
# # 监听服务有没有开启
# s.listen(3)   # 最大等待个数
# while True:
#     #  接收建立连接
#     #  第一个值：是建立连接的信息   第二个值：是客户端的ip地址和端口号
#     client,addr = s.accept()
#     # 接收客户端发送的请求
#     msg = client.recv(1024)  # 每次接收的数据的最大字节为1024
#     print(msg.decode('utf-8'))
#     reg = 'hello'
#     client.send(reg.encode('utf-8'))

# UDP服务器
# import socket
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# s.bind(('192.168.2.175',8888))
# while True:
#     #  第一个参数 ：是客户端的请求数据 ； 第二个参数 ：客户端的ip和端口号
#     client, addr = s.recvfrom(1024)
#     print(client.decode('utf-8'))
#     print(addr)
#     msg = 'hello'
#     s.sendto(msg.encode('utf-8'), addr)



# def zifu(a,b=0,c=1):
#     a = a.split(',')
#     if c < len(a)-b:
#         for i in range(c):
#             a.pop(b)
#             d = ','.join(a)
#         print(d)
#     if c >= len(a)-b:
#         for i in range(len(a)-b):
#             a.pop(b)
#             d = ','.join(a)
#         print(d)
#
# zifu('q,wi,uh,fo,e,i2,d,s,fa,v,D,SA,<,ga,W,F,DS,GA，S,f,as,f<，FA,SF,FZ,的,fdiu',2,10)

# 1、下载模块   selenium
from selenium import webdriver

dr = webdriver.Chrome()
dr.get('http://www.baidu.com')

