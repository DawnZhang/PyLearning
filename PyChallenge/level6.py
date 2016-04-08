#!/usr/bin/python -tt
"""
http://www.pythonchallenge.com/pc/def/channel.html
"""

import sys
import urllib
import re
import zipfile


url = 'http://www.pythonchallenge.com/pc/def/channel.html'


def main():
    uf = urllib.urlopen(url)
    text = uf.read()
    f = open('level6.html', 'wb')
    f.write(text)
    f.close()
    o, n, f = [], '90052', '%s.txt'
    nnr = 'Next nothing is (\d+)'
    myzip = zipfile.ZipFile('channel.zip')
    while True:
        try:
            n = re.search(nnr, myzip.read(f % n)).group(1)
        except:
            print myzip.read(f % n)
            break

        o.append(myzip.getinfo(f % n).comment)

    print ''.join(o)


if __name__ == '__main__':
    main()
