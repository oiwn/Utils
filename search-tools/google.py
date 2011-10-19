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

import re
import urllib
import random
from grab import Grab, DataNotFound

GOOGLE_SEARCH_REQUEST = """http://www.google.com/search?q=%s&ie=UTF-8"""
GOOGLE_SEARCH_NEXT_PAGE = """http://www.google.com/search?q=%s&start=%d&ie=UTF-8"""

GOOGLE_RESULTS = '//li[@class="g"]'
GOOGLE_RESULTS_TITLE = './/h3[@class="r"]'
GOOGLE_RESULTS_AHREF = './/h3[@class="r"]/a/@href'
GOOGLE_RESULTS_DESC = './/div[@class="s"]'

GOOGLE_RESULTS_VIDEO_TITLE = './/h3'

GOOGLE_RESULTS_RELATED = '//div[contains(text(), "Searches related")]/../table//td//a/text()'
GOOGLE_RESULTS_OVERALL = '//div[@id="resultStats"]/text()'
GOOGLE_OVERALL_REX = re.compile(r'About ([0-9,]+) result')

# will try variants
GOOGLE_TITLE_VARIANTS = (GOOGLE_RESULTS_TITLE, GOOGLE_RESULTS_VIDEO_TITLE, )
GOOGLE_AHREF_VARIANTS = ()
GOOGLE_DESC_VARIANTS = ()

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


class SearchResult(object):
    '''Store one search result'''
    def __init__(self, title, url, description):
        self.title = title
        self.url = url
        self.description = description

    def __str__(self):
        return '<google: %s: %s>' % (self.title, self.url)


class Serp(object):
    '''
    Store serp data

    Implements iterator

    '''
    def __init__(self, results, related=None, overall=None):
        self.overall = 0 if overall is None else overall
        self.results = results
        self.related = related

        self.index = 0

    def __iter__(self):
        return self

    def next(self):
        if ((self.index < 0) or (self.index >= len(self.results))):
            raise StopIteration
        else:
            result = self.results[self.index]
            self.index += 1
            return result


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


    def parse(self, snippet):
        # TODO implement snippet parsing logic
        pass


    def get(self, keyword):
        """
        Get google SERP by keyword
        """
        request = GOOGLE_SEARCH_REQUEST % urllib.quote(keyword)
        self.grab.go(request)
        
        # parse results
        body = self.grab.response.body

        # get related
        related = self.grab.xpath_list(GOOGLE_RESULTS_RELATED)

        # get overall number of results
        try:
            overall = int(GOOGLE_OVERALL_REX.search(body).group(1).replace(',', ''))
        except AttributeError:
            overall = 0

        # extract info
        search_results = []
        snippets = self.grab.xpath_list(GOOGLE_RESULTS)
        
        for snippet in snippets:
            node_title = snippet.xpath(GOOGLE_RESULTS_TITLE)
            # next we'll try to parse title
            # there is few kind of snippets in google:
            # video, news, realtime etc
            if node_title:
                # common snippet
                title = self.grab.get_node_text(node_title[0])
            else:
                node_title = snippet.xpath(GOOGLE_RESULTS_VIDEO_TITLE)
                if node_title:
                    # video title
                    title = self.grab.get_node_text(node_title[0])
                
            node_ahref = snippet.xpath(GOOGLE_RESULTS_AHREF)
            if node_ahref:
                ahref = node_ahref[0]
            
            node_desc = snippet.xpath(GOOGLE_RESULTS_DESC)
            if node_desc:
                desc = self.grab.get_node_text(node_desc[0])

            search_results.append(SearchResult(title, ahref, desc))

        return Serp(search_results, related, overall)
        
        

def main():
    """
    Run tests
    """
    goo = GoogleSearch(proxy_list=['lorien.name:7890'])
    for item in goo.get("vfsd0tl42flcx;"):
        #print item
        pass
    


if __name__ == '__main__':
    main()
    
        
        
