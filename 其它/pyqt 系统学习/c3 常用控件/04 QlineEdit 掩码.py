import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIntValidator,QDoubleValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
import os
"""
用掩码限制QLineEdit控件的输入

A    ASCII字母字符是必须输入的(A-Z、a-z)
a    ASCII字母字符是允许输入的,但不是必需的(A-Z、a-z)
N    ASCII字母字符是必须输入的(A-Z、a-z、0-9)
n    ASII字母字符是允许输入的,但不是必需的(A-Z、a-z、0-9)
X    任何字符都是必须输入的
x    任何字符都是允许输入的,但不是必需的
9    ASCII数字字符是必须输入的(0-9)
0    ASCII数字字符是允许输入的,但不是必需的(0-9)
D    ASCII数字字符是必须输入的(1-9)
d    ASCII数字字符是允许输入的,但不是必需的(1-9)
#    ASCI数字字符或加减符号是允许输入的,但不是必需的
H    十六进制格式字符是必须输入的(A-F、a-f、0-9)
h    十六进制格式字符是允许输入的,但不是必需的(A-F、a-f、0-9)
B    二进制格式字符是必须输入的(0,1)
b    二进制格式字符是允许输入的,但不是必需的(0,1)
>    所有的字母字符都大写
<    所有的字母字符都小写
!    关闭大小写转换
\    使用"\"转义上面列出的字符
"""

def chRec():
    absPath=__file__
    recPath=absPath[:absPath.rfind("\\")]
    os.chdir(recPath)
class QLineEditMask(QWidget):
    def __init__(self,parent=None):
        super().__init__(parent)
        self.setWindowTitle("QlineEdit 检验器")
        formLayout=QFormLayout()
        
        edit1=QLineEdit()
        edit2=QLineEdit()
        edit3=QLineEdit()
        edit4=QLineEdit()

        formLayout.addRow('IP',edit1)
        formLayout.addRow('Mac',edit2)
        formLayout.addRow('日期',edit3)
        formLayout.addRow('许可证',edit4)

        # ip
        edit1.setInputMask('000.000.000;_')
        # mac
        edit2.setInputMask('HH:HH:HH:HH:HH:HH;_')
        # date
        edit3.setInputMask('0000-00-00')
        # 许可证
        edit4.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA;_')

        self.setLayout(formLayout)




if  __name__ == "__main__":
    chRec()
    app=QApplication(sys.argv)
    main=QLineEditMask()
    main.show()

    sys.exit(app.exec_())