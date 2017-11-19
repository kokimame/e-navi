import forms
from qt import *


class AdminEntry(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.adminEntry.Ui_Form()
        self.form.setupUi(self)
        self.form.dbBtn.clicked.connect(lambda: self.goPage("AdminFirm"))
        self.form.qaBtn.clicked.connect(lambda: self.goPage("AdminQA"))
        self.form.applyBtn.clicked.connect(lambda: self.mw.dm.open("PopupDialog", self.mw,
                                        msg="変更を適応しますか？", okTrigger=lambda: self.goPage("AdminFirm")))
        self.form.endBtn.clicked.connect(lambda: self.mw.dm.open("PopupDialog", self.mw,
                                        msg="終了しますか？", okTrigger=lambda: self.goPage("HomePage")))


    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)