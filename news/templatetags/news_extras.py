#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: myTemplateFilters.py
@time: 2022/8/14 03:08
@desc: 
"""
from news.templatetags import register


def cut1(value):
    return value[0:1]


register.filter('cut1', cut1)
