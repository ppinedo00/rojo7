# what about making trans??

import string

# intab = "aeiou"
# outtab = "12345"
txt = '''g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.'''

## a >> c, b >> d, ...
trantab = str.maketrans(string.ascii_lowercase, string.ascii_lowercase[2:] + string.ascii_lowercase[:2])

print(trantab)

print(txt.translate(trantab))

# "abcdef".translate(str.maketrans('def', 'ghi'))
