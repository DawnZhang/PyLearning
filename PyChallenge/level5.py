#!/usr/bin/python -tt
"""
http://www.pythonchallenge.com/pc/def/peak.html
"""

import sys
import urllib
import re
import pickle


url = 'http://www.pythonchallenge.com/pc/def/peak.html'

def main():
    uf = urllib.urlopen(url)
    text = uf.read()
    f = open('level5.html', 'wb')
    f.write(text)
    f.close()
    f = open('banner.p', 'r')
    codes = pickle.load(f)
    f.close()
    f = open('banner.answer', 'wb')
    for row in codes:
        for item in row:
            for i in range(item[1]):
                f.write(item[0])
        f.write('\n')
    f.close()


if __name__ == '__main__':
    main()
