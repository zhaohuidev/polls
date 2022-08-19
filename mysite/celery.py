#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: celery.py
@time: 2022/8/15 13:56
@desc: 
"""
import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
# 创建Celery实例
app = Celery('mysite', backend='redis://localhost:6379/4',
             broker="redis://localhost:6379/3")  # 字符串参数可以是当前模块名,为了在__main__模块中定义任务时自动生成名称。

# namespace='CELERY'表示所有CELERY相关的配置键应该有一个' CELERY_ '前缀
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')
