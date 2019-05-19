#! /usr/bin/python
# -*- coding:utf-8 -*-
import xlrd
class Shuju():
    def qingqiushuju(self):
        f = xlrd.open_workbook(r'E:\Users\PycharmProjects\untitled\b.xls')
        sheet = f.sheets()[0]
        hang = sheet.nrows
        return hang,sheet

    def chaxunshuju(self):
        ff = xlrd.open_workbook(r'E:\Users\PycharmProjects\untitled\b.xls')
        sheet2 = ff.sheets()[1]
        row_2 = sheet2.nrows
        return row_2, sheet2

