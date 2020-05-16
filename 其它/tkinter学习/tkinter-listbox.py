from tkinter import *
root=Tk()
list=Listbox(root)
list.pack()

for item in [1,2,3,4]:
    list.insert(END,item)
b1=Button(root,text='删除',command=lambda x=list:x.delete(ACTIVE))
b2=Button(root,text='读取',command=lambda x=list:print(x.get(ACTIVE)))
b1.pack(side=RIGHT,padx=10,pady=10)
b2.pack(side=LEFT,padx=10,pady=10)

mainloop()