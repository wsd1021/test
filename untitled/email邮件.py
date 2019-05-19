#! /usr/bin/python
# -*- coding:utf-8 -*-

# import smtplib         #     封装了smtp协议
# import email.mime.multipart       #     处理邮件中的组成部分
# import email.mime.text     #    处理邮件中的正文
# # 定义一个发件人
# fr = 'w2386263770@163.com'
# # 收件人
# res = '18317822978@163.com'
# # 服务器
# server = 'smtp.163.com'
# # 授权码   授予登录客户端的权限的密码
# passwd = 'w2386263770'
# # 创建一个空邮件
# message = email.mime.multipart.MIMEMultipart()
# # 给邮件添加一个发件人
# message['From'] = fr
# # 添加一个收件人
# message['To'] = res
# # 添加一个主题
# message['Subject'] = 'python learn'
# text = '河南你好！！！  \n  我是洛阳人'
# # 处理正文文本
# txt = email.mime.text.MIMEText(text)
# message.attach(txt)
# # 添加附件 (附加的文件)
# att2 = email.mime.text.MIMEText(open('a.txt', 'rb').read(), 'base64', 'utf-8')
# att2["Content-Type"] = 'application/octet-stream'
# att2["Content-Disposition"] = 'attachment; filename="abc_new1.html"'
# # 头部字段
# message.attach(att2)
#
# # 定义一个服务器
# smtp123 =smtplib.SMTP_SSL(server, 465)
# # 登录服务器
# smtp123.login(fr, passwd)
# # 发送邮件
# smtp123.sendmail(fr, res, message.as_string())
