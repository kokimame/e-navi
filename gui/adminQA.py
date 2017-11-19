import forms
from qt import *


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
        table.setColumnWidth(0, 550)
        table.setColumnWidth(1, 110)
        table.setRowCount(100)

        for i in range(100):
            table.setItem(i, 0, QTableWidgetItem("質問" + str(i+1) + "の内容"))
            table.setItem(i, 1, QTableWidgetItem("質問" + str(i+1) + "の配点"))

    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)