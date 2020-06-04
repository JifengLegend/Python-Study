#括号匹配

SL, SR = '(', ')'

def check(s):
    arr=[]
    after=''
    for c in s:
        if c in SL:
            # 左符号入栈
            arr.append(c)
            print(arr)
            print('app')
        elif c in SR:
            if arr[-1]==SL:
                arr.pop()
            else:
                return False
            print(arr)
            print('pop')
            if arr==[]:
                after=after+c
                break
        after=after+c
        print(after)
    return after

print(check("power(u(1),2u(2)) + 0.01623 * u - 1195u(1)"))
