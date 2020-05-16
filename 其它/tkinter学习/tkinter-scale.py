from tkinter import *

root = Tk()
scale = Scale(root, from_=0, to=50)
scale.pack(side=RIGHT)
scale2 = Scale(root, from_=0, to=200,
               tickinterval=50,  # 显示的间隔
               resolution=10,    # 最小刻度
               length=200,       # 长度
               orient=HORIZONTAL)
scale2.pack(side=BOTTOM)

b1 = Button(root, text='read',
            command=lambda x=scale, y=scale2: print(f'x的值为：{x.get()}\ny的值为：{y.get()}'))
b1.pack(anchor=NW, padx=10, pady=10)
mainloop()
