import re
import pickle
from tkinter import *


class TextGet:
    def __init__(self, window, wide=40, high=7):
        self.window = window
        self.frame = Frame(self.window, padx=10, pady=10, bg='white')
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


class ProMode():
    def __init__(self):
        self.win2 = Tk()
        self.win2.title('Pro')
        self.win2.configure(bg='white')
        self.win2.iconbitmap('cake.ico')
        self.win2.geometry("+600+170")
        self.win2.minsize(300,100)
        self.frame = Frame(self.win2, bg='white')
        self.frame.pack(side=LEFT,expand=1,fill=BOTH)
        self.loadin()
        self.command()

    def loadin(self):
        try:
            f = open('regex history.pkl', 'rb')
            self.cache = pickle.load(f)
            f.close()
            self.list = Listbox(self.frame)
            self.list.pack(side=TOP, padx=10, pady=10,expand=1,fill=BOTH)
            if self.cache == []:
                self.list.insert(END, f'历史记录为空')
            else:
                for item in self.cache:
                    self.list.insert(END, item)
        except (FileNotFoundError, EOFError) as reason:
            self.list = Listbox(self.frame)
            self.list.pack(side=TOP, padx=10, pady=10)
            print(f'获取历史记录失败，detail：{reason}')
            self.list.insert(END, f'获取历史记录失败，detail：{reason}')

    def command(self):
        Button(self.frame, text='载入', command=self.add, bg='#11ac5a',
               fg='white', width=6).pack(side=LEFT, padx=10, pady=10)
        Button(self.frame, text='删除', command=self.delete, bg='#d4482f',
               fg='white', width=6).pack(side=RIGHT, padx=10, pady=10)

    def add(self):
        print(self.list.get(ACTIVE))
        global v1, v2
        if len(self.list.get(ACTIVE)) == 2:
            v1.set(self.list.get(ACTIVE)[0])
            v2.set(self.list.get(ACTIVE)[1])
        else:
            self.list.delete(END)
            self.list.insert(END, '没有元素可供添加')

    def delete(self):
        try:
            self.cache.remove(list(self.list.get(ACTIVE)))
            f = open('regex history.pkl', 'wb')
            print(self.cache)
            pickle.dump(self.cache, f)
            f.close()
            self.list.delete(ACTIVE)
        except ValueError:
            self.list.delete(END)
            self.list.insert(END, '已经没有元素可以删除了')

        pass


def regex(rule, a):
    a = re.sub(rule[0], rule[1], a, flags=re.M)
    return a


def ProModeGen():
    win2 = ProMode()


def save():
    rule = [e1.get(), e2.get()]
    cache = []
    try:
        f = open('regex history.pkl', 'rb')
        cache.extend(pickle.load(f))
        print(cache)
        f.close()
    except (FileNotFoundError, EOFError) as reason:
        pass
    if rule[0] == '':
        textresult.write('还没输入匹配呢，无法保存')
    else:
        cache.append(rule)
        print(cache)
        f = open('regex history.pkl', 'wb')
        pickle.dump(cache, f)
        f.close()



def read():
    f = open('regex history.pkl', 'rb')
    read = pickle.load(f)
    print(read)
    f.close()


def RegexStart():
    global a
    rule = [e1.get(), e2.get()]
    a = textget.get()
    print(f'原始文本\n{a}\n')
    print(rule)
    if a == '\n':
        a = '还没输入文本呢'
    else:
        if rule[0] == '':
            a = '还没输入匹配呢'
        else:
            a = regex(rule, a)
    print(a)
    textresult.write(a)


if __name__ == "__main__":
    root = Tk()
    root.title("正则计算器")
    root.iconbitmap('正则计算器\cake.ico')
    
    root.configure(bg='white')
    mm = Menu(root)
    mm.add_command(label='Save', command=save, accelerator='Ctrl+S')
    mm.add_command(label='Read', command=read)
    root.config(menu=mm)

    Label(root, text='在这里输入要转换的文本：', bg='white').pack(anchor=W, padx=10, pady=10)
    textget = TextGet(root)
    Label(root, text='转换后的结果：', bg='white').pack(anchor=W, padx=10, pady=10)
    textresult = TextGet(root)
    a = ''
    frame = Frame(root, bg='white')
    frame.pack(side=LEFT, padx=10, pady=10)
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
    root.bind_all('<Control-Key-s>', lambda event: save())

    root.mainloop()
