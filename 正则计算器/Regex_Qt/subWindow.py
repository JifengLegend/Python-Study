# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'subWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Warehouse(object):
    # render=QtCore.pyqtSignal(int)
    # def renderFun(self):
    #     self.render.emit(self.lv1.currentIndex())
    def setupUi(self, Warehouse):
        Warehouse.setObjectName("Warehouse")
        Warehouse.resize(485, 336)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(11)
        Warehouse.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Warehouse)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.le1 = QtWidgets.QLineEdit(Warehouse)
        self.le1.setObjectName("le1")
        self.gridLayout.addWidget(self.le1, 0, 0, 1, 1)
        self.reBtn = QtWidgets.QPushButton(Warehouse)
        self.reBtn.setObjectName("reBtn")
        self.gridLayout.addWidget(self.reBtn, 0, 1, 1, 1)
        self.delBtn = QtWidgets.QPushButton(Warehouse)
        self.delBtn.setObjectName("delBtn")
        self.gridLayout.addWidget(self.delBtn, 0, 2, 1, 1)
        self.le2 = QtWidgets.QLineEdit(Warehouse)
        self.le2.setAlignment(QtCore.Qt.AlignCenter)
        self.le2.setObjectName("le2")
        self.gridLayout.addWidget(self.le2, 1, 0, 1, 1)
        self.okBtn = QtWidgets.QPushButton(Warehouse)
        self.okBtn.setObjectName("okBtn")
        self.gridLayout.addWidget(self.okBtn, 1, 1, 1, 1)
        self.cancelBtn = QtWidgets.QPushButton(Warehouse)
        self.cancelBtn.setObjectName("cancelBtn")
        self.gridLayout.addWidget(self.cancelBtn, 1, 2, 1, 1)
        self.lv1 = QtWidgets.QListWidget(Warehouse)
        self.lv1.setObjectName("lv1")
        self.gridLayout.addWidget(self.lv1, 2, 0, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Warehouse)
        QtCore.QMetaObject.connectSlotsByName(Warehouse)

    def retranslateUi(self, Warehouse):
        _translate = QtCore.QCoreApplication.translate
        Warehouse.setWindowTitle(_translate("Warehouse", "Form"))
        self.reBtn.setText(_translate("Warehouse", "命名"))
        self.delBtn.setText(_translate("Warehouse", "删除"))
        self.okBtn.setText(_translate("Warehouse", "确认"))
        self.cancelBtn.setText(_translate("Warehouse", "取消"))
        