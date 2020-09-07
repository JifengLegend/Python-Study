import matplotlib.pyplot as plt
import xlwt
from dataSourse import dBAll

class Data:
    def __init__(self,source,xstep=8,ystep=0.3,xlimit=0,ylimit=0):
        self.xlimit=xlimit
        self.ylimit=ylimit
        self.xstep=xstep
        self.ystep=ystep
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
        try:
            self.shinek=self.fcns[0].k*self.fcns[0].k/self.fcns[1].k
            self.shineb=self.points[0].y-self.points[0].x*self.shinek
            self.newPoint=Point(self.points[0].x-self.xstep,(self.points[0].x-self.xstep)*self.shinek+self.shineb)
        except ZeroDivisionError:
            print(f'{self.points[0]}')
            pass
        plt.plot(self.newPoint.x,self.newPoint.y)

    def getDownPoint(self):
        self.shinek=self.fcns[-1].k*self.fcns[-1].k/self.fcns[-2].k
        self.shineb=self.points[-1].y-self.points[-1].x*self.shinek
        self.newPoint=Point((self.points[-1].y-self.ystep-self.shineb)/self.shinek,self.points[-1].y-self.ystep)
        # self.newPoint=Point(self.points[-1].x+self.xstep,(self.points[-1].x+self.xstep)*self.shinek+self.shineb)
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
def printWork(sheet,database,key):
    xx,yy=database.printPoints()

    writeList(sheet,0,xx)
    writeList(sheet,1,yy)
    for num,val in enumerate(xx):
        sheet.write(num,2,key)
    print(xx,"\n",yy,"\n\n")
    plt.plot(xx,yy,'b.')
    r=[]
    for num,val in enumerate(xx):
        r.append((xx[num],yy[num],key))
    return r

def writeList(sheet,adress,list):
    '''用于在指定sheet中写列表\n
    sheet=目标，adress=列数，list=要写入的列表'''
    for num in range(len(list)):
        sheet.write(num,adress,list[num])
def printAll(sheet,r):
    for num0,val0 in enumerate(r):
        row=num0
        for num1,val1 in enumerate(val0):
            sheet.write(row,num1,val1)


if __name__ == "__main__":
    

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

    keys=list(dBAll.keys())

    myfile=xlwt.Workbook()
    database,r=[],[]
    
    for num,keyNum in enumerate (keys):
        mysheet=myfile.add_sheet(str(keyNum))
        database.append(Data(dataPre(dBAll[keyNum]),ylimit=1))
        r+=printWork(mysheet,database[num],keyNum)
    sheetAll=myfile.add_sheet('All')
    printAll(sheetAll,r)
    myfile.save('dataBase.xls')
    plt.axis([0,110,0,5])
    plt.show()
