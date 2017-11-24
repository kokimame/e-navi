import forms
from qt import *
from adminQA import AttrBox

class LblAttr(QWidget):
    def __init__(self, label):
        super(LblAttr, self).__init__()
        vbox = QVBoxLayout()
        vbox.addWidget(QLabel(label))
        vbox.addWidget(AttrBox())
        self.setLayout(vbox)

class AdminEntry(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.form = forms.adminEntry.Ui_Form()
        self.form.setupUi(self)
        self.setupButtons()
        self.setupLists()

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

    def setupLists(self):
        form = self.form

        # Field list -------
        fieldLbl = ["農業，林業", "漁業", "鉱業，採石業，砂利採取業", "建設業", "製造業", "電気・ガス・熱供給・水道業",
                    "情報通信業", "運輸業・郵便業", "卸売業，小売業", "金融業，保険業", "不動産業，物品賃貸業",
                    "学術研究，専門・技術サービス業", "宿泊業，飲食サービス業", "生活関連サービス業，娯楽業",
                    "教育，学習支援業", "医療，福祉","複合サービス事業", "サービス業", "公務"]
        form.fieldList.setStyleSheet("""
                            QListWidget::item { border-bottom: 1px solid black; }
                            QListWidget::item:selected { background: rgba(0,255,255,30); }
                           """)
        for lbl in fieldLbl:
            lwi = QListWidgetItem()
            la = LblAttr(lbl)
            lwi.setSizeHint(la.sizeHint())
            form.fieldList.addItem(lwi)
            form.fieldList.setItemWidget(lwi, la)

        # Job list -------
        jobLbl = ["営業職","企画管理","事務・アシスタント","販売・サービス職","コンサル・専門事務所","金融系専門職",
                  "公務員・教員・農林水産関連職","技術職","医療系専門職","クリエイター・クリエイティブ職"]
        form.jobList.setStyleSheet("""
                            QListWidget::item { border-bottom: 1px solid black; }
                            QListWidget::item:selected { background: rgba(0,255,255,30); }
                           """)
        for lbl in jobLbl:
            lwi = QListWidgetItem()
            la = LblAttr(lbl)
            lwi.setSizeHint(la.sizeHint())
            form.jobList.addItem(lwi)
            form.jobList.setItemWidget(lwi, la)

        # General certification list -------
        genLbl = ["基本情報処理技術者","応用情報処理技術者","行政書士","司法書士",
                  "社会保険労務士","宅件建物取引士","簿記3級","簿記2級","介護福祉士","気象予報士"]
        form.generalList.setStyleSheet("""
                            QListWidget::item { border-bottom: 1px solid black; }
                            QListWidget::item:selected { background: rgba(0,255,255,30); }
                           """)
        for lbl in genLbl:
            lwi = QListWidgetItem()
            la = LblAttr(lbl)
            lwi.setSizeHint(la.sizeHint())
            form.generalList.addItem(lwi)
            form.generalList.setItemWidget(lwi, la)

        # Teaching certification list -----
        teachLbl = ["教員免許高一種","教員免許中一種","教員免許小一種","教員免許幼一種","養護教諭一種"]
        form.teachList.setStyleSheet("""
                            QListWidget::item { border-bottom: 1px solid black; }
                            QListWidget::item:selected { background: rgba(0,255,255,30); }
                           """)
        for lbl in teachLbl:
            lwi = QListWidgetItem()
            la = LblAttr(lbl)
            lwi.setSizeHint(la.sizeHint())
            form.teachList.addItem(lwi)
            form.teachList.setItemWidget(lwi, la)


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