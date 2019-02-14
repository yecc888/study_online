from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
# Create your models here.


class UserProfile(AbstractUser):
    """用户信息表"""
    nick_name = models.CharField(max_length=100, verbose_name=u'昵称')
    birth = models.DateTimeField(null=True, blank=True, verbose_name=u'生日')
    gender = models.CharField(choices=(('male', u'男'), ('female', u'女')), default='female', max_length=6)
    address = models.CharField(max_length=100, default=u'')
    mobile = models.CharField(max_length=11, default='')
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png')

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class EmailVerfyRecord(models.Model):
    """验证码表"""
    code = models.CharField(max_length=20, verbose_name='验证码')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    send_tpye = models.CharField(verbose_name='发送类型', choices=(('Register', '注册'), ('Forget', '忘记密码')),
                                 max_length=20)
    send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    class Meta:
        verbose_name = '邮箱验证码'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code


class Banner(models.Model):
    """轮播图"""
    title = models.CharField(max_length=50, verbose_name='标题')
    image = models.ImageField(upload_to="banner/%Y/%m",
                              verbose_name='轮播图', max_length=50)
    url = models.URLField(max_length=50, verbose_name='访问地址')
    add_time = models.DateTimeField(default=datetime.now,
                                    verbose_name='添加时间')
    index = models.IntegerField(default=100, verbose_name='顺序')

    class Meta:
        verbose_name = '轮播图'
        verbose_name_plural = verbose_name
