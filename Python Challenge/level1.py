#http://www.pythonchallenge.com/pc/def/map.html

import string

sentence = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
s_new = []

alphabet_all = list(string.ascii_lowercase)
for ch in sentence:
    if ch in alphabet_all:
		s_new.append(alphabet_all[(alphabet_all.index(ch)+2)%len(alphabet_all)])
    else:
		s_new.append(ch)

print ''.join(s_new)

intab = string.ascii_lowercase
outtab = intab[2:] + intab[:2]
trantab = string.maketrans(intab, outtab)
print sentence.translate(trantab)

url = "pc/def/map.html"
print url.translate(trantab)