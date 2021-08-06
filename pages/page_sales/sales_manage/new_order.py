#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
# Comment : 新建订单
from time import sleep
from utils.common.base_page import BasePage
from pages.page_sales.sales_manage.new_order_elements import NewOrderElements as order


# 新建订单页面
class NewOrderPage(BasePage):

    # 输入并选择客户
    def select_company(self, text):
        """
        :param text: 客户名称（str）
        :return:
        """
        self.send_keys(order.input_CustomerName, text)
        sleep(1)
        self.click(order.button_CustomerName.format(text))
        sleep(1)

    # 点击【创建新客户】"""
    def click_new_company(self):
        self.click(order.span_newCompany)
        self.click(order.div_moreInfo)  # 点击更多
        return NewCompany(self.driver)

    # 【批量输入商品】
    def input_batch_product(self, products):
        """
        :param products: 商品名称，多个商品用英文逗号隔开 例如：”商品1,商品2,商品3“
        :return:
        """
        for product in products.split(","):
            self.input_newline(order.input_batchSearch, product)

    # 点击【确认批量查询】
    def click_batch_product_query(self):
        self.click(order.button_search)
        sleep(1)
        # self.drag_and_drop_by_offset(order.table_extend, '500', '0')
        return ProductInfo(self.driver)

    # 输入查询的地址，再点击【查询收货地址按钮】
    def search_address_info(self, text):
        """
        :param text: 地址(str)
        :return:
        """
        self.input(order.input_address_info, text)
        self.click(order.address_search)

    # 根据收货人名称【选择地址】
    def select_address(self, text):
        """
        :param text: 地址(str)
        :return:
        """
        self.click(order.select_address.format(text))

    # 收货信息点击【添加地址】
    def add_address(self):
        """
        :return: 返回收货信息下的添加地址对象：AddAddress(class)
        """
        self.click(order.button_newShippingAddress)
        return AddAddress(self.driver)

    # 选择【运费结算】
    def select_freight_settlement(self, text):
        """
        :param text: 运费结算名称（str）
        :return:
        """
        self.click(order.freight_settlement.format(text))

    # 输入【运费】
    def input_freight_price(self, text):
        """
        :param text: 运费金额
        :return:
        """
        self.input(order.freight_price, text)

    # 点击【前往服务配置新增】
    def new_courier(self):
        self.click(order.new_courier)

    # 点击【点击刷新运费信息】
    def refresh_freight_info(self):
        self.click(order.button_freight_info)

    # 选择【开票类型】
    def select_invoice(self, text):
        """
        :param text: (暂不开发票/专用发票/普通发票)
        :return:
        """
        self.move_to_element(order.moveto_OrderComment)
        self.click(order.button_TicketType.format(text))
        if text == "普通发票":
            return GeneralInvoice(self.driver)
        if text == "专用发票":
            return SpecialInvoice(self.driver)

    # 输入客户合同号
    def input_contract_num(self, text):
        """
        :param text: 客户合同号
        :return:
        """
        self.input(order.contract_num, text)

    # 订单备注
    def input_order_remarks(self, text):
        """
        :param text: 订单备注(str), 最多输入200个字符
        :return:
        """
        self.input(order.order_remark, text)

    # 订单备忘
    def input_order_memo(self, text):
        """
        :param text: 订单备忘(str), 最多输入500个字符
        :return:
        """
        self.input(order.order_memo, text)

    # 等待客户通知出库
    def wait_customer_notice_out(self):
        self.click(order.button_waitNotice)

    # 提交订单
    def submit_order(self):
        self.click(order.button_SubmitOrder)
        sleep(1)
        return SubmitOrderAfter(self.driver)


