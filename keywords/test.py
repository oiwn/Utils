#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import unittest
from unittest import TestCase

from merger import KeywordsMerger

PREWORDS = ['where can i', 'how can i']
KEYWORDS = ['get', 'order', 'buy']
ADDWORDS = ['iphone', 'ipad']


class TestKeywords(TestCase):
    def test_keywords_merger(self):
        merger = KeywordsMerger(KEYWORDS, addwords=ADDWORDS, prewords=PREWORDS)
        print merger.merge()


if __name__ == '__main__':
    unittest.main()
        
