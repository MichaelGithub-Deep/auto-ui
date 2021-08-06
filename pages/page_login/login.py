#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
# Comment : 登录功能
from utils.common import log_tool
from utils.common.decorator_tool import screenshot
from utils.data import yaml_tool
from utils.common.base_page import *
from pages.page_login.login_elements import LoginElements as login


# 登录模
class LoginPage(BasePage):

    # 初始化
    def __init__(self, driver, user):
        """
        :param driver: 浏览器驱动
        """
        super().__init__()
        self.driver = driver
        self.data = yaml_tool.get_yaml('../../pages/page_login/login')[user]  # 获取配置文件

    # c端登录
    def login_c(self):
        try:
            self.get(self.data['c_url'] + "/user/pre-login?returnUrl=/")  # 打开网址
            self.send_keys(login.bs_username, self.data['c_username'])  # 输入账号
            self.send_keys(login.input_password, self.data['c_password'])  # 输入密码
            self.click(login.button_login)  # 点击登录
        except Exception as e:
            msg = "报错文件：{} 报错行数：{}".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno)
            log_tool.error(msg)

    # b端登录
    def login_b(self):
            self.get(self.data['b_url'] + "/user/operation/pre-login?loginName=" + self.data['b_username'])  # 打开网址
            self.send_keys(login.bs_username, self.data['b_username'])  # 输入账号
            self.send_keys(login.input_password, self.data['b_password'])  # 输入密码
            self.send_keys(login.input_verifyCode, self.data['b_verifyCode'])  # 输入验证码
            self.click(login.button_login)  # 点击登录

    # p端登录
    def login_p(self):
        try:
            self.get(self.data['p_url'] + "/user/employee/pre-login")  # 打开网址
            self.send_keys(login.p_username, self.data['p_username'])  # 输入账号
            self.send_keys(login.input_password, self.data['p_password'])  # 输入密码
            self.send_keys(login.input_verifyCode, self.data['p_verifyCode'])  # 输入验证码
            self.click(login.button_login)  # 点击登录
        except Exception as e:
            msg = "报错文件：{} 报错行数：{}".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno)
            log_tool.error(msg)

    # 获取验证码
    def get_verification_code(self):
        try:
            self.click(login.button_verification_code)
        except Exception as e:
            msg = "报错文件：{} 报错行数：{}".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno)
            log_tool.error(msg)

    # 立即注册
    def sing_up(self):
        try:
            self.click(login.button_sing_up)
        except Exception as e:
            msg = "报错文件：{} 报错行数：{}".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno)
            log_tool.error(msg)

    # 忘记密码
    def forget_password(self):
        try:
            self.click(login.button_forget_password)
        except Exception as e:
            msg = "报错文件：{} 报错行数：{}".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno)
            log_tool.error(msg)

    # 免费注册
    def free_sing_up(self):
        try:
            self.click(login.button_free_sing_up)
        except Exception as e:
            msg = "报错文件：{} 报错行数：{}".format(e.__traceback__.tb_frame.f_globals["__file__"], e.__traceback__.tb_lineno)
            log_tool.error(msg)
