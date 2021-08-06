#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
# Comment : 菜单功能
from utils.common.base_page import BasePage
from pages.page_sales.sales_manage.new_order import NewOrderPage
from pages.page_menu.menu_elements import MenuElements as menu


# 菜单类
class MenuPage(BasePage):

    # 点击一级菜单
    def click_first_menu(self, text):
        """
        :param text: 一级菜单名称（str）
        :return:
        """
        self.click(menu.locate_first_menu.format(text))

    # 点击二级菜单
    def click_second_menu(self, text):
        """
        :param text: 二级菜单名称（str）
        :return: 返回【新建订单】对象
        """
        self.click(menu.locate_second_menu.format(text))

    # 点击关闭广告
    def click_close_notice(self):
        notice_num = self.get_elements_num(menu.className_notNotice)
        if notice_num != 0:
            for index in range(notice_num, 0, -1):
                self.click(menu.button_notNotice.format(index))

    # 点击关闭提示
    def click_close_tip(self):
        tip_num = self.get_elements_num(menu.className_notTip)
        if tip_num != 0:
            for index in range(tip_num, 0, -1):
                self.click(menu.button_notTip.format(index))
