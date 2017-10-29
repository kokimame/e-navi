import forms
from qt import *


class InputPage(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.enaviInput.Ui_Form()
        self.form.setupUi(self)
        self.setupTable()
        self.form.endBtn.clicked.connect(self.goNextPage)

    def setupTable(self):
        table = self.form.qaTable
        table.setRowCount(10)
        table.setColumnWidth(0, 340)
        table.setColumnWidth(1, 340)
        [table.setItem(i, 0,
                QTableWidgetItem("これは " + str(i+1) + "番目の質問です")) for i in range(10)]


    def goNextPage(self):
        self.mw.pageStack.append(2)
        self.mw.pages.setCurrentIndex(3)