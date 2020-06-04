import re
a=r'sqrt(2*u(2)/(u(2)-1))'
a=input('请输入公式：')

#括号检查器
def check(s):
    SL, SR = '(', ')'
    arr=[]
    after=''
    for c in s:
        if c in SL:
            # 左符号入栈
            arr.append(c)                  
        elif c in SR:
            if arr[-1]==SL:
                arr.pop()
            else:
                return False         
            if arr==[]:
                after=after+c
                break
        after=after+c        
    return after

def sqrt(a):    
    le=len(re.findall(r'sqrt',a))
    if le==1:
        kuo=re.search(r'sqrt\(.*',a).group()
        kuo=check(kuo)
        cache=re.search(r'sqrt\(.*.*\)',kuo).group()
        cache=re.sub('sqrt\(','',cache)
        cache=cache[:-1]
        cache=r'\\'+r'sqrt{'+cache+'}'        
        kuo=re.sub(r'(?=[\-|\(|\)|\+|\*|\/|\{|\}|\^])',r'\\',kuo)
        print('cache:\t',cache,'\nkuo:\t',kuo)
        return re.sub(kuo,cache,a)
    elif le==0:
        a=a
    else:
        print('提示：该公式中含有多个Sqrt()函数')
    print('已完成Sqrt()的转换')

#Main Code
a=sqrt(a)
print(a)
        
