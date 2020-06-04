# import tkinter as tk  # 导入 tkinter 模块
import MatlabBox
from MatlabBox import *
from tkinter import *
import random


class textPlus:
    def __init__(self,root,wide=40,high=7):
        self.frame = Frame(root, padx=10, pady=10)
        self.frame.pack(side=TOP, padx=10, pady=10)
        self.scroll = Scrollbar(self.frame)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.text = Text(self.frame, width=wide, height=high,yscrollcommand=self.scroll.set)
        self.text.pack(fill=BOTH)

        self.scroll.config(command=self.text.yview)
        self.text.insert(1.0, f"Latex公式会显示在这里...\n\n")

        self.mm=Menu(self.frame,tearoff=False)
        self.mm.add_command(label='全选', command=self.selectAll)
        self.mm.add_command(label='复制',command=self.copy)
        self.mm.add_command(label='粘贴',command=self.paste)
        self.mm.add_separator()
        self.mm.add_command(label='复制+', command=self.copyAll)
        self.mm.add_command(label='清空', command=self.clear)
        self.text.bind('<Button-3>',self.popMenu)


    def show(self):
        self.text.delete(1.0,'end')
        self.text.insert(1.0, f"这里是开头~\n\n")
        self.init()
    def insert(self):
        self.text.insert(f"{INSERT}", f"\nI love Python3.{random.randint(0,1000)}\n")
    def copy(self):
        self.text.event_generate("<<Copy>>")
    def paste(self):
        self.text.event_generate("<<Paste>>")

    def selectAll(self):
        self.text.tag_add('sel','1.0',END)

    def copyAll(self):
        self.text.tag_add('sel', '1.0', END)
        self.text.event_generate("<<Copy>>")
    def clear(self):
        self.text.delete(1.0,END)
    def popMenu(self,event):
        self.mm.post(event.x_root,event.y_root)
    def input(self, word):
        self.text.delete(1.0,END)
        self.text.insert(f"{INSERT}", f"{word}")


root = Tk()
root.title('Matlab 公式转换器')

now = TimeGeter()

# timelabel.pack(side=LEFT)
frame1 = Frame(root, padx=0, pady=0)
frame1.pack(side=TOP, padx=20, pady=10)
lframe = LabelFrame(frame1, text='请选择模式：', padx=10, pady=10)
lframe.pack(side=LEFT, padx=40, pady=10)
# 模式选择
tishis = ('请输入要转换的公式：', '请输入要绘制的公式：')


def tiShi():
    ti = tishis[0] if not v.get() else tishis[1]
    tishi.set(ti)


v = IntVar()
v.set(0)
modes = [('转换模式', 0), ('绘制模式', 1)]
for mode, num in modes:
    b = Radiobutton(lframe, text=mode, variable=v, value=num, indicatoron=False, command=tiShi)
    b.pack(fill=X)

# 输入文本框
tishi = StringVar()
tishi.set('请输入要转换的公式：')
getFrame = Label(frame1, padx=10, pady=10)
getFrame.pack(side=RIGHT, padx=40, pady=10)

l1 = Label(getFrame, textvariable=tishi)
l1.grid(row=0, column=0)

e1 = Entry(getFrame)
e1.grid(row=1, column=0, pady=10)


# 开始按钮
def labelGen(window, num):
    global a

    def mathReplace():
        # for each in entryn[1:]:
        #     print(f'每个文本框的值为：{each.get()}')
        global a
        global t1
        for each_num in range(1, num):
            print(f"每个文本框的值为：{entryn[each_num].get()}")
            a = re.sub(r"u\(%d\)" % (each_num), entryn[each_num].get(), a)
        a = re.sub(r"(?=(pi|psi|eta|mu|alpha|theta|lambda))", r'\\', a)
        print(a)
        t1.input(a)
        ax = plt.figure(figsize=(len(a) / 4 if len(a) / 4 > 5 else 5, 3))
        ax.text(0.1, 0.8, r"$%s$" % (a), fontsize=30)
        print('您好，正在为您绘制目标公式')
        plt.show()

    entryn = [None, ]
    for each in range(1, num):
        ln = Label(window, text=f'u({each}):')
        ln.grid(row=each - 1, column=0, padx=10, pady=10)
        entryn.append(Entry(window))
        entryn[each].grid(row=each - 1, column=1, padx=10, pady=10)

    Button(window, text='~转换~', command=mathReplace).grid(row=num + 1, column=1, padx=20, pady=20)
    # Entry(window, state='readonly', width=40, textvariable=a3).grid(row=num+1,column=0,padx=20,pady=20)


def getMath():
    global a
    a = e1.get()
    print(f'获取的公式为：{a}')
    print(f'当前时间为：{now}')
    if not v.get():
        window1 = Tk()
        window1.title('开始转换')
        num = numx(a) + 1
        a = power(a)
        a = sqrt(a)

        labelGen(window1, num)

        print(f'转换后的的公式为：{a}')
    else:
        global t1
        ax = plt.figure(figsize=(len(a) / 4 if len(a) / 4 > 5 else 5, 3))
        ax.text(0.1, 0.8, r"$%s$" % (a), fontsize=30)
        print('您好，正在为您绘制目标公式')
        plt.show()
        t1.input(a)


Frame2 = Label(root, padx=20, pady=20)
Frame2.pack(side=BOTTOM, padx=10, pady=10)
Button(Frame2, text='开始！', command=getMath, width=10).pack(side=RIGHT, padx=20, pady=20)

# 显示窗口
# def textUndo():
# #     t1.edit_undo()
a3 = StringVar()
a3.set('转换的结果在这里~')
t1=textPlus(Frame2,30,5)

# Button(root,text="撤销",command=textUndo).pack()


'''
Label(frame, text='作品：').grid(row=0, column=0)
Label(frame, text='作者：').grid(row=1, column=0)

e1 = Entry(frame)
e1.grid(row=0, column=1, pady=10)
e2 = Entry(frame)
e2.grid(row=1, column=1, pady=10)





Button(root, text='获取信息', command=show, width=10).pack(side=LEFT,padx=20,pady=20)
Button(root, text='退出', command=root.quit, width=10).pack(side=RIGHT,padx=20,pady=20)

'''
root.mainloop()
