#!/usr/bin/python -tt

import sys
import urllib
import re
import Image

filename = 'level7.py'
url = 'http://www.pythonchallenge.com/pc/def/oxygen.html'


def main():
    uf = urllib.urlopen(url)
    text = uf.read()
    f = open(filename[:-3]+'.html', 'wb')
    f.write(text)
    f.close()
    urllib.urlretrieve(url[:-4]+'png', 'level7.png')
    im = Image.open('level7.png')
    row = [im.getpixel((x, 45))  for x in range(0, im.size[0], 7)]
    ords = [r  for r, g, b, a in row  if r == b == g]
    secret = ''.join(map(chr, ords))
    print secret
    secret = ''.join(map(chr, map(int, re.findall('\d+', secret))))
    print secret


if __name__ == '__main__':
    main()
