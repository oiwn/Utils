#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
import unittest
from unittest import TestCase

from google import GoogleSearch

class TestSE(TestCase):
    def test_google_search(self):
       goo = GoogleSearch()
       for item in goo.get("something"):
           print item
           

if __name__ == '__main__':
    unittest.main()
