#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: JimruEaster<jimru@qq.com>

import datetime as dt
import operator
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


def _offset_time_delta(s_operator, s_datetime, s_from_fmt, d_delta, s_to_fmt):
    """
    获得偏移后的时间
    :param string s_operator: 操作符
    :param string s_datetime: 时间
    :param string s_from_fmt: 时间格式
    :param dict d_delta: 时间间隔
    :param string s_to_fmt:
    :return: string
    """
    time_tuple = dt.datetime.strptime(s_datetime, s_from_fmt)

    days = d_delta.get('days', 0)
    seconds = d_delta.get('seconds', 0)
    microseconds = d_delta.get('microseconds', 0)
    milliseconds = d_delta.get('milliseconds', 0)
    minutes = d_delta.get('minutes', 0)
    hours = d_delta.get('hours', 0)
    weeks = d_delta.get('weeks', 0)

    delta = dt.timedelta(days=days, seconds=seconds, microseconds=microseconds, milliseconds=milliseconds,
                         minutes=minutes, hours=hours, weeks=weeks, )
    return getattr(operator, s_operator)(time_tuple, delta).strftime(s_to_fmt)


def sub_time_delta(s_datetime, s_from_fmt, d_delta, s_to_fmt):
    """
    减去一段时间后的时间
    :param string s_datetime:
    :param string s_from_fmt:
    :param dict d_delta:
    :param string s_to_fmt:
    :return: string
    """
    return _offset_time_delta('sub', s_datetime, s_from_fmt, d_delta, s_to_fmt)


def add_time_delta(s_datetime, s_from_fmt, d_delta, s_to_fmt):
    """
    增加一段时间后的时间
    :param string s_datetime:
    :param string s_from_fmt:
    :param dict d_delta:
    :param string s_to_fmt:
    :return: string
    """
    return _offset_time_delta('add', s_datetime, s_from_fmt, d_delta, s_to_fmt)
