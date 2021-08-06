#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
# Comment : 菜单元素


class MenuElements:
    # 菜单
    locate_first_menu = '//span[text()="{}"]/../..'
    locate_second_menu = '//span[text()="{}"]/../..'
    className_notNotice = 'coupon-action'
    className_notTip = 'iconfont close-tip fr'
    button_notNotice = '(//span[text()="不再提示"])[{}]'
    button_notTip = '(//i[@class="iconfont close-tip fr"])[{}]'
