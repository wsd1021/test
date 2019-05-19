
# -*- coding:utf-8 -*-

import requests
from jiekou_kuang.m_test.test_denglu import qwe
1

class jiekou_Qingqiu1():
    def chaxun(self,qq,accountGuid,targetUserGuid,accessToken):
        url = "http://120.132.8.33:9000/api/Account/GetUserInfo"

        querystring = {"accountGuid":"{}".format(qq[accountGuid]),
                       "target UserGuid":"{}".format(qq[targetUserGuid])}

        payload = ''
        headers = {
            'Content-Type': "application/json",
            'PhoneInfo': '{"platform": "iOS","systemVersion": "12.0","phoneModel": "iPhone X"}',
            'AppInfo': '{"version": "2.0.1","buildVersion": "2.0.1.3","type": 0}',
            'Language': "zh_CN",
            'APIVersion': "3.0",
            'accessToken': "{}".format(qq[accessToken]),
            'User-Agent': "PostmanRuntime/7.11.0",
            'Accept': "*/*",
            'Cache-Control': "no-cache",
            'Postman-Token': "b8b5f62e-7b4b-4065-9221-2083126beccd,6ec7e617-9de4-4a61-acfd-36d1ffffecae",
            'Host': "120.132.8.33:9000",
            'accept-encoding': "gzip, deflate",
            'content-length': "150",
            'Connection': "keep-alive",
            'cache-control': "no-cache"
            }

        response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

        res = response.json()
        return res



