import forms
from qt import *
from adminQA import AttrBox


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
        table.setColumnCount(4)
        table.setColumnWidth(0, 30)
        table.setColumnWidth(1, 280)
        table.setColumnWidth(2, 140)
        table.setColumnWidth(3, 240)
        table.verticalHeader().setVisible(False)
        table.setRowCount(100)

        for i in range(100):
            table.setRowHeight(i, 50)
            table.setItem(i, 0, QTableWidgetItem("x"))
            table.setItem(i, 1, QTableWidgetItem("企業" + str(i+1) + "の名前"))
            table.setItem(i, 2, QTableWidgetItem("企業" + str(i+1) + "の所在地"))
            table.setCellWidget(i, 3, AttrBox())

    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)