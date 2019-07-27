#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: JimruEaster<jimru@qq.com>

import unittest

import simple_time


class TestSimpleTime(unittest.TestCase):

    def test_is_valid_datetime(self):
        self.assertTrue(simple_time.is_valid_datetime('2019-09-01', '%Y-%m-%d'))
        self.assertFalse(simple_time.is_valid_datetime('2019-09-31', '%Y-%m-%d'))
        self.assertFalse(simple_time.is_valid_datetime('2019-09-01', '%Y-%m'))
