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
        self.form.agreeBtn.clicked.connect(lambda: self.goPage("EntryPage"))
        self.form.disagreeBtn.clicked.connect(lambda: self.goPage("EclassTop"))
        self.form.adminBtn.clicked.connect(lambda: self.goPage("AdminQA"))

    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)