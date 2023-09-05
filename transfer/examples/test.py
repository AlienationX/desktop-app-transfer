import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *

class CusWidget(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.layout = QHBoxLayout(self)
        self.setStyleSheet("background-color: red;")
        self.btn = QPushButton("Click CusWidget")
        self.layout.addWidget(self.btn)
        
        self.setAttribute(Qt.WA_StyledBackground, True)  # 无法继承背景色的设置，需要手动设置，便于测试 https://www.cnpython.com/qa/1523133
        # self.setStyleSheet("background-color: green;")
        print("HContainer", self.layout.getContentsMargins())
        self.layout.setContentsMargins(0, 0, 0, 0)  # 去掉默认边距
        print("HContainer", self.layout.getContentsMargins())


class MainWindow(QWidget):
    def __init__(self) -> None:
        super().__init__()
        self.resize(400, 300)
        self.layout = QHBoxLayout(self)
        
        self.btn = QPushButton("Click Me")
        self.layout.addWidget(self.btn)
        
        self.cusWidget = CusWidget()
        self.layout.addWidget(self.cusWidget)
        
        self.settingsVContainer = QWidget()
        self.settingsLayout = QVBoxLayout(self.settingsVContainer)
        self.settingsVContainer.setStyleSheet("background-color: red;")
        self.x = QPushButton("x")
        self.settingsLayout.addWidget(self.x)
        # self.settingsLayout.setContentsMargins(0, 0, 0, 0)
        self.layout.addWidget(self.settingsVContainer)
        self.setStyleSheet("background-color: green;")
        
        
if __name__=="__main__":
    app=QApplication(sys.argv)
    win=MainWindow()
    win.show()
    app.exit(app.exec())