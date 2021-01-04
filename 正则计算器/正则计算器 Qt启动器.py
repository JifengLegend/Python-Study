import re
import os
import os.path as path

def chRec():
    recPath=__file__
    cachePath=recPath.split('\\')
    tarPath=''
    for each in cachePath[0:-1]:
        tarPath+=each+'\\'
    print(tarPath)
    os.chdir(tarPath)
if  __name__ == "__main__":
   chRec()
   os.system(f'pythonw ".\Regex_Qt\work.py"') 