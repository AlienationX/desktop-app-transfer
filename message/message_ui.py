# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'send_message.ui'
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
        Form.resize(476, 343)
        Form.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_2 = QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plainTextEdit = QPlainTextEdit(Form)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        font = QFont()
        font.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.inputLineEdit = QLineEdit(Form)
        self.inputLineEdit.setObjectName(u"inputLineEdit")
        self.inputLineEdit.setReadOnly(False)

        self.horizontalLayout.addWidget(self.inputLineEdit)

        self.sendPushButton = QPushButton(Form)
        self.sendPushButton.setObjectName(u"sendPushButton")
        font1 = QFont()
        font1.setFamilies([u"\u5fae\u8f6f\u96c5\u9ed1"])
        font1.setBold(False)
        self.sendPushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.sendPushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Send Message", None))
        self.plainTextEdit.setPlaceholderText(QCoreApplication.translate("Form", u"Hello World", None))
#if QT_CONFIG(tooltip)
        self.sendPushButton.setToolTip(QCoreApplication.translate("Form", u"\u6309Enter\u952e\u53d1\u9001", None))
#endif // QT_CONFIG(tooltip)
        self.sendPushButton.setText(QCoreApplication.translate("Form", u"Enter", None))
#if QT_CONFIG(shortcut)
        self.sendPushButton.setShortcut(QCoreApplication.translate("Form", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

