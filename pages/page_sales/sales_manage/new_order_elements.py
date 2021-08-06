#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa


class NewOrderElements:
    # 新建订单定位元素
    input_CustomerName = '//input[@placeholder="输入客户名称"]'  # 输入客户名称
    button_CustomerName = '//li[text()="{}"]'  # 选择输入的客户名称
    select_PriorityChannel = "(//span[text()='{}']/..)[1]"  # 优先渠道
    input_batchSearch = "//textarea[@id='J_batchArea']"  # 批量查询输入框
    button_search = "//span[@id='J_batchCheck']"  # 查询（Ctrl+Enter）
    table_extend = '(//div[@class="tableExend-scroll-wrap"])[1]'  # 商品表单滑动
    button_cleanErrorModel = "//span[@class='clear-error-btn']"  # 清除错误类型
    button_ok = "//a[@class='layui-layer-btn0']"  # 确定
    error_class_name = 'add-err-btn'  # 错误类型
    span_operation = '(//div[text()="操作"])[1]'
    input_PayPrice = '//div[@materialno="{}"]//div[@class="salesPrice nestedTable-body-item nestedTable-item-style-line"]//input'  # 商品支付价格
    input_Num = '//div[@materialno="{}"]//div[@class="quantity nestedTable-body-item nestedTable-item-style-line"]//input'  # 商品数量
    input_Pay_Discount = '//div[@materialno="{}"]//div[@class="salesDiscount nestedTable-body-item nestedTable-item-style-line"]//input'  # 支付折扣
    input_Comment = '//div[@materialno="{}"]//div[@class="remark nestedTable-body-item"]//input'  # 商品备注
    input_materialClassName = "layui-input shadow-input stop material-no-input"  # 订货号class name
    button_cancelClassName = "layui-layer-ico layui-layer-close layui-layer-close1"  # 关闭弹框class name
    button_shut = "//a[@class='layui-layer-ico layui-layer-close layui-layer-close1']"  # 关闭弹框
    button_PriorityChannel = "//span[text()='{}']/.."  # 优先渠道
    input_ProductModel = '//input[@placeholder="输入产品型号"]'  # 输入产品型号
    button_ProductModel = '//span[text()="{}"]/..'  # 选择输入的产品型号
    input_PayDiscount = '(//div[@modelname="{}"]//input)[7]'  # 支付折扣
    moveto_OrderComment = '//span[text()="订单备注"]'  # 订单备注
    button_TicketType = "//li[contains(text(),'{}')]"  # 开票类型
    # 创建新客户
    span_newCompany = "//span[text()='创建新客户']"  # 创建新客户（按钮）
    div_moreInfo = "//div[@class='more-new-information']"  # 其他信息
    input_companyName = "//input[@id='J_newCompanyName']"  # 客户名称
    input_companyTypeCode = "//select[@name='companyTypeCode']/..//input"  # 客户类型
    dd_select = "(//dd[@title='{}'])[{}]"  # 选择下拉框中的值（根据名称选择）
    input_realName = "//input[@name='realName']"  # 联系人
    input_layerSales = "//select[@class='layer-sales']/..//input"  # 负责销售
    input_phoneNumber = "//input[@name='mobile']"  # 联系电话
    input_layerBusiness = "//select[@class='layer-business']/..//input"  # 负责商务
    input_bankAccount = "//input[@name='bankAccount']"  # 开户账号
    input_taxRegistrationNo = "//input[@name='taxRegistrationNo']"  # 税号
    input_registerAddress = "//input[@name='registerAddress']"  # 注册地址
    input_bankName = "//input[@name='bankName']"  # 开户银行
    input_registerAddressPhone = "//input[@name='registerAddressPhone']"  # 注册电话
    button_okOrCancel = "//a[@class='layui-layer-btn{}']"  # 确定/取消
    # 收货信息
    input_address_info = '//input[@placeholder="请输入地址信息"]'  # 请输入地址信息
    address_search = '//span[text()="查询地址"]'  # 查询地址
    select_address = '//div[@class="address-list-body"]//span[text()="{}"]'  # 选择已存在的地址
    button_newShippingAddress = '//span[@id="J_newShippingAddress"]'  # 添加地址
    input_receiver = '//input[@name="receiver"]'  # 收货人 !
    input_mobile = '//dd//input[@name="mobile"]'  # 手机号码

    select_province = '//div[text()="{}"]/..//input[@placeholder="请选择省份"]'  # 请选择省份(新增收货地址/新增收票地址)
    select_city = '//div[text()="{}"]/..//input[@placeholder="请选择城市"]'  # 请选择城市
    select_county = '//div[text()="{}"]/..//input[@placeholder="请选择县区"]'  # 请选择县区
    select_optionProvince = '//div[text()="{}"]/..//input[@placeholder="请选择省份"]/../..//dd[@title="{}"]'  # 请选择省份：的选项
    select_optionCity = '//div[text()="{}"]/..//input[@placeholder="请选择城市"]/../..//dd[@title="{}"]'  # 请选择城市：的选项
    select_optionCounty = '//div[text()="{}"]/..//input[@placeholder="请选择县区"]/../..//dd[@title="{}"]'  # 请选择县区：的选项

    input_addressDetail = '//input[@name="addressDetail"]'  # 详细地址
    input_zipCode = '//input[@name="zipCode"]'  # 邮编
    input_phone = '//input[@name="phone"]'  # 固定电话
    input_addressAlias = '//input[@name="addressAlias"]'  # 地址别名
    radio_defaultedDeliver = '//input[@name="defaultedDeliver"]'  # 设置为默认收货地址
    button_saveORCancel = '//a[@class="layui-layer-btn{}"]'  # 保存/取消
    # 运费结算
    freight_settlement = '//li[text()="{}"]'  # 选择快递服务
    freight_price = '//div[text()="运费"]//input'  # 输入快递费用
    new_courier = '//a[text()="前往服务配置新增>"]'  # 前往服务配置新增
    button_freight_info = '//i[@data-tippy-content="点击刷新运费信息"]'  # 点击刷新运费信息
    # 选择普通发票后的操作
    select_invoiceTitle = '//em[text()="{}"]'  # 根据发票抬头选择发票信息
    radio_sameAddress = '//span[text()="同收货地址"]'  # 勾选同收货地址
    span_editInvoice = '//em[text()="{}"]/../..//span[@class="href-btn edit"]'  # 根据发票抬头修改发票信息
    # 新增发票信息
    button_newGeneralInvoice = '//span[@id="J_newGeneralInvoice"]'  # 新增发票信息标签
    input_invoiceTitle = '//input[@class="layui-input J_title"]'  # 发票抬头
    input_taxpayerNum = '//input[@class="layui-input J_taxRegistrationNo"]'  # 纳税人识别号
    button_alertSaveORCancel = '//a[@class="layui-layer-btn{}"]'  # 保存/取消
    add_ticket_address = '//div[text()="新增收票地址"]'  # 新增收票地址
    #
    contract_num = '//input[@placeholder="请输入客户合同号，选填"]'  # 自定义合同号
    order_remark = '//input[@name="remark"]'  # 订单备注
    order_memo = '//input[@name="remarkBox"]'  # 备忘
    # 底部功能区
    button_waitNotice = "//span[text()='等待客户通知出库']/.."  # 等待客户通知出库
    button_SubmitOrder = "//span[text()='提交订单']"  # 提交订单
    button_CollectMoney = "//a[text()='去收款']"  # 去收款
    button_continueOrder = '//a[text()="继续下单"]'  # 继续下单
    button_orderList = '//a[text()="订单列表"]'  # 订单列表
