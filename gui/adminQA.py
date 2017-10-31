import forms
from qt import *


class AdminQA(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.adminQA.Ui_Form()
        self.form.setupUi(self)
        self.form.dbBtn.clicked.connect(lambda: self.goPage("AdminFirm"))
        self.form.applyBtn.clicked.connect(lambda: self.mw.dm.open("PopupDialog", self.mw,
                                        msg="変更を適応しますか？"))
        self.form.endBtn.clicked.connect(lambda: self.mw.dm.open("PopupDialog", self.mw,
                                        msg="終了しますか？"))

    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)