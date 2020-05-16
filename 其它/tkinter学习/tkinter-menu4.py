from tkinter import *

root = Tk()


def callback():
    pass
menuButton=Menubutton(root,text='调出菜单',relief=RAISED)
menuButton.pack()

fileMenu=Menu(menuButton)
fileMenu.add_command(label='open',command=callback)
fileMenu.add_command(label='save',command=callback)
fileMenu.add_command(label='quit',command=callback)


menuButton.config(menu=fileMenu)

# editMenu=Menu(menuButton)
# # editMenu.add_command(label='111',command=callback)
# # editMenu.add_command(label='222',command=callback)
# # editMenu.add_command(label='333',command=callback)


# menuButton.config(menu=editMenu)
mainloop()