# 新建订单二级功能 -- 创建新客户
class NewCompany(BasePage):

    # 输入【客户名称】
    def input_company_name(self, text):
        """
        :param text: 客户名称 (str)
        :return:
        """
        self.send_keys(order.input_companyName, text)

    # 选择【客户类型】
    def select_company_type(self, text):
        """
        :param text: 客户类型 （str\客户类型名称）
        :return:
        """
        self.click(order.input_companyTypeCode)
        self.click(order.dd_select.format(text, "1"))

    # 输入【联系人】
    def input_real_name(self, text):
        """
        :param text: 联系人 (str、联系人名称)
        :return:
        """
        self.send_keys(order.input_realName, text)

    # 选择【负责销售】
    def input_layer_sales(self, text):
        """
        :param text: 负责销售 (str、销售的名称)
        :return:
        """
        self.click(order.input_layerSales)
        self.click(order.dd_select.format(text, "2"))

    # 输入【联系电话】
    def input_phone_number(self, text):
        """
        :param text: 联系电话（str\数字字符串）
        :return:
        """
        self.send_keys(order.input_phoneNumber, text)

    # 选择【负责商务】
    def select_layer_business(self, text):
        """
        :param text: 负责商务
        :return:
        """
        self.click(order.input_layerBusiness)
        self.click(order.dd_select.format(text, "2"))

    # 输入【开户账号】
    def input_bank_account(self, text):
        """
        :param text: 开户账号(str)
        :return:
        """
        self.send_keys(order.input_bankAccount, text)

    # 输入【税号】
    def input_tax_registration_num(self, text):
        """
        :param text: 税号(str)
        :return:
        """
        self.send_keys(order.input_taxRegistrationNo, text)

    # 输入【注册地址】
    def input_register_address(self, text):
        """
        :param text: 注册地址
        :return:
        """
        self.send_keys(order.input_registerAddress, text)

    # 输入【开户银行】
    def input_bank_name(self, text):
        """
        :param text: 开户银行
        :return:
        """
        self.send_keys(order.input_bankName, text)

    # 输入【注册电话】
    def input_register_phone(self, text):
        """
        :param text: 注册电话
        :return:
        """
        self.send_keys(order.input_registerAddressPhone, text)

    # 上传【营业执照】
    # def input_layer_business(self):
    #     pass

    # 点击【确认】
    def click_ok(self):
        self.click(order.button_okOrCancel.format("0"))

    # 点击【取消】
    def click_cancel(self):
        self.click(order.button_okOrCancel.format("1"))


# 开票类型 - 普通发票
class GeneralInvoice(BasePage):

    # 根据发票抬头选择发票信息
    def select_invoice_title(self, text):
        """
        :param text: 发票抬头名称（str）
        :return:
        """
        self.click(order.select_invoiceTitle.format(text))

    # 新增发票
    def click_new_general_invoice(self):
        self.click(order.button_newGeneralInvoice)

    # 输入发票抬头
    def input_invoice_title(self, text):
        """
        :param text: 发票抬头(str)
        :return:
        """
        self.send_keys(order.input_invoiceTitle, text)

    # 输入纳税人识别号
    def input_taxpayer_identify_num(self, text):
        """
        :param text: 纳税人识别号（str）
        :return:
        """
        self.send_keys(order.input_taxpayerNum, text)

    # 根据发票抬头修改发票信息
    def click_update_invoice_info(self, text):
        """
        :param text: 发票抬头名称（str）
        :return:
        """
        self.click(order.span_editInvoice.format(text))

    # 点击【确认】
    def click_ok(self):
        self.click(order.button_okOrCancel.format("0"))
        sleep(1)

    # 点击【取消】
    def click_cancel(self):
        self.click(order.button_okOrCancel.format("1"))

    # 勾选同收货地址
    def tick_same_address(self):
        self.click(order.radio_sameAddress)

    # 新增收票地址
    def add_ticket_address(self):
        """
        :return: 返回新增收票地址对象（class）
        """
        self.click(order.add_ticket_address)
        return AddAddress(self.driver)


# 开票类型 - 专用发票
class SpecialInvoice(BasePage):

    # 勾选同收货地址
    def tick_same_address(self):
        self.click(order.radio_sameAddress)

    # 新增收票地址
    def add_ticket_address(self):
        self.click(order.add_ticket_address)
        return AddAddress(self.driver)


