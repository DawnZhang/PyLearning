#!/usr/bin/python -tt

import os, sys
import urllib
import re
import itertools

filename = 'level10.py'
url = 'http://www.pythonchallenge.com/pc/return/bull.html'


def look_and_say(length):
    table = {
        ('1', '1', '1'): '31',  \
        ('1', '1'): '21',       \
        ('1', ): '11',          \
        ('2', '2', '2'): '32',  \
        ('2', '2'): '22',       \
        ('2', ): '12',          \
        ('3', '3', '3'): '33',  \
        ('3', '3'): '23',       \
        ('3', ): '13'           \
    }
    prec, result = '1', [1]
    for i in xrange(length-1):
        prec = ''.join(table[tuple(l)] for e, l in itertools.groupby(prec))
        result.append(int(prec))
    return result


def main():
#    uf = urllib.urlopen(url)
#    text = uf.read()
#    f = open(filename[:-3]+'.html', 'wb')
#    f.write(text)
#    f.close()
    print len(str(look_and_say(31)[30]))


if __name__ == '__main__':
    main()
