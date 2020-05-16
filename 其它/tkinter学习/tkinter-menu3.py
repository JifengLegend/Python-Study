from tkinter import *

root = Tk()


def callback():
    pass
openvar=IntVar()
savevar=IntVar()
quitvar=IntVar()
mm = Menu(root)
fileMenu=Menu(mm,tearoff=False)
fileMenu.add_checkbutton(label='open',command=callback,variable=openvar)
fileMenu.add_checkbutton(label='save',command=callback,variable=savevar)
fileMenu.add_checkbutton(label='quit',command=callback,variable=quitvar)

editvar=IntVar()
editMunu=Menu(mm)
editMunu.add_radiobutton(label='copy',command=callback,value=1,variable=editvar)
editMunu.add_radiobutton(label='redo',command=callback,value=2,variable=editvar)
editMunu.add_radiobutton(label='del',command=callback,value=3,variable=editvar)

mm.add_cascade(label='file',menu=fileMenu)
mm.add_cascade(label='eidt',menu=editMunu)
root.config(menu=mm)
mainloop()