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

Q_SAMPLE = ["自分と周囲とのバランスを大切にする．",
            "つい自分の中の世界に浸りがちになる．",
            "楽観的すぎて問題になることがある．",
            "冷静沈着で合理的な人と思われる．",
            "気持ちを発散したら，気がおさまる．",
            "欲しいものは遠慮せず確実に手に入れたい．",
            "いつもいろいろな可能性を探している．",
            "人に頼らなければならない状況は好まない．",
            "用心深く，心配事が多い",
            "個性的であることは何よりも大切だと思う",]

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
        [table.setItem(i, 0, QTableWidgetItem(Q_SAMPLE[i])) for i in range(10)]

        [table.setCellWidget(i, 1, AnswerBox()) for i in range(10)]


    def goPage(self, pageName):
        if not self.form.unfillLbl.isVisible():
            # Show up the label and stay at the page only once
            self.form.unfillLbl.setVisible(True)
            return
        self.mw.pm.setPage(pageName)