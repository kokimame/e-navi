import sys

import forms
from qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pages = QStackedLayout()
        self.pages.addWidget(EclassTop(self))
        self.pages.addWidget(EnaviPage(self))
        self.pages.setCurrentIndex(0)
        self.setLayout(self.pages)


class EnaviPage(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()
        self.center()

    def initUi(self):
        self.form = forms.enaviPage.Ui_Form()
        self.form.setupUi(self)
        self.form.backBtn.clicked.connect(lambda: self.mw.pages.setCurrentIndex(0))

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())




class EclassTop(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()
        self.center()

    def initUi(self):
        self.form = forms.eclassTop.Ui_topView()
        self.form.setupUi(self)
        self.setupButton()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

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
            (lambda: self.mw.pages.setCurrentIndex(1))

if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = MainWindow()
    app.exec_()
