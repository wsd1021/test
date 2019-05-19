#! /usr/bin/python
# -*- coding:utf-8 -*-

import unittest
from jiekou_kuang.m_test.test_denglu import qwe
from jiekou_kuang.config.chaxun import jiekou_Qingqiu1
from jiekou_kuang.data.duqu import Shuju


class ASD(unittest.TestCase):
    # chaxun = jiekou_Qingqiu1().chaxun
    row_2,sheet2 = Shuju().chaxunshuju()
    # def duqu(self):
        # for i in range(1,self.row_2):
        #     accountGuid_1 = self.sheet2.cell(i, 0).value
        #     targetUserGuid_1 = self.sheet2.cell(i, 1).value
        #     accessToken_1= self.sheet2.cell(i, 2).value
        # return accountGuid_1,targetUserGuid_1,accessToken_1
    def test_1(self):
        ss = jiekou_Qingqiu1().chaxun(qwe().test_1(),self.sheet2.cell(1, 0).value, self.sheet2.cell(1, 1).value, self.sheet2.cell(1,2).value)

        self.assertEqual(ss['code'], 0)
        self.assertEqual(ss['msg'],'OK')
        print('成功')
        return ss


    def test_2(self):
        for j in range(2, self.row_2):
            ww = jiekou_Qingqiu1().chaxun(qwe().test_1(),self.sheet2.cell(j, 0).value, self.sheet2.cell(j, 1).value,self.sheet2.cell(j,2).value)
            print(ww)
            self.assertNotEqual(ww['code'], 0)
            self.assertNotEqual(ww['msg'],'OK')
            print('失败')

# accountGuid,targetUserGuid,accessToken = ASD().duqu()
# jiekou_Qingqiu1().chaxun(qwe().test_1(),accountGuid,targetUserGuid,accessToken)
if __name__ == '__main__':

    unittest.main()









