#!/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: JimruEaster<jimru@qq.com>

import unittest

from simple_time import st


class TestSimpleTime(unittest.TestCase):

    def test_is_valid_datetime(self):
        self.assertTrue(st.is_valid_datetime('2019-09-01', '%Y-%m-%d'))
        self.assertFalse(st.is_valid_datetime('2019-09-31', '%Y-%m-%d'))
        self.assertFalse(st.is_valid_datetime('2019-09-01', '%Y-%m'))

    def test_compare_date(self):
        self.assertEqual(st.compare_datetime('2019-09-01', '%Y-%m-%d',
                                                  '2019-10-02', '%Y-%m-%d'), -1)
        self.assertEqual(st.compare_datetime('2019-09-01', '%Y-%m-%d',
                                                  '2019-09-01', '%Y-%m-%d'), 0)
        self.assertEqual(st.compare_datetime('2019-11-01', '%Y-%m-%d',
                                                  '2019-10-02', '%Y-%m-%d'), 1)
        self.assertEqual(st.compare_datetime('2019-11', '%Y-%m',
                                                  '2019-10', '%Y-%m'), 1)
        self.assertEqual(st.compare_datetime('2019-11', '%Y-%m',
                                                  '2019-10-15', '%Y-%m-%d'), 1)