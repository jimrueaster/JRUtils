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

    def test_compare_date(self):
        self.assertEqual(simple_time.compare_datetime('2019-09-01', '%Y-%m-%d',
                                                  '2019-10-02', '%Y-%m-%d'), -1)
        self.assertEqual(simple_time.compare_datetime('2019-09-01', '%Y-%m-%d',
                                                  '2019-09-01', '%Y-%m-%d'), 0)
        self.assertEqual(simple_time.compare_datetime('2019-11-01', '%Y-%m-%d',
                                                  '2019-10-02', '%Y-%m-%d'), 1)
        self.assertEqual(simple_time.compare_datetime('2019-11', '%Y-%m',
                                                  '2019-10', '%Y-%m'), 1)
        self.assertEqual(simple_time.compare_datetime('2019-11', '%Y-%m',
                                                  '2019-10-15', '%Y-%m-%d'), 1)