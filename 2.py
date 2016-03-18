#!/usr/bin/python
# -*- coding: utf-8 -*-
input = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
## 将输入转换成Ascii码存放进list中
asciiInput = [ord(a) for a in input]

## 如果字符的ascii码在97～123之间，则进行转换
output = ""
for a in asciiInput:
    if a >= 97 and a <= 120:
        output = output + chr(a+2)
    elif a > 120 and a <= 122:
        output = output + chr(a-24)
    else:
        output = output + chr(a)

print output



# method2 use string.maketrans()
import string
a = "abcdefghijklmnopqrstuvwxyz"
b = "cdefghijklmnopqrstuvwxyzab"
trans = string.maketrans(a,b)
print input.translate(trans)


print "map".translate(trans)




