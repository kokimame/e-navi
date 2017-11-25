import random

import forms
from qt import *
from adminEntry import FIELDLBL, JOBLBL


class FirmAttr(QWidget):
    class MySpin(QSpinBox):
        def __init__(self, val=None):
            QSpinBox.__init__(self)

            if val != None:
                self.setValue(val)
            else:
                self.setValue(random.randint(1, 4))

    def __init__(self):
        super(FirmAttr, self).__init__()
        hbox = QHBoxLayout()
        hbox.addWidget(self.MySpin())
        hbox.addWidget(self.MySpin())
        lastTwo = random.choice([[0,0],[random.randint(1,4),0],[random.randint(1,4),random.randint(1,4)]])
        hbox.addWidget(self.MySpin(val=lastTwo[0]))
        hbox.addWidget(self.MySpin(val=lastTwo[1]))
        self.setLayout(hbox)

class LblCombo(QComboBox):
    def __init__(self, labels):
        QComboBox.__init__(self)
        self.addItems(labels)
        self.setCurrentText(random.choice(labels))
        self.setStyleSheet("QComboBox::item { background-color: rgb(200, 200, 200); }")

class AdminFirm(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.adminFirm.Ui_Form()
        self.form.setupUi(self)
        self.form.qaBtn.clicked.connect(lambda: self.goPage("AdminQA"))
        self.form.entryBtn.clicked.connect(lambda: self.goPage("AdminEntry"))

        self.form.applyBtn.clicked.connect(lambda: self.mw.dm.open("PopupDialog", self.mw,
                                        msg="変更を適応しますか？", okTrigger=lambda: self.goPage("AdminFirm")))
        self.form.endBtn.clicked.connect(lambda: self.mw.dm.open("PopupDialog", self.mw,
                                        msg="終了しますか？", okTrigger=lambda: self.goPage("HomePage")))
        self.setupTable()

    def setupTable(self):
        table = self.form.firmTable
        table.setColumnCount(5)
        table.setColumnWidth(0, 280)    # Company name
        table.setColumnWidth(1, 140)    # Location
        table.setColumnWidth(2, 200)    # attribute for personality test
        table.setColumnWidth(3, 150)     # Industry type
        table.setColumnWidth(4, 150)     # Job type

        firmN = 50
        table.setRowCount(firmN)

        for i in range(firmN):
            table.setRowHeight(i, 50)
            table.setItem(i, 0, QTableWidgetItem("企業" + str(i+1) + "の名前"))
            table.setItem(i, 1, QTableWidgetItem("企業" + str(i+1) + "の所在地"))
            table.setCellWidget(i, 2, FirmAttr())
            table.setCellWidget(i, 3, LblCombo(FIELDLBL))
            table.setCellWidget(i, 4, LblCombo(JOBLBL))

    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)