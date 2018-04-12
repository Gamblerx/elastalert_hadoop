#!/usr/bin/python
#-*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

mail_host="smtp.partner.outlook.cn"
mail_port="XXXXX"
mail_user="XXXXXXX"
mail_pass="XXXXXXX"

def sendmail(msg):
    sender = 'XXXXXX'
    receivers = ['XXXXXXX', 'XXXXXXXX', 'XXXXXXXX']

    message = MIMEText(msg, 'plain', 'utf-8')
    subject = 'elastalert 进程异常报警'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, mail_port)
        smtpObj.ehlo()
        smtpObj.starttls()
        smtpObj.ehlo()
        smtpObj.login(mail_user,mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print "邮件发送成功"
        smtpObj.quit()
    except smtplib.SMTPException:
        print "Error: 无法发送邮件"

if __name__ == "__main__":
        sendmail("elastalert刚才异常，正在重新启动，请悉知。")
