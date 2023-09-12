# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'show.ui'
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
        Form.resize(400, 300)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(250, 0, 153, 301))
        self.frame.setStyleSheet(u"background-color:rgb(155, 255, 144)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.verticalLayout.addWidget(self.lineEdit)

        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout.addWidget(self.pushButton_2)

        self.hideBtn = QPushButton(Form)
        self.hideBtn.setObjectName(u"hideBtn")
        self.hideBtn.setGeometry(QRect(200, 170, 75, 24))
        self.label_back = QLabel(Form)
        self.label_back.setObjectName(u"label_back")
        self.label_back.setGeometry(QRect(220, 110, 55, 16))
        self.showBtn = QPushButton(Form)
        self.showBtn.setObjectName(u"showBtn")
        self.showBtn.setGeometry(QRect(110, 70, 61, 24))
        self.label_back.raise_()
        self.frame.raise_()
        self.hideBtn.raise_()
        self.showBtn.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.lineEdit.setText(QCoreApplication.translate("Form", u"welcome", None))
        self.label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.hideBtn.setText(QCoreApplication.translate("Form", u"hide", None))
        self.label_back.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.showBtn.setText(QCoreApplication.translate("Form", u"show", None))
    # retranslateUi

