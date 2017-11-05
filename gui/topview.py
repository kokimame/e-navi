import sys

from qt import *
from eclassTop import EclassTop
from homePage import HomePage
from entryPage import EntryPage
from inputPage import InputPage
from outputPage import OutputPage
from popupDialog import PopupDialog
from adminFirm import AdminFirm
from adminQA import AdminQA

class PageManager:
    # { "Name Reference to the page": (PageClass, index in stacked layout)}
    # Note: Store pages in order of alphabet
    PAGES = {"AdminFirm": (AdminFirm, 0),
             "AdminQA": (AdminQA, 1),
             "EclassTop": (EclassTop, 2),
             "EntryPage": (EntryPage, 3),
             "HomePage": (HomePage, 4),
             "InputPage": (InputPage, 5),
             "OutputPage": (OutputPage, 6)}

    def __init__(self, mw):
        self.mw = mw
        self.pages = QStackedLayout()
        self.pageHistory = []
        for pkey in sorted(PageManager.PAGES.keys()):
            self.pages.addWidget(PageManager.PAGES[pkey][0](self.mw))

    def setPage(self, pageName):
        self.pageHistory.append(self.pages.currentIndex())
        self.pages.setCurrentIndex(PageManager.PAGES[pageName][1])

    def undo(self):
        if len(self.pageHistory) == 0: return
        prev = self.pageHistory.pop()
        self.pages.setCurrentIndex(prev)

class DialogManager:
    _dialogs = {
        "PopupDialog": [PopupDialog, None],
    }

    def open(self, name, *args, **kargs):
        (creator, instance) = self._dialogs[name]
        if instance:
            instance.setWindowState(Qt.WindowNoState)
            instance.activateWindow()
            instance.raise_()
            return instance
        else: # if Dialog instace is new
            instance = creator(*args, **kargs)
            # Remember the newly created instance
            self._dialogs[name][1] = instance
            return instance

    def close(self, name):
        self._dialogs[name] = [self._dialogs[name][0], None]


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.pm = PageManager(self)
        self.pm.setPage("EclassTop")
        self.dm = DialogManager()

        cw = QWidget()
        cw.setLayout(self.pm.pages)

        self.setupMenu()
        self.setGeometry(0,0,720,921)
        self.setCentralWidget(cw)
        self.setWindowTitle("e-navi プロトタイプ")
        self.center()
        self.show()

    def setupMenu(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&ファイル')
        editMenu = menubar.addMenu('&編集')

        undoAction = QAction('&戻る', self)
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
