from qt import *
import forms

class PopupDialog(QDialog):
    def __init__(self, mw):
        QDialog.__init__(self, mw, Qt.Window)
        self.mw = mw
        self.form = forms.popupDialog.Ui_PopupDialog()
        self.form.setupUi(self)
        self.initUi()
        self.show()

    def reject(self):
        self.done(0)
        mw.dm.close("Preferences")