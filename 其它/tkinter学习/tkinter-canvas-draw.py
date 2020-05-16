from tkinter import *

root = Tk()

can = Canvas(root, width=400, height=200)
can.pack()


def paint(event, color):
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    can.create_oval(x1, y1, x2, y2, fill=color)

def paint1(event):
    paint(event,'blue')
def paint2(event):
    paint(event,'red')
def paint3(event):
    paint(event,'green')
can.bind("<B1-Motion>", paint1)
can.bind("<B2-Motion>", paint2)
can.bind("<B3-Motion>", paint3)
Button(root, text='清空', command=lambda x=can: x.delete(ALL)).pack(side=BOTTOM)
mainloop()
