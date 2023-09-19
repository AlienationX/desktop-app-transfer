from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

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
        self.resize(400, 600)
        
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        # self.setModal(True)
        self.setStyleSheet("""
            background-color: rgb(22, 130, 93);
            border-radius: 0;
        """)
        self.setStyleSheet("""
            QWidget {
                border: 1px solid red;
                background-color: blue;
            }
        """)
        
        self.closeBtn = QPushButton("close")
        self.closeBtn.clicked.connect(self.hideSelf)
        
        self.label1 = QLabel("Free")  # Preview / Pro
        self.label2 = QLabel("主题选择")
        self.label3 = QLabel("隐藏状态栏")
        self.btn1 = QPushButton("TopLeft")
        self.btn2 = QPushButton("TopRight")
        self.btn3 = QPushButton("BottomLeft")
        self.btn4 = QPushButton("BottomRight")
                
        self.gridLayout = QGridLayout(self)
        print(self.gridLayout.columnCount())
        self.gridLayout.addWidget(self.closeBtn, 0, 1, alignment=Qt.AlignRight)
        self.gridLayout.addWidget(self.label1, 1, 0)
        self.gridLayout.addWidget(self.btn1, 1, 1)
        self.gridLayout.addWidget(self.label2, 2, 0)
        self.gridLayout.addWidget(self.btn2, 2, 1)
        self.gridLayout.addWidget(self.label3, 3, 0)
        self.gridLayout.addWidget(self.btn3, 3, 1)
        self.gridLayout.addWidget(self.btn4)
        self.gridLayout.setRowStretch(99, 1)
        self.setLayout(self.gridLayout)
        self.setHidden(True)  # 需要默认隐藏
    
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
    