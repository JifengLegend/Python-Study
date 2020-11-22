import  pandas as pd
from pyecharts.charts import  Sankey
from pyecharts import options as opts

# 整理基础数据
df=pd.DataFrame({
    '类型':['遥控','遥控','遥控','非遥控','非遥控','非遥控'],
    '产品名称':['机器人','猛击赛车','莱肯赛车','机器人','猛击赛车','莱肯赛车'],
    '数量':[15,23,36,48,21,11]
})
print(df)
# 第一步:节点

# 先把所有涉及到的节点去重规整到一起,即把“类型”列的“遥控”、“非遥控”和产品名称列中的“机器人”、“猛击赛车”、“莱肯赛车”以列表内嵌套字典的形式去重汇总:
nodes=[]
for i in range(2):
    vales=df.iloc[:,i].unique()
    for value in vales:
        dic={}
        dic['name']=value
        nodes.append(dic)
print(nodes)
# 第二步:定义边和流量
linkes=[]
for i in df.values:
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
    )
    .set_global_opts(title_opts=opts.TitleOpts(title='创意李公馆产品分类图'))
)
pic.render('test.html')