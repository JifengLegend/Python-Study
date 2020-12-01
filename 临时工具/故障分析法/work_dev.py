class System:
    def __init__(self):
        self.addParts()
        self.addEnvironments()
        self.E00()
        pass
    def addParts(self):
        '为系统添加 部件'
        pass
    def addEnvironments(self):
        '为系统添加 场景条件'
        pass
    def M00(self):
        pass
    def E00(self):
        pass

class Part:
    def __init__(self):
        self.addPara()
    def addPara(self):
        self.P00='结构'
    def M00(self):
        pass

class FA(System):
    def __init__(self):
        self.addParts()
        self.addEnvironments()
        self.E00()
    def addParts(self):
        '为系统添加 部件'
        QA,QB=Part(),Part()
        self.QA=QA
        self.QB=QB
    def addEnvironments(self):
        '为系统添加 场景条件'
        self.e01=True if 1+1>0 else False
    def M00(self):
        pass
    def M01(self):
        '''系统功能01\n
        paras：登记该函数用的变量名'''
        paras=[self.QA.P00,self.QB.P00]
        result01='返回参数'
        return result01
    def E00(self):
        self.M01()
        if self.e01==True:
            self.E01()

    def E01(self):
        pass

if __name__ == "__main__":
    QA=Part()
    print(QA.P00)