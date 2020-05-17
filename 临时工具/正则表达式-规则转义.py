import re
patten=' (\d+)'
patten=re.sub(r'(?=\\)',r'\\',patten)
replace=',\1'
replace=re.sub(r'(?=\\)',r'\\',replace)
print(patten,replace)

text='''第一章 自动控制的一般概念 1
... 第二章 控制系统的数学模型 8
... 第三章 线性系统的时域分析法 38
... 第四章 线性系统的根轨迹法 83
... 第五章 线性系统的频域分析法 134
... 第六章 线性系统的校正方法 177
... 第七章 线性离散系统的分析与校正 219
... 第八章 非线性控制系统分析 255
... 第九章 线性系统的状态空间分析与综合 298
... 第十章 动态系统的优控制方法 356
... 参考文献 391 '''
a=re.sub(patten,replace,text)
print(a)