#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.header import Header


class Client:
    def __init__(self, email_dict):
        # 邮件信息
        self.server = email_dict.get("server", "smtp.163.com")
        self.sender = email_dict.get("sender")
        self.receiver = email_dict.get("receiver")
        self.password = email_dict.get("password")
        self.subject = email_dict.get("subject")
        self.message = email_dict.get("message")
        self.sender_name = email_dict.get("sender_name", "发件人")

    @staticmethod
    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr((Header(name, "utf-8").encode(), addr))

    def send_mail(self):
        # 设置邮件内容
        message = MIMEText(self.message, "html", "utf-8")
        message["Subject"] = Header(self.subject, "utf-8").encode()
        message["From"] = self._format_addr("%s <%s>" % (self.sender_name, self.sender))
        message["To"] = ",".join(self.receiver)
        # 发送邮件
        try:
            smtp = smtplib.SMTP(self.server)
            smtp.set_debuglevel(1)
            smtp.login(self.sender, self.password)
            smtp.sendmail(self.sender, self.receiver, message.as_string())
            smtp.quit()
            print("send mail succeed")
        except Exception as ex:
            print("send mail error :")
            print(ex)
