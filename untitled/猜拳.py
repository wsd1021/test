#! /usr/bin/python
# -*- coding:utf-8 -*-
#编程实现'石头、剪子、布'游戏，游戏的规则为：
#1）布包石头；2）石头砸剪子；3）剪子剪布。
import random
li=['石头','剪子','布']
y=-1
while True:
    y=input('请输入正确的值(0-石头,1-剪子,2-布)：')
    try:
        print ('你：'+li[y])
        break
    except:
        print ('输入有误！')
        c=random.randint(0,len(li)-1)
        print ('电脑：'+li[c])
    if c==y:
        print('平手')
    else:
        if y==0:
            if c==1:
                print ('You win！')
            else:
                print ('You lose！')
        elif y==1:
            if c==2:
                print ('You win！')
            else:
                print ('You lose！')
        elif y==2:
            if c==0:
                print ('You win！')
            else:
                print ('You lose！')