#! /usr/bin/python
#-*- coding:utf-8 -*-

import requests


class jiekou_qingqiu():
    def denglu(self, user, password):
        url = "http://120.132.8.33:9000/api/Account/LoginByPhone"

        payload = '{"phone":"%s","password":"%s",' \
                  '"zone":"86","loginType":0,"isAuto":0,' \
                  '"deviceId":"ec:89:14:54:93:007"}' % (user, password)
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "90834b61-e0c4-44ee-9652-a87b698b93cd,ed8a20cd-d86c-4ad8-a8e5-26f5e8d2501c",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'content-length': "150",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
        }
        response = requests.request("POST", url, data=payload, headers=headers)
        res = response.json()
        return res



