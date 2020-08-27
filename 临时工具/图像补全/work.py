import matplotlib.pyplot as plt

class Data:
    def __init__(self,source,xstep=2,xlimit=0,ylimit=0):
        self.xlimit=xlimit
        self.ylimit=ylimit
        self.xstep=xstep
        self.points=[] # 存储所有的点
        for eachpoint in source:
           self.points.append( Point(eachpoint[0],eachpoint[1]))
        self.startCalc()


    def startCalc(self):
        # 开始计算，包含计算当前，上升推算，添加新的点
        while self.points[0].x>=self.xlimit:
            self.calcFcns()
            self.getUpPoint()
            self.addNewPoint()
        y=self.xlimit*self.fcns[0].k+ self.fcns[0].b
        self.newPoint=Point(self.xlimit,y)
        del self.points[0]        
        self.addNewPoint()
        while self.points[-1].y>=self.ylimit:
            self.calcFcns()
            self.getDownPoint()
            self.addNewPoint(1)
        x=(self.ylimit-self.fcns[-1].b)/self.fcns[-1].k
        self.newPoint=Point(x,self.ylimit)
        del self.points[-1]          
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
    
def dataPre(sources):
    a=sources.split('\n')
    plist=[]
    for each in a:
        cache = each.split(',')
        p=(float(cache[0]),float(cache[1]))
        plist.append(p)
    return plist    
def printWork(database):
    xx,yy=database.printPoints()
    print(xx,"\n",yy,"\n\n")
    plt.plot(xx,yy,'r-')

if __name__ == "__main__":
    sources50='''26.684371, 1.5220760
28.275614, 1.5187379
32.112329, 1.5087399
37.020924, 1.4856027
40.058047, 1.4555062
42.488420, 1.4089503
44.797824, 1.3463756
45.557358, 1.3022745'''

    sources60='''36.258619, 1.8206283
39.450710, 1.8180601
43.316538, 1.8090900
47.241341, 1.7865943
50.815205, 1.7482100
53.218139, 1.6947793
54.391001, 1.6453959
55.007027, 1.6103620'''

    sources70='''47.521810, 2.1994055
49.923265, 2.1952915
52.266271, 2.1872036
54.843672, 2.1751253
58.124214, 2.1526663
61.405280, 2.1127079
63.749621, 2.0600760
65.391227, 2.0043024
66.300719, 1.9485706
67.181021, 1.8896587
67.791005, 1.8180417'''

    sources80='''61.153642, 2.6917939
65.136680, 2.6804308
68.885632, 2.6627177
72.459234, 2.6330832
75.535762, 2.5780233
77.616684, 2.5206338
78.966303, 2.4362415
79.877369, 2.3280113
80.465207, 2.2563893
80.847719, 2.1959150'''

    sources90='''75.718313, 3.3265107
78.705794, 3.3112273
83.333856, 3.2743738
85.677625, 3.2408322
88.607753, 3.1849852
90.425210, 3.1244291
91.686498, 3.0559504
92.655226, 2.9779432
93.361014, 2.8792699
93.656530, 2.7901651
94.333415, 2.6787665
94.540076, 2.6230748'''

    sources100='''89.694001, 4.0710303
93.384503, 4.0493433
96.138280, 4.0149829
99.068527, 3.9551588
100.88634, 3.8826712
101.91402, 3.7919338
102.47358, 3.6869054
102.88742, 3.5580225
103.36013, 3.4195910
103.45118, 3.3129985
103.48332, 3.2175452'''

    sources106='''96.534814, 4.4635818
99.112812, 4.4316177
101.48656, 4.3750070
102.95238, 4.3216298
104.50738, 4.2244989
105.62482, 4.0701222
106.06919, 3.8998752
106.24900, 3.7630513
106.31952, 3.6262291'''

    # xx=[4,5,6]
    # yy=[5.5,5,4]
    # plt.plot(xx,yy,'r')

    # 导数数据方法1
    # database50=Data(dataPre(sources50))
    # xx,yy=database50.printPoints()
    # print(xx,yy)

    # 导入数据方法2
    # database01=Data2(xx,yy,xstep=0.5)
    # xx,yy=database01.printPoints()
    # database01.calcFcns()

    database50=Data(dataPre(sources50),xlimit=10,ylimit=1)
    printWork(database50)

    database60=Data(dataPre(sources60),xlimit=10,ylimit=1)
    printWork(database60)

    database70=Data(dataPre(sources70),xlimit=10,ylimit=1)
    printWork(database70)

    database80=Data(dataPre(sources80),xlimit=10,ylimit=1)
    printWork(database80)

    database90=Data(dataPre(sources90),xlimit=10,ylimit=1)
    printWork(database90)

    database100=Data(dataPre(sources100),xlimit=10,ylimit=1)
    printWork(database100)

    database106=Data(dataPre(sources106),xlimit=10,ylimit=1)
    printWork(database106)
    
    plt.axis([10,110,1,5])
    plt.show()
