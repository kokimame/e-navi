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

    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)