#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author : LongHa
import yaml


def get_yaml(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        content = yaml.load(f.read(), Loader=yaml.FullLoader)
    return content


if __name__ == '__main__':
    t = get_yaml('./test.yarm')
    print(t)
