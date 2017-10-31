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
        self.msgLabel = QtWidgets.QLabel(PopupDialog)
        self.msgLabel.setGeometry(QtCore.QRect(40, 10, 271, 81))
        self.msgLabel.setObjectName("msgLabel")
        self.cancelBtn = QtWidgets.QPushButton(PopupDialog)
        self.cancelBtn.setGeometry(QtCore.QRect(60, 110, 99, 27))
        self.cancelBtn.setObjectName("cancelBtn")
        self.okBtn = QtWidgets.QPushButton(PopupDialog)
        self.okBtn.setGeometry(QtCore.QRect(190, 110, 99, 27))
        self.okBtn.setObjectName("okBtn")

        self.retranslateUi(PopupDialog)
        QtCore.QMetaObject.connectSlotsByName(PopupDialog)

    def retranslateUi(self, PopupDialog):
        _translate = QtCore.QCoreApplication.translate
        PopupDialog.setWindowTitle(_translate("PopupDialog", "確認"))
        self.msgLabel.setText(_translate("PopupDialog", "<html><head/><body><p><br/></p></body></html>"))
        self.cancelBtn.setText(_translate("PopupDialog", "キャンセル"))
        self.okBtn.setText(_translate("PopupDialog", "確認"))

