import threading
import time

def timeShow(times):
    if times>=10:
        sec=times/10
        for eachsec in range(10):
            eachsec+=1
            print(f'{str(eachsec*10).rjust(3)}%:|{"="*eachsec}{"-"*(10-eachsec)}|')
            time.sleep(sec)

class MyThread(threading.Thread):
    def __init__(self,thID,times):
        threading.Thread.__init__(self)
        self.thID=thID
        self.times=times
    def run(self):
        print(f'start thread {self.thID}')
        timeShow(self.times)
        print(f'exit thread {self.thID}')
class MyTimer(threading.Thread):
    def __init__(self,thID,times):
        threading.Thread.__init__(self)
        self.thID=thID
        self.times=times
        self.timeinit=0
    def run(self):
        print(f'start timer {self.thID}')
        while 1:
            time.sleep(1)
            self.timeinit+=1
            print(f'{self.timeinit}s')
        print(f'stop timer {self.thID}')

def record(times,timeinit):
    timeinit+=1
    print(f'{timeinit}s')

if __name__ == "__main__":

    t1=MyThread('001',10)
    # t1.setDaemon(True)
    t1.start()
    # t1.join()

    # t2=MyTimer('002',12)
    # t2.setDaemon(True)
    # t2.start()
    timeinit=0
    t3=threading.Timer(1,record,(12,timeinit))
    t3.start()


    time.sleep(12)
    print("主进程结束")
