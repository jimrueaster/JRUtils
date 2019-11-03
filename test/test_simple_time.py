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

    def test_convert_format(self):
        self.assertEqual(simple_time.convert_format('2019-09-01', '%Y-%m-%d', '%Y-%m'), '2019-09')
        self.assertEqual(simple_time.convert_format('2019-09-01', '%Y-%m-%d', '%m-%d'), '09-01')
        self.assertEqual(simple_time.convert_format('2019-09', '%Y-%m', '%Y'), '2019')
        self.assertEqual(simple_time.convert_format('2019-09', '%Y-%m', '%m-%d'), '09-01')

    def test_sub_time_delta(self):
        self.assertEqual(
            simple_time.sub_time_delta('2019-09-01 11:22:00', '%Y-%m-%d %H:%M:%S', {'hours': 1, 'minutes': 20},
                                       '%Y-%m-%d %H:%M:%S'), '2019-09-01 10:02:00')

    def test_add_time_delta(self):
        self.assertEqual(
            simple_time.add_time_delta('2019-09-01 11:22:00', '%Y-%m-%d %H:%M:%S', {'hours': 1, 'minutes': 20},
                                       '%Y-%m-%d %H:%M:%S'), '2019-09-01 12:42:00')