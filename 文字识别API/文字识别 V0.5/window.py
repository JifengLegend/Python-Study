# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(379, 616)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/ico/开心果.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(14)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.genBtn = QtWidgets.QPushButton(self.groupBox)
        self.genBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.genBtn.setObjectName("genBtn")
        self.horizontalLayout.addWidget(self.genBtn)
        self.transBtn = QtWidgets.QPushButton(self.groupBox)
        self.transBtn.setMinimumSize(QtCore.QSize(0, 35))
        self.transBtn.setObjectName("transBtn")
        self.horizontalLayout.addWidget(self.transBtn)
        self.gridLayout_2.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(28, 17, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        self.autoR = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.autoR.setFont(font)
        self.autoR.setChecked(True)
        self.autoR.setObjectName("autoR")
        self.gridLayout.addWidget(self.autoR, 0, 3, 1, 1)
        self.autoBtn = QtWidgets.QPushButton(self.groupBox)
        self.autoBtn.setMinimumSize(QtCore.QSize(26, 0))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(9)
        self.autoBtn.setFont(font)
        self.autoBtn.setStyleSheet("text-align:center;padding:3px 0px")
        self.autoBtn.setCheckable(False)
        self.autoBtn.setChecked(False)
        self.autoBtn.setObjectName("autoBtn")
        self.gridLayout.addWidget(self.autoBtn, 0, 4, 1, 1)
        self.autoTo = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.autoTo.setFont(font)
        self.autoTo.setStyleSheet("")
        self.autoTo.setAlignment(QtCore.Qt.AlignCenter)
        self.autoTo.setObjectName("autoTo")
        self.gridLayout.addWidget(self.autoTo, 0, 5, 1, 1)
        self.copyBtn = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.copyBtn.setFont(font)
        self.copyBtn.setObjectName("copyBtn")
        self.gridLayout.addWidget(self.copyBtn, 1, 0, 1, 1)
        self.delBtn = QtWidgets.QPushButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.delBtn.setFont(font)
        self.delBtn.setObjectName("delBtn")
        self.gridLayout.addWidget(self.delBtn, 1, 1, 1, 1)
        self.defR = QtWidgets.QRadioButton(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.defR.setFont(font)
        self.defR.setObjectName("defR")
        self.gridLayout.addWidget(self.defR, 1, 3, 1, 1)
        self.defBtn = QtWidgets.QPushButton(self.groupBox)
        self.defBtn.setMinimumSize(QtCore.QSize(26, 0))
        font = QtGui.QFont()
        font.setFamily("MS Serif")
        font.setPointSize(9)
        self.defBtn.setFont(font)
        self.defBtn.setStyleSheet("text-align:center;padding:3px 0px")
        self.defBtn.setObjectName("defBtn")
        self.gridLayout.addWidget(self.defBtn, 1, 4, 1, 1)
        self.defTo = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.defTo.setFont(font)
        self.defTo.setStyleSheet("")
        self.defTo.setAlignment(QtCore.Qt.AlignCenter)
        self.defTo.setObjectName("defTo")
        self.gridLayout.addWidget(self.defTo, 1, 5, 1, 1)
        self.c01 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.c01.setFont(font)
        self.c01.setStyleSheet("")
        self.c01.setChecked(True)
        self.c01.setObjectName("c01")
        self.gridLayout.addWidget(self.c01, 0, 0, 1, 1)
        self.c02 = QtWidgets.QCheckBox(self.groupBox)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(11)
        self.c02.setFont(font)
        self.c02.setObjectName("c02")
        self.gridLayout.addWidget(self.c02, 0, 1, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setColumnStretch(2, 1)
        self.gridLayout.setColumnStretch(3, 1)
        self.gridLayout.setColumnStretch(4, 1)
        self.gridLayout.setColumnStretch(5, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabCtrl = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.tabCtrl.setFont(font)
        self.tabCtrl.setObjectName("tabCtrl")
        self.tab = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.tab.setFont(font)
        self.tab.setObjectName("tab")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.rawText = QtWidgets.QTextEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.rawText.setFont(font)
        self.rawText.setObjectName("rawText")
        self.horizontalLayout_3.addWidget(self.rawText)
        self.tabCtrl.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(12)
        self.tab_2.setFont(font)
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.transText = QtWidgets.QTextEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("微软雅黑 Light")
        font.setPointSize(14)
        self.transText.setFont(font)
        self.transText.setObjectName("transText")
        self.horizontalLayout_4.addWidget(self.transText)
        self.tabCtrl.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabCtrl)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 379, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabCtrl.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "青灵OCR V0.5"))
        self.groupBox.setTitle(_translate("MainWindow", "执行："))
        self.genBtn.setText(_translate("MainWindow", "文字识别"))
        self.transBtn.setText(_translate("MainWindow", "百度翻译"))
        self.autoR.setText(_translate("MainWindow", "Auto"))
        self.autoBtn.setText(_translate("MainWindow", "-->"))
        self.autoTo.setText(_translate("MainWindow", "Zh"))
        self.copyBtn.setText(_translate("MainWindow", "复制"))
        self.delBtn.setText(_translate("MainWindow", "清空"))
        self.defR.setText(_translate("MainWindow", "Zh"))
        self.defBtn.setText(_translate("MainWindow", "-->"))
        self.defTo.setText(_translate("MainWindow", "En"))
        self.c01.setText(_translate("MainWindow", "文本净化"))
        self.c02.setText(_translate("MainWindow", "公式识别"))
        self.rawText.setPlaceholderText(_translate("MainWindow", "识别后的文本会出现在这里~"))
        self.tabCtrl.setTabText(self.tabCtrl.indexOf(self.tab), _translate("MainWindow", "Raw Text"))
        self.transText.setPlaceholderText(_translate("MainWindow", "Raw Text 的翻译结果会出现在这里~"))
        self.tabCtrl.setTabText(self.tabCtrl.indexOf(self.tab_2), _translate("MainWindow", "Trans Text"))
import rec_rc
