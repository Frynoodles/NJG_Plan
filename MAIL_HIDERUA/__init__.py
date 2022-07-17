import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr


def send_mail(title: str, msg: str, tomails: list[str], smtp_host: str,
              smtp_user: str, smtp_pass: str,
              from_name: str = 'bot-N'):
    """
    发送信息

    :param to_name: 发送对象的名字，默认为 用户
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
    message = MIMEText(msg, 'html', 'utf-8')
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


