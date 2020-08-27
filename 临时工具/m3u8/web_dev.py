import sys
import os
from glob import glob
realPath=os.path.abspath(".")
realPath=os.path.join(realPath,"临时工具\m3u8")

flists=glob(os.path.join(realPath,'*.m3u8'))
print(flists)