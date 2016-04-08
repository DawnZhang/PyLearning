#!/usr/bin/python -tt

import os, sys
import urllib
import re

filename = 'level8.py'
url = 'http://www.pythonchallenge.com/pc/def/integrity.html'


def main():
    uf = urllib.urlopen(url)
    text = uf.read()
    f = open(filename[:-3]+'.html', 'wb')
    f.write(text)
    f.close()


if __name__ == '__main__':
    main()
