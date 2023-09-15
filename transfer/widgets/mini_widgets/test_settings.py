
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys

from settings_hierarchy import SettingsHierarchy
from addons_widget import MaskWidget


class TestSettingsHierarchy(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.resize(600, 400)
        self.setWindowTitle("Test")
        # self.setWindowOpacity(0.8)  # 设置窗口透明度
        # self.setStyleSheet("background-color: gray")
        self.btn = QPushButton("show", self)
        self.label = QLabel("aa", self)
        self.label.move(0, 50)
        self.label1 = QLabel("asdfsadfasdfsdfsfa", self)
        self.label1.move(400, 50)
        
        self.settingsFrame = SettingsHierarchy(self)
        self.maskWidget = MaskWidget(self)
        
        self.btn.clicked.connect(self.showSettingsFrame)
        
        self.toggleBtn = QPushButton(">>", self)
        self.toggleBtn.setStyleSheet("""
            background-color: orange;
            margin: 0;
            padding: 0;
        """)
        self.toggleBtn.show()
        self.toggleBtn.move(0, self.height() - self.toggleBtn.height())
        
        self.setMinimumWidth(self.settingsFrame.width())
    
    def showSettingsFrame(self):
        # 添加遮罩层
        self.settingsFrame.show()
    
    def delayMask(self):
        self.maskWidget.resize(self.width() - self.settingsFrame.width() + 1, self.height())
        self.maskWidget.show()
    
    def showEvent(self, event) -> None:
        # return super().showEvent(event)
        print("parent show")
        self.resize(self.size())  # 更新实际的尺寸大小
        
    def resizeEvent(self, event) -> None:
        # return super().resizeEvent(event)
        self.settingsFrame.resize(self.settingsFrame.width(), self.height())
        x = self.width() - self.settingsFrame.width()
        y = 0
        self.settingsFrame.move(x, y)
        
        # 左下角buttom也跟着移动
        self.toggleBtn.move(0, self.height() - self.toggleBtn.height())
        # 遮罩也随着调整大小
        self.maskWidget.resize(self.width() - self.settingsFrame.width(), self.height())
        
    def mousePressEvent(self, event) -> None:
        if not self.settingsFrame.underMouse():
            print("click")
            self.maskWidget.hide()
            self.settingsFrame.hideSelf()

 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = TestSettingsHierarchy()
    w.show()
    app.exec()