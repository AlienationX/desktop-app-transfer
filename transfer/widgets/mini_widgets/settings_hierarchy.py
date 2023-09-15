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
        self.setStyleSheet("background-color: green;")
        
        self.closeBtn = QPushButton("close")
        self.closeBtn.clicked.connect(self.hideSelf)
        self.btn1 = QPushButton("TopLeft")
        self.btn2 = QPushButton("TopRight")
        self.btn3 = QPushButton("BottomLeft")
        self.btn4 = QPushButton("BottomRight")
                
        self.layout = QGridLayout(self)
        self.layout.addWidget(self.closeBtn)
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)
        self.layout.addWidget(self.btn4)
        self.setLayout(self.layout)
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
        self.hideAnim.finished.connect(self.parent().delayMask)  # 动画完成后去掉遮罩
        self.hideAnim.start()
    