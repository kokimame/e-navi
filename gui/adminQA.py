import forms
from qt import *
from random import randint


class AttrBox(QWidget):
    class MySpin(QSpinBox):
        def __init__(self):
            QSpinBox.__init__(self)
            self.setValue(randint(0, 99))

    def __init__(self):
        super(AttrBox, self).__init__()
        hbox = QHBoxLayout()
        hbox.addWidget(self.MySpin())
        hbox.addWidget(self.MySpin())
        hbox.addWidget(self.MySpin())
        hbox.addWidget(self.MySpin())
        self.setLayout(hbox)


class AdminQA(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.adminQA.Ui_Form()
        self.form.setupUi(self)
        self.form.dbBtn.clicked.connect(lambda: self.goPage("AdminFirm"))
        self.form.entryBtn.clicked.connect(lambda: self.goPage("AdminEntry"))
        self.form.applyBtn.clicked.connect(lambda: self.mw.dm.open("PopupDialog", self.mw,
                                        msg="変更を適応しますか？", okTrigger=lambda: self.goPage("AdminQA")))
        self.form.endBtn.clicked.connect(lambda: self.mw.dm.open("PopupDialog", self.mw,
                                        msg="終了しますか？", okTrigger=lambda: self.goPage("HomePage")))
        self.setupTable()

    def setupTable(self):
        table = self.form.QAeditTable
        table.setColumnCount(2)
        table.setColumnWidth(0, 450)
        table.setColumnWidth(1, 210)
        table.setRowCount(90)

        for i in range(90):
            table.setRowHeight(i, 50)
            table.setItem(i, 0, QTableWidgetItem("質問" + str(i+1) + "の内容"))
            table.setCellWidget(i, 1, AttrBox())

    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)