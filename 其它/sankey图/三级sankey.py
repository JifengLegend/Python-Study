import  pandas as pd
from pyecharts.charts import  Sankey
from pyecharts import options as opts

# 整理基础数据
df=pd.DataFrame({
    '产品名称':['机器人','猛击赛车','莱肯赛车','机器人','猛击赛车','莱肯赛车'],
    '第一次购买':['遥控机器人','遥控猛击赛车','遥控莱肯赛车','非遥控机器人','非遥控猛击赛车','非遥控莱肯赛车'],
    '第二次购买':['未购买','购买','未购买','购买','未购买','购买'],
    '数量':[12,23,45,32,11,12]
})
print(df)
# 第一步:节点

# 先把所有涉及到的节点去重规整到一起,即把“类型”列的“遥控”、“非遥控”和产品名称列中的“机器人”、“猛击赛车”、“莱肯赛车”以列表内嵌套字典的形式去重汇总:
nodes=[]
for i in range(3):#修改处
    vales=df.iloc[:,i].unique()
    for value in vales:
        dic={}
        dic['name']=value
        nodes.append(dic)
print(nodes)
# 第二步:定义边和流量
# 形成 first second 列表
first=df.groupby(['产品名称','第一次购买'])['数量'].sum().reset_index()
second=df.iloc[:,1:]
first.columns=['source','target','value']
second.columns=['source','target','value']
result=pd.concat([first,second])
print(result.head(6))

linkes=[]
for i in result.values:
    dic={}
    dic['source']=i[0]
    dic['target']=i[1]
    dic['value']=i[2]
    linkes.append(dic)
print(linkes)

pic=(
    Sankey().add(
        '',#图例名称
        nodes,#传入节点数据
        linkes,#传入边和流量数据
        #设置透明度、弯曲度、颜色
        linestyle_opt=opts.LineStyleOpts(opacity=0.3,curve=0.5,color='source'),
        #标签显示位置
        label_opts=opts.LabelOpts(position='right'),
        #节点之间的距离
        node_gap=30,
        #orient="vertical",#查看垂直图片的操作
    )
    .set_global_opts(title_opts=opts.TitleOpts(title='创意李公馆产品分类图'))
)
pic.render('test.html')