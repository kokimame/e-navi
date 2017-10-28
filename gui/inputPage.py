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
        self.form.endBtn.clicked.connect(self.goNextPage)

    def goNextPage(self):
        self.mw.pageStack.append(2)
        self.mw.pages.setCurrentIndex(3)