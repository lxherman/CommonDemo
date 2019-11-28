#!/usr/bin/python3
# -*- coding: UTF-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import sys

#发送outlook邮件
my_sender = '*****@****.com'  # 发件人邮箱账号
my_pass = '*******'  # 发件人邮箱密码
my_user = '****@*****.com'  # 收件人邮箱账号
subject = "爬虫邮件告警"  # 邮件的主题


def mail():
    ret = True
    try:
        msg = MIMEText('邮件内容~~~~~', 'plain', 'utf-8')
        msg['From'] = formataddr(["爬虫监控", my_sender])  # 括号里的对应发件人邮箱昵称、发件人邮箱账号
        msg['To'] = formataddr(["爬虫开发者", my_user])  # 括号里的对应收件人邮箱昵称、收件人邮箱账号
        msg['Subject'] = subject

        # server = smtplib.SMTP_SSL("smtp.qq.com", 25)  #===============SSL加密  如QQ邮箱
        server = smtplib.SMTP("smtp.office365.com", 25)  # 发件人邮箱中的SMTP服务器，端口是25
        server.starttls()      #===============TLS加密  如outlook邮箱
        server.login(my_sender, my_pass)  # 括号中对应的是发件人邮箱账号、邮箱密码
        server.sendmail(my_sender, my_user, msg.as_string())  # 括号中对应的是发件人邮箱账号、收件人邮箱账号、发送邮件
        server.quit()  # 关闭连接
    except Exception as e:  # 如果 try 中的语句没有执行，则会执行下面的 ret=False
        print(e)
        ret = False

    return ret


ret = mail()
if ret:
    print("success")
else:
    print("fail")