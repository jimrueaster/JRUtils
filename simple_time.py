#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: JimruEaster<jimru@qq.com>

import datetime as dt


def is_valid_datetime(date_str, fmt):
    """
    验证是否正确日期
    :param date_str: 日期字符串
    :param fmt: 格式
    :return: void
    """
    try:
        dt.datetime.strptime(date_str, fmt)
        return True
    except ValueError:
        return False
