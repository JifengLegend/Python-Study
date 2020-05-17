import re
import BaiduTrans
from tkinter import *
import pyperclip

raw='''
可以避免安装大量阳极牺牲物，并可减少航行阻力/which can avoid the installation of a large number of anode sacrifices and can reduce the navigation resistance
所谓外加电流阴极保护法是对被保护的金属表面施加一定的直流电流/The so-called impressed current cathodic protection method is to apply a certain DC current to the surface of the metal to be protected
使其产生阴极极化从而达到保护的目的/so that it produces cathodic polarization to achieve the purpose of protection
该系统由以下几部分组成/The system consists of the following parts
'''
def dataCalc(raw):
    raw=re.sub(r"\n\n",'',raw)
    section=re.split(r'\n',raw)
    try:
        section.remove("")
    except ValueError as reason:
        pass
    CalcResult=""
    for each in section:
        each=re.split(r'\/',each)
        zh,en=each[0],each[1]
        reTrans=BaiduTrans.BaiduTrans(zh)
        print(f"-{zh}\n  {reTrans}\n  {en}\n\n")
        CalcResult+=f"-{zh}\n  {reTrans}\n  {en}\n\n"
    return CalcResult

def dataCalcPro(raw):
    raw=re.sub(r"\n\n",'',raw)
    section=re.split(r'\n',raw)
    try:
        section.remove("")
    except ValueError as reason:
        pass
    CalcResult=""
    zhSentence=""
    enSentence = ""

    for eacha in section:
        each=re.split(r'\/',eacha)
        zh,en=each[0],each[1]
        if eacha!=section[-1]:
            zhSentence += zh + "，"
            enSentence += en + ","
        else:
            zhSentence += zh + "。"
            enSentence += en + "."

        # reTrans=BaiduTrans.BaiduTrans(zh)
        # print(f"-{zh}\n  {reTrans}\n  {en}\n\n")
        # CalcResult+=f"-{zh}\n  {reTrans}\n  {en}\n\n"
    pyperclip.copy(zhSentence)
    reTrans = BaiduTrans.BaiduTrans(zhSentence)
    CalcResult += f"-{zhSentence}\n  {reTrans}\n\n  {enSentence}\n\n"
    return CalcResult

class TextGet:
    def __init__(self, window, wide=40, high=7):
        self.window = window
        self.frame = Frame(self.window, padx=10, pady=5, bg='white')
        self.frame.pack(padx=10, pady=10)
        self.scroll = Scrollbar(self.frame)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.text = Text(self.frame, width=wide, height=high,
                         yscrollcommand=self.scroll.set,font="微软雅黑 16")
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

def ProModeGen():
    global a
    rule = [e1.get(), e2.get()]
    a = textget.get()
    print(f'原始文本\n{a}\n')
    print(rule)
    if a == '\n':
        a = '还没输入文本呢'
    else:
        a = dataCalcPro(a)
    print(a)
    textresult.write(a)
def RegexStart():
    global a
    rule = [e1.get(), e2.get()]
    a = textget.get()
    print(f'原始文本\n{a}\n')
    print(rule)
    if a == '\n':
        a = '还没输入文本呢'
    else:
        a = dataCalc(a)
    print(a)
    textresult.write(a)


if __name__ == '__main__':
    root = Tk()
    root.title("ReTrans")
    root.configure(bg='white')

    Label(root, text='在这里输入要校验的文本：', bg='white').pack(anchor=W, padx=10)
    textget = TextGet(root)
    Label(root, text='对比展示：', bg='white').pack(anchor=W, padx=10)
    textresult = TextGet(root,high=14)

    a = ''
    frame = Frame(root, bg='white')
    frame.pack(side=LEFT, padx=10, pady=5)
    v1 = StringVar()
    v2 = StringVar()
    e1 = Entry(frame, textvariable=v1)
    Label(frame, text='匹配：', bg='white').grid(row=0, column=0, padx=10, pady=10)
    e1.grid(row=0, column=1, padx=10, pady=10)
    e2 = Entry(frame, textvariable=v2)
    Label(frame, text='替换：', bg='white').grid(row=1, column=0, padx=10, pady=10)
    e2.grid(row=1, column=1, padx=10, pady=10)

    b2 = Button(root, text="Pro", width=5, command=ProModeGen, fg='#ffffff', bg='#666699')
    b2.pack(anchor=SE, padx=10, pady=10)
    b1 = Button(root, text="Start", width=5, command=RegexStart)
    b1.pack(anchor=SE, padx=10, pady=10)


    root.mainloop()
