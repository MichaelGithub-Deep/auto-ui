#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa


class LoginElements:
    # 登录定位元素
    bs_username = "//input[@placeholder='手机号/公司名称']"
    p_username = '//input[@placeholder="账号"]'
    input_password = '//input[@placeholder="密码"]'
    input_verifyCode = '//input[@placeholder="请输入验证码"]'
    button_login = '//button[text()="登录"]'
    button_verification_code = '//input[@value="获取验证码"]'
    button_sing_up = '//a[text()="立即注册"]'
    button_forget_password = '//a[text()="忘记密码"]'
    button_free_sing_up = '//a[text()="免费注册"]'


