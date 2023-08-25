# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(599, 424)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.treeWidget = QTreeWidget(Form)
        __qtreewidgetitem = QTreeWidgetItem(self.treeWidget)
        __qtreewidgetitem1 = QTreeWidgetItem(__qtreewidgetitem)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(__qtreewidgetitem1)
        QTreeWidgetItem(self.treeWidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setEnabled(True)
        self.treeWidget.setMaximumSize(QSize(200, 16777215))
        self.treeWidget.setAutoFillBackground(True)
        self.treeWidget.setStyleSheet(u"\n"
"border:none;")
        self.treeWidget.setAutoScroll(True)
        self.treeWidget.setDragEnabled(False)
        self.treeWidget.setUniformRowHeights(False)
        self.treeWidget.setAllColumnsShowFocus(False)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.header().setVisible(False)

        self.horizontalLayout.addWidget(self.treeWidget)

        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setAutoFillBackground(False)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 170, 75, 24))
        self.pushButton.setAutoFillBackground(True)
        self.pushButton.setStyleSheet(u"outline:none;\n"
"\n"
"")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setEnabled(True)
        self.lineEdit.setGeometry(QRect(20, 40, 201, 22))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 55, 16))
        self.plainTextEdit = QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(10, 330, 351, 71))
        self.progressBar = QProgressBar(self.widget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setGeometry(QRect(10, 290, 351, 23))
        self.progressBar.setValue(24)
        self.progressBar.setAlignment(Qt.AlignCenter)
        self.radioButton = QRadioButton(self.widget)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(20, 140, 95, 20))
        self.radioButton_2 = QRadioButton(self.widget)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(20, 80, 95, 20))
        self.radioButton_2.setCheckable(True)
        self.radioButton_2.setChecked(True)
        self.radioButton_3 = QRadioButton(self.widget)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(20, 110, 131, 20))
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(300, 40, 75, 24))
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(180, 150, 120, 80))
        self.radioButton_4 = QRadioButton(self.groupBox)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(10, 30, 95, 20))
        self.radioButton_5 = QRadioButton(self.groupBox)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(10, 50, 95, 20))
        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(230, 40, 69, 22))

        self.horizontalLayout.addWidget(self.widget)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("Form", u"\u76ee\u5f55", None));

        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        ___qtreewidgetitem1 = self.treeWidget.topLevelItem(0)
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("Form", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem2 = ___qtreewidgetitem1.child(0)
        ___qtreewidgetitem2.setText(0, QCoreApplication.translate("Form", u"\u65b0\u5efa\u5b50\u9879\u76ee", None));
        ___qtreewidgetitem3 = ___qtreewidgetitem2.child(0)
        ___qtreewidgetitem3.setText(0, QCoreApplication.translate("Form", u"\u65b0\u5efa\u5b50\u9879\u76ee", None));
        ___qtreewidgetitem4 = ___qtreewidgetitem2.child(1)
        ___qtreewidgetitem4.setText(0, QCoreApplication.translate("Form", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem5 = ___qtreewidgetitem2.child(2)
        ___qtreewidgetitem5.setText(0, QCoreApplication.translate("Form", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qtreewidgetitem6 = self.treeWidget.topLevelItem(1)
        ___qtreewidgetitem6.setText(0, QCoreApplication.translate("Form", u"\u65b0\u5efa\u9879\u76ee2", None));
        self.treeWidget.setSortingEnabled(__sortingEnabled)

        self.pushButton.setText(QCoreApplication.translate("Form", u"\u5f00\u59cb\u6267\u884c", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u4e0d\u5e26\u53cc\u5f15\u53f7", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u53cc\u5f15\u53f7\u8f6c\u4e49", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u6240\u6709\u6587\u672c\u5e26\u53cc\u5f15\u53f7", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u9009\u62e9\u6587\u4ef6", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u7f16\u7801", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"utf8", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"gbk", None))
    # retranslateUi

