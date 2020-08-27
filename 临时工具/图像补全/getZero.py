import matplotlib.pyplot as plt

class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
class oneDFcn:
    def __init__(self,point1,point2):
        self.k=(point2.y-point1.y)/(point2.x-point1.x)
        self.b=point1.y-self.k*point1.x
    def plotFcn(self):
        x=[i for i in range(10)]
        y=[self.k*i+self.b for i in x]
        plt.plot(x,y,'--')
    def gety0(self):
        pcache=Point(0,0)
        x=(pcache.y-self.b)/self.k
        p3=Point(x,0)
        return p3
    def getx0(self):
        y=self.b
        p3=Point(0,y)
        return p3       

if __name__ == "__main__":
    # p1=Point(103.483320000000,3.21754520000000)
    # p2=Point(105.483320000000,-11.8510736400000)
    # l1=oneDFcn(p1,p2)
    # p3=l1.gety0()
    # print(p3.x,p3.y)

    p1=Point(9.69400100000000,4.08149292401459)
    p2=Point(11.6940010000000,4.08149292401459)
    l1=oneDFcn(p1,p2)
    p3=l1.getx0()
    print(p3.x,p3.y)
