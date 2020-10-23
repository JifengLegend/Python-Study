import os
import os.path as path
import re
def chRec():
    recPath=__file__
    recPath=re.sub(r'[a-z_ 文字识别 V0.5 启动器.py]+\.py','',recPath)
    print(recPath)
    os.chdir(recPath)
if __name__ == "__main__":
    chRec()
    os.system(f'python ".\文字识别 V0.5\OCR_V0.5.py"')