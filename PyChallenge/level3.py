#!/usr/bin/python -tt
"""
http://www.pythonchallenge.com/pc/def/equality.html
"""

import urllib
import re


def main():
    uf = urllib.urlopen('http://www.pythonchallenge.com/pc/def/equality.html')
    text = uf.read()
    f = open('level3.html', 'wb')
    f.write(text)
    f.close()
    mess = re.findall(r'<!--[\n\S\s]*', text)
    secret = re.findall(r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]', mess[0])
    print ''.join(secret)


if __name__ == '__main__':
    main()
