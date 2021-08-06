#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
import datetime


# 获取当前时间 yearn-month-day
def now_ymd():
    today = datetime.date.today()
    year = today.year
    month = today.month
    day = today.day
    ymd = "%s-%s-%s" % (year, month, day)
    return ymd


# 获取当前时间 yearn-month-day hour:minute:second
def now_hms():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second
    timenow = "%s-%s-%s %s:%s:%s" % (year, month, day, hour, minute, second)
    return timenow


# 图片后缀
def image_suffix():
    now = datetime.datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute
    second = now.second  # ︰
    suffix = "%s-%s-%s %s.%s.%s " % (year, month, day, hour, minute, second)
    return suffix
