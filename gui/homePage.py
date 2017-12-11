import forms
from qt import *

class HomePage(QWidget):
    def __init__(self, mw):
        super().__init__()
        self.mw = mw
        self.initUi()

    def initUi(self):
        self.form = forms.enaviHome.Ui_Form()
        self.form.setupUi(self)
        termLbl = QLabel(TERMS)
        termLbl.setStyleSheet("background-color: rgb(255,255,255);")
        self.form.verticalLayout_3.addWidget(termLbl)
        self.form.agreeBtn.clicked.connect(lambda: self.goPage("EntryPage"))
        self.form.disagreeBtn.clicked.connect(lambda: self.goPage("EclassTop"))
        self.form.adminBtn.clicked.connect(lambda: self.goPage("AdminQA"))

    def goPage(self, pageName):
        self.mw.pm.setPage(pageName)

TERMS = '<html><head/><body><p><span style=" font-size:24pt; font-weight:600;">利用規約について</span></p>' \
        '<p>MASK（以下「弊社」と言います．）が提供するアンケートシステム「e-navi」（以下「本サイト」</p>' \
        '<p>と言います．）の利用について，以下の通り本規約を定めます．<br/></p>' \
        '<p><br/><span style=" font-size:15pt; font-weight:bold;">第1 条 本規約の範囲</span></p>' \
        '<p>本規約は本サイトが提供するサービスについて規定したものです．</p>' \
        '<p>なお本サイトは本規約の他にe-classに関する利用規約にも準ずるものとします．</p>' \
        '<p><br/><span style=" font-size:15pt; font-weight:bold;">第2条 利用者の範囲</span></p>' \
        '<p>本サイトを利用できるのは，同志社大学に所属する全ての学生とします．</p>' \
        '<p>またシステムの管理者としてキャリアセンター職員並びにITサポートオフィス職員を含みますが</p>' \
        '<p>利用者には含みません．</p>' \
        '<p><br/><span style=" font-size:15pt; font-weight:bold;">第3条 個人情報の取り扱い</span></p>' \
        '<p>本サイトを利用する際に使用する個人情報は以下のように取り扱います．利用者様が弊社に個人</p>' \
        '<p>情報をご提供下さる際には，以下の取り扱いについてご同意下さいますようよろしくお願い申し</p>' \
        '<p>あげます．<\p>' \
        '<p>1.個人情報の使用目的</p><p>（１）性格分析</p><p>（２）スキル診断</p>' \
        '<p>（３）適性企業の提示</p>' \
        '<p>2.上記の個人情報を弊社が第3者に開示，漏洩することはございません．ただし，以下の場合は</p>' \
        '<p>この限りではございませんので，あらかじめご了承ください．</p>' \
        '<p>（１）法令に基づき裁判所その他司法機関及び行政機関から利用者様に関する情報の開示を要求さ</p><' \
        'p>れた場合</p><p>（２）弊社並びに同志社大学様，利用者様の権利および財産を保護する必要がある場合</p>' \
        '<p><br/><span style=" font-size:15pt; font-weight:bold;">第4条 規約の変更</span></p>' \
        '<p>弊社は，利用者様への事前通知，承諾なしに本規約を随時変更することができる者とします．</p>' \
        '<p>変更内容については，本サイト上に1ヶ月表示した時点で，全ての利用者様が了承したものと</p>' \
        '<p>みなします．ただし，第3者に不利益を及ぼす恐れのある場合等不足の事態が予想される場合は，</p>' \
        '<p>上記機関を待たずに規約変更が実施されたものとします．</p>' \
        '<p><br/><span style=" font-size:15pt; font-weight:bold;">第5条 サービスの中断，停止</span></p>' \
        '<p>1.弊社は，以下に該当する場合，利用者への事前通知，承諾なしに，弊社のサービス内容の</p>' \
        '<p>一部または，全てを停止または中断する場合があります．</p>' \
        '<p>（１）本サイトの定期保守，更新並びに緊急事態発生の場合</p>' \
        '<p>（２）火災，停電，天災等の不可抗力その他不足の事態により，本サイト運営継続が困難</p>' \
        '<p>になった場合<\p>' \
        '<p>2.上記事態などに伴い，利用者様に不利益，損害が生じた場合であっても，弊社はその責任を</p>' \
        '<p>免れるものとします．</p>' \
        '<p><br/><span style=" font-size:15pt; font-weight:bold;">第6条 サービスの内容の変更，中止</span></p>' \
        '<p>1.弊社は，利用者様への事前通知，承諾なしに本サイトのサービス内容を変更，または中止</p>' \
        '<p>する場合があります．</p>' \
        '<p>2.前項に基づき，サービス内容を変更・中止した場合といえども弊社はその責任を免れるもの</p>' \
        '<p>とします．<\p>' \
        '<p><br/><span style=" font-size:15pt; font-weight:bold;">第7条 サービスの停止</span></p>' \
        '<p>弊社は，一定の予告期間をもって本サイトのサービス停止を行う場合があります．</p>' \
        '<p><br/><span style=" font-size:15pt; font-weight:bold;">第8条 免責</span></p>' \
        '<p>1. 弊社は，理由の如何を問わず本サイトのサービス提供が遅延し，又は中断したことに起因して</p>' \
        '<p>利用者様又は第3者が被った被害について，一切の責任を追わないものとします．</p>' \
        '<p>2.弊社は，本サイトのサービスの利用を通じて得た情報等の正確性，特定の目的への適合性等</p>' \
        '<p>について，一切の責任を負わないものとします．</p>' \
        '<p>3.弊社は，本サイトのサービスの利用を通じて得た情報等に起因して損害が生じた場合一切の</p>' \
        '<p>責任を負わないものとします．</p>' \
        '<p>4.本サイトを通じて提供される情報・サービスに関し、利用者様と他の利用者様あるいは第三者</p>' \
        '<p>と紛争が生じた場合は、利用者様は、自己の費用と責任においてこれを解決するものとし、</p>' \
        '<p>弊社に損害を与えないものとします。</p>' \
        '<p><br/><span style=" font-size:15pt; font-weight:bold;">第9条 合意管轄</span></p>' \
        '<p>本サイトに関して，弊社と利用者様との間，訴訟の必要性が生じた場合は京都地方裁判所を</p>' \
        '<p>専属的合意管轄裁判所とします．</p>' \
        '<p><br/><span style=" font-size:15pt; font-weight:bold;">第10条 準拠法</span></p>' \
        '<p>本規約の成立，効力，履行および解釈に関しては日本法が適用されるものとします．</p>' \
        '<p>以上</p><p>平成29年12月11日制定</p></body></html>'