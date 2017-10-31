import forms
from qt import *


class AdminFirm(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.adminFirm.Ui_Form()
        self.form.setupUi(self)
        self.form.dbBtn.clicked.connect(lambda: self.goPage("AdminQA"))
        self.form.applyBtn.clicked.connect(lambda: self.mw.dm.open("PopupDialog", self.mw,
                                        msg="変更を適応しますか？"))
        self.form.endBtn.clicked.connect(lambda: self.mw.dm.open("PopupDialog", self.mw,
                                        msg="終了しますか？"))
        self.setupTable()

    def setupTable(self):
        table = self.form.firmTable
        table.setColumnCount(4)
        table.setColumnWidth(0, 30)
        table.setColumnWidth(1, 300)
        table.setColumnWidth(2, 220)
        table.setColumnWidth(3, 140)
        table.verticalHeader().setVisible(False)
        table.setRowCount(100)

    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)