# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'design/enaviEntry.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(724, 910)
        Form.setStyleSheet("background-color: rgb(255,255,255)")
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setContentsMargins(5, 0, 5, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(Form)
        self.scrollArea.setStyleSheet("")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 712, 908))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("../image/enavi_header.png"))
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 1, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.comboBox_4 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_4.setObjectName("comboBox_4")
        self.horizontalLayout_4.addWidget(self.comboBox_4)
        self.comboBox_5 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_5.setObjectName("comboBox_5")
        self.horizontalLayout_4.addWidget(self.comboBox_5)
        self.comboBox_6 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_6.setObjectName("comboBox_6")
        self.horizontalLayout_4.addWidget(self.comboBox_6)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioButton = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout_5.addWidget(self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout_5.addWidget(self.radioButton_2)
        self.radioButton_3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout_5.addWidget(self.radioButton_3)
        self.radioButton_6 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_6.setObjectName("radioButton_6")
        self.horizontalLayout_5.addWidget(self.radioButton_6)
        self.radioButton_5 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_5.addWidget(self.radioButton_5)
        self.radioButton_4 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_5.addWidget(self.radioButton_4)
        self.radioButton_20 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_20.setObjectName("radioButton_20")
        self.horizontalLayout_5.addWidget(self.radioButton_20)
        self.radioButton_19 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_19.setObjectName("radioButton_19")
        self.horizontalLayout_5.addWidget(self.radioButton_19)
        self.verticalLayout_3.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.radioButton_21 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_21.setObjectName("radioButton_21")
        self.horizontalLayout_6.addWidget(self.radioButton_21)
        self.radioButton_22 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_22.setObjectName("radioButton_22")
        self.horizontalLayout_6.addWidget(self.radioButton_22)
        self.radioButton_13 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_13.setObjectName("radioButton_13")
        self.horizontalLayout_6.addWidget(self.radioButton_13)
        self.radioButton_23 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_23.setObjectName("radioButton_23")
        self.horizontalLayout_6.addWidget(self.radioButton_23)
        self.radioButton_24 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_24.setObjectName("radioButton_24")
        self.horizontalLayout_6.addWidget(self.radioButton_24)
        self.radioButton_14 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_14.setObjectName("radioButton_14")
        self.horizontalLayout_6.addWidget(self.radioButton_14)
        self.radioButton_15 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_15.setObjectName("radioButton_15")
        self.horizontalLayout_6.addWidget(self.radioButton_15)
        self.radioButton_16 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_16.setObjectName("radioButton_16")
        self.horizontalLayout_6.addWidget(self.radioButton_16)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.radioButton_17 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_17.setObjectName("radioButton_17")
        self.horizontalLayout_9.addWidget(self.radioButton_17)
        self.radioButton_25 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_25.setObjectName("radioButton_25")
        self.horizontalLayout_9.addWidget(self.radioButton_25)
        self.radioButton_18 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_18.setObjectName("radioButton_18")
        self.horizontalLayout_9.addWidget(self.radioButton_18)
        self.radioButton_29 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_29.setObjectName("radioButton_29")
        self.horizontalLayout_9.addWidget(self.radioButton_29)
        self.radioButton_28 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_28.setObjectName("radioButton_28")
        self.horizontalLayout_9.addWidget(self.radioButton_28)
        self.radioButton_27 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_27.setObjectName("radioButton_27")
        self.horizontalLayout_9.addWidget(self.radioButton_27)
        self.radioButton_26 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_26.setObjectName("radioButton_26")
        self.horizontalLayout_9.addWidget(self.radioButton_26)
        self.radioButton_30 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_30.setObjectName("radioButton_30")
        self.horizontalLayout_9.addWidget(self.radioButton_30)
        self.verticalLayout_3.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.radioButton_45 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_45.setObjectName("radioButton_45")
        self.horizontalLayout_10.addWidget(self.radioButton_45)
        self.radioButton_46 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_46.setObjectName("radioButton_46")
        self.horizontalLayout_10.addWidget(self.radioButton_46)
        self.radioButton_47 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_47.setObjectName("radioButton_47")
        self.horizontalLayout_10.addWidget(self.radioButton_47)
        self.radioButton_48 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_48.setObjectName("radioButton_48")
        self.horizontalLayout_10.addWidget(self.radioButton_48)
        self.radioButton_49 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_49.setObjectName("radioButton_49")
        self.horizontalLayout_10.addWidget(self.radioButton_49)
        self.radioButton_50 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_50.setObjectName("radioButton_50")
        self.horizontalLayout_10.addWidget(self.radioButton_50)
        self.radioButton_51 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_51.setObjectName("radioButton_51")
        self.horizontalLayout_10.addWidget(self.radioButton_51)
        self.radioButton_52 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_52.setObjectName("radioButton_52")
        self.horizontalLayout_10.addWidget(self.radioButton_52)
        self.verticalLayout_3.addLayout(self.horizontalLayout_10)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.radioButton_53 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_53.setObjectName("radioButton_53")
        self.horizontalLayout_15.addWidget(self.radioButton_53)
        self.radioButton_54 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_54.setObjectName("radioButton_54")
        self.horizontalLayout_15.addWidget(self.radioButton_54)
        self.radioButton_55 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_55.setObjectName("radioButton_55")
        self.horizontalLayout_15.addWidget(self.radioButton_55)
        self.radioButton_56 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_56.setObjectName("radioButton_56")
        self.horizontalLayout_15.addWidget(self.radioButton_56)
        self.radioButton_57 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_57.setObjectName("radioButton_57")
        self.horizontalLayout_15.addWidget(self.radioButton_57)
        self.radioButton_58 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_58.setObjectName("radioButton_58")
        self.horizontalLayout_15.addWidget(self.radioButton_58)
        self.radioButton_59 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_59.setObjectName("radioButton_59")
        self.horizontalLayout_15.addWidget(self.radioButton_59)
        self.radioButton_60 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_60.setObjectName("radioButton_60")
        self.horizontalLayout_15.addWidget(self.radioButton_60)
        self.verticalLayout_3.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.radioButton_35 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_35.setObjectName("radioButton_35")
        self.horizontalLayout_16.addWidget(self.radioButton_35)
        self.radioButton_36 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_36.setObjectName("radioButton_36")
        self.horizontalLayout_16.addWidget(self.radioButton_36)
        self.radioButton_7 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_7.setObjectName("radioButton_7")
        self.horizontalLayout_16.addWidget(self.radioButton_7)
        self.radioButton_31 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_31.setObjectName("radioButton_31")
        self.horizontalLayout_16.addWidget(self.radioButton_31)
        self.radioButton_32 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_32.setObjectName("radioButton_32")
        self.horizontalLayout_16.addWidget(self.radioButton_32)
        self.radioButton_34 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_34.setObjectName("radioButton_34")
        self.horizontalLayout_16.addWidget(self.radioButton_34)
        self.radioButton_37 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        self.radioButton_37.setObjectName("radioButton_37")
        self.horizontalLayout_16.addWidget(self.radioButton_37)
        self.verticalLayout_3.addLayout(self.horizontalLayout_16)
        self.gridLayout_2.addLayout(self.verticalLayout_3, 2, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.comboBox_2 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_2.setObjectName("comboBox_2")
        self.horizontalLayout.addWidget(self.comboBox_2)
        self.comboBox_3 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_3.setObjectName("comboBox_3")
        self.horizontalLayout.addWidget(self.comboBox_3)
        self.gridLayout_2.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 3, 0, 1, 1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        self.label_9 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_11.addWidget(self.label_9)
        self.comboBox_16 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_16.setObjectName("comboBox_16")
        self.horizontalLayout_11.addWidget(self.comboBox_16)
        self.comboBox_17 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_17.setObjectName("comboBox_17")
        self.horizontalLayout_11.addWidget(self.comboBox_17)
        self.comboBox_18 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_18.setObjectName("comboBox_18")
        self.horizontalLayout_11.addWidget(self.comboBox_18)
        self.verticalLayout_4.addLayout(self.horizontalLayout_11)
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.label_10 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_12.addWidget(self.label_10)
        self.comboBox_9 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_9.setObjectName("comboBox_9")
        self.horizontalLayout_12.addWidget(self.comboBox_9)
        self.comboBox_8 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_8.setObjectName("comboBox_8")
        self.horizontalLayout_12.addWidget(self.comboBox_8)
        self.comboBox_7 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_7.setObjectName("comboBox_7")
        self.horizontalLayout_12.addWidget(self.comboBox_7)
        self.verticalLayout_4.addLayout(self.horizontalLayout_12)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.label_11 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_13.addWidget(self.label_11)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem1)
        self.label_12 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_13.addWidget(self.label_12)
        self.comboBox_10 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_10.setObjectName("comboBox_10")
        self.horizontalLayout_13.addWidget(self.comboBox_10)
        self.label_13 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_13.setObjectName("label_13")
        self.horizontalLayout_13.addWidget(self.label_13)
        self.comboBox_11 = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.comboBox_11.setObjectName("comboBox_11")
        self.horizontalLayout_13.addWidget(self.comboBox_11)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_13)
        self.gridLayout_2.addLayout(self.verticalLayout_4, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout_2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem3)
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem4)
        self.backBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.backBtn.setObjectName("backBtn")
        self.horizontalLayout_14.addWidget(self.backBtn)
        self.label_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("../image/link_btns.png"))
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_14.addWidget(self.label_3)
        self.nextBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.nextBtn.setObjectName("nextBtn")
        self.horizontalLayout_14.addWidget(self.nextBtn)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_14.addItem(spacerItem5)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem6)
        self.endBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.endBtn.setStyleSheet("background-color: rgb(0,255,255)")
        self.endBtn.setObjectName("endBtn")
        self.horizontalLayout_7.addWidget(self.endBtn)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem7)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.label_6 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("../image/eclass_lower.png"))
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem9)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_2.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">業種</span></p></body></html>"))
        self.label_4.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">職種</span></p></body></html>"))
        self.radioButton.setText(_translate("Form", "北海道"))
        self.radioButton_2.setText(_translate("Form", "青森"))
        self.radioButton_3.setText(_translate("Form", "岩手"))
        self.radioButton_6.setText(_translate("Form", "宮城"))
        self.radioButton_5.setText(_translate("Form", "秋田"))
        self.radioButton_4.setText(_translate("Form", "山形"))
        self.radioButton_20.setText(_translate("Form", "茨城"))
        self.radioButton_19.setText(_translate("Form", "福島"))
        self.radioButton_21.setText(_translate("Form", "栃木"))
        self.radioButton_22.setText(_translate("Form", "群馬"))
        self.radioButton_13.setText(_translate("Form", "東京"))
        self.radioButton_23.setText(_translate("Form", "埼玉"))
        self.radioButton_24.setText(_translate("Form", "千葉"))
        self.radioButton_14.setText(_translate("Form", "神奈川"))
        self.radioButton_15.setText(_translate("Form", "新潟"))
        self.radioButton_16.setText(_translate("Form", "富山"))
        self.radioButton_17.setText(_translate("Form", "石川"))
        self.radioButton_25.setText(_translate("Form", "山梨"))
        self.radioButton_18.setText(_translate("Form", "福井"))
        self.radioButton_29.setText(_translate("Form", "愛知"))
        self.radioButton_28.setText(_translate("Form", "静岡"))
        self.radioButton_27.setText(_translate("Form", "岐阜"))
        self.radioButton_26.setText(_translate("Form", "長野"))
        self.radioButton_30.setText(_translate("Form", "三重"))
        self.radioButton_45.setText(_translate("Form", "石川"))
        self.radioButton_46.setText(_translate("Form", "山梨"))
        self.radioButton_47.setText(_translate("Form", "福井"))
        self.radioButton_48.setText(_translate("Form", "愛知"))
        self.radioButton_49.setText(_translate("Form", "静岡"))
        self.radioButton_50.setText(_translate("Form", "岐阜"))
        self.radioButton_51.setText(_translate("Form", "長野"))
        self.radioButton_52.setText(_translate("Form", "三重"))
        self.radioButton_53.setText(_translate("Form", "石川"))
        self.radioButton_54.setText(_translate("Form", "山梨"))
        self.radioButton_55.setText(_translate("Form", "福井"))
        self.radioButton_56.setText(_translate("Form", "愛知"))
        self.radioButton_57.setText(_translate("Form", "静岡"))
        self.radioButton_58.setText(_translate("Form", "岐阜"))
        self.radioButton_59.setText(_translate("Form", "長野"))
        self.radioButton_60.setText(_translate("Form", "三重"))
        self.radioButton_35.setText(_translate("Form", "愛知"))
        self.radioButton_36.setText(_translate("Form", "三重"))
        self.radioButton_7.setText(_translate("Form", "山梨"))
        self.radioButton_31.setText(_translate("Form", "山梨"))
        self.radioButton_32.setText(_translate("Form", "長野"))
        self.radioButton_34.setText(_translate("Form", "静岡"))
        self.radioButton_37.setText(_translate("Form", "岐阜"))
        self.label_5.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">希望勤務地</span></p></body></html>"))
        self.label_8.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">資格情報</span></p></body></html>"))
        self.label_9.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">一般</span></p></body></html>"))
        self.label_10.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">教職</span></p></body></html>"))
        self.label_11.setText(_translate("Form", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">語学</span></p></body></html>"))
        self.label_12.setText(_translate("Form", "TOEIC"))
        self.label_13.setText(_translate("Form", "TOEIC"))
        self.backBtn.setText(_translate("Form", "前へ"))
        self.nextBtn.setText(_translate("Form", "次へ"))
        self.endBtn.setText(_translate("Form", "診断終了"))

