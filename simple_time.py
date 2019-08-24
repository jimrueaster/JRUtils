#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: JimruEaster<jimru@qq.com>

import datetime as dt
import time


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


def validate_datetime(date_str, fmt):
    """
    验证日期
    :param date_str: 日期字符串
    :param fmt: 格式
    :return:
    """
    if not is_valid_datetime(date_str, fmt):
        raise ValueError("Incorrect data format, should be " + fmt)


def compare_datetime(datetime1, fmt1, datetime2, fmt2):
    """
    比较两个日期
    :param datetime1: 日期1
    :param fmt1: 格式1
    :param datetime2: 日期2
    :param fmt2: 格式2
    :return: int
    """
    validate_datetime(datetime1, fmt1)
    validate_datetime(datetime2, fmt2)

    t1 = time.strptime(datetime1, fmt1)
    t2 = time.strptime(datetime2, fmt2)

    if t1 < t2:
        return -1
    if t1 == t2:
        return 0
    if t1 > t2:
        return 1


def convert_format(s_datetime, s_from_fmt, s_to_fmt):
    """
    改变时间的格式
    :param s_datetime: 时间字符串
    :param s_from_fmt: 原本格式
    :param s_to_fmt:  目标格式
    :return: string
    """
    return dt.datetime.strptime(s_datetime, s_from_fmt).strftime(s_to_fmt)
