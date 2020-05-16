from tkinter import *
import random


class textPlus:
    def __init__(self, root, wide=40, high=7):
        self.frame = Frame(root, padx=10, pady=10)
        self.frame.pack(side=TOP, padx=10, pady=10)
        self.scroll = Scrollbar(self.frame)
        self.scroll.pack(side=RIGHT, fill=Y)
        self.text = Text(self.frame, width=wide, height=high, yscrollcommand=self.scroll.set)
        self.text.pack(fill=BOTH)

        self.scroll.config(command=self.text.yview)
        self.text.insert(1.0, f"这里是开头~\n\n")

        self.mm = Menu(self.frame, tearoff=False)
        self.mm.add_command(label='全选', command=self.selectAll)
        self.mm.add_command(label='复制', command=self.copy)
        self.mm.add_command(label='粘贴', command=self.paste)
        self.mm.add_separator()
        self.mm.add_command(label='复制+', command=self.copyAll)
        self.mm.add_command(label='清空', command=self.clear)
        self.text.bind('<Button-3>', self.popMenu)

    def show(self):
        self.text.delete(1.0, 'end')
        self.text.insert(1.0, f"这里是开头~\n\n")
        self.init()

    def insert(self):
        self.text.insert(f"{INSERT}", f"\nI love Python3.{random.randint(0, 1000)}\n")

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

    def input(self, word):
        self.text.insert(f"{INSERT}", f"\n{word}\n")


def wordin():
    t1.text.insert(f"{INSERT}", f"\nI love Python3.{random.randint(0, 1000)}\n")


if __name__ == '__main__':
    root = Tk()
    root.title("记事本")
    t1 = textPlus(root)
    Button(text='插入', command=wordin).pack(side=BOTTOM)

# def show():
#     t1.delete(1.0,'end')
#     b1 = Button(t1, text="撤销", command=show)
#     b1.pack(side=RIGHT)
#     t1.window_create(INSERT, window=b1)
# b1=Button(t1,text="撤销",command=show)
# # b1.pack(side=RIGHT)
# # t1.window_create(INSERT,window=b1)


mainloop()
