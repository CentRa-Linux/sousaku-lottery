# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sousaku-software.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
import os
import datetime
from PyQt5 import QtCore, QtGui, QtWidgets
import lottery
import pyperclip
import multiprocessing
import time


class Ui_MainWindow(object):
    fn = ""

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(832, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.fplabel = QtWidgets.QLabel(self.centralwidget)
        self.fplabel.setObjectName("fplabel")
        self.verticalLayout_2.addWidget(self.fplabel)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        self.fpline = QtWidgets.QLineEdit(self.centralwidget)
        self.fpline.setObjectName("fpline")
        self.fpline.setReadOnly(True)
        self.horizontalLayout_3.addWidget(self.fpline)
        self.fpexp = QtWidgets.QPushButton(self.centralwidget)
        self.fpexp.setObjectName("fpexp")
        self.horizontalLayout_3.addWidget(self.fpexp)
        self.fcheck = QtWidgets.QCheckBox()
        self.fcheck.setObjectName("fcheck")

        self.horizontalLayout_3.addWidget(self.fcheck)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.clabel = QtWidgets.QLabel(self.centralwidget)
        self.clabel.setObjectName("clabel")
        self.horizontalLayout_6.addWidget(self.clabel)
        self.clabel1 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clabel1.sizePolicy().hasHeightForWidth())
        self.clabel1.setSizePolicy(sizePolicy)
        self.clabel1.setObjectName("clabel1")
        self.horizontalLayout_6.addWidget(self.clabel1)
        self.cline1 = QtWidgets.QLineEdit(self.centralwidget)
        self.cline1.setObjectName("cline1")
        self.horizontalLayout_6.addWidget(self.cline1)
        self.clabel2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clabel2.sizePolicy().hasHeightForWidth())
        self.clabel2.setSizePolicy(sizePolicy)
        self.clabel2.setObjectName("clabel2")
        self.horizontalLayout_6.addWidget(self.clabel2)
        self.cline2 = QtWidgets.QLineEdit(self.centralwidget)
        self.cline2.setObjectName("cline2")
        self.horizontalLayout_6.addWidget(self.cline2)
        self.clabel3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clabel3.sizePolicy().hasHeightForWidth())
        self.clabel3.setSizePolicy(sizePolicy)
        self.clabel3.setObjectName("clabel3")
        self.horizontalLayout_6.addWidget(self.clabel3)
        self.cline3 = QtWidgets.QLineEdit(self.centralwidget)
        self.cline3.setObjectName("cline3")
        self.horizontalLayout_6.addWidget(self.cline3)
        self.clabel4 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clabel4.sizePolicy().hasHeightForWidth())
        self.clabel4.setSizePolicy(sizePolicy)
        self.clabel4.setObjectName("clabel4")
        self.horizontalLayout_6.addWidget(self.clabel4)
        self.cline4 = QtWidgets.QLineEdit(self.centralwidget)
        self.cline4.setObjectName("cline4")
        self.horizontalLayout_6.addWidget(self.cline4)
        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.plabel = QtWidgets.QLabel()
        self.plabel.setText("当選後何パーセント下がるか")
        self.pspin = QtWidgets.QSpinBox()
        self.pspin.setRange(0, 100)
        self.horizontalLayout_6.addWidget(self.plabel)
        self.horizontalLayout_6.addWidget(self.pspin)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.d2check1 = QtWidgets.QCheckBox(self.centralwidget)
        self.d2check1.setChecked(True)
        self.d2check1.setObjectName("d2check1")
        self.horizontalLayout_9.addWidget(self.d2check1)
        self.d2label = QtWidgets.QLabel(self.centralwidget)
        self.d2label.setObjectName("d2label")
        self.horizontalLayout_9.addWidget(self.d2label)
        self.d2line = QtWidgets.QLineEdit(self.centralwidget)
        self.d2line.setObjectName("d2line")
        self.horizontalLayout_9.addWidget(self.d2line)
        self.d2check2 = QtWidgets.QCheckBox(self.centralwidget)
        self.d2check2.setObjectName("d2check2")
        self.horizontalLayout_9.addWidget(self.d2check2)
        self.d2check3 = QtWidgets.QCheckBox(self.centralwidget)
        self.d2check3.setObjectName("d2check3")
        self.horizontalLayout_9.addWidget(self.d2check3)
        self.verticalLayout.addLayout(self.horizontalLayout_9)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.clabeld = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.clabeld.sizePolicy().hasHeightForWidth())
        self.clabeld.setSizePolicy(sizePolicy)
        self.clabeld.setObjectName("clabeld")
        self.horizontalLayout_5.addWidget(self.clabeld)
        self.g5a = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g5a.sizePolicy().hasHeightForWidth())
        self.g5a.setSizePolicy(sizePolicy)
        self.g5a.setObjectName("g5a")
        self.horizontalLayout_5.addWidget(self.g5a)
        self.g5aspin = QtWidgets.QSpinBox(self.centralwidget)
        self.g5aspin.setMaximum(99)
        self.g5aspin.setObjectName("g5aspin")
        self.horizontalLayout_5.addWidget(self.g5aspin)
        self.g5b = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g5b.sizePolicy().hasHeightForWidth())
        self.g5b.setSizePolicy(sizePolicy)
        self.g5b.setObjectName("g5b")
        self.horizontalLayout_5.addWidget(self.g5b)
        self.g5bspin = QtWidgets.QSpinBox(self.centralwidget)
        self.g5bspin.setMaximum(99)
        self.g5bspin.setObjectName("g5bspin")
        self.horizontalLayout_5.addWidget(self.g5bspin)
        self.g5c = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g5c.sizePolicy().hasHeightForWidth())
        self.g5c.setSizePolicy(sizePolicy)
        self.g5c.setObjectName("g5c")
        self.horizontalLayout_5.addWidget(self.g5c)
        self.g5cspin = QtWidgets.QSpinBox(self.centralwidget)
        self.g5cspin.setObjectName("g5cspin")
        self.horizontalLayout_5.addWidget(self.g5cspin)
        self.g5d = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g5d.sizePolicy().hasHeightForWidth())
        self.g5d.setSizePolicy(sizePolicy)
        self.g5d.setObjectName("g5d")
        self.horizontalLayout_5.addWidget(self.g5d)
        self.g5dspin = QtWidgets.QSpinBox(self.centralwidget)
        self.g5dspin.setObjectName("g5dspin")
        self.horizontalLayout_5.addWidget(self.g5dspin)
        self.g6a = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g6a.sizePolicy().hasHeightForWidth())
        self.g6a.setSizePolicy(sizePolicy)
        self.g6a.setObjectName("g6a")
        self.horizontalLayout_5.addWidget(self.g6a)
        self.g6aspin = QtWidgets.QSpinBox(self.centralwidget)
        self.g6aspin.setObjectName("g6aspin")
        self.horizontalLayout_5.addWidget(self.g6aspin)
        self.g6b = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g6b.sizePolicy().hasHeightForWidth())
        self.g6b.setSizePolicy(sizePolicy)
        self.g6b.setObjectName("g6b")
        self.horizontalLayout_5.addWidget(self.g6b)
        self.g6bspin = QtWidgets.QSpinBox(self.centralwidget)
        self.g6bspin.setObjectName("g6bspin")
        self.horizontalLayout_5.addWidget(self.g6bspin)
        self.g6c = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g6c.sizePolicy().hasHeightForWidth())
        self.g6c.setSizePolicy(sizePolicy)
        self.g6c.setObjectName("g6c")
        self.horizontalLayout_5.addWidget(self.g6c)
        self.g6cspin = QtWidgets.QSpinBox(self.centralwidget)
        self.g6cspin.setObjectName("g6cspin")
        self.horizontalLayout_5.addWidget(self.g6cspin)
        self.g6d = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.g6d.sizePolicy().hasHeightForWidth())
        self.g6d.setSizePolicy(sizePolicy)
        self.g6d.setObjectName("g6d")
        self.horizontalLayout_5.addWidget(self.g6d)
        self.g6dspin = QtWidgets.QSpinBox(self.centralwidget)
        self.g6dspin.setObjectName("g6dspin")
        self.horizontalLayout_5.addWidget(self.g6dspin)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.slabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.slabel.sizePolicy().hasHeightForWidth())
        self.slabel.setSizePolicy(sizePolicy)
        self.slabel.setObjectName("slabel")
        self.horizontalLayout_8.addWidget(self.slabel)
        self.nllabel = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.nllabel.sizePolicy().hasHeightForWidth())
        self.nllabel.setSizePolicy(sizePolicy)
        self.nllabel.setObjectName("nllabel")
        self.horizontalLayout_8.addWidget(self.nllabel)
        self.nlspin = QtWidgets.QSpinBox(self.centralwidget)
        self.nlspin.setObjectName("nlspin")
        self.horizontalLayout_8.addWidget(self.nlspin)
        self.mlabel2 = QtWidgets.QLabel(self.centralwidget)
        self.mlabel2.setObjectName("mlabel2")
        self.horizontalLayout_8.addWidget(self.mlabel2)
        self.mline = QtWidgets.QLineEdit(self.centralwidget)
        self.mline.setObjectName("mline")
        self.horizontalLayout_8.addWidget(self.mline)
        self.mcheck = QtWidgets.QCheckBox(self.centralwidget)
        self.mcheck.setObjectName("mcheck")
        self.horizontalLayout_8.addWidget(self.mcheck)
        self.verticalLayout.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.lb = QtWidgets.QPushButton(self.centralwidget)
        self.lb.setObjectName("lb")
        self.horizontalLayout_7.addWidget(self.lb)
        self.sb = QtWidgets.QPushButton(self.centralwidget)
        self.sb.setObjectName("sb")
        self.horizontalLayout_7.addWidget(self.sb)
        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.restext = QtWidgets.QTextEdit(self.centralwidget)
        self.restext.setReadOnly(True)
        self.restext.setAcceptRichText(False)
        self.restext.setObjectName("restext")
        self.horizontalLayout_2.addWidget(self.restext)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.cpybtn = QtWidgets.QPushButton(self.centralwidget)
        self.cpybtn.setObjectName("cpybtn")
        self.verticalLayout.addWidget(self.cpybtn)
        self.verticalLayout.setStretch(7, 1)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.d2check1.toggled['bool'].connect(self.d2line.setEnabled)
        self.d2check1.toggled['bool'].connect(self.d2label.setEnabled)
        self.d2check1.toggled['bool'].connect(self.d2check2.setEnabled)
        self.d2check1.toggled['bool'].connect(self.d2check3.setEnabled)
        self.cpybtn.clicked.connect(self.copy)
        self.fpexp.clicked.connect(self.selectfolder)
        self.lb.clicked.connect(self.dolottery)
        self.sb.clicked.connect(self.reprocess)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def selectfolder(self):
        self.fn = QtWidgets.QFileDialog.getOpenFileName(
            None, 'Open file', os.getcwd(), "*.csv")
        if self.fn[0] != "":
            self.fpline.setText(self.fn[0])
    
    def ex(self):
        self.terminated = True
        print("process terminated")
        self.tp.terminate()

    def ex2(self):
        self.terminated = True
        print("process terminated")
        self.t.terminate()

    def dolottery(self):
        if self.fn != "" and self.fn[0] != "":
            root, ext = os.path.splitext(self.fn[0])
            if (ext == ".csv"):
                pd = QtWidgets.QProgressDialog(
                    "Operation in progress.", "Cancel", 0, 0)
                pd.show()
                f = open(self.fn[0])
                kh = lottery.usparser(f.read())
                f.close()
            else:
                return 1
            lt = multiprocessing.Queue()
            wt = multiprocessing.Queue()
            try:
                self.terminated = False
                self.t = multiprocessing.Process(target=lottery.lottery, args=(kh, "db.csv", self.pspin.value(), lottery.alpha2dec(self.cline4.text()), lottery.alpha2dec(self.d2line.text()), [self.g5aspin.value(), self.g5bspin.value(), self.g5cspin.value(), self.g5dspin.value(
                ), self.g6aspin.value(), self.g6bspin.value(), self.g6cspin.value(), self.g6dspin.value()], lottery.alpha2dec(self.cline1.text()), lottery.alpha2dec(self.cline2.text()), lottery.alpha2dec(self.cline3.text()), not self.fcheck.isChecked(), self.d2check1.isChecked(), self.d2check2.isChecked(), self.d2check3.isChecked(), lt, wt))
                self.t.start()
                pd.canceled.connect(self.ex2)
                pd.show()
                print("first lottery")
                while self.t.is_alive():
                    time.sleep(0.01)
                    QtWidgets.QApplication.instance().processEvents()
                pd.hide()
                if self.terminated == True:
                    self.terminated = False
                    return 1
                # print(wt.get())
                # print(lt.get())
                self.wt2 = wt.get()
                self.lt2 = lt.get()
                print("get")
                lottery.dbupdate(self.wt2, "db.csv", 0, 1, 2)
                today = datetime.date.today()
                self.restext.setText(lottery.postprocess(self.lt2, self.nlspin.value(), self.mline.text(),
                                                         self.mcheck.isChecked(), today.year))
                return 0
            except:
                QtWidgets.QMessageBox.warning(
                    None, "警告", "抽選中にエラーが発生しました。\n今一度列番号等が間違っていないかご確認ください。", QtWidgets.QMessageBox.Yes)
                pass
            return 2
        else:
            QtWidgets.QMessageBox.warning(
                None, "警告", "ファイルが入力されていません。", QtWidgets.QMessageBox.Yes)
            return 3

    def copy(self):
        pyperclip.copy(self.restext.toPlainText())

    def reprocess(self):
        try:
            if len(self.lt2) != 0:
                today = datetime.date.today()
                self.restext.setText(lottery.postprocess(self.lt2, self.nlspin.value(), self.mline.text(),
                                                         self.mcheck.isChecked(), today.year))
        except:
            QtWidgets.QMessageBox.warning(
                None, "警告", "書式変更中にエラーが発生しました。\n抽選を先に行ってください。", QtWidgets.QMessageBox.Yes)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "創作部門抽選ソフトウェア"))
        self.label.setText(_translate("MainWindow", "創作部門向けの抽選ソフトウェアです。"))
        self.fplabel.setToolTip(_translate("MainWindow", "<html><head/><body><p>Formsから作成した応募データのファイルがどこにあるかを入力してください。<span style=\" font-weight:600;\">右にある「...」ボタン</span>でエクスプローラーを起動し、そこから当該ファイルを選択してください。また、<span style=\" font-weight:600;\">ファイルは「.csv」形式である必要があります。</span>まだExcelで変換操作を行っていない場合は、「名前をつけて保存」から形式で.csvを選択して保存してください。</p></body></html>"))
        self.fplabel.setText(_translate(
            "MainWindow", "<html><head/><body><p>入力ファイルのパス：</p></body></html>"))
        self.fpline.setPlaceholderText(
            _translate("MainWindow", "ここにファイルパスが出ます..."))
        self.fpexp.setToolTip(_translate("MainWindow", "ここを押してファイルを選択"))
        self.fpexp.setText(_translate("MainWindow", "..."))
        self.fcheck.setText(_translate("MainWindow", "1列目にデータが入っている"))
        self.clabel.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>学年、組、番号、希望する劇がそれぞれ入力するcsvファイルの<span style=\" font-weight:600;\">何列目に入っているか</span>を<span style=\" font-weight:600;\">アルファベットで</span>入力してください。</p></body></html>"))
        self.clabel.setText(_translate(
            "MainWindow", "ファイルの何列目に各項目が入っているか"))
        self.clabel1.setText(_translate("MainWindow", "学年："))
        self.clabel2.setText(_translate("MainWindow", "組："))
        self.clabel3.setText(_translate("MainWindow", "番号："))
        self.clabel4.setText(_translate("MainWindow", "希望する劇："))
        self.d2check1.setText(_translate("MainWindow", "第2希望までとる"))
        self.d2label.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>ここに上と同じくファイルの何列目に第2希望クラスが入っているかをアルファベットで入力してください。</p></body></html>"))
        self.d2label.setText(_translate("MainWindow", "何列目に第二希望が入っているか"))
        self.d2check2.setText(_translate("MainWindow", "第2希望当選者を当選者として記録する"))
        self.d2check3.setText(_translate("MainWindow", "第2希望抽選に確率変動を反映する"))
        self.clabeld.setToolTip(_translate(
            "MainWindow", "<html><head/><body><p>各クラスごとに何人ずつ当選するか記入してください。</p></body></html>"))
        self.clabeld.setText(_translate("MainWindow", "各クラスの当選人数　"))
        self.g5a.setText(_translate("MainWindow", "5-A"))
        self.g5b.setText(_translate("MainWindow", "5-B"))
        self.g5c.setText(_translate("MainWindow", "5-C"))
        self.g5d.setText(_translate("MainWindow", "5-D"))
        self.g6a.setText(_translate("MainWindow", "6-A"))
        self.g6b.setText(_translate("MainWindow", "6-B"))
        self.g6c.setText(_translate("MainWindow", "6-C"))
        self.g6d.setText(_translate("MainWindow", "6-D"))
        self.slabel.setText(_translate("MainWindow", "書式の変更"))
        self.nllabel.setText(_translate("MainWindow", "改行するまでの人数："))
        self.mlabel2.setText(_translate(
            "MainWindow", "最初にメンションする文言（しない場合は空欄）"))
        self.mcheck.setText(_translate("MainWindow", "個人にメンションする"))
        self.lb.setText(_translate("MainWindow", "抽選を行う"))
        self.sb.setText(_translate("MainWindow", "書式の変更のみ反映"))
        self.restext.setPlaceholderText(
            _translate("MainWindow", "ここに抽選結果が出ます..."))
        self.cpybtn.setText(_translate("MainWindow", "クリップボードにコピー"))


if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
