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
        self.form.nextBtn.clicked.connect(self.goNextPage)

    def goNextPage(self):
        self.mw.pageStack.append(4)
        self.mw.pages.setCurrentIndex(2)

    def goToEnd(self):
        self.mw.pageStack.append(4)
        self.mw.pages.setCurrentIndex(1)