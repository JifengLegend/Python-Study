import tkinter as tk    # 导入 tkinter 模块

class App:
    def __init__(self,window):
        frame=tk.Frame(window)
        frame.pack(side=tk.LEFT,padx=30,pady=30)
        self.hi=tk.Button(frame,text="hi~~~",command=self.say_hi)
        self.hi.pack(side=tk.RIGHT)

    def say_hi(self):
        print('hi hi hi hi hi')

root=tk.Tk()
app=App(root)
root.mainloop()
