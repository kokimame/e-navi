import sys


from qt import *
import forms

class EclassTop(QWidget):
    def __init__(self):
        super().__init__()
        self.initUi()
        self.show()

    def initUi(self):
        self.setupWidget()
        self.setupButton()

    def setupWidget(self):
        self.form = forms.eclassTop.Ui_topView()
        self.form.setupUi(self)


    def setupButton(self):
        form = self.form
        form.webmailBtn.clicked.connect\
            (lambda: print("'WebMail for PC' Button clicked"))
        form.webdiskBtn.clicked.connect\
            (lambda: print("'WebDisk for PC' Button clicked"))
        form.duetBtn.clicked.connect\
            (lambda: print("'Duet' Button clicked"))
        form.goGlobalBtn.clicked.connect\
            (lambda: print("'GoGlobal' Button clicked"))
        form.elearningBtn.clicked.connect\
            (lambda: print("'e-learning' Button clicked"))
        form.enaviBtn.clicked.connect\
            (lambda: print("This is the entry point for E-Navi"))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = EclassTop()
    app.exec_()
