#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
""" 英跃自动化数据库相关配置 """
import pymysql


# 本地数据库
def db_local():
    conn = pymysql.connect(host='127.0.0.1', user="root", passwd="longhai123", db="GKM_AUTO_TEST")
    cursor = conn.cursor()
    return cursor, conn


# 工控QA数据库
def db_qa_gks():
    conn = pymysql.connect(host='192.168.0.8', user="gksadmin", passwd="admingks")
    cursor = conn.cursor()
    return cursor, conn






