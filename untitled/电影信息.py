#! /usr/bin/python
# -*- coding:utf-8 -*-
# from xlutils.copy import copy
# import xlwt
# import xlrd
# import re
# import requests
# class xinxi(object):
#     def qingqiu(self, page):
#         url = 'https://movie.douban.com/top250?start={}&filter='.format(25*page)
#         head = {
#             'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
#                           'AppleWebKit/537.36 (KHTML, like Gecko) '
#                           'Chrome/71.0.3578.98 Safari/537.36'
#         }
#         res = requests.get(url, headers=head)
#         html = res.content.decode('utf-8')
#         return html
#     def guolv(self,html1):
#         nianfen = []; guojia = []; pingjia = []
#         a = re.compile(r'<img width="100" alt="(.*?)" src="', re.S)
#         name = a.findall(html1)
#         c = re.compile(r'导演:(.*?)<div class="star">', re.S)
#         cc = c.findall(html1)
#         b = re.compile(r'导演:(.*?)&nbsp;', re.S)
#         daoyan = b.findall(html1)
#         d = re.compile(r'content="10.0"></span>(.*?)</div>', re.S)
#         dd = d.findall(html1)
#         for i in cc:
#             new_c = re.compile(r'<br>(.*?)&nbsp;',re.S)
#             nian = new_c.findall(i)
#             for ii in nian:
#                 ii = ii.replace('\n','')
#                 ii = ii.strip()
#             nianfen.append(ii)
#             new_cc = re.compile(r'/&nbsp;(.*?)&nbsp;/', re.S)
#             guo = new_cc.findall(i)
#             guojia.extend(guo)
#         for j in dd:
#             new_d = re.compile(r'<span>(.*?)人评价', re.S)
#             ping = new_d.findall(j)
#             pingjia.extend(ping)
#         return list(zip(name, daoyan, nianfen, guojia, pingjia))
#     def save(self, zhi):
#         try:
#             rea=xlrd.open_workbook('xinxi.xls')
#             read=rea.sheets()[0]
#             hang=read.nrows
#             new_rea=copy(rea)
#             new_sheet=new_rea.get_sheet(0)
#             z2=hang+1
#             for q, w, e, r, t in zhi:
#                 new_sheet.write(z2, 0, q)
#                 new_sheet.write(z2, 1, w)
#                 new_sheet.write(z2, 2, e)
#                 new_sheet.write(z2, 3, r)
#                 new_sheet.write(z2, 4, t)
#                 z2+=1
#             new_rea.save('xinxi.xls')
#         except:
#             wri=xlwt.Workbook()
#             sheet=wri.add_sheet('sheet1')
#             sheet.write(0, 0, '电影名称')
#             sheet.write(0, 1, '导演')
#             sheet.write(0, 2, '上映时间')
#             sheet.write(0, 3, '国家')
#             sheet.write(0, 4, '评价人数')
#             z1=1
#             for q, w, e, r, t in zhi:
#                 sheet.write(z1, 0, q)
#                 sheet.write(z1, 1, w)
#                 sheet.write(z1, 2, e)
#                 sheet.write(z1, 3, r)
#                 sheet.write(z1, 4, t)
#                 z1+=1
#             wri.save('xinxi.xls')
# a = xinxi()
# for page in range(1, 6):
#     b = a.qingqiu(page)
#     c = a.guolv(b)
#     a.save(c)

# 爬虫:爬取的任何资源，HTML文件  # 静态网页
# 动态网页：资源不在html文件中的，实时动态刷新的
# 加载网页资源  : Javascript ,ajax    浏览器调试工具
# xhr Javascript报文    js  ajax报文   media 音频

# {json}是一种轻量级的数据传输格式 python不是认识的json数据，字符串
# json.loads 将json格式转化为字典
# json.dumps() 将字典转化为json模式
# import requests
# import json
# url = 'https://www.amap.com/service/poiInfo?query_type=TQUERY&pagesize=20&pagenum=1&qii=true&cluster_state=5&need_utd=true&utd_sceneid=1000&div=PC1000&addr_poi_merge=true&is_classify=true&zoom=12&city=410200&geoobj=114.244286%7C34.736976%7C114.548471%7C34.862713&keywords=洗浴中心'









