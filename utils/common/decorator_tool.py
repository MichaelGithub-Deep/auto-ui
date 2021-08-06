#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
import sys
import traceback

from utils.common import log_tool as log, log_tool
from utils.common import system_tool as system
from utils.common.base_page import BasePage
from utils.common.time_tool import image_suffix


# 捕获异常行数
def catch(fun):
    def wrapper(self, driver):
        try:
            fun(self, driver)
        except Exception as e:
            path = system.absPath('../../report/image_error')
            suffix = fun.__name__
            prefix = image_suffix()
            file_path = path + "/{}{}.png".format(prefix, suffix)
            BasePage().screenshot(file_path)
            errors = traceback.format_exc().split("  ")
            for error in errors:
                if "test_case" in error or "pages" in error:
                    log.error(error)
    return wrapper


# 异常截屏
def screenshot(fun):
    def wrapper(self, driver):
        try:
            fun(self, driver)
        except Exception as e:
            path = system.absPath('../../report/image_error')
            suffix = fun.__name__
            prefix = image_suffix()
            file_path = path + "/{}{}.png".format(prefix, suffix)
            BasePage(driver).screenshot(file_path)

    return wrapper


# 可以忽略的功能块
def maylose(msg):
    def middle(fun):
        def wrapper():
            try:
                fun()
            except KeyError as e:
                log.info("{}  没有为{}的key".format(msg, e))
        return wrapper
    return middle
