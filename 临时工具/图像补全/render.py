import matplotlib.pyplot as plt

class Data:
    def __init__(self,*arg):
        self.points=[]
        for eachpoint in arg:
           self.points.append( Point(eachpoint[0],eachpoint[1]))
        
class oneDFcn:
    def __init__(self,point1,point2):
        self.p1=point1
        self.p2=point2
        self.k=(point2.y-point1.y)/(point2.x-point1.x)
        self.b=point1.y-self.k*point1.x
    def plotFcn(self):
        x=[i for i in range(10)]
        y=[self.k*i+self.b for i in x]
        plt.plot(x,y,'--')


class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y

sources=[(4,5.5),(5,5),(6,4),(7,2)]
print(sources)
xx=[]
yy=[]
for point in sources:
    xx.append(point[0])
    yy.append(point[1])

def plotFcn(k,b):
    x=[i for i in range(10)]
    y=[k*i+b for i in x]
    plt.plot(x,y,'--')
def getKB(p0,p1):
    k=(p1[1]-p0[1])/(p1[0]-p0[0])
    b=p0[1]-p0[0]*k
    print(k,b)
    return [k,b]
Fcn=[]

for num in range(len(sources)-1):
    Fcn.append(getKB(sources[num],sources[num+1]))
    plotFcn(Fcn[num][0],Fcn[num][1])
# Fcn.append(getKB(sources[0],sources[1]))
# plotFcn(Fcn[0][0],Fcn[0][1])

# Fcn.append(getKB(sources[1],sources[2]))
# plotFcn(Fcn[1][0],Fcn[1][1])
def shineFcn(Fcn,p0):
    shine=Fcn[1][0]/Fcn[0][0]
    newS=Fcn[0][0]/shine
    newB= p0[1]-newS*p0[0]
    plotFcn(newS,newB)





shineFcn(Fcn,sources[0])
plt.plot(xx,yy)
plt.axis([0,10,0,10])
plt.show()