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
        MainWindow.resize(439, 775)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.l01 = QtWidgets.QListWidget(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.l01.sizePolicy().hasHeightForWidth())
        self.l01.setSizePolicy(sizePolicy)
        self.l01.setResizeMode(QtWidgets.QListView.Adjust)
        self.l01.setViewMode(QtWidgets.QListView.ListMode)
        self.l01.setModelColumn(0)
        self.l01.setItemAlignment(QtCore.Qt.AlignLeading)
        self.l01.setObjectName("l01")
        self.horizontalLayout.addWidget(self.l01)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.b01 = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.b01.sizePolicy().hasHeightForWidth())
        self.b01.setSizePolicy(sizePolicy)
        self.b01.setMinimumSize(QtCore.QSize(0, 45))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.b01.setFont(font)
        self.b01.setCheckable(False)
        self.b01.setChecked(False)
        self.b01.setAutoDefault(True)
        self.b01.setObjectName("b01")
        self.verticalLayout_2.addWidget(self.b01)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        self.frame1 = QtWidgets.QFrame(self.centralwidget)
        self.frame1.setEnabled(True)
        self.frame1.setMinimumSize(QtCore.QSize(0, 142))
        self.frame1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame1.setObjectName("frame1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.pname = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(20)
        self.pname.setFont(font)
        self.pname.setStyleSheet("color: rgb(243, 21, 106)")
        self.pname.setFrameShadow(QtWidgets.QFrame.Plain)
        self.pname.setAlignment(QtCore.Qt.AlignCenter)
        self.pname.setObjectName("pname")
        self.horizontalLayout_2.addWidget(self.pname)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.m01 = QtWidgets.QLCDNumber(self.frame1)
        self.m01.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.m01.setFont(font)
        self.m01.setStyleSheet("color:rgb(7, 145, 230)")
        self.m01.setSmallDecimalPoint(False)
        self.m01.setDigitCount(7)
        self.m01.setProperty("value", 0.0)
        self.m01.setObjectName("m01")
        self.horizontalLayout_3.addWidget(self.m01)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.frame1)
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.m02 = QtWidgets.QLCDNumber(self.frame1)
        self.m02.setMinimumSize(QtCore.QSize(130, 0))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(16)
        self.m02.setFont(font)
        self.m02.setStyleSheet("color:rgb(139, 139, 139)")
        self.m02.setDigitCount(8)
        self.m02.setObjectName("m02")
        self.horizontalLayout_4.addWidget(self.m02)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.verticalLayout.setStretch(0, 1)
        self.verticalLayout.setStretch(1, 1)
        self.verticalLayout.setStretch(2, 1)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.frame1)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 110))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.addText01 = QtWidgets.QLineEdit(self.tab)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.addText01.sizePolicy().hasHeightForWidth())
        self.addText01.setSizePolicy(sizePolicy)
        self.addText01.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.addText01.setFont(font)
        self.addText01.setText("")
        self.addText01.setObjectName("addText01")
        self.horizontalLayout_5.addWidget(self.addText01)
        self.label_2 = QtWidgets.QLabel(self.tab)
        self.label_2.setMaximumSize(QtCore.QSize(20, 20))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        self.addText02 = QtWidgets.QLineEdit(self.tab)
        self.addText02.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.addText02.setFont(font)
        self.addText02.setText("")
        self.addText02.setObjectName("addText02")
        self.horizontalLayout_5.addWidget(self.addText02)
        self.addAction = QtWidgets.QPushButton(self.tab)
        self.addAction.setObjectName("addAction")
        self.horizontalLayout_5.addWidget(self.addAction)
        self.addText03 = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.addText03.setFont(font)
        self.addText03.setText("")
        self.addText03.setObjectName("addText03")
        self.horizontalLayout_5.addWidget(self.addText03)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.tab_2)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.decText01 = QtWidgets.QLineEdit(self.tab_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.decText01.sizePolicy().hasHeightForWidth())
        self.decText01.setSizePolicy(sizePolicy)
        self.decText01.setMinimumSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.decText01.setFont(font)
        self.decText01.setText("")
        self.decText01.setObjectName("decText01")
        self.horizontalLayout_6.addWidget(self.decText01)
        self.label_5 = QtWidgets.QLabel(self.tab_2)
        self.label_5.setEnabled(True)
        self.label_5.setMaximumSize(QtCore.QSize(20, 20))
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_6.addWidget(self.label_5)
        self.decText02 = QtWidgets.QLineEdit(self.tab_2)
        self.decText02.setEnabled(False)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.decText02.setFont(font)
        self.decText02.setText("")
        self.decText02.setObjectName("decText02")
        self.horizontalLayout_6.addWidget(self.decText02)
        self.decAction = QtWidgets.QPushButton(self.tab_2)
        self.decAction.setObjectName("decAction")
        self.horizontalLayout_6.addWidget(self.decAction)
        self.decText03 = QtWidgets.QLineEdit(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Adobe Devanagari")
        font.setPointSize(14)
        self.decText03.setFont(font)
        self.decText03.setText("")
        self.decText03.setObjectName("decText03")
        self.horizontalLayout_6.addWidget(self.decText03)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.verticalLayout_2.setStretch(0, 3)
        self.verticalLayout_2.setStretch(1, 1)
        self.verticalLayout_2.setStretch(2, 1)
        self.verticalLayout_2.setStretch(3, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 439, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.setRec = QtWidgets.QAction(MainWindow)
        self.setRec.setCheckable(False)
        self.setRec.setChecked(False)
        self.setRec.setObjectName("setRec")
        self.menu.addAction(self.setRec)
        self.menu.addSeparator()
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "账单分析器"))
        self.groupBox.setTitle(_translate("MainWindow", "读取到的账单文件在这里~"))
        self.b01.setText(_translate("MainWindow", "分 析"))
        self.label.setText(_translate("MainWindow", "账单持有人："))
        self.pname.setText(_translate("MainWindow", "[基尼]"))
        self.pname.setProperty("setStyleSheet", _translate("MainWindow", "\"color:green\""))
        self.label_3.setText(_translate("MainWindow", "公账结余："))
        self.m01.setProperty("display", _translate("MainWindow", "170"))
        self.label_4.setText(_translate("MainWindow", "其它结余："))
        self.label_2.setText(_translate("MainWindow", "+"))
        self.addAction.setText(_translate("MainWindow", "="))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "昨天余额 加 当天流水"))
        self.label_5.setText(_translate("MainWindow", "-"))
        self.decAction.setText(_translate("MainWindow", "="))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "今天余额 减 今天流水"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.setRec.setText(_translate("MainWindow", "选择文件目录"))
