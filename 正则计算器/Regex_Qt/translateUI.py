import sys
import os
def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
if __name__ == "__main__":
    chRec()
    os.system('pyuic5 -o subWindow.py subWindow.ui')