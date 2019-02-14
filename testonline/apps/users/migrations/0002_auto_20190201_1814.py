# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-02-01 10:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.DateTimeField(max_length=50, verbose_name='标题')),
                ('image', models.ImageField(max_length=50, upload_to='banner/%Y/%m', verbose_name='轮播图')),
                ('url', models.URLField(max_length=50, verbose_name='访问地址')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('index', models.IntegerField(default=100, verbose_name='顺序')),
            ],
            options={
                'verbose_name': '轮播图',
                'verbose_name_plural': '轮播图',
            },
        ),
        migrations.CreateModel(
            name='EmailVerfyRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=20, verbose_name='验证码')),
                ('email', models.EmailField(max_length=50, verbose_name='邮箱')),
                ('send_tpye', models.CharField(choices=[('Register', '注册'), ('Forget', '忘记密码')], max_length=20)),
                ('send_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'verbose_name': '邮箱验证码',
                'verbose_name_plural': '邮箱验证码',
            },
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': '用户信息', 'verbose_name_plural': '用户信息'},
        ),
    ]
