import forms
from qt import *

class HomePage(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.enaviHome.Ui_Form()
        self.form.setupUi(self)
        self.form.startBtn.clicked.connect(self.goNextPage)

    def goNextPage(self):
        self.mw.pageStack.append(1)
        self.mw.pages.setCurrentIndex(4)