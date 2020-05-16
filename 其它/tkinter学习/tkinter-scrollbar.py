from tkinter import *
root=Tk()
scroll=Scrollbar(root)
scroll.pack(side=RIGHT,fill=Y)
t1=Text(root,yscrollcommand=scroll.set) # 把要控制的组件的ysvrollcommand属性设定为scroll组件的set
for i in range(20):
    t1.insert(INSERT,str(i)+'\n')
t1.pack(side=LEFT,fill=BOTH,expand=YES)
scroll.config(command=t1.yview)     # 给scroll组件设定command=要控制的组件.yview
def wordin():
    t1.mark_set('here','2.0')
    t1.mark_gravity('here',LEFT)
    t1.insert('here','-233-')
    t1.insert('here', '-110-')
b1=Button(root,text='插入' ,command=wordin)
b1.pack()
mainloop()