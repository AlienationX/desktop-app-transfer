import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class MyWidget(QWidget):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.resize(200, 20)
        # self.setWindowFlags(Qt.Dialog | Qt.FramelessWindowHint)  # 隐藏边框\总在最前\禁止调整大小
        self.setAttribute(Qt.WA_TranslucentBackground, True)  # 背景透明（添加阴影必须背景透明）
        
        self.label = QLabel("Are you ok?")
        self.btn = QPushButton("ok")
        self.btn.clicked.connect(self.close)
        
        self.frame = QFrame(self)
        self.frameLayout = QVBoxLayout(self.frame)
        self.frameLayout.addWidget(self.label)
        self.frameLayout.addWidget(self.btn)
        
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(self.frame)
        
        self.setStyleSheet("""
            QFrame {
                background-color: green;
                border: 1px solid red;
            }
        """)
        
    def paintEvent(self, event) -> None:
        opt = QStyleOption()
        opt.initFrom(self)
        painter = QPainter(self)
        #painter.setRenderHint(QtGui.QPainter.Antialiasing) # 反锯齿
        self.style().drawPrimitive(QStyle.PE_Widget, opt, painter, self)


class MyWindow(MyWidget):
    
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        # self.setAttribute(Qt.WA_StyledBackground, True)
        self.setStyleSheet("""
            QFrame {
                background-color: blue;
                border: 1px solid red;
            }
        """)
        

if __name__=="__main__":
    app=QApplication(sys.argv)
    w = QWidget()
    w.resize(600, 400)
    
    m = MyWindow(w)
    m.resize(m.sizeHint())
    # m.show()
    w.show()
    app.exit(app.exec())