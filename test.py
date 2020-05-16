import tkinter as tk  # 导入 tkinter 模块

root = tk.Tk()
root.title('Matlab 公式转换器')

frame = tk.LabelFrame(root, text='选择模式', padx=20, pady=20)
frame.pack(padx=40, pady=40)
# 模式选择
tishis=('请输入要转换的公式：','请输入要绘制的公式：')
def tiShi():
    ti= tishis[0] if not v.get() else tishis[1]
    tishi.set(ti)

v = tk.IntVar()
v.set(0)
modes = [('转换模式', 0), ('绘制模式', 1)]
for mode, num in modes:
    b = tk.Radiobutton(frame, text=mode, variable=v, value=num, indicatoron=False,command=tiShi)
    b.pack(fill=tk.X)

# 输入文本框
tishi=tk.StringVar()
tishi.set('请输入要转换的公式：')
getFrame = tk.Label(root,padx=20, pady=20)
getFrame.pack(padx=40, pady=40)

l1=tk.Label(getFrame,textvariable=tishi)
l1.grid(row=0,column=0)

e1 = tk.Entry(getFrame)
e1.grid(row=0, column=1, pady=10)


# 开始按钮
def getMath():
    global a
    a=e1.get()
    print(f'获取的公式为：{e1.get()}')


tk.Button(root, text='开始！', command=getMath, width=10).pack(side=tk.RIGHT, padx=20, pady=20)

'''
tk.Label(frame, text='作品：').grid(row=0, column=0)
tk.Label(frame, text='作者：').grid(row=1, column=0)

e1 = tk.Entry(frame)
e1.grid(row=0, column=1, pady=10)
e2 = tk.Entry(frame)
e2.grid(row=1, column=1, pady=10)





tk.Button(root, text='获取信息', command=show, width=10).pack(side=tk.LEFT,padx=20,pady=20)
tk.Button(root, text='退出', command=root.quit, width=10).pack(side=tk.RIGHT,padx=20,pady=20)

'''
root.mainloop()
