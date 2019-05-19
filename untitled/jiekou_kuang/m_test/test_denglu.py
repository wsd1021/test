#! /usr/bin/python
# -*- coding:utf-8 -*-
import unittest
from jiekou_kuang.config.denglu import jiekou_qingqiu
from jiekou_kuang.data.duqu import Shuju


class qwe(unittest.TestCase):
    denglu = jiekou_qingqiu().denglu
    hang,sheet = Shuju().qingqiushuju()
    def test_1(self):
        qq = self.denglu(int(self.sheet.cell(1, 0).value), int(self.sheet.cell(1, 1).value))
        self.assertEqual(qq['code'], 0)
        self.assertEqual(qq['msg'],'OK')
        print('成功')
        return qq


    def test_2(self):
        for i in range(2, self.hang):
            ww = self.denglu(int(self.sheet.cell(i, 0).value), int(self.sheet.cell(i, 1).value))
            print(ww)
            self.assertNotEqual(ww['code'], 0)
            print('失败')
if __name__ == '__main__':
    unittest.main()