from tkinter import *

root = Tk()


def callback():
    pass
def read():
    print(v1.get())
v1=StringVar()
l1=['777','888','999']
v1.set('111')

op=OptionMenu(root,v1,'222','333',*l1)
op.pack(side=LEFT,padx=10,pady=10)
Button(root,text='read',command=read).pack(side=RIGHT,padx=10,pady=10)
mainloop()