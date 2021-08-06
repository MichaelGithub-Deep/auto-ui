#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
import time
from selenium import webdriver
from utils.common import log_tool as log
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from config.chromedriver.ChromeDriver import DRIVER_PATH
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException, WebDriverException


class BasePage(object):
    original_window = None
    driver = None

    def __init__(self, timeout=10):
        """
            :param timeout: 显式等待超时时间
        """
        self.timeout = timeout
        self.location_type_dict = {
            "xpath": By.XPATH,
            "id": By.ID,
            "name": By.NAME,
            "css_selector": By.CSS_SELECTOR,
            "class_name": By.CLASS_NAME,
            "tag_name": By.TAG_NAME,
            "link_text": By.LINK_TEXT,
            "partial_link_text": By.PARTIAL_LINK_TEXT
        }

    def start_browser(self, browser='chrome'):
        """
            启动浏览器
            :param browser: 浏览器类型
        """
        # if BasePage.driver:
        #     log.info("浏览器以启动，请勿再次启动浏览器。")
        #     return
        try:
            if browser == "firefox" or browser == "ff":
                BasePage.driver = webdriver.Firefox()
            elif browser == "chrome":
                BasePage.driver = webdriver.Chrome(DRIVER_PATH)
                BasePage.driver.maximize_window()
                # BasePage.driver.implicitly_wait(10)
            elif browser == "internet explorer" or browser == "ie":
                BasePage.driver = webdriver.Ie()
            elif browser == "opera":
                BasePage.driver = webdriver.Opera()
            elif browser == "chrome_headless":
                chrome_options = Options()
                chrome_options.add_argument('--headless')
                BasePage.driver = webdriver.Chrome(DRIVER_PATH, options=chrome_options)
            elif browser == "chrome_debugger":
                chrome_options = Options()
                chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
                BasePage.driver = webdriver.Chrome(DRIVER_PATH, options=chrome_options)
                # BasePage.driver.maximize_window()
                BasePage.driver.implicitly_wait(10)
            elif browser == "mobile":
                # mobileEmulation = {'deviceName': 'Galaxy S5'}
                # chrome_options = webdriver.ChromeOptions()
                # chrome_options.add_experimental_option('mobileEmulation', mobileEmulation)
                # BasePage.driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=chrome_options)
                width = 1500
                height = 300
                pixel_ratio = 3.0
                ua = 'Mozilla/5.0 (Linux; Android 4.1.1; GT-N7100 Build/JRO03C) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/35.0.1916.138 Mobile Safari/537.36 T7/6.3'
                mobile_emulation = {"deviceMetrics": {"width": width, "height": height, "pixelRatio": pixel_ratio},
                                    "userAgent": ua}
                options = webdriver.ChromeOptions()
                options.add_experimental_option('mobileEmulation', mobile_emulation)
                BasePage.driver = webdriver.Chrome(executable_path=DRIVER_PATH, chrome_options=options)
                BasePage.driver.maximize_window()
                BasePage.driver.implicitly_wait(10)
            elif browser == "headless":
                chrome_options = Options()
                # chrome_options.add_argument('--no-sandbox')  # 解决DevToolsActivePort文件不存在的报错
                # chrome_options.add_argument('window-size=1920x3000')  # 指定浏览器分辨率
                # chrome_options.add_argument('--disable-gpu')  # 谷歌文档提到需要加上这个属性来规避bug
                # chrome_options.add_argument('--hide-scrollbars')  # 隐藏滚动条, 应对一些特殊页面
                # chrome_options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
                chrome_options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
                chrome_options.binary_location = r"C:\Program Files\Google\Chrome\Application\chrome.exe"  # 手动指定本机电脑使用的浏览器位置
                # 创建一个driver,进行后面的请求页面等操作，executable_path指定本机中chromedriver.exe的位置
                BasePage.driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=DRIVER_PATH)

            elif browser == 'edge':
                BasePage.driver = webdriver.Edge()
            else:
                log.error("启动浏览器失败，没有找到%s浏览器，请输入'ie', 'ff', 'opera', 'edge', 'chrome' or 'chrome_headless'" % browser)
                raise NameError(
                    "启动浏览器失败，没有找到%s浏览器，请输入'ie', 'ff', 'opera', 'edge', 'chrome' or 'chrome_headless'" % browser)
        except WebDriverException:
            log.error("启动浏览器失败,请检查webdriver是否配置，或者webdriver版本是否和浏览器匹配")
            raise
        self.shot("-------测试开始，启动{}浏览器成功-------".format(browser))

    def get_locator(self, locator):
        """
            解析定位关键字
            :param locator:定位语句 例如：xpath=>//*[@id='kw']
            :return: 元组(By.XPATH,"//*[@id='kw']")
        """
        if "=>" not in locator and "xpath" not in locator:
            by = "xpath"
            value = locator
        elif "=>" in locator:
            by = locator.split("=>")[0].strip()
            value = locator.split("=>")[1].strip()
            if by not in self.location_type_dict:
                log.error("%s中的定位方式错误，请输入正确的定位方式:"
                          "id,name,class_name,xpath,tag_name,css_selector,link_text,partial_link_text" % (locator))
                raise TypeError("%s中的定位方式错误，请输入正确的定位方式:"
                                "id,name,class_name,xpath,tag_name,css_selector,link_text,partial_link_text" % (
                                    locator))
            if by == "" or value == "":
                log.error("%s格式错误，定位方式=>值 示例：'id=>useranme'" % (locator))
                raise NameError("%s格式错误，定位方式=>值 示例：'id=>useranme'" % (locator))
        else:
            log.error("%s格式错误，定位方式=>值 示例：'id=>useranme'" % (locator))
            raise NameError("%s格式错误，定位方式=>值 示例：'id=>useranme'" % (locator))
        return self.location_type_dict[by], value

    def get_element(self, locator):
        """
            根据传入的数据来定位页面元素
            :param locator: 定位语句 例如：xpath=>//*[@id='kw']
            :return: 元素定位结果
        """
        self.shot("定位元素：" + str(locator))
        try:
            return self.wait_util_visibility(locator)
        except TimeoutException:
            time_out_error = "异常错误：{}定位元素超时，请检查定为语句是否正确，或者尝试其他定位方式".format(locator)
            log.error(time_out_error)
            raise TimeoutException(time_out_error)

    def shot(self, *args):
        message = ""
        for i in range(len(args)):
            message += "{} "
            log.info(message.format(*args))
        # allure.attach(BasePage.driver.get_screenshot_as_png(), message.format(*args), allure.attachment_type.PNG)

    def get_png(self):
        BasePage.driver.get_screenshot_as_file("./option.png")

    def max_window(self):
        """
        最大化浏览器
        :return:
        """
        self.shot("最大化浏览器")
        BasePage.driver.maximize_window()

    def set_window(self, wide, high):
        """
        设置浏览器大小
        :param wide: 宽
        :param high: 高
        :return:
        """
        self.shot("设置浏览器大小,宽：", wide, "高", high)
        BasePage.driver.set_window_size(wide, high)

    def close(self):
        """
        关闭浏览器，不退出driver
        :return:
        """
        self.shot("浏览器: 关闭浏览器,不退出driver")
        BasePage.driver.close()

    def quit(self):
        """
        关闭浏览器并退出driver
        :return:
        """
        self.shot("浏览器: 关闭浏览器并退出driver")
        BasePage.driver.quit()

    def get(self, url):
        """
        打开网址
        :param url:网址
        :return:
        """
        self.shot("打开网址: " + str(url))
        BasePage.driver.get(url)

    def forward(self):
        """
        前进
        :return:
        """
        self.shot("前进")
        BasePage.driver.forward()

    def back(self):
        """
        后退
        :return:
        """
        self.shot("后退")
        BasePage.driver.back()

    def refresh(self):
        """
        刷新
        :return:
        """
        self.shot("刷新")
        BasePage.driver.refresh()

    def get_title(self):
        """
        获取当前页面的title
        :return: title
        """
        self.shot("获取当前页面的title: " + str(BasePage.driver.title))
        return BasePage.driver.title

    def get_url(self):
        """
        获取当前页面的网址
        :return: url
        """
        self.shot("获取URL: " + str(BasePage.driver.current_url))
        return BasePage.driver.current_url

    def send_keys(self, locator, text):
        """
        先清空文本(clear)输入框，再输入(send_keys)内容
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param text: 输入的文本内容
        :return:
        """
        element = self.get_element(locator)
        el = str(element).split(", ")[1]
        self.shot("输入内容：在{}中输入: {}".format(el, text))
        ActionChains(BasePage.driver).click(element).key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        element.send_keys(text)

    # 双击清除并输入输入
    def input(self, locator, text):
        """
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param text: 输入的文本内容
        :return:
        """
        element = self.get_element(locator)
        # self.move_to_element(locator)
        ActionChains(BasePage.driver).double_click(element).key_down(Keys.BACKSPACE).key_up(Keys.BACKSPACE).perform()
        element.send_keys(text)

    def click(self, locator):
        """
        左键单击操作
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :return:
        """
        element = self.get_element(locator)
        if element is not None:
            self.shot("点击元素: " + str(element))
            ActionChains(BasePage.driver).move_to_element(element).click(element).perform()

    def click_by_js(self, locator):
        """
        #通过xpath执行js代码点击元素
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :return:
        """
        try:
            el = self.get_element(locator)
            loc = self.get_locator(locator)
            self.shot("使用js代码点击元素: " + str(el))
            if loc[0] == self.location_type_dict["xpath"]:
                js = "var xpath = \"" + self.double_to_single_mark(loc[1]) + "\";var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.click();"
                self.driver.execute_script(js)
            else:
                message = "元素点击失败，请使用xpath定位，例如：xpath=>//*[@id='kw']"
                log.error(message)
                raise TypeError(message)
        except:
            log.error("点击元素失败:" + locator)
            raise

    def right_click(self, locator):
        """
        右键单击操作
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :return:
        """
        el = self.get_element(locator)
        self.shot("右击元素: " + str(el))
        ActionChains(BasePage.driver).context_click(el).perform()

    def double_click(self, locator):
        """
        左键双击操作
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :return:
        """
        el = self.get_element(locator)
        self.shot("双击元素: " + str(el))
        ActionChains(BasePage.driver).double_click(el).perform()

    def move_to_element(self, locator):
        """
        鼠标移动到元素上方，并保持悬浮
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :return:
        """
        el = self.get_element(locator)
        self.shot("鼠标悬浮在：", el)
        ActionChains(BasePage.driver).move_to_element(el).perform()

    def drag_and_drop(self, el_locator, ta_locator):
        """
        拖拽一个元素到另一个元素
        :param el_locator: 要拖拽的元素，定位语句 例如：xpath=>//*[@id='kw']
        :param ta_locator: 拖拽的目标元素，定位语句 例如：xpath=>//*[@id='kw']
        :return:
        """
        element = self.get_element(el_locator)
        target = self.get_element(ta_locator)
        self.shot("拖拽：", element, " 至： ", target)
        ActionChains(BasePage.driver).drag_and_drop(element, target).perform()

    def drag_and_drop_by_offset(self, locator, x, y):
        """
        拖拽元素移动一定距离
        :param locator: 要拖拽的元素，定位语句 例如：xpath=>//*[@id='kw']
        :param x: 屏幕横向移动的距离，往右为正，往左为负
        :param y: 屏幕纵向移动的距离，往下为正，往上为负
        :return:
        """
        element = self.get_element(locator)
        self.shot("拖拽：", element, "横向移动：", x, "像素,纵向移动", y, '像素')
        ActionChains(BasePage.driver).drag_and_drop_by_offset(element, x, y).perform()

    def submit(self, locator):
        """
        对元素执行表单提交操作
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :return:
        """
        el = self.get_element(locator)
        self.shot("提交表单：", el)
        el.submit()

    def scroll_screen_x_y(self, x, y):
        """
        滚动窗口横向滚动x像素，纵向滚动y像素， 往右x为正值，左x为负值，下y为正值，上y为负值
        :param x:屏幕横向滚动的距离，单位像素 往右x为正值，左x为负值
        :param y:屏幕纵向滚动的距离，单位像素 下y为正值，上y为负值
        :return:
        """
        self.shot("屏幕横向滚动：", x, "像素", '纵向滚动:', y, '像素')
        js = "window.scrollBy({},{})".format(x, y)
        BasePage.driver.execute_script(js)

    def scroll_screen_to_element(self, locator):
        """
        滚动窗口至元素locator出现
        :param locator: 要拖拽的元素，定位语句 例如：xpath=>//*[@id='kw']
        :return:
        """
        el = self.get_element(locator)
        self.shot("屏幕滚动至元素：", el, '出现')
        js = "arguments[0].scrollIntoView();"
        BasePage.driver.execute_script(js, el)

    def e_script(self, script):
        """
        执行js代码
        :param script:
        :return:
        """
        self.shot("执行js代码：", script)
        BasePage.driver.execute_script(script)

    def re_execute_script(self, script):
        """
        执行js代码
        :param script:
        :return:
        """
        self.shot("执行js代码：", script)
        return BasePage.driver.execute_script(script)

    def get_attribute(self, locator, attribute):
        """
        获取元素属性的值
        :param locator:定位语句 例如：xpath=>//*[@id='kw']
        :param attribute: 属性名
        :return: 属性值
        """
        el = self.get_element(locator)
        value = el.get_attribute(attribute)
        self.shot("获取元素：", el, ' 属性: ', attribute, " 的值为: ", value)
        return value

    def get_text(self, locator):
        """
        获取元素展示文本
        :param locator:定位语句 例如：xpath=>//*[@id='kw']
        :return: 展示文本
        """
        el = self.get_element(locator)
        text = el.text
        if "\n" in str(text):
            text = str(text).split('\n')
            self.shot("获取元素: " + str(el) + " 元素文本: " + str(text))
        else:
            self.shot("获取元素: " + str(el) + " 元素文本: " + str(text))
        return text

    def get_page_source(self):
        page_source = BasePage.driver.page_source
        self.shot("获取页面源代码为: ")
        return page_source

    def is_display(self, locator):
        """
        判断元素是否可见
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :return: 可见为true 不可见为false
        """
        el = self.get_element(locator)
        display = el.is_displayed()
        if display:
            self.shot("元素：", el, " 可见 ")
        else:
            self.shot("元素：", el, " 不可见 ")
        return display

    def double_to_single_mark(self, s):
        """
        将字符串中的双引号转换成单引号
        :param s: 字符串
        :return: 字符串
        """
        return s.replace('"', '\'')

    def update_attribute_by_xpath(self, locator, attribute_name, attribute_value):
        """
        #通过xpath根据修改html标签属性的值
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param attribute_name:属性名
        :param attribute_value: 属性值
        :return:
        """
        try:
            el = self.get_element(locator)
            loc = self.get_locator(locator)
            self.shot("修改元素：", el, '属性:', attribute_name, '的值为：', attribute_value)
            if loc[0] == self.location_type_dict["xpath"]:
                js = "var xpath = \"" + self.double_to_single_mark(
                    loc[
                        1]) + "\";var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.setAttribute(\"" + attribute_name + "\",\"" + attribute_value + "\");"
                self.driver.execute_script(js)
            else:
                message = "修改元素：{} 属性的值失败，请使用xpath定位，示例：xpath=>//*[@id='kw']"
                log.error(message)
                raise TypeError(message)
        except:
            log.error("修改属性值失败，属性名:" + attribute_name + " 属性值:" + attribute_value)
            raise

    def remove_attribute_by_xpath(self, locator, attribute_name):
        """
        #通过xpath删除html标签属性
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param attribute_name:属性名
        :return:
        """
        try:
            el = self.get_element(locator)
            loc = self.get_locator(locator)
            self.shot("删除元素：", el, '的', attribute_name, '属性:')
            if loc[0] == self.location_type_dict["xpath"]:
                js = "var xpath = \"" + self.double_to_single_mark(
                    loc[
                        1]) + "\";var element = document.evaluate(xpath,document,null,XPathResult.ANY_TYPE,null).iterateNext();element.removeAttribute(\"" + attribute_name + "\");"
                self.driver.execute_script(js)
        except:
            self.shot("修改属性值失败，属性名:" + attribute_name)
            raise

    # def file_upload(self, locator, file_path):
    #     """
    #     点击上传文件按钮并上传文件
    #     :param locator: 定位语句 例如：xpath=>//*[@id='kw']
    #     :param file_path: 文件路径
    #     :return:
    #     """
    #     self.click(locator)
    #     autoit.win_wait("打开", 10)
    #     self.sleep(1)
    #     file_path = os.path.abspath(file_path)
    #     self.shot("上传文件",file_path)
    #     # autoit.control_send("打开", "Edit1", os.path.abspath(file_path))
    #     autoit.control_set_text("打开", "Edit1", file_path)
    #     autoit.control_click("打开", "Button1")

    def get_alert_text(self):
        """
        获取弹框的展示文本
        :return:展示文本
        """
        try:
            WebDriverWait(BasePage.driver, 5, 0.5).until(EC.alert_is_present)
        except:
            log.error("切换弹窗失败，当前页面不存在弹窗")
            raise
        text = BasePage.driver.switch_to.alert.text
        self.shot("获取弹框展示文本为：", text)
        return text

    def alert_send_keys(self, text):
        """
        #窗口切换至弹窗输入内容并确定
        :param text: 输入的文本
        :return:
        """

        try:
            WebDriverWait(BasePage.driver, 5, 0.5).until(EC.alert_is_present)
        except:
            log.error("切换弹窗失败，当前页面不存在弹窗")
            raise

        alert = BasePage.driver.switch_to.alert
        self.shot("弹框输入：", text)
        alert.send_keys(text)

    def alert_accept(self):
        """
        切换到弹框并确认
        :return:
        """
        try:
            alert = WebDriverWait(BasePage.driver, 5, 0.5).until(EC.alert_is_present)
            alert.accept()
        except:
            log.error("切换弹窗失败，当前页面不存在弹窗")
            raise
        self.shot("弹框确定操作")

    def alert_dismiss(self):
        """
        切换至弹框，并取消
        :return:
        """
        try:
            WebDriverWait(BasePage.driver, 5, 0.5).until(EC.alert_is_present)
        except:
            log.error("切换弹窗失败，当前页面不存在弹窗")
            raise
        self.shot("弹框取消操作")
        BasePage.driver.switch_to.alert.dismiss()

    def switch_to_frame(self, locator):
        """
        切入iframe框架里边
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :return:
        """
        iframe_el = self.get_element(locator)
        self.shot("切入iframe：", iframe_el)
        BasePage.driver.switch_to.frame(iframe_el)

    def switch_to_current_frame_out(self):
        """
        退出当前iframe
        :return:
        """
        self.shot("退出当前iframe")
        BasePage.driver.switch_to.parent_frame()

    def switch_to_frame_out(self):
        """
        切出iframe,回到主界面
        :return:
        """
        self.shot("切出iframe，回到主界面")
        BasePage.driver.switch_to.default_content()

    def switch_to_windows_by_title(self, title):
        """
        #切换到名字为title的窗口
        :param title: 窗口标题
        :return: 返回值：当前窗口的句柄
        """
        self.shot("切换窗口至：", title)
        current = BasePage.driver.current_window_handle
        handles = BasePage.driver.window_handles
        for handle in handles:
            BasePage.driver.switch_to.window(handle)
            if (BasePage.driver.title.__contains__(title)):
                break
        return current

    def screenshot(self, file_path):
        """
        截图
        :param file_path: 文件路径
        :return:
        """
        self.shot("截取图片：图片已保存至> {}".format(file_path))
        BasePage.driver.get_screenshot_as_file(file_path)

    def select_by_value(self, locator, value):
        """
        操作select标签，根据标签的value属性值选择
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param value: select标签value属性的值
        :return:
        """
        el = self.get_element(locator)
        self.shot("选择value值为：", value, ' 的选项')
        Select(el).select_by_value(value)

    def select_by_index(self, locator, value):
        """
        操作select标签，根据选项的下标选择，下标从0开始
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param value: 选项的下标
        :return:
        """
        el = self.get_element(locator)
        self.shot("选择第", value + 1, ' 个选项')
        Select(el).select_by_index(value)

    def select_by_text(self, locator, value):
        """
        操作select标签，根据选项的展示文本选择
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param value: 下拉选项的展示文本
        :return:
        """
        el = self.get_element(locator)
        self.shot("选择文本为:", value, ' 的选项')
        Select(el).select_by_visible_text(value)

    def sleep(self, sec):
        """
        线程休眠
        :param sec: 秒数
        :return:
        """
        time.sleep(sec)

    def wait_time(self, secs):
        """
        元素定位的隐式等待
        :param secs: 最长秒数
        :return:
        """
        BasePage.driver.implicitly_wait(secs)

    def wait_util_presence(self, locator, secs=10):
        """
        显示等待页面元素出现在DOM中，但并不一定可见，存在则返回该页面元素对象
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param secs: 最长等待时间
        :return:元素对象
        """
        locator = self.get_locator(locator)
        try:
            element = WebDriverWait(BasePage.driver, secs).until(
                EC.presence_of_element_located(locator))
            return element
        except Exception as e:
            raise e

    def wait_util_visibility(self, locator, secs=10):
        """
        显示等待页面元素的出现，并返回元素对象
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param secs: 最长等待时间
        :return:元素对象
        """
        locator = self.get_locator(locator)
        try:
            element = WebDriverWait(BasePage.driver, secs).until(EC.visibility_of_element_located(locator))
            return element
        except Exception as e:
            raise e

    def is_ElementExist(self, locator, secs=2):
        """
        显示等待页面元素的出现，并返回元素对象
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param secs: 最长等待时间
        :return:元素对象
        """
        locator = self.get_locator(locator)
        try:
            element = WebDriverWait(BasePage.driver, secs).until(
                EC.visibility_of_element_located(locator))
            return True
        except:
            return False

    def wait_util_not_visibility(self, locator, secs=10):
        """
        显示等待页面元素不可见
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param secs: 最长等待时间
        :return:
        """
        locator = self.get_locator(locator)
        try:
            WebDriverWait(BasePage.driver, secs).until(
                EC.invisibility_of_element_located(locator))

        except Exception as e:
            raise e

    def wait_util_clickable(self, locator, secs=10):
        """
        判断某个元素中是否可见并且是可点击的，并返回元素对象
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param secs: 等待超时时间
        :return:元素对象
        """
        locator = self.get_locator(locator)
        try:
            element = WebDriverWait(BasePage.driver, secs).until(
                EC.element_to_be_clickable(locator))
            return element
        except Exception as e:
            raise e

    def wait_util_selected(self, locator, secs=10):
        """
        判断某个元素是否被选中了,一般用在select下拉框
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param secs: 等待超时时间
        :return:
        """
        locator = self.get_locator(locator)
        try:
            element = WebDriverWait(BasePage.driver, secs).until(
                EC.element_to_be_selected(locator))
            return element
        except Exception as e:
            raise e

    def wait_util_text(self, locator, text, secs=10):
        """
        判断text是否存在于元素展示文本中
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param text: 判断内容
        :param secs: 等待超时时间
        :return: 存在返回：true 不存在返回：flase
        """
        locator = self.get_locator(locator)
        try:
            is_true = WebDriverWait(BasePage.driver, secs).until(
                EC.text_to_be_present_in_element(locator, text))
            return is_true
        except Exception as e:
            raise e

    def wait_util_at_lest_one(self, locator, secs=10):
        """
        判断是否至少有1个元素存在于dom树中，如果定位到就返回列表
        :param locator: 定位语句 例如：xpath=>//*[@id='kw']
        :param secs: 等待超时时间
        :return: 定位到的元素对象列表
        """
        locator = self.get_locator(locator)
        try:
            items = WebDriverWait(BasePage.driver, secs).until(
                EC.presence_of_all_elements_located(locator))
            return items
        except Exception as e:
            raise e

    def wait_util_title_is(self, title, secs=10):
        """
        判断页面标题和title相等
        :param title: 指定标题内容
        :param secs: 等待超时时间
        :return: 相等返回：true 不相等返回：false
        """
        try:
            is_true = WebDriverWait(BasePage.driver, secs).until(
                EC.title_is(title))
            return is_true
        except Exception as e:
            raise e

    def wait_util_title_contains(self, title, secs=10):
        """
        显示等待页面title包含指定内容
        :param title: 标题指定内容
        :param secs: 等待超时时间
        :return: 包含返回：true，不包含返回：false
        """
        try:
            is_true = WebDriverWait(BasePage.driver, secs).until(
                EC.title_contains(title))
            return is_true
        except Exception as e:
            raise e

    def wait_util_alert_present(self, secs=10):
        """
        判断页面上是否存在alert,如果有就切换到alert
        :param secs: 等待超时时间
        :return: 弹框对象
        """
        try:
            return WebDriverWait(BasePage.driver, secs).until(
                EC.alert_is_present())
        except Exception as e:
            raise e

    def wait_util_frame_available(self, locator, secs=10):
        """
        检查frame是否存在，存在则切换进去
        :param locator:定位语句 例如：xpath=>//*[@id='kw']
        :param secs: 等待超时时间
        :return:
        """
        locator = self.get_locator(locator)
        try:
            WebDriverWait(BasePage.driver, secs).until(
                EC.frame_to_be_available_and_switch_to_it(locator))
        except Exception as e:
            raise e

    # 换行输入
    def input_newline(self, locator, text):
        """
        :param locator: 定位语句
        :param text: 要输入的内容
        :return:
        """
        element = self.get_element(locator)
        element.send_keys(text)
        ActionChains(BasePage.driver).key_down(Keys.ENTER).key_up(Keys.ENTER).perform()

    # 获取class=***的元素个数
    def get_elements_num(self, class_name):
        """
        :param class_name: 元素类名称
        :return: 元素个数
        """
        elements = BasePage.driver.execute_script(
            "return document.getElementsByClassName('{}').length".format(class_name))
        return int(elements)

    # 获取元素属性值
    def get_elements_attribute_val(self, class_name, index, attribute):
        """
        :param class_name: 元素类名称
        :param index: 元素列表中的第几个元素
        :return: 返回当前下标元素某个属性的值
        """
        element_val = BasePage.driver.execute_script("return document.getElementsByClassName('{}')[{}].getAttribute('{}')".format(class_name, index, attribute))
        return element_val

    # 获取元素文本内容
    def get_innerText(self, class_name, index):
        """
        :param class_name: 元素类名称
        :param index: 元素列表中的第几个元素
        :return: 返回元素的文本
        """
        js = "return document.getElementsByClassName('{}')[{}].innerText".format(class_name, index)
        text = BasePage.driver.execute_script(js)
        return str(text)

    # 断言：文本1是否在文本2中
    def assert_in_text(self, text1, text2):
        """
        :param text1: 判断文本
        :param text2: 目标内容
        :return:
        """
        assert text1 in text2

    # 断言：文本1是否等于文本2
    def assert_is_text(self, text1, text2):
        """
        :param text1: 判断文本
        :param text2: 目标内容
        :return:
        """
        assert text1 == text2

    # 断言：文本1是否等于文本2
    def assert_have_element(self, locator):
        """
        :param locator: 定位语句
        :return:
        """
        self.get_element(locator)
