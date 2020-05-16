import tkinter as tk  # 导入 tkinter 模块
from tkinter import filedialog

root = tk.Tk()
root.title('nb')
label1=tk.Label(root,text='禁止访问').pack(side=tk.TOP)

photo=tk.PhotoImage(file='18.gif')
label2=tk.Label(root,image=photo)
label2.pack()
root.mainloop()
