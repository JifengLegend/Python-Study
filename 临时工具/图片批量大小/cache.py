from PIL import Image
import os
import os.path
import glob

def resizeImage(pngFile,outDir,width=1540,height=2430):
    img=Image.open(pngFile)
    try:
        new_img=img.resize((width,height),Image.BILINEAR)
        if new_img.mode=='P':
            new_img=new_img.convert('RGB')
        if new_img.mode=="RGBA":
            new_img=new_img.convert('RGB')
        new_img.save(os.path.join(outDir,os.path.basename(pngFile)))
    except Exception as e:
        print(e)
os.mkdir('./ReSizeImage')
for img in glob.glob('*.png'):

    print(img)
    resizeImage(img,'./ReSizeImage')
