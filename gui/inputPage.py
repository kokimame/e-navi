import forms
from qt import *

class AnswerBox(QWidget):
    def __init__(self):
        super(AnswerBox, self).__init__()
        hbox = QHBoxLayout()
        hbox.addWidget(QRadioButton("4"))
        hbox.addWidget(QRadioButton("3"))
        hbox.addWidget(QRadioButton("2"))
        hbox.addWidget(QRadioButton("1"))
        self.setLayout(hbox)



class InputPage(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.enaviInput.Ui_Form()
        self.form.setupUi(self)
        self.form.unfillLbl.setVisible(False)
        self.setupTable()
        self.form.nextBtn.clicked.connect(lambda: print("Move to the next QA page"))
        self.form.backBtn.clicked.connect(lambda: self.goPage("EntryPage"))
        self.form.endBtn.clicked.connect(lambda: self.goPage("OutputPage"))

    def setupTable(self):
        table = self.form.qaTable
        table.setSelectionMode(QAbstractItemView.NoSelection)
        table.setRowCount(10)
        table.setColumnWidth(0, 340)
        table.setColumnWidth(1, 340)
        [table.setItem(i, 0,
                QTableWidgetItem("これは " + str(i+1) + "番目の質問です")) for i in range(10)]

        [table.setCellWidget(i, 1, AnswerBox()) for i in range(10)]


    def goPage(self, pageName):
        if not self.form.unfillLbl.isVisible():
            self.form.unfillLbl.setVisible(True)
            return
        self.mw.pm.setPage(pageName)