import forms
from qt import *


class AdminEntry(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.form = forms.adminEntry.Ui_Form()
        self.form.setupUi(self)
        self.setupButtons()

    def setupButtons(self):
        form = self.form
        form.dbBtn.clicked.connect(lambda: self.goPage("AdminFirm"))
        form.qaBtn.clicked.connect(lambda: self.goPage("AdminQA"))
        form.applyBtn.clicked.connect(lambda: self.mw.dm.open("PopupDialog", self.mw,
                                        msg="変更を適応しますか？", okTrigger=lambda: self.goPage("AdminFirm")))
        form.endBtn.clicked.connect(lambda: self.mw.dm.open("PopupDialog", self.mw,
                                        msg="終了しますか？", okTrigger=lambda: self.goPage("HomePage")))
        form.fieldDelBtn.clicked.connect(lambda: self.deleteListWidgetItem(form.fieldList))
        form.jobDelBtn.clicked.connect(lambda: self.deleteListWidgetItem(form.jobList))
        form.genDelBtn.clicked.connect(lambda: self.deleteListWidgetItem(form.generalList))
        form.teachDelBtn.clicked.connect(lambda: self.deleteListWidgetItem(form.teachList))

        form.fieldAddBtn.clicked.connect(lambda: self.addLineEdit(form.fieldList))
        form.jobAddBtn.clicked.connect(lambda: self.addLineEdit(form.jobList))
        form.genAddBtn.clicked.connect(lambda: self.addLineEdit(form.generalList))
        form.teachAddBtn.clicked.connect(lambda: self.addLineEdit(form.teachList))

    def deleteListWidgetItem(self, list):
        if len(list.selectedItems()) == 0:
            return

        for item in list.selectedItems():
            for i in range(list.count()):
                if list.item(i) == item:
                    list.takeItem(i)
                    break

        list.repaint()

    def addLineEdit(self, list):
        lwi = QListWidgetItem()
        list.addItem(lwi)
        list.setItemWidget(lwi, QLineEdit())
        list.repaint()






    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)