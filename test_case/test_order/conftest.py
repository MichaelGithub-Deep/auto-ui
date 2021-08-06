#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
import allure
import pytest
from pages.page_login.login import LoginPage
from utils.common.base_page import BasePage


@pytest.fixture(scope="session")
@allure.title("获取浏览器驱动")
def driver():
    page = BasePage()
    #  启动浏览器 chrome_debugger chrome
    page.start_browser("chrome")
    login = LoginPage(driver, '龙海')
    login.login_b()
    yield page
    # 用例执行结束关闭driver退出浏览器
    # page.close()
    # page.quit()

