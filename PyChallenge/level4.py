#!/usr/bin/python -tt
"""
http://www.pythonchallenge.com/pc/def/linkedlist.php
"""

import sys
import urllib
import re


urlstart = 'http://www.pythonchallenge.com/pc/def/linkedlist.php'

def main():
    uf = urllib.urlopen(urlstart)
    text = uf.read()
    f = open('level4.html', 'wb')
    f.write(text)
    f.close()
    nothing = []
    chain = urllib.urlopen(urlstart+'?nothing=37278').read()
    for i in range(400):
        match = re.search(r'\d+', chain)
        if match:
            chain = urllib.urlopen(urlstart+'?nothing='+match.group()).read()
            nothing.append(match.group())
        else:
            print i, nothing, chain
            break
        if i % 10 == 0:
            print i


if __name__ == '__main__':
    main()
