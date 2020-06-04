import re



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

#乘幂
def power(a):    
    le=len(re.findall(r'power',a))
    if le==1:
        kuo=re.search(r'power\(.*',a).group()
        kuo=check(kuo)
        cache=re.search(r'power\(.*,.*\)',kuo).group()
        cache1=re.search(r'(?<=power\().*(?=\,)',cache).group()
        cache2=re.search(r'(?<=,).*(?=\))',cache).group()
        cache='{'+cache1+'}^{'+cache2+'}'
        kuo=re.sub(r'\(',r'\(',kuo)
        kuo=re.sub(r'\)',r'\)',kuo)
        print(cache,cache1,cache2,kuo)
        return re.sub(kuo,cache,a)
    elif le==0:
        a=a
    else:
        print('提示：该公式中含有多个Power()函数')
    print(le)


#Main Code

a=r'u-1.278e-8 * power(u(1),2u(2)) + 0.01623 * u - 1195u(1)'

a=power(a)
print(a)
