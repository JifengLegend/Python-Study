from tkinter import *
import webbrowser
root=Tk()
scroll=Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)
t1=Text(root,yscrollcommand=scroll.set) # 把要控制的组件的ysvrollcommand属性设定为scroll组件的set
# for i in range(20):
#     t1.insert(INSERT,str(i)+'\n')
t1.insert(1.0,'I love python\nI love 4399.com')
t1.pack(side=LEFT,fill=BOTH,expand=YES)
scroll.config(command=t1.yview)     # 给scroll组件设定command=要控制的组件.yview
def wordin():
        t1.tag_config('tag1', foreground='blue', underline=True)
t1.tag_add('tag1',2.0,END)

def hand(event):
    t1.config(cursor='arrow')
def arrow(event):
    t1.config(cursor='xterm')
def click(event):
    webbrowser.open('http://www.4399.com')
t1.tag_bind('tag1','<Enter>',hand)
t1.tag_bind('tag1', '<Leave>', arrow)
t1.tag_bind('tag1', '<Button-1>', click)


b1=Button(root,text='插入' ,command=wordin)
b1.pack()
mainloop()