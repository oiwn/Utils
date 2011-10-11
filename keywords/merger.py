# -*- coding: utf-8 -*-
'''
Used to construct keyphreases, add locations, add clarifying terms etc.
'''
import itertools

class KeywordsMerger(object):
    '''
    Merge keywords:
    * keywords = [get, order, buy]
    * addwords = [iphone, ipad]
    result = ['get iphone', 'get ipad', 'order iphone'..., 'buy ipad']
    
    Same for prewords, keywords, addwords.
    '''

    def __init__(self, keywords, addwords=None, prewords=None):
        self.keywords = keywords
        self.addwords = addwords
        self.prewords = prewords

    def load_from_file(self, filename):
        pass

    def merge(self):
        if self.addwords and self.prewords is None:
            return map(' '.join, list(itertools.product(self.keywords, self.addwords)))
        elif self.prewords and self.addwords is None:
            return map(' '.join, list(itertools.product(self.prewords, self.keywords)))
        elif self.prewords and self.addwords:
            key_and_add = map(' '.join, list(itertools.product(self.keywords, self.addwords)))
            return map(' '.join, list(itertools.product(self.prewords, key_and_add)))
            
