from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import qtawesome as qta

import sys

"""
什么是层级关系
区别于控件间的父子关系，层级关系是值显示的顺序。
一般来说，当两个控件显示范围出现重叠时，如果两个控件的父子关系为同一级，那么后定义的控件将显示在先定义的控件之上；但是可以使用以下 API 进行层级关系的调整。

lower()
作用：将控件降低到最底层
raise_()
作用：将控件提升到最上层
a.stackUnder(b)
作用：让 a 置于 b 下
"""

from typing import Optional

class SettingsHierarchy(QFrame):
    
    def __init__(self, parent:QWidget=None) -> None:
        super().__init__(parent)
        
        self._data = {
            "currentTheme": "Dark",
            "hideStatueBar": False
        }
        
        self.resize(260, 600)
        
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        # self.setModal(True)
        
        self.titleLabel = QLabel("Settings")
        font = QFont()
        font.setBold(True)
        self.titleLabel.setFont(font)
        self.closeBtn = QPushButton()
        self.closeBtn.setIcon(qta.icon("msc.arrow-circle-right", color=QColor(200, 200, 200)))  # msc.arrow-circle-right / msc.arrow-right
        self.closeBtn.setIconSize(QSize(28, 28))
        self.closeBtn.clicked.connect(self.hideSelf)
        
        self.titleWidget = QWidget()
        self.titleWidget.setObjectName("titleWidget")
        self.titleLayout = QHBoxLayout(self.titleWidget)
        self.titleLayout.setContentsMargins(12, 0, 12, 12)
        self.titleLayout.addWidget(self.titleLabel)
        self.titleLayout.addStretch()
        self.titleLayout.addWidget(self.closeBtn)
        
        self.label1 = QLabel("当前版本:")  # Preview / Pro
        self.label2 = QLabel("主题选择:")
        self.label3 = QLabel("隐藏状态栏:")
        
        self.item1 = QLabel("Free")
        self.item1.setObjectName("item1")
        self.item1.setFont(font)
        self.item1.setAlignment(Qt.AlignRight)  # Qt.AlignCenter|Qt.AlignLeft|Qt.AlignTop
        self.item1.setMinimumWidth(100)
        
        self.item2 = QComboBox()
        self.item2.setMinimumWidth(100)
        self.item2.addItem("Dark")
        self.item2.addItem("Light")
        self.item2.addItem("Color")
        
        self.item3 = QPushButton()
        self.item3.setIcon(qta.icon("mdi.toggle-switch-off", color=QColor(200, 200, 200)))
        # self.item3.setIconSize(QSize(30, 30))
        self.item3.clicked.connect(self.switchIcon)
        
        self.contentWidget = QWidget()
        
        self.gridLayout = QGridLayout(self.contentWidget)
        self.gridLayout.setContentsMargins(12, 12, 12, 12)
        self.gridLayout.setSpacing(10)
        self.gridLayout.addWidget(self.label1, 1, 0)
        self.gridLayout.addWidget(self.item1, 1, 1, alignment=Qt.AlignRight)
        self.gridLayout.addWidget(self.label2, 2, 0)
        self.gridLayout.addWidget(self.item2, 2, 1, alignment=Qt.AlignRight)
        self.gridLayout.addWidget(self.label3, 3, 0)
        self.gridLayout.addWidget(self.item3, 3, 1, alignment=Qt.AlignRight)
        self.gridLayout.setRowStretch(99, 1)
        
        # self.formLayout = QFormLayout(self.contentWidget)
        # self.formLayout.addRow(self.label1, self.item1)
        # self.formLayout.addRow(self.label2, self.item2)
        # self.formLayout.addRow(self.label3, self.item3)
        
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(12, 12, 12, 12)
        self.layout.addWidget(self.titleWidget)
        self.layout.addWidget(self.contentWidget)
        self.layout.addStretch()
        self.setHidden(True)  # 需要默认隐藏

        self.setStyleSheet("""
            QWidget {
                /* border: 1px solid red; */
                color: rgb(200, 200, 200);   /* rgb(44, 222, 133) */
                background-color: rgb(48, 48, 49);
                border-radius: 0;
            }
            #titleWidget {
                border-bottom: 1px solid rgb(200, 200, 200);
            }
            #item1 {
                color: rgb(204, 102, 51);
                background-color: rgb(44, 222, 133);
            }
        """)
    
    @Slot()
    def switchIcon(self):
        self.item3.setIcon(qta.icon("mdi.toggle-switch", color=QColor(200, 200, 200)))
    
    def showEvent(self, event) -> None:
        self.resize(min(self.width(), self.parent().width()), self.parent().height())
        
        x = self.parent().width() - self.width() + 1
        y = 0
        # self.move(x, y)
        
        self.showAnim = QPropertyAnimation(self, b"geometry")
        self.showAnim.setStartValue(QRect(self.parent().width(), y, self.width(), self.height()))
        self.showAnim.setEndValue(QRect(x, y, self.width(), self.height()))
        self.showAnim.setDuration(200)
        self.showAnim.start()
        
    def hideSelf(self) -> None:   
        # self.resize(min(self.width(), self.parent().width()), self.parent().height())
        
        x = self.parent().width() - self.width() + 1
        y = 0
        # self.move(x, y)

        self.hideAnim = QPropertyAnimation(self, b"geometry")
        self.hideAnim.setStartValue(QRect(x, y, self.width(), self.height()))
        self.hideAnim.setEndValue(QRect(self.parent().width(), y, self.width(), self.height()))
        self.hideAnim.setDuration(200)
        self.hideAnim.finished.connect(self.hide)  # 动画完成后执行隐藏
        self.hideAnim.finished.connect(self.parent().delay_mask)  # 动画完成后去掉遮罩
        self.hideAnim.start()
    