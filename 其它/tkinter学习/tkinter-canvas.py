from tkinter import *
root=Tk()

can=Canvas(root,width=100,height=50)
can.pack()
line1=can.create_line(0,50,100,25,fill='yellow')
rect=can.create_rectangle(0,50,100,0,dash=(4,4))

def delcan():
    can.coords(line1,0,0,50,50)
    can.itemconfig(rect,fill='red')
b1=Button(root,text='删除',command=lambda x=can:x.delete(ALL))
b1.pack()
mainloop()