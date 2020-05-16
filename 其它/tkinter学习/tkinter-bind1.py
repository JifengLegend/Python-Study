from tkinter import*
root=Tk()
frame=Frame(root,width=500,height=200)
frame.pack()
frame.focus_set()

def callback(event):
    print(event.char)
frame.bind('<Key>',callback)

mainloop()