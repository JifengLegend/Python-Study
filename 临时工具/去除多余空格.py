import re
import pyperclip
import pickle
from tkinter import *

class TextGet:
    def __init__(self, window, wide=40, high=9):
        self.window = window
        self.frame = Frame(self.window, padx=10, pady=2, bg='white')
        self.frame.pack(padx=10, pady=10)
        self.scroll = Scrollbar(self.frame)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.text = Text(self.frame, width=wide, height=high,
                         yscrollcommand=self.scroll.set)
        self.text.pack(fill=BOTH, expand=YES)
        self.scroll.config(command=self.text.yview)

        self.mm = Menu(self.frame, tearoff=False)
        self.mm.add_command(label='全选', command=self.selectAll)
        self.mm.add_command(label='复制', command=self.copy)
        self.mm.add_command(label='粘贴', command=self.paste)
        self.mm.add_separator()
        self.mm.add_command(label='复制+', command=self.copyAll)
        self.mm.add_command(label='清空', command=self.clear)
        self.text.bind('<Button-3>', self.popMenu)

    def get(self):
        return self.text.get(1.0, END)

    def write(self, a):
        self.text.delete(1.0, END)
        self.text.insert(INSERT, a)

    def copy(self):
        self.text.event_generate("<<Copy>>")

    def paste(self):
        self.text.event_generate("<<Paste>>")

    def selectAll(self):
        self.text.tag_add('sel', '1.0', END)

    def copyAll(self):
        self.text.tag_add('sel', '1.0', END)
        self.text.event_generate("<<Copy>>")

    def clear(self):
        self.text.delete(1.0, END)

    def popMenu(self, event):
        self.mm.post(event.x_root, event.y_root)





def RegexStart():
    dataCache=textget.get()

    
    # textresult.write(dataCache)

    dataCache=dataCache.split("\n")
    print(dataCache)
    nums=[]
    
    for eachline in dataCache:

        num=0
        try:
            a=re.search(r'^\s+\w',eachline).group()
        except AttributeError as kong:
            pass
        
        print(a)
        num=len(a)-1
        nums.append(num)

    num=min(nums)

    result=''
    for eachline in dataCache:
        a=re.sub('^'+' '*num,'',eachline)
        result+=a+'\n'
    result=result.strip()
    print(result)
    textresult.write(result)


if __name__ == "__main__":
    root = Tk()
    root.title("去除多余空格")
    # root.iconbitmap('正则计算器\cake.ico')
    
    root.configure(bg='white')


    Label(root, text='在这里输入要转换的文本：', bg='white').pack(anchor=W, padx=10, pady=2)
    textget = TextGet(root)
    Label(root, text='转换后的结果：', bg='white').pack(anchor=W, padx=10, pady=2)
    textresult = TextGet(root)
    a = ''

    b1 = Button(root, text="Start", width=5, command=RegexStart,fg='#ffffff', bg='#666699')
    b1.pack(anchor=SE, padx=10, pady=10)

    root.mainloop()

