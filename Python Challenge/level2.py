# http://www.pythonchallenge.com/pc/def/ocr.html

import string
import urllib
import re

uf = urllib.urlopen('http://www.pythonchallenge.com/pc/def/ocr.html')
text = uf.read()
mess = re.findall(r'<!--\n%%[\n\S\s]*', text)
print filter(lambda x: x in string.ascii_letters, mess[0])
