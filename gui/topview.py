import sys

import forms
from qt import *
from homePage import HomePage
from entryPage import EntryPage
from inputPage import InputPage
from outputPage import OutputPage

class PageManager:
    # { "Name Reference to the page": (PageClass, index in stacked layout)}
    PAGES = {"EclassTop": (EclassTop, 0),
             "HomePage": (HomePage, 1),
             "EntryPage": (EntryPage, 2),
             "InputPage": (InputPage, 3),
             "OutputPage": (OutputPage, 4)}

    def __init__(self):
        self.pages = QStackedLayout()
        self.pageHistory = []
        for pval in PageManager.PAGES.values():
            self.pages.addWidget(pval[0])

    def setPage(self, pageName):
        self.pageHistory.append(self.pages.currentIndex())
        self.pages.setCurrentIndex(PageManager.PAGES[pageName][1])


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.pageStack = []

        # TODO: Make a Page Manager
        # and reference each of pages by its name not a number(index)
        self.pages = QStackedLayout()
        self.pages.addWidget(EclassTop(self))   # 0
        self.pages.addWidget(HomePage(self))    # 1
        self.pages.addWidget(InputPage(self))   # 2
        self.pages.addWidget(OutputPage(self))  # 3
        self.pages.addWidget(EntryPage(self))   # 4
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
