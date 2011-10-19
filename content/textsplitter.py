# -*- coding: utf-8 -*-
import os
import re
import sys
import time
import logging

from optparse import OptionParser

__version__ = "1.0"

nltk_exist = True
try:
    import nltk.data
except:
    nltk_exist = False

logger = logging.getLogger('textsplitter')

class TextSplitter():
    def __init__(self, lines, use_nltk = False):
        self.lines = lines
        self.use_nltk = use_nltk
        if use_nltk:
            # upload this shit using ntlk.download() >>> punkt
            self.tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')

    def split(self, lines=""):
        result = []
        
        if not lines:
            lines = self.lines
          
        for line in lines:
            if self.use_nltk:
                result += self.tokenizer.tokenize(line, realign_boundaries=True)
            else:
                grams = [x.strip() + "\n" for x in re.split(r'(?:[!?\.]\s+)+', line)
                         if x.strip()]
                result += grams
        return result

       
def main():
    usage = '%s [options] [source]' % sys.argv[0]
    parser = OptionParser(usage)

    parser.add_option('-l', '--log', default='-',
                      help='redirect logs to file')
    parser.add_option('-d', '--dst', default='',
                      help='destination file')
    parser.add_option('-n', '--nltk', default=False,
                      help='use NLTK as advanched text splitter')

    opts, args = parser.parse_args()

    if opts.log == '-':
        logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    else:
        logging.basicConfig(filename=opts.log, level=logging.INFO)

    if opts.nltk and nltk_exist:
        use_nltk = True
        logging.info("use natural language took kit")
    else:
        use_nltk = False
        logging.info("use regexp")

    if args:
        src = os.path.abspath(args[0])
        if not os.path.isfile(src):
            logging.info("Can't locate file")
            sys.exit(1)
    else:
        logging.info("Enter source filename")
        sys.exit(1)

    dst = opts.dst or (os.path.splitext(src)[0] + ".spl")

    # open source file
    try:
        with open(src, "r+") as f:
            lines = f.readlines()
    except IOError:
        logging.info("Can't open file")
        sys.exit(1)

    # split text
    text = TextSplitter(lines, use_nltk=use_nltk)
    result = text.split()

    # save result
    try:
        with open(dst, "w+") as f:
            for item in result:
                f.write(item)
    except IOError:
        logging.info("Can't save file")
        sys.exit(1)
    
start_time = time.time()
main()
print "Estimatied time:\t%s" % (time.time() - start_time)
    
