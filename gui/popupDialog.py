from qt import *
import forms

class PopupDialog(QDialog):
    def __init__(self, mw, *args, **kwargs):
        QDialog.__init__(self, mw, Qt.Window)
        self.mw = mw
        self.kwargs = kwargs
        self.form = forms.popupDialog.Ui_PopupDialog()
        self.form.setupUi(self)
        self.form.cancelBtn.clicked.connect(self.reject)
        if "msg" in kwargs:
            self.form.msgLabel.setText(kwargs["msg"])
        self.form.okBtn.clicked.connect(self.okTrigger)

        self.show()

    def okTrigger(self):
        if "okTrigger" in self.kwargs:
            self.kwargs["okTrigger"]()
        self.reject()

    def reject(self):
        self.done(0)
        self.mw.dm.close("PopupDialog")