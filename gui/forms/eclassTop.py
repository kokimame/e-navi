# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/eclassTop.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_topView(object):
    def setupUi(self, topView):
        topView.setObjectName("topView")
        topView.resize(721, 910)
        topView.setStyleSheet("background-color: rgb(255,255,255);")
        self.gridLayout = QtWidgets.QGridLayout(topView)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(topView)
        self.scrollArea.setStyleSheet("border: none;")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 721, 910))
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.upperLayout = QtWidgets.QHBoxLayout()
        self.upperLayout.setObjectName("upperLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.upperLayout.addItem(spacerItem)
        self.upperLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.upperLabel.setText("")
        self.upperLabel.setPixmap(QtGui.QPixmap("../image/eclass_upper.png"))
        self.upperLabel.setObjectName("upperLabel")
        self.upperLayout.addWidget(self.upperLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.upperLayout.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.upperLayout)
        self.buttonsLayout = QtWidgets.QHBoxLayout()
        self.buttonsLayout.setObjectName("buttonsLayout")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem2)
        self.gridLayout_7 = QtWidgets.QGridLayout()
        self.gridLayout_7.setSpacing(0)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.webdiskBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.webdiskBtn.setStyleSheet("border: none;")
        self.webdiskBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../image/webdisk_pc_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.webdiskBtn.setIcon(icon)
        self.webdiskBtn.setIconSize(QtCore.QSize(170, 70))
        self.webdiskBtn.setObjectName("webdiskBtn")
        self.gridLayout_7.addWidget(self.webdiskBtn, 1, 0, 1, 1)
        self.webmailBtn_63 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.webmailBtn_63.setStyleSheet("border: none;")
        self.webmailBtn_63.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../image/webmail_pc.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.webmailBtn_63.setIcon(icon1)
        self.webmailBtn_63.setIconSize(QtCore.QSize(170, 70))
        self.webmailBtn_63.setObjectName("webmailBtn_63")
        self.gridLayout_7.addWidget(self.webmailBtn_63, 0, 2, 1, 1)
        self.webmailBtn_60 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.webmailBtn_60.setStyleSheet("border: none;")
        self.webmailBtn_60.setText("")
        self.webmailBtn_60.setIcon(icon1)
        self.webmailBtn_60.setIconSize(QtCore.QSize(170, 70))
        self.webmailBtn_60.setObjectName("webmailBtn_60")
        self.gridLayout_7.addWidget(self.webmailBtn_60, 1, 1, 1, 1)
        self.duetBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.duetBtn.setStyleSheet("border: none;")
        self.duetBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../image/duet_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.duetBtn.setIcon(icon2)
        self.duetBtn.setIconSize(QtCore.QSize(170, 70))
        self.duetBtn.setObjectName("duetBtn")
        self.gridLayout_7.addWidget(self.duetBtn, 2, 0, 1, 1)
        self.webmailBtn_59 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.webmailBtn_59.setStyleSheet("border: none;")
        self.webmailBtn_59.setText("")
        self.webmailBtn_59.setIcon(icon1)
        self.webmailBtn_59.setIconSize(QtCore.QSize(170, 70))
        self.webmailBtn_59.setObjectName("webmailBtn_59")
        self.gridLayout_7.addWidget(self.webmailBtn_59, 2, 1, 1, 1)
        self.webmailBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.webmailBtn.setStyleSheet("border: none;")
        self.webmailBtn.setText("")
        self.webmailBtn.setIcon(icon1)
        self.webmailBtn.setIconSize(QtCore.QSize(170, 70))
        self.webmailBtn.setObjectName("webmailBtn")
        self.gridLayout_7.addWidget(self.webmailBtn, 0, 0, 1, 1)
        self.goGlobalBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.goGlobalBtn.setStyleSheet("border: none;")
        self.goGlobalBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../image/goglobal_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.goGlobalBtn.setIcon(icon3)
        self.goGlobalBtn.setIconSize(QtCore.QSize(170, 70))
        self.goGlobalBtn.setObjectName("goGlobalBtn")
        self.gridLayout_7.addWidget(self.goGlobalBtn, 3, 0, 1, 1)
        self.elearningBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.elearningBtn.setStyleSheet("border: none;")
        self.elearningBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("../image/elearning_btn.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.elearningBtn.setIcon(icon4)
        self.elearningBtn.setIconSize(QtCore.QSize(170, 70))
        self.elearningBtn.setObjectName("elearningBtn")
        self.gridLayout_7.addWidget(self.elearningBtn, 4, 0, 1, 1)
        self.webMail_56 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.webMail_56.setStyleSheet("border: none;")
        self.webMail_56.setText("")
        self.webMail_56.setIcon(icon1)
        self.webMail_56.setIconSize(QtCore.QSize(170, 70))
        self.webMail_56.setObjectName("webMail_56")
        self.gridLayout_7.addWidget(self.webMail_56, 2, 2, 1, 1)
        self.webmailBtn_58 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.webmailBtn_58.setStyleSheet("border: none;")
        self.webmailBtn_58.setText("")
        self.webmailBtn_58.setIcon(icon1)
        self.webmailBtn_58.setIconSize(QtCore.QSize(170, 70))
        self.webmailBtn_58.setObjectName("webmailBtn_58")
        self.gridLayout_7.addWidget(self.webmailBtn_58, 1, 2, 1, 1)
        self.webmailBtn_64 = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.webmailBtn_64.setStyleSheet("border: none;")
        self.webmailBtn_64.setText("")
        self.webmailBtn_64.setIcon(icon1)
        self.webmailBtn_64.setIconSize(QtCore.QSize(170, 70))
        self.webmailBtn_64.setObjectName("webmailBtn_64")
        self.gridLayout_7.addWidget(self.webmailBtn_64, 0, 1, 1, 1)
        self.buttonsLayout.addLayout(self.gridLayout_7)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.buttonsLayout.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.buttonsLayout)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.lowerLayout = QtWidgets.QHBoxLayout()
        self.lowerLayout.setObjectName("lowerLayout")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lowerLayout.addItem(spacerItem5)
        self.lowerLabel = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        self.lowerLabel.setText("")
        self.lowerLabel.setPixmap(QtGui.QPixmap("../image/eclass_lower.png"))
        self.lowerLabel.setObjectName("lowerLabel")
        self.lowerLayout.addWidget(self.lowerLabel)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.lowerLayout.addItem(spacerItem6)
        self.verticalLayout.addLayout(self.lowerLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.scrollArea.raise_()

        self.retranslateUi(topView)
        QtCore.QMetaObject.connectSlotsByName(topView)

    def retranslateUi(self, topView):
        _translate = QtCore.QCoreApplication.translate
        topView.setWindowTitle(_translate("topView", "同志社大学Webシングルサインオンシステム"))
