from tkinter import *
root=Tk()
def callback():
    pass
mm=Menu(root)
fileMenu=Menu(mm,tearoff=False)
fileMenu.add_command(label='open',command=callback)
fileMenu.add_separator()
fileMenu.add_command(label='exit',command=root.quit)
subMenu=Menu(fileMenu)
subMenu.add_command(label="fuck",command=callback)
fileMenu.add_cascade(label='18/',menu=subMenu)

mm.add_cascade(label='file',menu=fileMenu)
root.config(menu=mm)
mainloop()