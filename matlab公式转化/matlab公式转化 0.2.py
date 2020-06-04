import re
import time
import matplotlib.pyplot as plt
import matplotlib
matplotlib.get_configdir()
#时间检查器
def TimeGeter():
    now=time.strftime('%H')
    now=int(now)
    if now<=4:
        now='凌晨好'
    elif now<=9:
        now='早上好'
    elif now<=13:
        now='中午好'
    elif now<=18:
        now='下午好'
    elif now<=22:
        now='晚上好'
    elif now<=24:
        now='深夜好'
    return now
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
        cache='{('+cache1+')}^{'+cache2+'}'
        kuo=re.sub(r'(?=[\-|\(|\)|\+|\*|\/|\{|\}|\^])',r'\\',kuo)
        #print('cache:\t',cache,cache1,cache2,'\nkuo:\t',kuo)
        return re.sub(kuo,cache,a)
    elif le==0:
        return a
    else:
        print('提示：该公式中含有多个Power()函数')
    print('已完成Sqrt()的转换,目标公示中Power()的个数为：\t',le,'个')
def numx(a):        #获取有多少个元素
    if re.findall(r'(?<=u\()\d*(?=\))',a)!=[]:
        numx=int(max(re.findall(r'(?<=u\()\d*(?=\))',a)))
        return numx
    else:
        return 1
    print(num)

def sqrt(a):        #开根号
    le=len(re.findall(r'sqrt',a))
    if le==1:
        kuo=re.search(r'sqrt\(.*',a).group()
        kuo=check(kuo)
        cache=re.search(r'sqrt\(.*.*\)',kuo).group()
        cache=re.sub('sqrt\(','',cache)
        cache=cache[:-1]
        cache=r'\\'+r'sqrt{'+cache+'}'        
        kuo=re.sub(r'(?=[\-|\(|\)|\+|\*|\/|\{|\}|\^])',r'\\',kuo)
        #print('cache:\t',cache,'\nkuo:\t',kuo)
        return re.sub(kuo,cache,a)
    elif le==0:
        return a
    else:
        print('提示：该公式中含有多个Sqrt()函数')
    print('已完成Sqrt()的转换目标公示中Sqrt()的个数为：\t',le,'个')

#Main Code
if __name__=='__main__':
    now=TimeGeter()
    while 1 :
        try:
            mode=int(input(now+',请选择运行模式:\n\t（0:公式转换）\n\t（1：公式绘制）：'))
        except ValueError:
            print('输入的值有问题，这里只接受0和1')
            continue
        
        if mode==0:
            try:
                a=input('——请输入公式：')
                if a=='':
                    a=r'(u(1)-u(2)*u(4)*u(5)-u(3)-u(7))/(u(4)*u(6)+power(u(2),9u(8))))+12)'
                num=numx(a)+1
                a=power(a)
                a=sqrt(a)
            except:
                print('出错啦，是正则模块的问题')
            
            #print('After power(a)',a)
            u=[''for c in range(num)]
            num_i=1
            while num-num_i>=1: #依次输入u()元素值并对原公式进行替换
                u[num_i]=input("——请输入u(%d）的值："%(num_i))
                if num >2:
                    a=re.sub(r"u\(%d\)"%(num_i),u[num_i],a)
                else:
                    a=re.sub(r"u",u[num_i],a)
                print('——',u)
                num_i=1+num_i

            print('您好，'+now,'，转化后的Latex公式为：')
            a=re.sub(r"(?=(pi|psi|eta|mu|alpha|theta|lambda))",r'\\',a)
            print(a)
        elif mode==1:
            a=input('——请输入公式：')
            if a=='':
                    a=r'(c_pT_im_c-Ims-dQwb-T*c_v*m_{in})/(c_v*\int{m})'
        else:
            print('您输入的内容有误，请重新输入：')
            continue
        #plt.rcParams['font.sans-serif'] = ['SimHei']
        #plt.rcParams['font.serif'] = ['SimHei']
        ax=plt.figure()
        ax.text(0.1,0.8,r"$%s$"%(a),fontsize=30)
        print('您好，正在为您绘制目标公式')
        plt.show()
