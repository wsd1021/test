#! /usr/bin/python
# -*- coding:utf-8 -*-
import re
import requests
import json
import xlwt
import pymysql
import xlrd
from xlutils.copy import copy
class zhilian(object):
    def qingqiu(self,page):
        url = 'https://fe-api.zhaopin.com/c/i/sou?start={}' \
         '&pageSize=90&cityId=653&salary=0,0' \
         '&workExperience=-1&education=-1&companyType=-1&employmentType=-1' \
         '&jobWelfareTag=-1&kw=%E8%BD%AF%E4%BB%B6%E6%B5%8B%E8%AF%95%E5%B7%A5%E7%A8%8B%E5%B8%88' \
         '&kt=3&=0&_v=0.56370674&x-zp-page-request-id=' \
         '64373c72a732417d8652b7b210366653-1554177577889-202627'.format(90*page)
        head = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/71.0.3578.98 Safari/537.36'
        }
        res = requests.get(url,headers=head)
        html = res.content.decode('utf-8')
        return html
    def guolv(self,html1):
        jieguo = json.loads(html1)
        xinxi = []
        for i in range(len(jieguo['data']['results'])):
            kong = []
            a = jieguo['data']['results'][i]['updateDate']; kong.append(a)
            b = jieguo['data']['results'][i]['city']['items'][0]['name'];kong.append(b)
            c = jieguo['data']['results'][i]['salary'];kong.append(c)
            d = jieguo['data']['results'][i]['workingExp']['name'];kong.append(d)
            e = jieguo['data']['results'][i]['company']['name'];kong.append(e)
            f = jieguo['data']['results'][i]['jobName'];kong.append(f)
            g = jieguo['data']['results'][i]['eduLevel']['name'];kong.append(g)
            xinxi.append(kong)
        print(xinxi)
        return xinxi
    def exc(self,zhi):
        try:
            fff = xlrd.open_workbook('zhilian.xls')
            new_fff = copy(fff)
            new_sheet = new_fff.get_sheet(0)
            read = fff.sheets()[0]
            hang1 = read.nrows
            hang2 = hang1
            for j in range(len(cc)):
                new_sheet.write(hang2, 0, zhi[j][0])
                new_sheet.write(hang2, 1, zhi[j][1])
                new_sheet.write(hang2, 2, zhi[j][2])
                new_sheet.write(hang2, 3, zhi[j][3])
                new_sheet.write(hang2, 4, zhi[j][4])
                new_sheet.write(hang2, 5, zhi[j][5])
                new_sheet.write(hang2, 6, zhi[j][6])
                hang2 += 1
                new_fff.save('zhilian.xls')
        except:
            ff = xlwt.Workbook(encoding='utf-8')
            sheet = ff.add_sheet('sheet1')
            sheet.write(0, 0, '上架时间')
            sheet.write(0, 1, '工作地点')
            sheet.write(0, 2, '工作薪资')
            sheet.write(0, 3, '工作经验')
            sheet.write(0, 4, '公司名称')
            sheet.write(0, 5, '招聘岗位')
            sheet.write(0, 6, '学历要求')
            hang = 1
            for j in range(len(zhi)):
                sheet.write(hang, 0, zhi[j][0])
                sheet.write(hang, 1, zhi[j][1])
                sheet.write(hang, 2, zhi[j][2])
                sheet.write(hang, 3, zhi[j][3])
                sheet.write(hang, 4, zhi[j][4])
                sheet.write(hang, 5, zhi[j][5])
                sheet.write(hang, 6, zhi[j][6])
                hang += 1
                ff.save('zhilian.xls')


aa = zhilian()
for p in range(4):
    bb = aa.qingqiu(p)
    cc = aa.guolv(bb)
    aa.exc(cc)

