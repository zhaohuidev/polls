#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: task.py
@time: 2022/8/15 12:09
@desc: 
"""

from celery import Celery, shared_task

# app = Celery('tasks', backend='redis://localhost:6379/4', broker="redis://localhost:6379/3")


@shared_task
def add(x, y):
    return x + y
