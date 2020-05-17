import re
a='''i: i love fish.com
from: AUTO
to: AUTO
smartresult: dict
client: fanyideskweb
salt: 15811605959637
sign: 2b3d3c8b01002be2faf7f08a5eb95dab
ts: 1581160595963
bv: 7bcd9ea3ff9b319782c2a557acee9179
doctype: json
version: 2.1
keyfrom: fanyi.web
action: FY_BY_REALTlME'''
a=re.sub(r': ','\']=\'',a)
a=re.sub(r'\n','\'\ndata[\'',a)
a='data[\''+a+'\''
print(a)