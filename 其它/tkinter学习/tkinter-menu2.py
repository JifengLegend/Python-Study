from tkinter import *
import re

root = Tk()


def callback():
    pass


mm = Menu(root)

mm.add_command(label='open', command=callback)
frame = Frame(root, width=500, height=300)
frame.pack()


def popMenu(event):
    mm.post(event.x_root,event.y_root)

frame.bind("<Button-3>",popMenu)

mainloop()
