import forms
from qt import *


class OutputPage(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.enaviOutput.Ui_Form()
        self.form.setupUi(self)
        self.form.homeBtn.clicked.connect(lambda: self.goPage("HomePage"))

    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)

