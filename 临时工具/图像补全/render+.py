import matplotlib.pyplot as plt

class Data:
    def __init__(self,xstep=1,xlimit=0,ylimit=0,*arg):
        self.xlimit=xlimit
        self.ylimit=ylimit
        self.xstep=xstep
        self.points=[]
        for eachpoint in arg:
           self.points.append( Point(eachpoint[0],eachpoint[1]))
        self.startCalc()


    def startCalc(self):
        while self.points[0].x>=self.xlimit:
            self.calcFcns()
            self.getUpPoint()
            self.addNewPoint()
        while self.points[-1].y>=self.ylimit:
            self.calcFcns()
            self.getDownPoint()
            self.addNewPoint(1)

    def printPoints(self):
        self.xx=[i.x for i in self.points]
        self.yy=[i.y for i in self.points]
        return self.xx,self.yy

    def calcFcns(self):
        self.fcns=[]
        for num in range(len(self.points)-1):
            self.fcns.append(oneDFcn(self.points[num],self.points[num+1]))
            # self.fcns[num].plotFcn()

    def getUpPoint(self):
        self.shinek=self.fcns[0].k*self.fcns[0].k/self.fcns[1].k
        self.shineb=self.points[0].y-self.points[0].x*self.shinek
        self.newPoint=Point(self.points[0].x-self.xstep,(self.points[0].x-self.xstep)*self.shinek+self.shineb)
        plt.plot(self.newPoint.x,self.newPoint.y)

    def getDownPoint(self):
        self.shinek=self.fcns[-1].k*self.fcns[-1].k/self.fcns[-2].k
        self.shineb=self.points[-1].y-self.points[-1].x*self.shinek
        self.newPoint=Point(self.points[-1].x+self.xstep,(self.points[-1].x+self.xstep)*self.shinek+self.shineb)
        plt.plot(self.newPoint.x,self.newPoint.y)

    def addNewPoint(self,flag=0):
        if flag==0:
            self.points.insert(0,self.newPoint)
        else:
            self.points.append(self.newPoint)


class Data2(Data):
    def __init__(self,xx,yy,xstep=1,xlimit=0,ylimit=0):
        self.xlimit=xlimit
        self.ylimit=ylimit
        self.xstep=xstep

        self.points=[]
        if len(xx)==len(yy):
            for num in range(len(xx)):
                self.points.append(Point(xx[num],yy[num]))
        else:
            print('xy两数列阶数不同\n')
            
        self.startCalc()

class oneDFcn:
    def __init__(self,point1,point2):
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
    
    

if __name__ == "__main__":
    sources=[(4,5.5),(5,5),(6,4),(7,2)]
    xx=[4,5,6]
    yy=[5.5,5,4]
    plt.plot(xx,yy,'r')

    # 导数数据方法1
    # database01=Data((4,5.5),(5,5),(6,4),(7,2))
    # xx,yy=database01.printPoints()
    # database01.calcFcns()

    # 导入数据方法2
    database01=Data2(xx,yy,xstep=0.5)
    xx,yy=database01.printPoints()
    database01.calcFcns()

    print(xx,yy)

    plt.plot(xx,yy,'b--')
    plt.axis([0,10,0,10])
    plt.show()
'''
26.984371, 1.5220760
28.275614, 1.5187379
32.112329, 1.5087399
37.020924, 1.4856027
40.058047, 1.4555062
42.488420, 1.4089503
44.797824, 1.3463756
45.557358, 1.3022745
'''