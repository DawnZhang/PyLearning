#!/usr/bin/python -tt

import os, sys
import urllib
import re
import bz2

filename = 'level8.py'
url = 'http://www.pythonchallenge.com/pc/def/integrity.html'
un = 'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
pw = 'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'


def main():
    uf = urllib.urlopen(url)
    text = uf.read()
    f = open(filename[:-3]+'.html', 'wb')
    f.write(text)
    f.close()
    print [bz2.decompress(elt) for elt in (un, pw)]


if __name__ == '__main__':
    main()
