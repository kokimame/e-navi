import forms
from qt import *
from adminEntry import FIELDLBL, JOBLBL, GENLBL, TEACHLBL

class EntryPage(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.form = forms.enaviEntry.Ui_Form()
        self.form.setupUi(self)
        self.setupButton()
        self.setupCombo()

    def setupButton(self):
        form = self.form
        form.unfillLbl.setVisible(False)
        form.nextBtn.clicked.connect(lambda: self.goPage("InputPage"))
        form.endBtn.clicked.connect(lambda: self.goPage("HomePage"))
       
    def setupCombo(self):
        form = self.form
        form.fieldCombo1.addItems(FIELDLBL)
        form.fieldCombo2.addItems(FIELDLBL)
        form.fieldCombo3.addItems(FIELDLBL)
        form.jobCombo1.addItems(JOBLBL)
        form.jobCombo2.addItems(JOBLBL)
        form.jobCombo3.addItems(JOBLBL)
        form.genCombo1.addItems(GENLBL)
        form.genCombo2.addItems(GENLBL)
        form.genCombo3.addItems(GENLBL)
        form.teachCombo1.addItems(TEACHLBL)
        form.teachCombo2.addItems(TEACHLBL)
        form.teachCombo3.addItems(TEACHLBL)

        form.toeflCombo.addItem('---')
        form.toeicCombo.addItem('---')
        form.toeicCombo.addItems(['%d' % i for i in range(991)])
        form.toeflCombo.addItems(['%d' % i for i in range(121)])


    def goPage(self, pageName):
        if not self.form.unfillLbl.isVisible():
            # Show up the label and stay at the page only once
            self.form.unfillLbl.setVisible(True)
            return
        self.mw.pm.setPage(pageName)
