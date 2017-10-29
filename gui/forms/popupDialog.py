# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/popupDialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PopupDialog(object):
    def setupUi(self, PopupDialog):
        PopupDialog.setObjectName("PopupDialog")
        PopupDialog.resize(359, 161)
        self.label = QtWidgets.QLabel(PopupDialog)
        self.label.setGeometry(QtCore.QRect(40, 10, 271, 81))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(PopupDialog)
        self.pushButton.setGeometry(QtCore.QRect(60, 110, 99, 27))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(PopupDialog)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 110, 99, 27))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(PopupDialog)
        QtCore.QMetaObject.connectSlotsByName(PopupDialog)

    def retranslateUi(self, PopupDialog):
        _translate = QtCore.QCoreApplication.translate
        PopupDialog.setWindowTitle(_translate("PopupDialog", "確認"))
        self.label.setText(_translate("PopupDialog", "<html><head/><body><p>これはポップアップのテストだよ</p><p>いろいろなボタンをのせることができるよ</p></body></html>"))
        self.pushButton.setText(_translate("PopupDialog", "キャンセル"))
        self.pushButton_2.setText(_translate("PopupDialog", "確認"))

