import re
import pickle
from tkinter import *


class TextGet:
    def __init__(self, window, wide=40, high=7):
        self.window = window
        self.frame = Frame(self.window, padx=10, pady=10)
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


class Window2:
    def __init__(self):
        self.window2 = Tk()
        self.window2.title('Pro')
        self.window2.geometry('+600+150')
        self.frame = Frame(self.window2, pady=10)
        self.frame.pack()
        Label(self.frame, text='匹配：').grid(row=0, column=0, padx=10, pady=10)
        Label(self.frame, text='替换：').grid(row=1, column=0, padx=10, pady=10)
        self.t1 = Entry(self.frame)
        self.t1.grid(row=0, column=1, padx=10, pady=10)
        self.t2 = Entry(self.frame)
        self.t2.grid(row=1, column=1, padx=10, pady=10)

        self.b1 = Button(self.window2, text='START', command=self.proRegex)
        self.b1.pack(side=RIGHT, padx=10, pady=10)

        self.mm = Menu(self.window2)
        self.mm.add_command(label='save', command=self.save)
        self.mm.add_command(label='read', command=self.read)
        self.window2.config(menu=self.mm)

    def proRegex(self):
        self.rule = [self.t1.get(), self.t2.get()]
        global a
        a = textget.get()
        print('原始文本：\n' + a + '\n')
        print(self.rule)

        if a == '\n':
            a = '还没输入原始文本呢\n'
        else:
            a = self.regex2x(a)
        print(a)
        textresult.write(a)

    def regex2x(self, a):
        a = re.sub(self.rule[0], self.rule[1], a, flags=re.M)
        return a

    def save(self):
        self.rule = [self.t1.get(), self.t2.get()]
        self.cache = []
        try:
            f = open('regex history.pkl', 'rb')
            self.cache.extend(pickle.load(f))
            print(self.cache)
            f.close()
        except (FileNotFoundError,EOFError) as reason:
            pass
        self.cache.append(self.rule)
        print(self.cache)
        f = open('regex history.pkl', 'wb')
        pickle.dump(self.cache, f)
        f.close()
        pass

    def read(self):
        f = open('regex history.pkl', 'rb')
        self.read = pickle.load(f)
        print(self.read)
        f.close()
        pass


def textIN(int=1):
    global a
    a = textget.get()
    print('刚刚获得的' + a)

    if a == '\n':
        a = '还没输入原始文本呢\n'
    else:
        if int == 1:
            a = regex1(a)
        # elif int==2:
        #     a=regex2(self.rule,a)
        #     pass
    print('之后的' + a)

    textresult.write(a)


def regex1(a):
    a = re.sub(r'\n{2,}', r'\n', a, flags=re.M)
    a = re.sub(r'^(.*)\n', r'<p>\1</p>\n', a, flags=re.M)
    print(a)
    return a


def regex2(rule, a):
    a = re.sub(rule[0], rule[1], a, flags=re.M)
    return a


def window2Gen():
    window2 = Window2()


if __name__ == "__main__":
    root = Tk()
    root.title("正则计算器")
    Label(root, text='在这里输入要转换的文本：').pack(anchor=W, padx=10, pady=10)
    textget = TextGet(root)
    Label(root, text='转换后的结果：').pack(anchor=W, padx=10, pady=10)
    textresult = TextGet(root)
    a = ''

    b1 = Button(root, text="GET", command=textIN)
    b1.pack(side=RIGHT, padx=10, pady=10)
    b2 = Button(root, text="Pro", command=window2Gen, fg='#ffffff', bg='#666699')
    b2.pack(side=RIGHT, padx=10, pady=10)

    root.mainloop()
