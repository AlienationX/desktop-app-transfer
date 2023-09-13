from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

import sys

class Test(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.resize(400, 300)
        
        # 没有show之前的坐标是不准确的
        print(self.size())
        print(self.geometry())
        print(self.pos())
        print(self.mapToGlobal(self.pos()))
        print(self.rect())
        
        self.btn1 = QPushButton("TopLeft")
        self.btn2 = QPushButton("TopRight")
        self.btn3 = QPushButton("BottomLeft")
        self.btn4 = QPushButton("BottomRight")
        self.btn1.clicked.connect(self.showed)
        self.btn2.clicked.connect(self.showed)
        self.btn3.clicked.connect(self.showed)
        self.btn4.clicked.connect(self.showed)
                
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.btn1)
        self.layout.addWidget(self.btn2)
        self.layout.addWidget(self.btn3)
        self.layout.addWidget(self.btn4)
        self.setLayout(self.layout)
        
    def showed(self):
        print("==> ", self.size())
        print("==> ", self.width())
        print("==> ", self.height())
        print("==> ", self.geometry())               # 窗体位置和大小，强烈推荐
        print("--> ", self.geometry().left())        # 左边距距离左侧的长度
        print("--> ", self.geometry().right())       # 右边距距离左侧的长度
        print("--> ", self.geometry().top())         # 上边距距离顶部的高度
        print("--> ", self.geometry().bottom())      # 下边距距离顶部的高度
        print("--> ", self.geometry().topLeft())     # 左上角坐标
        print("--> ", self.geometry().topRight())    # 右上角坐标
        print("--> ", self.geometry().bottomLeft())  # 左下角坐标
        print("--> ", self.geometry().bottomRight()) # 右下角坐标
        
        self.dialog = QDialog()
        self.dialog.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)  # Qt.Tool 任务栏不会显示新开的窗体
        self.dialog.setWindowTitle("welcome")
        self.dialog.setStyleSheet("background-color: green")
        
        self.dialog.btn = QPushButton("hello world")
        self.dialog.btn.clicked.connect(self.dialog.close)
        _layout = QVBoxLayout()
        _layout.addWidget(self.dialog.btn)
        self.dialog.setLayout(_layout)
        
        print("dialog ", self.dialog.width())
        self.dialog.show()
        self.dialog.hide()
        print("dialog ", self.dialog.width())
        
        direction = self.sender().text()  # 获取发送信号过来的部件的文本信息
        if direction == "TopLeft":
            self.dialog.move(self.geometry().topLeft())
        if direction == "TopRight":
            x = self.geometry().topLeft().x() + self.width() - self.dialog.width()
            y = self.geometry().topLeft().y()
            self.dialog.move(x, y)
        if direction == "BottomLeft":
            x = self.geometry().topLeft().x()
            y = self.geometry().topLeft().y() + self.height() - self.dialog.height()
            self.dialog.move(x, y)
        if direction == "BottomRight":
            x = self.geometry().topLeft().x() + self.width() - self.dialog.width()
            y = self.geometry().topLeft().y() + self.height() - self.dialog.height()
            self.dialog.move(x, y)

        # self.dialog.setModal(True)
        self.dialog.setWindowModality(Qt.ApplicationModal)  # 还有个动画效果
        self.dialog.show()

        
if __name__=="__main__":
    app=QApplication(sys.argv)
    m=Test()
    m.show()
    app.exit(app.exec())
    