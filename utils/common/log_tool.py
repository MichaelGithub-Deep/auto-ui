#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
import os
import time
import logging
import datetime
from utils.common.time_tool import now_ymd
from logging.handlers import TimedRotatingFileHandler


logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)
root_path = os.path.realpath("../../report/log/")
# root_path = os.path.realpath("./report/log/")

# 定义日志级别（一般日志）
handler = TimedRotatingFileHandler(root_path + '{}_info.log'.format(now_ymd()), when='d', interval=1, backupCount=30, encoding='utf-8')
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)

# 定义日志级别（错误日志）
handler2 = TimedRotatingFileHandler(root_path + '{}_error.log'.format(now_ymd()), when='d', interval=1, backupCount=30, encoding='utf-8')
handler2.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler2.setFormatter(formatter)
logger.addHandler(handler2)

# 定义日志级别（Debug日志）
handler3 = logging.StreamHandler()
handler3.setLevel(logging.DEBUG)
formatter = logging.Formatter()
handler3.setFormatter(formatter)
logger.addHandler(handler3)


# 正常日志信息
def info(msg):
    get_files_name(root_path)
    logger.info(msg)


# 调试日志信息
def debug(msg):
    logger.debug(msg)


# 警告日志信息
def warning(msg):
    logger.warning(msg)


# 错误日志信息
def error(msg):
    logger.error(msg)


# 重要的信息
def critical(msg):
    logger.critical(msg)


# 接口类使用日志
def req_log(code, req):
    if code == 200:
        info('请求状态：{} 请求地址：{}'.format(code, req))
    else:
        error('请求状态：{} 请求地址：{}'.format(code, req))


# 将 “2021-01-01” 格式的日期转为时间戳
def get_timestamp(dt):
    ts = time.strptime(dt, "%Y-%m-%d")
    tm = time.mktime(ts)
    return tm


# 获得当前时间前N天的日志文件
def get_files_name(path):
    p_timestamp = datetime.datetime.now() - datetime.timedelta(days=3)
    p_time = get_timestamp(p_timestamp.strftime("%Y-%m-%d"))
    for file in os.listdir(path):
        str_list = file.split("_")
        t_name = get_timestamp(str_list[0])  # 提取文件的时间前缀
        if t_name < p_time:
            os.remove(path+"/{}".format(file))


if __name__ == '__main__':
    info("info message")
    error("error message")
    debug("debug message")
