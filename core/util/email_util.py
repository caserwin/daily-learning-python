#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText


class Client:
    def __init__(self):
        # 邮件信息
        self.server = 'smtp.163.com'
        self.sender = 'send_test@163.com'
        self.receiver = ['receive_test@163.com']
        self.password = '123456789'

    def send_mail(self, msg):
        # 设置邮件内容
        message = MIMEText(msg.decode('utf-8').encode('gb2312'), 'plain', 'gb2312')
        message['Subject'] = 'email_test_subject'
        message['From'] = self.sender
        message['To'] = ','.join(self.receiver)
        # 发送邮件
        try:
            smtp = smtplib.SMTP(self.server)
            smtp.set_debuglevel(1)
            smtp.login(self.sender, self.password)
            smtp.sendmail(self.sender, self.receiver, message.as_string())
            smtp.quit()
            print("send mail succeed")
        except Exception as ex:
            print("send mail error : \n")
            print(ex)


# 测试
if __name__ == '__main__':
    msg = 'hello! 你好,我是一封邮件!'
    client = Client()
    client.send_mail(msg)
