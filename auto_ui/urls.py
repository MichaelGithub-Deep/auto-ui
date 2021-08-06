#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
"""
    URL配置
"""
from django.contrib import admin
from django.urls import path
import apps.login.views as login
import apps.dashboard.views as dashboard


urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login.login),
    path('index/', login.index),
    path('userLogin/', login.login),
    path('getUserInfo/', login.user_info),
    path('getServices/', dashboard.get_services),   # 获取服务
]
