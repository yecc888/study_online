__author__ = 'yecc'
__date__ = '2019/2/14 10:43'

from random import Random
from django.core.mail import send_mail

from testonline.settings import EMAIL_FROM
from users.models import EmailVerfyRecord


def random_str(str_length=8):
    """随机产生字符串"""
    strs = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    random = Random()
    length = len(chars) - 1
    for i in range(str_length):
        strs += chars[random.randint(0, length)]
    return strs


def send_register_email(email, send_type="Register"):
    """发送邮件"""
    emails = EmailVerfyRecord()
    code = random_str(16)
    emails.code = code
    emails.email = email
    emails.send_tpye = send_type
    emails.save()

    email_title = ""
    email_body = ""
    if send_type == 'Register':
        email_title = '测试学习网账号激活'
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)
        code_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if code_status:
            pass
    elif send_type == 'Forget':
        email_title = '测试学习网密码找回'
        email_body = "请点击下面的链接找回你的密码: http://127.0.0.1:8000/reset/{0}".format(code)
        code_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if code_status:
            pass


