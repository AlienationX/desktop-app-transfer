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
        self.parent = parent
        
        # self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        # self.setModal(True)
        self.setStyleSheet("background-color: green;")
        
        self.closeBtn = QPushButton("close")
        self.closeBtn.clicked.connect(self.close)
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
        self.hide()  # 需要默认隐藏
    
    def showEvent(self, event) -> None:
        print(self.parent.geometry())
        print(self.parent.geometry().right())
        print(self.parent.geometry().top())
        print(self.parent.geometry().bottom())
        self.resize(min(self.width(), self.parent.width()), self.parent.height())
        
        x = self.parent.width() - self.width() + 1
        y = 0
        
        self.anim = QPropertyAnimation(self, b"geometry")
        self.anim.setStartValue(QRect(self.parent.geometry().width(), y, self.width(), self.height()))
        self.anim.setEndValue(QRect(x, y, self.width(), self.height()))
        self.anim.setDuration(200)
        self.anim.start()
        
        # self.move(x, y)
    
class Test(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.resize(600, 400)
        self.setWindowTitle("Test")
        # self.setWindowOpacity(0.8)  # 设置窗口透明度
        self.btn = QPushButton("show", self)
        self.label = QLabel("aa", self)
        self.label.move(0, 50)
        self.label1 = QLabel("asdfsadfasdfsdfsfa", self)
        self.label1.move(400, 50)
        
        self.settingsFrame = SettingsHierarchy(self)
        self.btn.clicked.connect(self.settingsFrame.show)
    
    def showEvent(self, event) -> None:
        # return super().showEvent(event)
        print("parent show")
        self.resize(self.size())  # 更新实际的尺寸大小
        
    def resizeEvent(self, event) -> None:
        # return super().resizeEvent(event)
        self.settingsFrame.resize(self.width()-self.settingsFrame.width(), self.height())
        
    def mousePressEvent(self, event) -> None:
        if not self.settingsFrame.underMouse():
            print("click")
            self.settingsFrame.hide()
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    m=Test()
    m.show()
    app.exit(app.exec())
    