#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: urls.py
@time: 2022/8/13 19:23
@desc: 
"""
from django.urls import path

from . import views

app_name = 'news'
urlpatterns = [
    path('articles/<int:year>/', views.year_archive),
    path('articles/<int:year>/<int:month>/', views.month_archive),
    path('articles/<int:year>/<int:month>/<int:pk>/', views.article_detail),
]
