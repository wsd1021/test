#! /usr/bin/python
# -*- coding:utf-8 -*-
def gouwu():
    a = int(input('【请输入你的总资产】：'))
    if a < 0:
        raise NameError('The integer you entered is not a positive integer')
    b =['笔记本电脑:4399',
        '华为手机:1888',
        '智能手环:300',
        '蓝牙耳机:200']
    print('【余额{}】'.format(a))
    car =[]
    z = 1
    while z > 0:
        while z > 0:
            for x, y in enumerate(b):
                print(x+1, y)
            print('【进入购物车请输入 0】')
            print('【加入购物车请输入商品号】')
            print('【退出请输入 101】')
            c = int(input('【请输入提示值】：'))
            if c == 101:
                break
            elif 0 < c < 5:
                print('【已加入购物车:{}】'.format(b[c - 1]))
                car.append(b[c - 1])
            elif c == 0:
                while z == 1:
                    print('【余额{}】'.format(a))
                    print('【充值请输入(充值)】')
                    for i, j in enumerate(car):
                        print(i+1, j)
                    print('【返回商品区请输入（返回）】')
                    print('【购买全部商品请输入0】')
                    print('【输入要移除的商品号】')
                    e = input('【请输入>>>')
                    if e == '返回':
                        break
                    elif e == '充值':
                        o = int(input('【请输入要充值的金额】'))
                        a += o
                    elif int(e) == 0:
                        n = []
                        for A in car:
                            m = A.split(':')[1]
                            n.append(int(m))
                        f = sum(n)
                        if f == 0:
                            print('【没有购买任何商品】')
                        elif f <= a:
                            print('【购买成功】')
                            a -= f
                            print('购买的商品为{},剩余资金为{}'.format(car, a))
                            car.clear()
                            break
                        elif f > a:
                            print('【余额不足,剩余{}，请充值】'.format(a))
                            p = int(input('【充值请输入1，返回请输入0】：'))
                            if p == 1:
                                g = int(input('【请输入充值金额】'))
                                a +=g
                                print('【充值成功】')
                            else:
                                continue
                    else:
                        print('【{}成功移除购物车】'.format(car[int(e)-1]))
                        car.pop(int(e)-1)
        if c == 101:
            print('【欢迎下次再来】')
            break
gouwu()
