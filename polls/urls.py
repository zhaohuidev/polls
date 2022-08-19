#!/usr/bin/python3
# -*- coding:utf-8 -*-
"""
@author: 
@file: urls.py
@time: 2022/8/14 15:54
@desc: 
"""
from django.urls.conf import path
from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name='detail'),
    path("<int:pk>/results/", views.ResultsView.as_view(), name='results'),
    path("<int:question_id>/vote/", views.vote, name='vote'),
]
