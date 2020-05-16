import tkinter as tk  # 导入 tkinter 模块

root = tk.Tk()
root.title('元气满满')

frame = tk.LabelFrame(root, text='输入信息', padx=20, pady=20)
frame.pack(padx=40, pady=40)

tk.Label(frame, text='作品：').grid(row=0, column=0)
tk.Label(frame, text='作者：').grid(row=1, column=0)

e1 = tk.Entry(frame)
e1.grid(row=0, column=1, pady=10)
e2 = tk.Entry(frame)
e2.grid(row=1, column=1, pady=10)


def show():
    print(f'作品《{e1.get()}》')
    print(f'作者：{e2.get()}')


tk.Button(root, text='获取信息', command=show, width=10).pack(side=tk.LEFT,padx=20,pady=20)
tk.Button(root, text='退出', command=root.quit, width=10).pack(side=tk.RIGHT,padx=20,pady=20)
root.mainloop()
