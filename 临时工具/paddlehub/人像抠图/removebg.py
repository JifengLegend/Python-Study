import paddlehub as hub   # 导入PaddleHub代码库
import re
import os
def chRec():
    recPath=__file__
    recPath=re.sub(r'[a-z_ 文字识别 V0.5 启动器人像抠图.py]+\.py','',recPath)
    print(recPath)
    os.chdir(recPath)

if __name__ == "__main__":
    chRec()
    module = hub.Module(name="deeplabv3p_xception65_humanseg")    # 指定模型名称
    res = module.segmentation(paths = ["./test.jpg"], visualization=True, output_dir='humanseg_output')  
    # 指定模型的输入和输出路径，执行并输出预测结果，其中visualization=True表示将结果可视化输出