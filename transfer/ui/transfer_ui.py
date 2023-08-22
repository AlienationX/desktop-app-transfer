# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transfer.ui'
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
        Form.resize(585, 455)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.pushButton_5 = QPushButton(Form)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 3, 1, 1, 1)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")

        self.gridLayout.addWidget(self.checkBox, 4, 1, 1, 1)

        self.pushButton_3 = QPushButton(Form)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 2, 0, 1, 1)

        self.pushButton_4 = QPushButton(Form)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(False)

        self.gridLayout.addWidget(self.pushButton_4, 2, 1, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")

        self.horizontalLayout_2.addWidget(self.pushButton_1)

        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_2.addWidget(self.pushButton_2)


        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.pushButton_6 = QPushButton(Form)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.gridLayout.addWidget(self.pushButton_6, 4, 0, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setMaximumSize(QSize(16777215, 60))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 5, 0, 1, 1)

        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.radioButton = QRadioButton(self.groupBox)
        self.radioButton.setObjectName(u"radioButton")

        self.verticalLayout.addWidget(self.radioButton)

        self.radioButton_2 = QRadioButton(self.groupBox)
        self.radioButton_2.setObjectName(u"radioButton_2")

        self.verticalLayout.addWidget(self.radioButton_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout.addWidget(self.groupBox, 3, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"PushButton5", None))
        self.checkBox.setText(QCoreApplication.translate("Form", u"CheckBox", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton3", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"PushButton4", None))
        self.pushButton_1.setText(QCoreApplication.translate("Form", u"PushButton1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton2", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"PushButton6", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"RadioButton", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"RadioButton", None))
    # retranslateUi

