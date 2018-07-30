#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
import cx_Oracle  # 引用模块cx_Oracle


class Client:
    def __init__(self):
        # 邮件信息
        self.server = 'mailman.cisco.com'
        self.sender = 'test@cisco.com'
        self.receiver = ['yidxue@cisco.com']

    def send_mail(self, msg):
        # 设置邮件内容
        message = MIMEText(msg.decode('utf-8').encode('gb2312'), 'plain', 'gb2312')
        message['Subject'] = 'Daily Oracle Data Report'
        message['From'] = self.sender
        message['To'] = ','.join(self.receiver)
        # 发送邮件
        try:
            smtp = smtplib.SMTP(self.server)
            smtp.set_debuglevel(1)
            smtp.sendmail(self.sender, self.receiver, message.as_string())
            smtp.quit()
            print("send mail succeed")
        except Exception as ex:
            print("send mail error : \n", ex)


class OracleService:
    def __init__(self):
        self.dsnStr = cx_Oracle.makedsn("10.252.10.14", "1521", "stapdb")
        self.conn = cx_Oracle.connect(user="stapuser", password="se#0stpdb", dsn=self.dsnStr)
        self.cur = self.conn.cursor()  # 获取cursor

    def get_data(self, day):
        sql = "SELECT count(*) as count from DAP_JMFUSER WHERE DATATIME='" + day + "'"
        print(sql)
        self.cur.execute(sql)  # 使用cursor进行各种操作
        dap_jmfuser_row = self.cur.fetchone()
        sql = "SELECT * from DAP_JMFOVERALL WHERE DATATIME='" + day + "'"
        print(sql)
        self.cur.execute(sql)  # 使用cursor进行各种操作
        dap_jmfoverall_row = self.cur.fetchone()
        self.cur.close()  # 关闭cursor
        self.conn.close()
        return dap_jmfuser_row[0], dap_jmfoverall_row


if __name__ == '__main__':
    day = "20171023"
    count, dap_jmfuser_row = OracleService().get_data(day)

    if dap_jmfuser_row is None:
        dap_jmfuser_row = [0, 0, 0, 0, 0]

    msg = 'Date: {0}\n\nDAP_JMFUSER: total number is {1} \n\nDAP_JMFOVERALL: CREATETIME                    DATATIME          JMFUSER       JMFRATE         TOTALATT\n                                {2}         {3}         {4}             {5}             {6}'.format(
        day, count, dap_jmfuser_row[0], dap_jmfuser_row[1], dap_jmfuser_row[2], dap_jmfuser_row[3], dap_jmfuser_row[4])
    print(msg)
    client = Client()
    client.send_mail(msg)
