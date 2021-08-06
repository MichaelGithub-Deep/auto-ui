#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
# Comment : 数据看板
import requests
from django.http import JsonResponse

# springBoot接口配置
from utils.data import yaml_tool

springBoot_url = "http://qa.springbootadmin.gongkongsaas.com/applications"
springBoot_headers = {"Accept": "application/json"}

# skyWalking接口配置
skyWalking_url = "https://prod.skywalking.gongkongsaas.com/graphql"
skyWalking_headers = {"content-type": "application/json;charset=UTF-8"}

# swagger接口配置
swagger_url = "http://qa.swagger.gongkongsaas.com/v2/api-docs"
swagger_headers = {"Accept": "application/json, text/plain, */*", "knfie4j-gateway-request": ""}
# 获取服务
def get_services(request):
    # 获取所有服务
    result_applications = requests.request(method="GET", url=springBoot_url, headers=springBoot_headers)
    serviceForm = result_applications.json()
    interfaceForm = []
    # print(serviceForm)
    # for serve in serviceForm:
    #     serve_name = str(serve['name']).lower()
    #     # 获取swagger中所有接口
    #     interface_num = 0
    #
    #     try:
    #         result_interface = requests.request(method="GET", url=swagger_url, headers=swagger_headers, params=query_data)
    #         paths = result_interface.json()['paths']
    #         interface_num = len(paths)
    #     except Exception as e:
    #         print(e)
    #     serve_length = {serve_name: interface_num}
    #     interfaceForm.append(serve_length)

    data = {"code": 200, "message": "请求成功", "serviceForm": serviceForm, "interfaceForm": interfaceForm}
    return JsonResponse(data)


def swagger_data():
    # query_data = {"group": serve_name}
    # result_interface = requests.request(method="GET", url=swagger_url, headers=swagger_headers, params=query_data)
    # paths = result_interface.json()['paths']
    dashboard = yaml_tool.get_yaml('./config/dashboard')
    url = dashboard['swagger_headers']
    url['knfie4j-gateway-request'] = "xxx"
    print(url)

swagger_data()
