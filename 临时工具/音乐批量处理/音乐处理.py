import re

with open("name.txt",'r',encoding='utf-8')as f:
    a=f.read()
    
a=re.sub("付费","",a)

print(a)
f.close
with open("output.txt",'w',encoding='utf-8')as f:
    f.writelines(a)
