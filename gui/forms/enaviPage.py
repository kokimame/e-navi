# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/enaviPage.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(721, 910)
        Form.setStyleSheet("background-color: rgb(255,255,80);")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 701, 890))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setGeometry(QtCore.QRect(0, 0, 701, 891))
        self.label.setStyleSheet("background-color: rgb(255,255,255);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../image/enavi_page.png"))
        self.label.setObjectName("label")
        self.backBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.backBtn.setGeometry(QtCore.QRect(0, 0, 51, 21))
        self.backBtn.setStyleSheet("background-color: rgb(200,200,200);")
        self.backBtn.setObjectName("backBtn")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.backBtn.setText(_translate("Form", "戻る"))

