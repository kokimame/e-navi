import forms
from qt import *
from adminQA import AttrBox

FIELDLBL = ["---", "農業，林業", "漁業", "鉱業，採石業", "建設業", "製造業", "電気・ガス・熱供給",
            "情報通信業", "運輸業・郵便業", "卸売業，小売業", "金融業，保険業", "不動産業，物品賃貸業",
            "学術研究，専門業", "宿泊業，飲食サービス業", "生活サービス業，娯楽業",
            "教育，学習支援業", "医療，福祉", "複合サービス事業", "サービス業", "公務"]

JOBLBL = ["---", "営業職","企画管理","アシスタント","販売・サービス職","コンサル・専門事務所","金融系専門職",
                  "公務員・教員","技術職","医療系専門職","クリエイティブ職"]

# General certification list -------
GENLBL = ["---", "基本情報情報処理技術者","応用情報処理情報技術者","行政書士","司法書士",
                  "社会保険労務士","宅件建物取引士","簿記3級","簿記2級","介護福祉士","気象予報士"]


# Teaching certification list -----
TEACHLBL = ["---", "教員免許高一種","教員免許中一種","教員免許小一種","教員免許幼一種","養護教諭一種"]


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
                                        msg="変更を適応しますか？", okTrigger=lambda: self.goPage("AdminEntry")))
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

        for lbl in FIELDLBL:
            lwi = QListWidgetItem(lbl)
            form.fieldList.addItem(lwi)

        # Job list -------

        for lbl in JOBLBL:
            lwi = QListWidgetItem(lbl)
            form.jobList.addItem(lwi)

        for lbl in GENLBL:
            lwi = QListWidgetItem(lbl)
            form.generalList.addItem(lwi)

        for lbl in TEACHLBL:
            lwi = QListWidgetItem(lbl)
            form.teachList.addItem(lwi)


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
