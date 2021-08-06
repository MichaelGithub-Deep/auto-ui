#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
# Comment : 测试类
from pages.page_menu.menu import MenuPage
from utils.common.decorator_tool import catch
from pages.page_sales.sales_manage.new_order import NewOrderPage, ProductInfo, AddAddress, GeneralInvoice


# 测试实例
class TestAddOrder(object):

    # 进入某个菜单
    @catch
    def test_menu(self, driver):
        menu = MenuPage(driver)
        menu.click_first_menu("销售")
        menu.click_second_menu("新建订单")
        menu.click_close_notice()
        menu.click_close_tip()

    # 新建订单
    @catch
    def test_order(self, driver):
        order = NewOrderPage(driver)
        # 创建新客户
        new_company = order.click_new_company()
        new_company.input_company_name("工控猫科技10")
        new_company.select_company_type("EU")
        new_company.input_real_name("龙海")
        new_company.input_layer_sales("lyh3")
        new_company.input_phone_number("19999999999")
        new_company.select_layer_business("lyh4")
        new_company.input_bank_account("777788889999")
        new_company.input_tax_registration_num("92350782MA8TKU0H8E")
        new_company.input_register_address("上海市工控猫")
        new_company.input_bank_name("招商银行")
        new_company.input_register_phone("023-123456789")
        new_company.click_ok()
        # 选择客户
        order.select_company("工控猫科技3")
        # 批量查询商品
        order.input_batch_product("接口_编辑_1389,接口_新增_279_771,NSX-LYH-01")
        order.click_batch_product_query()
        # 操作商品信息
        prod = ProductInfo(driver)
        prod.priority_channel("现货")
        prod.comment("接口_编辑_1389", "自动化测试")
        prod.comment("接口_新增_279_771", "自动化测试")
        prod.comment("NSX-LYH-01", "自动化测试")
        # 添加地址
        add_address = AddAddress(driver)
        order.add_address()
        add_address.input_receiver("上海工控猫")
        add_address.input_mobile("19999999999")
        add_address.select_region("新增收货地址", "上海市", "上海市", "闵行区")
        add_address.input_address_detail("智谷8号楼2层F工控猫")
        add_address.input_zip_code("200000")
        add_address.input_phone("012-12345678")
        add_address.input_address_alias("工控猫")
        add_address.tick_default_address()
        add_address.click_ok()
        # 开票类型
        order.select_invoice("普通发票")
        general = GeneralInvoice(driver)
        general.click_new_general_invoice()
        general.input_invoice_title("title1")
        general.input_taxpayer_identify_num("82350782MA8TKU0H8E")
        general.click_ok()
        general.tick_same_address()
        # 订单备注
        order.input_order_remarks("这是备注：界面自动化测试...")
        # 订单备忘
        order.input_order_memo("这是备忘：界面自动化测试...")
        # 等待客户通知出库
        order.wait_customer_notice_out()
        # 提交订单
        submit_after = order.submit_order()
        order_num = submit_after.get_order_num()
        info = submit_after.get_submit_info()
        print(order_num, "成功提示：", info)
        driver.assert_is_text('点击"去收款"前往去收款，点击"订单列表"前往查看该订单', info)
