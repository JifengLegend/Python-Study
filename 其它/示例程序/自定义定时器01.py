'''
定制一个定时器的类，要求：
    start/stop分别代表定时器启动和停止
    假设定时器对象t1，print（t1）和直接调用t1均显示计时的值
    当定时器未启动，或者已经停止计时，调用stop方法将会提示
    两个计时器对象可以相加
    只能用提供的有限资源完成'''
import time as t


class MyTimer:
    def __str__(self):
        return self.prompt

    __repr__ = __str__

    def __init__(self):
        self.prompt = '未开始计时'
        self.unit = ['年', '月', '日', '时', '分', '秒']
        self.lasted = []
        self.begin = 0
        self.end = 0

    def __add__(self, other):
        prompt = '总共运行了'
        result = []
        for index in range(6):
            result.append(self.lasted[index] + other.lasted[index])
            if result[index]:
                prompt += (str(result[index]) + self.unit[index])

    # 开始计时
    def start(self):
        self.begin = t.localtime()
        self.prompt = '请先调用stop停止计时'
        print('计时开始！')

    # 停止计时
    def stop(self):
        self.end = t.localtime()
        if not self.begin:
            print('请先调用start进行计时')
        self.__calc()
        print('计时结束~')

    # 内部方法计算运行时间
    def __calc(self):
        self.prompt = '总共运行了'
        for index in range(6):
            self.lasted.append(self.end[index] - self.begin[index])
            if self.lasted:
                self.prompt += (str(result[index]) + self.unit[index])
        # 为下一轮计时提供初始化
        self.begin = 0
        self.end = 0
        print(self.prompt)
