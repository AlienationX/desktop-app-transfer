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

import tt_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(585, 455)
        icon = QIcon()
        icon.addFile(u"../resources/logo.ico", QSize(), QIcon.Normal, QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.left = QWidget(Form)
        self.left.setObjectName(u"left")
        self.verticalLayout = QVBoxLayout(self.left)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.leftSub = QWidget(self.left)
        self.leftSub.setObjectName(u"leftSub")
        self.verticalLayout_2 = QVBoxLayout(self.leftSub)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(self.leftSub)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setPixmap(QPixmap(u":/icons/8680047_checkbox_circle_fill_icon.svg"))

        self.horizontalLayout_2.addWidget(self.label_2)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_2.addWidget(self.pushButton, 0, Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_2 = QFrame(self.leftSub)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.verticalLayout_3.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout_3.addWidget(self.pushButton_4)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.leftSub)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_5 = QPushButton(self.frame_3)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout_4.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_3)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout_4.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.frame_3)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout_4.addWidget(self.pushButton_7)


        self.verticalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.leftSub)


        self.horizontalLayout.addWidget(self.left)

        self.main = QWidget(Form)
        self.main.setObjectName(u"main")
        self.toolBox = QToolBox(self.main)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(110, 160, 121, 241))
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setGeometry(QRect(0, 0, 121, 181))
        self.verticalLayout_6 = QVBoxLayout(self.page_3)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.pushButton_9 = QPushButton(self.page_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        icon1 = QIcon()
        icon1.addFile(u":/icons/8680047_checkbox_circle_fill_icon.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon1)
        self.pushButton_9.setIconSize(QSize(20, 20))

        self.verticalLayout_6.addWidget(self.pushButton_9)

        self.pushButton_8 = QPushButton(self.page_3)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout_6.addWidget(self.pushButton_8, 0, Qt.AlignTop)

        self.toolBox.addItem(self.page_3, u"Page 1")
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setGeometry(QRect(0, 0, 121, 181))
        self.verticalLayout_5 = QVBoxLayout(self.page_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pushButton_10 = QPushButton(self.page_4)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_5.addWidget(self.pushButton_10)

        self.toolBox.addItem(self.page_4, u"Page 2")
        self.label = QLabel(self.main)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(80, 70, 51, 31))
        self.label.setPixmap(QPixmap(u":/icons/8680047_checkbox_circle_fill_icon.svg"))

        self.horizontalLayout.addWidget(self.main)


        self.retranslateUi(Form)

        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText("")
        self.pushButton.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_4.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_9.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_3), QCoreApplication.translate("Form", u"Page 1", None))
        self.pushButton_10.setText(QCoreApplication.translate("Form", u"PushButton", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_4), QCoreApplication.translate("Form", u"Page 2", None))
        self.label.setText("")
    # retranslateUi

