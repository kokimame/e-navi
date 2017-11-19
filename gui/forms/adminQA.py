# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/adminQA.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(721, 908)
        Form.setStyleSheet("background-color: rgb(255,255,255)")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(5, 0, 5, 9)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 709, 897))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("../image/enavi_header.png"))
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dbBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.dbBtn.setStyleSheet("background-color: rgb(0,255,255)")
        self.dbBtn.setObjectName("dbBtn")
        self.verticalLayout.addWidget(self.dbBtn)
        self.entryBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.entryBtn.setStyleSheet("background-color: rgb(0,255,255)")
        self.entryBtn.setObjectName("entryBtn")
        self.verticalLayout.addWidget(self.entryBtn)
        self.horizontalLayout_3.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.QAeditTable = QtWidgets.QTableWidget(self.scrollAreaWidgetContents_2)
        self.QAeditTable.setObjectName("QAeditTable")
        self.QAeditTable.setColumnCount(2)
        self.QAeditTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.QAeditTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.QAeditTable.setHorizontalHeaderItem(1, item)
        self.verticalLayout_2.addWidget(self.QAeditTable)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem1)
        self.endBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.endBtn.setObjectName("endBtn")
        self.horizontalLayout_4.addWidget(self.endBtn)
        self.applyBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.applyBtn.setObjectName("applyBtn")
        self.horizontalLayout_4.addWidget(self.applyBtn)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "管理者画面（質問編集）"))
        self.dbBtn.setText(_translate("Form", "企業DB"))
        self.entryBtn.setText(_translate("Form", "エントリー"))
        item = self.QAeditTable.horizontalHeaderItem(0)
        item.setText(_translate("Form", "質問内容"))
        item = self.QAeditTable.horizontalHeaderItem(1)
        item.setText(_translate("Form", "配点"))
        self.endBtn.setText(_translate("Form", "終了"))
        self.applyBtn.setText(_translate("Form", "確定"))

