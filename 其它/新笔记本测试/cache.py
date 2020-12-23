import os
import re
def chRec():
    """
    获取当前python脚本的工作目录
    """
    pyPath=__file__
    recPath=re.sub(r'\\[A-z0-9_]+\.py','',pyPath)
    print(f'      源目录为：\t {pyPath}')
    print(f'当前工作目录为：\t {recPath}')
    os.chdir(recPath)
if __name__ == "__main__":
    chRec()
    print(os.path.abspath('.'))
    # os.chdir('d:\Python学习\其它\新笔记本测试')