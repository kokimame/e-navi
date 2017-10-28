import forms
from qt import *


class OutputPage(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.enaviOutpu.Ui_Form()
        self.form.setupUi(self)
        self.form.homeBtn.clicked.connect(self.goNextPage)

    def goNextPage(self):
        self.mw.pageStack.append(3)
        self.mw.pages.setCurrentIndex(1)

