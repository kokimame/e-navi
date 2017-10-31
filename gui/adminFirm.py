import forms
from qt import *


class AdminFirm(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.adminFirm.Ui_Form()
        self.form.setupUi(self)
        self.form.dbBtn.clicked.connect(lambda: self.goPage("AdminQA"))

    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)