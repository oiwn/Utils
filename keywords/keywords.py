# -*- coding: utf-8 -*-
'''
Used to construct keyphreases, add locations, add clarifying terms etc.
'''
import itertools

class Keywords(object):
    def __init__(self, keywords=None):
        pass

    def load_from_file(self, filename):
        with open(filename, 'r') as f:
            return [line.strip() for line in f.readlines()]

    def merge(self, keywords, addwords=None, prewords=None):
        '''
        Merge keywords:
        * keywords = [get, order, buy]
        * addwords = [iphone, ipad]
        result = ['get iphone', 'get ipad', 'order iphone'..., 'buy ipad']
    
        Same for prewords, keywords, addwords.
        '''
        result = []
        if addwords and prewords is None:
            result = map(' '.join, list(itertools.product(keywords, addwords)))
        elif prewords and addwords is None:
            result =  map(' '.join, list(itertools.product(prewords, keywords)))
        elif prewords and addwords:
            key_and_add = map(' '.join, list(itertools.product(keywords, addwords)))
            result = map(' '.join, list(itertools.product(prewords, key_and_add)))

        return [keyword.strip() for keyword in result]
