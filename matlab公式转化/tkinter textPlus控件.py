from tkinter import *
import random
class textPlus:
    def __init__(self,root,wide=40,high=7):
        frame = Frame(root, padx=10, pady=10)
        frame.pack(side=LEFT, padx=10, pady=10)
        self.scroll = Scrollbar(frame)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.text = Text(frame, width=wide, height=high,yscrollcommand=self.scroll.set)
        self.text.pack(fill=BOTH)

        self.scroll.config(command=self.text.yview)
        self.text.insert(1.0, f"这里是开头~\n\n")
        self.init()
    def show(self):
        self.text.delete(1.0,'end')
        self.text.insert(1.0, f"这里是开头~\n\n")
        self.init()
    def insert(self):
        self.text.insert(f"{INSERT}-1lines", f"\nI love Python3.{random.randint(0,1000)}\n")
    def init(self):
        self.b1 = Button(self.text, text="清空", command=self.show)
        self.b1.pack()
        self.text.window_create(f"{INSERT}+1lines", window=self.b1)
        self.b2 = Button(self.text, text="插入", command=self.insert)
        self.b2.pack()
        self.text.window_create(f"{INSERT}+1lines", window=self.b2)
    def input(self,word):
        self.text.insert(f"{INSERT}-1lines", f"\n{word}\n")







root = Tk()
root.title("记事本")
t1=textPlus(root,200,18)

# def show():
#     t1.delete(1.0,'end')
#     b1 = Button(t1, text="撤销", command=show)
#     b1.pack(side=RIGHT)
#     t1.window_create(INSERT, window=b1)
# b1=Button(t1,text="撤销",command=show)
# # b1.pack(side=RIGHT)
# # t1.window_create(INSERT,window=b1)


mainloop()