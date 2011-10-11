#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Toolkit for work with google search

особенности:
- многопоточный не только по потокам парсинга, а и по потокам обработки спарсенных данных, за счет чего ускоряется работа
- парсит все до последней страницы по всем кеям, даже если гугль обломал с капчей и т.п.
- все ошибки, которые может гугль выдать - шарит, обходит
- есть опция сохранять в спаршенную базу только новые паги, без повторений
- есть опция парсить все известные поисковики сразу
"""

import urllib
from grab import Grab
from lxml import etree
from lxml.html import fromstring, tostring

GOOGLE_SEARCH_REQUEST = """http://www.google.com/search?q=%s&ie=UTF-8"""
GOOGLE_SEARCH_NEXT_PAGE = """http://www.google.com/search?q=%s&start=%d&ie=UTF-8"""

GOOGLE_RESULTS = '//li[@class="g"]'
GOOGLE_RESULTS_TITLE = './/h3[@class="r"]'
GOOGLE_RESULTS_AHREF = './/h3[@class="r"]/a/@href'
GOOGLE_RESULTS_DESC = './/span[@class="st"]'


# settings
LOG_DIR = 'log'

def default_config():
    """
    default config for module
    """
    return dict(
        proxy = None,
        timeout = 5,
        randomize_timeouts = True)


class SearchResult:
    '''Store one search result'''
    def __init__(self, title, url, description):
        self.title = title
        self.url = url
        self.description = description

    def __str__(self):
        return '<google: %s: %s>' % (self.title, self.url)


class SearchesRelated:
    '''Store list of related keyword'''
    def __init__(self, keyword, related):
        self.title = title
        self.related = related

class GoogleSearch(object):
    """
    Implements Google search
    """
    
    def __init__(self, proxy_list=None):
        """
        Init all shit we need
        """
        self.proxies = proxy_list
        self.grab = self.init_grab()
        # select proxy
        proxy = random.choice(self.proxies) if self.proxies else None
        self.grab.setup(proxy=proxy)

    def init_grab(self):
        return Grab(log_dir='log', hammer_mode=True)

    def get(self, keyword):
        """
        Get google SERP by keyword
        """
        request = GOOGLE_SEARCH_REQUEST % urllib.quote(keyword)
        print request
        self.grab.go(request)
        
        # parse results
        body = self.grab.response.body
        
        snippets = self.grab.xpath_list(GOOGLE_RESULTS)
        
        for snippet in snippets:
            title = snippet.xpath(GOOGLE_RESULTS_TITLE)
            ahref = snippet.xpath(GOOGLE_RESULTS_AHREF)
            print title, ahref
            
        return snippets
        
        


def main():
    """
    Run tests
    """
    goo = GoogleSearch()
    for item in goo.get("something"):
        pass
    


if __name__ == '__main__':
    main()
    
        
        
