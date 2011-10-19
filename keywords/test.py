#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import unittest
from unittest import TestCase

from keywords import Keywords

PREWORDS = ['where can i', 'how can i']
KEYWORDS = ['get', 'order', 'buy']
ADDWORDS = ['iphone', 'ipad']


class TestKeywords(TestCase):
    def test_keywords_merger(self):
        keys = Keywords()
        self.assertEqual(12, len(keys.merge(KEYWORDS, addwords=ADDWORDS, prewords=PREWORDS)))


if __name__ == '__main__':
    unittest.main()
        
