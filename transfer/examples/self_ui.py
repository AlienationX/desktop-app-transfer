import sys
import os
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class Ui:
    pass

ui=Ui()
ui.a="hello"
print(ui.a)

class MyWidget(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle("空白测试模板")
        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self) -> None:
        """设置界面"""
        # 在此处编写设置UI的代码
        self.ui = QObject()
        self.ui.name = QPushButton("ok")
        print(self.ui.name)
        self.ui.label = QLabel("Hello")
        self.ui.layout = QVBoxLayout(self)
        self.ui.layout.addWidget(self.ui.label)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWidget()
    window.show()
    sys.exit(app.exec())