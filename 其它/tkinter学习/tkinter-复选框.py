import tkinter as tk  # 导入 tkinter 模块

root = tk.Tk()
root.title('元气满满')

frame = tk.LabelFrame(root,text='今晚要谁陪我呢？',padx=20,pady=20)
frame.pack(padx=40,pady=40)

girls = [('貂蝉', 1),
         ('西施', 2),
         ('杨玉环', 3),
         ('王昭君', 4)]
v = tk.IntVar()
v=[]
for girl,num in girls:
    v.append(tk.IntVar())
    b = tk.Checkbutton(frame, text=girl, variable=v[-1],indicatoron=False)
    b.pack(fill=tk.X)

root.mainloop()
