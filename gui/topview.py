import sys

import forms
from qt import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.pageStack = []
        self.pages = QStackedLayout()
        self.pages.addWidget(EclassTop(self))
        self.pages.addWidget(EnaviPage(self))
        self.pages.addWidget(EnaviStart(self))
        self.pages.addWidget(EnaviEnd(self))
        self.pages.setCurrentIndex(0)
        cw = QWidget()
        cw.setLayout(self.pages)

        self.setupMenu()
        self.setGeometry(0,0,720,921)
        self.setCentralWidget(cw)
        self.center()
        self.show()

    def setupMenu(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        editMenu = menubar.addMenu('&Edit')

        undoAction = QAction('&Undo', self)
        undoAction.setShortcut('Ctrl+Z')
        undoAction.triggered.connect(self.undo)
        editMenu.addAction(undoAction)

    def undo(self):
        if len(self.pageStack) == 0: return
        prev = self.pageStack.pop()
        self.pages.setCurrentIndex(prev)

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


class EnaviPage(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.enaviPage.Ui_Form()
        self.form.setupUi(self)
        self.form.startBtn.clicked.connect(self.goNextPage)

    def goNextPage(self):
        self.mw.pageStack.append(1)
        self.mw.pages.setCurrentIndex(2)

class EnaviStart(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.enaviStart.Ui_Form()
        self.form.setupUi(self)
        self.form.endBtn.clicked.connect(self.goNextPage)

    def goNextPage(self):
        self.mw.pageStack.append(2)
        self.mw.pages.setCurrentIndex(3)


class EnaviEnd(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.enaviEnd.Ui_Form()
        self.form.setupUi(self)
        self.form.homeBtn.clicked.connect(self.goNextPage)

    def goNextPage(self):
        self.mw.pageStack.append(3)
        self.mw.pages.setCurrentIndex(1)



class EclassTop(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.eclassTop.Ui_topView()
        self.form.setupUi(self)
        self.setupButton()

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
            (self.goNextPage)

    def goNextPage(self):
        self.mw.pageStack.append(0)
        self.mw.pages.setCurrentIndex(1)


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = MainWindow()
    app.exec_()
