#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
import configparser


class ReadConfigIni:

    """
        实例化ConfigParser
        :param filename：文件路径
    """
    def __init__(self, filename):
        self.cf = configparser.ConfigParser()
        self.cf.read(filename)

    """
        获取配置文件内容
        :param Section 
        :param KeyName
    """
    def getConfigValue(self, Section, KeyName):
        value = self.cf.get(Section, KeyName)
        return value
