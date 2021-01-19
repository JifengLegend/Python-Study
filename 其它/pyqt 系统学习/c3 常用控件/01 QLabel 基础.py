import sys
import os
from PyQt5.QtWidgets import QVBoxLayout,QMainWindow,QApplication,QLabel,QWidget
from PyQt5.QtGui import QPixmap, QPalette
from PyQt5.QtCore import Qt

def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)

class QLabelDemo(QWidget):
    def __init__(self,parent=None):
        super().__init__()
        self.setWindowTitle("QLabel")
        self.resize(400,300)
 
        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)

        label1.setText("<font color=yellow>这是一个文本标签.</font>")
        label1.setAutoFillBackground(True)
        
        
        palette=QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)


        label2.setText("<a href='#'>欢迎使用Python  GUI程序</a>")

        label3.setAlignment(Qt.AlignCenter)

        label3.setPixmap(QPixmap('./卷蛋糕.png'))
        

        label4.setOpenExternalLinks(True)
        label4.setAlignment(Qt.AlignRight)

        label4.setText("<a href='https://item.jd.com/12417265.html'>感谢关注《Python从菜鸟到高手》</a>")

        vbox = QVBoxLayout()

        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)


        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)

        self.setLayout(vbox)
    def linkHovered(self):
        print('当鼠标滑过label2标签时，触发事件')

    def linkClicked(self):
        print('当鼠标单击label4标签时，触发事件')


if __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    win00=QLabelDemo()
    win00.show()

    sys.exit(app.exec_())
