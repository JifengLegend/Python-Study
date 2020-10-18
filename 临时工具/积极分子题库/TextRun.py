import re

with open ('积极分子题库.md','r',encoding='utf-8')as f:
    a=f.read()
    try:
        a=re.sub(r'答错次数.*','',a)
        a=re.sub(r'\n\n\**易错.*\*\*\n','',a)
        a=re.sub(r'：([ABCD]+)',r'：`\1`',a)
        a=re.sub(r'\*\*\n知识点',r'**\n\n知识点',a)
    except :
        pass
    print(a)

with open ('积极分子题库.md','w',encoding='utf-8')as f:
    f.write(a)