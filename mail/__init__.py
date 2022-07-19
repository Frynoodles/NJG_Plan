import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

import requests


def sendmail(title, msg, tomails, smtp_host, smtp_user, smtp_pass, from_name='bot-N', pic=""):
    """
    发送信息

    :param pic: 附带图片的链接
    :param from_name: 发送方的名字，默认为bot-N
    :param title: 邮件的标题
    :param tomails: 发送邮件对象的邮件，列表
    :param smtp_pass: SMTP服务的秘钥（口令）
    :param smtp_user: SMTP服务的邮箱
    :param smtp_host: SMTP服务的主机，如 smtp.126.com
    :param msg: 消息内容，支持HTML
    """
    # 第三方 SMTP 服务
    mail_host = smtp_host  # 设置服务器
    mail_user = smtp_user  # 用户名
    mail_pass = smtp_pass  # 口令
    sender = smtp_user
    receivers = tomails
    message = MIMEMultipart('related')
    msgAlternative = MIMEMultipart('alternative')
    message.attach(msgAlternative)
    msgAlternative.attach(MIMEText(msg, 'html', 'utf-8'))
    if len(pic) < 5:  # 其实链接长度肯定不止五，而这里不等于0就行
        fp = open('./resource/header.jpg', 'rb')
        msgImage = MIMEImage(fp.read())
        fp.close()
    else:
        msgImage = MIMEImage(requests.get(pic).content)
    msgImage.add_header('Content-ID', '<image1>')
    message.attach(msgImage)
    message['From'] = formataddr((from_name, smtp_user))
    subject = title
    message['Subject'] = Header(subject, 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")
