import forms
from qt import *


class EntryPage(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.enaviEntry.Ui_Form()
        self.form.setupUi(self)
        self.form.nextBtn.clicked.connect(lambda: self.goPage("InputPage"))
        self.form.endBtn.clicked.connect(lambda: self.goPage("HomePage"))
        # self.setupTable()

    def setupTable(self):
        table = self.form.ebtryTable
        table.setRowCount(3)
        table.setColumnCount(2)
        table.horizontalHeader().setVisible(False)
        table.setColumnWidth(0, 340)
        table.setColumnWidth(1, 340)
        table.setItem(0, 0, QTableWidgetItem("業種"))
        table.setItem(1, 0, QTableWidgetItem("職種"))


    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)