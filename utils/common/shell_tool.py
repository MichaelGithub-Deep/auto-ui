#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
import subprocess
from utils.common import log_tool as log


# 执行shell脚本
def invoke(cmd):
    try:
        subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
        return None
    except Exception as e:
        log.error('执行命令失败，请检查环境配置')
        log.error(str(e))
        raise

