import sys

import forms
from qt import *
from eclassTop import EclassTop
from homePage import HomePage
from entryPage import EntryPage
from inputPage import InputPage
from outputPage import OutputPage

class PageManager:
    # { "Name Reference to the page": (PageClass, index in stacked layout)}
    # Note: Store pages in order of alphabet
    PAGES = {"EclassTop": (EclassTop, 0),
             "EntryPage": (EntryPage, 1),
             "HomePage": (HomePage, 2),
             "InputPage": (InputPage, 3),
             "OutputPage": (OutputPage, 4)}

    def __init__(self, mw):
        self.mw = mw
        self.pages = QStackedLayout()
        self.pageHistory = []
        for pkey in sorted(PageManager.PAGES.keys()):
            print(pkey)
            self.pages.addWidget(PageManager.PAGES[pkey][0](self.mw))

    def setPage(self, pageName):
        self.pageHistory.append(self.pages.currentIndex())
        self.pages.setCurrentIndex(PageManager.PAGES[pageName][1])

    def undo(self):
        if len(self.pageHistory) == 0: return
        prev = self.pageHistory.pop()
        self.pages.setCurrentIndex(prev)


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.pm = PageManager(self)
        self.pm.setPage("EclassTop")

        cw = QWidget()
        cw.setLayout(self.pm.pages)

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
        self.pm.undo()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == "__main__":
    app = QApplication(sys.argv)

    mw = MainWindow()
    app.exec_()