# 商品信息
class ProductInfo(BasePage):

    # 选择优先渠道
    def priority_channel(self, text):
        """
        :param text: 优先渠道名称 (str\渠道的名称)
        :return:
        """
        self.click(order.select_PriorityChannel.format(text))
        sleep(1)

    # 输入支付单价
    def pay_price(self, product_code, text):
        """
        :param product_code: 订货号
        :param text: 支付价格 (str\整数或浮点数)
        :return:
        """
        self.input(order.input_PayPrice.format(product_code), text)

    # 下单数量
    def buy_number(self, product_code, text):
        """
        :param product_code: 订货号
        :param text: 下单数量 (str\整数)
        :return:
        """
        self.input(order.input_Num.format(product_code), text)

    # 支付折扣
    def pay_discount(self, product_code, text):
        """
        :param product_code: 订货号
        :param text: 支付折扣 (str\整数或浮点数)
        :return:
        """
        self.input(order.input_Pay_Discount.format(product_code), text)

    # 商品备注
    def comment(self, product_code, text):
        """
        :param product_code: 订货号
        :param text: 备注内容
        :return:
        """
        self.input(order.input_Comment.format(product_code), text)


# 点击添加地址后可操作的方法
class AddAddress(BasePage):

    # 输入【收货人】
    def input_receiver(self, text):
        """
        :param text:
        :return:
        """
        self.send_keys(order.input_receiver, text)

    # 输入【手机号码】
    def input_mobile(self, text):
        """
        :param text:
        :return:
        """
        self.send_keys(order.input_mobile, text)

    # 选择【所在地区】
    def select_region(self, title, province, city, county):
        """
        :param title: 弹窗标题=（新增收货地址/新增收票地址）
        :param province: 省份(str)
        :param city: 城市(str)
        :param county: 区县(str)
        :return:
        """
        # 选择省份
        self.click(order.select_province.format(title))
        self.click(order.select_optionProvince.format(title, province))
        # 选择城市
        self.click(order.select_city.format(title))
        self.click(order.select_optionCity.format(title, city))
        # 选择区县
        self.click(order.select_county.format(title))
        self.click(order.select_optionCounty.format(title, county))

    # 输入【详细地址】
    def input_address_detail(self, text):
        """
        :param text: 详细地址
        :return:
        """
        self.send_keys(order.input_addressDetail, text)

    # 输入【邮编】
    def input_zip_code(self, text):
        """
        :param text: 邮编
        :return:
        """
        self.send_keys(order.input_zipCode, text)

    # 输入【固定电话】
    def input_phone(self, phone):
        """
        :param phone: 固定电话
        :return:
        """
        self.send_keys(order.input_phone, phone)

    # 输入【地址别名】
    def input_address_alias(self, text):
        """
        :param text: 地址别名
        :return:
        """
        self.send_keys(order.input_addressAlias, text)

    # 勾选【设置为默认收货地址】
    def tick_default_address(self):
        """
        :return:
        """
        self.click(order.radio_defaultedDeliver)

    # 点击【确认】
    def click_ok(self):
        self.click(order.button_okOrCancel.format("0"))
        sleep(1)

    # 点击【取消】
    def click_cancel(self):
        self.click(order.button_okOrCancel.format("1"))


# 提交订单之后可操作的功能
class SubmitOrderAfter(BasePage):

    # 去收款
    def collect_money(self):
        self.click(order.button_CollectMoney)

    # 继续下单
    def continue_order(self):
        self.click(order.button_continueOrder)

    # 订单列表
    def order_list(self):
        self.click(order.button_orderList)

    # 点击提交订单,提交成功后可获取订单号
    def get_order_num(self):
        order_text = self.get_innerText("href-url", "7")
        order_num = order_text[0:len(order_text) - 1]
        return order_num

    # 获取订单提交成功提示
    def get_submit_info(self):
        msg = self.get_innerText("success-layer-msg", "0")
        return msg
