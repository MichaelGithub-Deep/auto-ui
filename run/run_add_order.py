#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
import os
import pytest
import psutil
import subprocess
from utils.common import log_tool as log
from utils.common import shell_tool as shell

# 报告保存路径
xml_report_path = os.path.abspath("../Report/ReportGKM/xml")
html_report_path = os.path.abspath("../Report/ReportGKM/html")


def base_run():
    # 测试用例路径
    log.info("当前步骤：执行base_run{}".format(os.path.abspath("../TestCase/TestCase/")))
    test_case = os.path.abspath("../TestCase/TestCase/TestGKMall.py")
    # 主方法
    pytest.main(['-sq', '--alluredir', xml_report_path, test_case])
    cmd1 = 'allure generate %s -o %s -alluredir --clean' % (xml_report_path, html_report_path)
    shell.invoke(cmd1)


if __name__ == '__main__':
    base_run()


# 打开报告指定端口号
def open_report():
    cmd1 = 'allure serve {} -p 8003'.format(xml_report_path)
    shell.invoke(cmd1)


# (Linux系统)根据端口寻找该进程对应的pid
def close_report_Linux(port=8001):
    # 获取当前的网络连接信息
    net_con = psutil.net_connections()
    for con_info in net_con:
        if con_info.laddr.port == port:
            try:
                pids = con_info.pid
                log.info(pids)
                subprocess.call(["kill", str(pids)])
            except:
                log.info('服务未启动')


# (Windows系统)更具进程名关闭进程_Windows
def close_report(name="java.exe"):
    pids = psutil.process_iter()
    for pid in pids:
        if pid.name() == name:
            cmd2 = "taskkill /F /PID {}".format(pid.pid)
            shell.invoke(cmd2)
