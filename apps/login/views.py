#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
from django.http import JsonResponse
from django.shortcuts import render


# Create your views here.
def login(request):
    user_data = request.body
    user_name = "admin"
    data = {"code": 200, "message": "登录成功", "Author": user_name}
    return JsonResponse(data)


def index(request):
    return render(request, "dist/index.html")


def user_info(request):
    """获取用户信息"""
    data = {"name": "admin", "avatar": "测试"}
    token = "mqgpgwqeqokiojioejiojioooqfoieoiemji"
    return JsonResponse({"code": 200, "message": "请求成功", "data": data})
